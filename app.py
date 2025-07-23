from flask import Flask,render_template,request,session,redirect,flash,send_file
import sqlite3
import csv
from database import init_db
app=Flask(__name__)
app.secret_key="Sunny"

# def init_db():
#     # Connect to SQLite (this will create data.db if it doesn't exist)
#     conn = sqlite3.connect('data.db')
#     c = conn.cursor()  #to implement all the commands 
 
#     # Create the responses table
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS responses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT,
#             age INTEGER,
#             gender TEXT,
#             contact_number TEXT,
#             email TEXT,
#             address TEXT,
#             education TEXT,
#             occupation TEXT,
#             income_range TEXT,
#             device_availability TEXT,
#             learning_language TEXT,
#             learning_mode TEXT,
#             time_slot TEXT,
#             main_skill TEXT,
#             sub_skill TEXT,
#             experience_level TEXT,
#             motivation TEXT,
#             commitment TEXT,
#             special_needs TEXT,
#             referred_by TEXT
#         )
#     ''')
 
#     # Commit changes and close connection
#     conn.commit()
#     conn.close()
 
#     print("✅ Database initialized and table created (if not already).")

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Admin')
def admin():
    if session.get('Admin_login'):
        conn=sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute(" SELECT * FROM responses ")
        data=c.fetchall()
        conn.close()
        return render_template('Dashboard.html',responses=data)
    return render_template('Login.html')

@app.route("/Logout")
def Logout():
    session['Admin_login']=False
    return render_template('Login.html')



@app.route('/Login', methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form.get("Username")
        Password = request.form.get("Password")
        if username == "admin" and Password == "vamsi":
            session['Admin_login'] = True
            return redirect('/Dashboard')
        else:
            flash("Invalid credentials")
            return redirect('/Login')
    return render_template('Login.html')
    



@app.route('/Surveyform')
def Surveyform():
    return render_template('Survey.html')

@app.route('/Backtohome')
def Backtohome():
    return render_template('Home.html')

@app.route('/Dashboard')
def Dashboard():
    if not session.get('Admin_login'):
        return render_template('Login.html')
    conn=sqlite3.connect('data.db')
    c=conn.cursor()
    c.execute(" SELECT * FROM responses ")
    data=c.fetchall()
    conn.close()
    return render_template('Dashboard.html',responses=data)

@app.route('/DownloadCSV')
def DownloadCSV():
    conn=sqlite3.connect('data.db')
    c=conn.cursor()
    c.execute(" SELECT * FROM responses ")
    data=c.fetchall()
    headers=[d[0] for d in c.description]
    conn.close()   
    
    with open('output.csv','w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    return send_file('output.csv',as_attachment=True)

@app.route('/Survey',methods=["POST","GET"])
def submit_survey():
    # Get data from form
    if request.method=='POST':
        full_name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        contact_number = request.form.get('contact') or 'Not Given'
        email = request.form.get('email') or 'Not Given'
        address = request.form.get('address')
        education = request.form.get('education')
        occupation = request.form.get('occupation')
        income_range = request.form.get('income')
        device_availability = ', '.join(request.form.getlist('device')) or 'None'
        learning_language = request.form.get('language')
        learning_mode = request.form.get('learning_mode')
        time_slot = request.form.get('time_slots')
        main_skill = request.form.get('main_skill')
        sub_skill = request.form.get('sub_skill')
        experience_level = request.form.get('experience')
        motivation = request.form.get('motivation') or 'Not Given'
        commitment = request.form.get('commit_time') or 'Not Given'
        special_needs = request.form.get('special_needs') or 'None'
        referred_by = request.form.get('referred_by') or 'Not specified'

    
        # Insert into SQLite DB
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
    
        c.execute('''
            INSERT INTO responses (
                full_name, age, gender, contact_number, email, address, education,
                occupation, income_range, device_availability, learning_language,
                learning_mode, time_slot, main_skill, sub_skill, experience_level,
                motivation, commitment, special_needs, referred_by
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            full_name, age, gender, contact_number, email, address, education,
            occupation, income_range, device_availability, learning_language,
            learning_mode, time_slot, main_skill, sub_skill, experience_level,
            motivation, commitment, special_needs, referred_by
        ))
    
        conn.commit()
        flash("Form Submitted Successfully")
        return redirect('/Survey')
    return render_template('/Survey.html')


if __name__=='__main__':
    init_db()
    app.run(port=8080,debug=True)
    
     