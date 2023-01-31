from flask import Flask, render_template, flash, redirect, url_for, session, request, logging,send_file
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, IntegerField,FileField, SubmitField
import daredevil
from passlib.hash import sha256_crypt
from functools import wraps
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired,DataRequired
import deadpool
import Ironman
import bcrypt
import mysql.connector
import zipping
import matplotlib.pyplot as plt
import os
import shutil


def hash_it(password):

    bytes = password.encode('utf-8')
    hash = bcrypt.hashpw(bytes, b'$2b$12$ikFJLhhV.1ziQsq0cT94IO')
    hash=str(hash)
    return hash[2:-1]

mydb = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12592957",
    passwd="QuJkuAYhUk",
    database="sql12592957"
    
)
my_cursor = mydb.cursor()
global current_filename
global global_dict
file_name=''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.secret_key='a'

class UploadFileForm(FlaskForm):
    Project_Name =  StringField("Name of the Project: ",validators=[DataRequired()])
    Author_Name =  StringField("Name of the Author: ",validators=[DataRequired()])
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File",)

class TextAreaForm(FlaskForm):
    textarea  = StringField("Enter the text you want to check for plaigarism : ",validators=[DataRequired()])
    submit = SubmitField("Check for plaigarsm")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('dashboard.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

@app.route('/update_signup',methods=["POST"])
def validate():
    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    email=request.form.get("email")
    password=request.form.get("password")
    q="INSERT INTO Details (first_name, last_name, username, password) VALUES ('{first_name}', '{last_name}', '{email}', '{password}');".format(first_name=first_name,last_name=last_name,email=email,password=hash_it(password))
    print(q)
    my_cursor.execute(q)
    mydb.commit()

    return render_template("home.html")

@app.route('/dashboard',methods=["POST"])
def final():
    user_name=request.form.get("email")
    password=request.form.get("password")
    print(user_name,password)
    q="SELECT * FROM Details;"# where email='{user_name}' and 'password='{password}';".format(user_name=user_name,password=hash_it(password))
    my_cursor.execute(q)
    out = my_cursor.fetchall()[0]

    if out[2] == user_name and out[3] == hash_it(password):
        return render_template("dashboard.html")
    else:
        return render_template("home.html")

@app.route('/signup')
def dashboard():
    return render_template('signup.html')

@app.route('/download/<filename>')
def download(filename):
    try:
        path = "static/files/{}".format(filename)
        print(path)
        return send_file(path, as_attachment=True)
    except Exception as e:
        return str(e)

@app.route('/temp',methods=["GET","POST"])
def temp():
    form = UploadFileForm()
    Project_Name = None
    Author_Name = None
    if form.validate_on_submit():
        Project_Name = form.Project_Name.data
        form.Project_Name.data = ' '
        Author_Name = form.Author_Name.data
        form.Author_Name.data = ' '
        file = form.file.data # First grab the file
        current_filename = file.filename
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        return "success"
    return render_template('v.html', form=form,Project_Name=Project_Name,Author_Name=Author_Name)
    


@app.route('/upload',methods=["GET","POST"])
def upload():
    global global_dict
    global current_filename
    form = UploadFileForm()
    Project_Name = None
    Author_Name = None
    if form.validate_on_submit():
        Project_Name = form.Project_Name.data
        form.Project_Name.data = ' '
        Author_Name = form.Author_Name.data
        form.Author_Name.data = ' '
        file = form.file.data # First grab the file
        current_filename = file.filename
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        
        
        if 1:
            string=daredevil.customize_card(Project_Name,Author_Name,current_filename)
            fin = open("templates\\dashboard.html", "rt")
            #read file contents to string
            data = fin.read()
            #replace all occurrences of the required string
            data = data.replace("<!-- <p>vetha</p> -->", string)
            #close the input file
            fin.close()
            #open the input file in write mode
            fin = open("templates\\dashboard.html", "wt")
            #overrite the input file with the resulting data
            fin.write(data)
            #close the file
            fin.close()
            return "nee pozhachipa da!!!"
        

        return render_template('dashboard.html')
    return render_template('upload.html', form=form,Project_Name=Project_Name,Author_Name=Author_Name)
    
@app.route("/ve")
def ve():
    labels = ['Jan', 'Feb', 'Mar', 'Apr']
    values = [12, 19, 3, 5]

    plt.pie(labels, values)
    plt.savefig('static/images/chart.png')
    return render_template("test.html")
@app.route('/valid')
def valid():
    return render_template("valid.html",dict = global_dict)
@app.route('/plaigarism',methods=["GET","POST"])
def plaigarism():
    form = TextAreaForm()
    textarea = None
    if form.validate_on_submit():
        textarea = form.textarea.data
        copied_links,word_count,Index_value=Ironman.plag_cheker(textarea)
        print(copied_links)
        return render_template("plaigarism.html",data = copied_links,form=form,textarea=textarea)
    return render_template("plaigarism.html",form=form,textarea=textarea)
@app.route('/vetha',methods=["POST"])
def vetha():
    print("inga iruken")
    string='<div class="col-md-4"> <div class="card p-3 mb-2"> <div class="d-flex justify-content-between"> <div class="d-flex flex-row align-items-center"> <div class="icon"> <i class="bx bxl-mailchimp"></i> </div> <div class="ms-2 c-details"> <h6 class="mb-0">Vethanathan</h6> <span>4 days ago</span> </div> </div> <div class="badge"> <span>Python</span> </div> </div> <div class="mt-5"> <h3 class="heading">Automatic Attendence System</h3><br> <div class="badge"><button class="btn btn-primary btn-sm"> <i class="fa fa-plus"></i> Download </button> </div> <div class="mt-5"></div> </div> </div> </div> \n <!-- <p>vetha</p> -->'
    fin = open("templates/dashboard.html", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace("<!-- <p>vetha</p> -->", '<div class="col-md-4"> <div class="card p-3 mb-2"> <div class="d-flex justify-content-between"> <div class="d-flex flex-row align-items-center"> <div class="icon"> <i class="bx bxl-mailchimp"></i> </div> <div class="ms-2 c-details"> <h6 class="mb-0">Vethanathan</h6> <span>4 days ago</span> </div> </div> <div class="badge"> <span>Python</span> </div> </div> <div class="mt-5"> <h3 class="heading">Automatic Attendence System</h3><br> <div class="badge"><button class="btn btn-primary btn-sm"> <i class="fa fa-plus"></i> Download </button> </div> <div class="mt-5"></div> </div> </div> </div> \n <!-- <p>vetha</p> -->')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("templates/dashboard.html", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    # with open("templatesupload.html", "r+") as f:
    #         print("naana vandhuten daaa!!!")
    #         html = f.read()
    #         f.seek(0)
    #         f.write(html.replace("<!-- <p>vetha</p> -->", string))
    return render_template("dashboard.html")

