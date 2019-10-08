from flask import render_template, flash, url_for, redirect, Flask, send_file, request, send_from_directory, jsonify
from datetime import datetime
import requests, regex
from app import app
import config as cfg

from app.models.forms import RegisterForm, PostForm, EditForm

@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=['GET', 'POST'])
def index():
    postlist = requests.get("http://localhost:3000/api/Post").json()
    msgs = []
    usrs = []
    usrIDS = []
    usrNames = []
    userID = ""
    for i in postlist:
        msgs.append(i.get('msg'))
        usrs.append(i.get('user'))
    for j in usrs:
        teste = regex.findall("[0-9]", j)
        for k in teste:
            userID = userID + str(k)
        usrIDS.append(userID)
        userID = ""
    for l in usrIDS:
        name = requests.get("http://localhost:3000/api/User/" + l).json()
        usrNames.append(name.get('firstName') + " " + name.get('lastName'))

#    print(msgs)
 #   print(usrIDS)
    return render_template('index.html', msgs = msgs, usrIDS = usrIDS,usrNames = usrNames, tam = len(msgs))

@app.route('/register', methods=['GET', 'POST'])
def register():
    rf = RegisterForm()
    seeID = requests.get("http://localhost:3000/api/User").json()
    nextID = int(seeID[len(seeID)-1].get('userId')) + 1
    if rf.validate_on_submit():
        newUsr = jsonify(userID = str(nextID), firstName = rf.firstName.data, lastName = rf.lastName.data)
        print(newUsr)
        flash("Seu ID é : " + str(nextID))
        flash("Bem vindo, " + rf.firstName.data + " " + rf.lastName.data)

    return render_template('register.html', rf = rf)

@app.route('/post', methods=['GET', 'POST'])
def post():
    pf = PostForm()
    seeID = requests.get("http://localhost:3000/api/Post").json()
    nextID = int(seeID[len(seeID)-1].get('postId')) + 1
    
    if pf.validate_on_submit():
        completeUsr = "resource:org.example.basic.User#" + str(pf.user.data)
        newUsr = jsonify(userID = str(nextID), user = completeUsr, msg = pf.msg.data)
        print(newUsr)
        flash("O ID do seu Post é : " + str(nextID))
        flash("Sua mensagem postada foi: " + pf.msg.data)

    return render_template('post.html', pf = pf)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    ef = EditForm()
    seeID = requests.get("http://localhost:3000/api/Post").json()
    nextID = seeID[len(seeID)-1].get('postId')
    
    if ef.validate_on_submit():
        completePost = "resource:org.example.basic.Post#" + str(ef.postID.data)
        updPost = jsonify(userID = str(nextID), user = completePost, msg = ef.newMsg.data)
        print(updPost)
        flash("O ID do seu Post é : " + str(nextID))
        flash("Sua mensagem foi alterada para: " + ef.newMsg.data)

    return render_template('edit.html', ef = ef)