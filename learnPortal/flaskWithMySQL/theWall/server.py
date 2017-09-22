from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re, os, binascii, md5
app=Flask(__name__)
mysql = MySQLConnector(app, 'thewall')

NAME_REGEX = re.compile(r'[^a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
UNAME_REGEX = re.compile(r'[^a-zA-Z0-9]')
PASS1_REGEX = re.compile(r'[A-Z]')
PASS2_REGEX = re.compile(r'[0-9]')
regreq = ['fname','lname','email','uname','pw','cpw']

def uname_check():
    uname_query = 'SELECT * FROM users WHERE username = :uname'
    uname_data = {'uname':session['uname']}
    uname = mysql.query_db(uname_query,uname_data)
    return uname

def email_check():
    email_query = 'SELECT * FROM users WHERE email = :email'
    email_data = {'email':session['email']}
    email = mysql.query_db(email_query,email_data)
    return email

def msg_check(idnum):
    msgs = mysql.query_db('SELECT * FROM messages WHERE to_id = {}'.format(idnum))
    return msgs

def cmt_check(idnum):
    cmts = mysql.query_db('SELECT * FROM comments WHERE message_id = {}'.format(idnum))
    return cmts

@app.route('/')
def index():
    if 'loggedin' in session:
        if session['loggedin']==True:
            return redirect('/wall/{}'.format(session['user'][0]['username']))
    if 'message' not in session or session['message'] == False:
        session.clear()
        session['fname']=''
        session['lname']=''
        session['email']=''
        session['uname']=''
        session['pw']=''
        session['cpw']=''
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    session['fname']=request.form['fname']
    session['lname']=request.form['lname']
    session['email']=request.form['email']
    session['uname']=request.form['uname']
    session['pw']=request.form['password']
    session['cpw']=request.form['confirmation']
    session['message']=False
    for i in session.keys():
        if i in regreq:
            if len(session[i]) < 1:
                flash(u'This field is required', str(i))
                session['message']=True
    if NAME_REGEX.search(session['fname']):
        flash(u'First name can only include letters', 'fname')
        session['message']=True
    if NAME_REGEX.search(session['lname']):
        flash(u'Last name can only include letters', 'lname')
        session['message']=True
    if len(uname_check()) > 0:
        flash(u'Username is taken! Try adding a number to the end', 'uname')
        session['message']=True
    if UNAME_REGEX.search(session['uname']):
        flash(u'Username can only include letters and numbers', 'uname')
    if len(session['pw']) < 8:
        flash(u'Password must be longer than 8 characters', 'pw')
        session['message']=True
    elif (not PASS1_REGEX.search(session['pw'])) or (not PASS2_REGEX.search(session['pw'])):
        flash(u'Password must include at least 1 uppercase letter and 1 number', 'pw')
        session['message']=True
    elif session['pw'] != session['cpw']:
        flash(u'Password and confirmation must match', 'pw')
        session['message']=True
    if not EMAIL_REGEX.match(session['email']):
        flash(u'Please enter a valid email', 'email')
        session['message']=True
    if len(email_check()) > 0:
        flash(u'This email has already been used to create an account', 'email')
        session['message']=True
    if session['message']==False:
        session['salt']= binascii.b2a_hex(os.urandom(15))
        session['pw']=md5.new(session['pw']+session['salt']).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, username, password, salt, created_at, modified_at) VALUES (:fname, :lname, :email, :uname, :pw, :salt, NOW(), NOW())"
        data = {'fname':session['fname'],'lname':session['lname'], 'email':session['email'], 'uname':session['uname'],'pw':session['pw'], 'salt':session['salt']}
        mysql.query_db(query,data)
        session['user']=uname_check()
        session['loggedin'] = True
        return redirect('/wall/{}'.format(session['user'][0]['username']))
    return redirect('/')

@app.route('/login', methods=['post'])
def login():
    session['uname'] = request.form['uname']
    session['pw'] = request.form['pw']
    session['user'] = uname_check()
    print session['user']
    if session['user']:
        session['pw'] = md5.new(session['pw']+session['user'][0]['salt']).hexdigest()
        print session['pw']
        if session['user'][0]['password'] != session['pw']:
            flash(u"Sorry, it looks like either this account does not exist or your password isn't quite right  - try again or register below!", 'no_acct')
            session['message']=True
            return redirect('/')
        session['loggedin']=True
        return redirect('/wall/{}'.format(session['user'][0]['username']))
    else:
        flash(u"Sorry, it looks like either this account does not exist or your password isn't quite right  - try again or register below!", 'no_acct')
        session['message']=True
        return redirect('/')

@app.route('/wall/<uname>')
def wall_display(uname):
    if 'loggedin' not in session:
        return redirect('/')
    elif len(mysql.query_db('SELECT * FROM users WHERE username = :uname',{'uname':uname})) == 0 :
        return redirect('/')
    else:
        session['msgs']=[]
        session['auth']=[]
        session['timestamp']=[]
        session['thesecmts']=[]
        session['numocmt']=[]
        session['wall']= mysql.query_db('SELECT * FROM users WHERE username = "{}"'.format(uname))
        idnum=session['wall'][0]['id']
        session['wallname'] = session['wall'][0]['first_name'] + ' ' + session['wall'][0]['last_name']
        if int(session['user'][0]['id']) == int(idnum):
            session['home'] = True
        else:
            session['home'] = False
        session['wallmsgs']=msg_check(idnum)
        if len(session['wallmsgs']) == 0:
            session['msgs'].append('No messages yet!')
        else:
            session['numomsgs'] = len(session['wallmsgs'])
            for i in range(0,session['numomsgs']):
                cmts = []
                cmtauth = []
                cmttimestamp = []
                session['msgs'].append(session['wallmsgs'][i]['message'])
                username = mysql.query_db('SELECT username FROM users WHERE id={}'.format(session['wallmsgs'][i]['from_id']))
                session['auth'].append(username[0]['username'])
                session['timestamp'].append(session['wallmsgs'][i]['modified_at'])
                msgcmts = cmt_check(session['wallmsgs'][i]['id'])
                session['numocmt'].append(len(msgcmts))
                if session['numocmt'][i] != 0:
                    for j in range(0,session['numocmt'][i]):
                        cmts.append(msgcmts[j]['comment'])
                        username = mysql.query_db('SELECT username FROM users WHERE id={}'.format(msgcmts[j]['from_id']))
                        cmtauth.append(username[0]['username'])
                        cmttimestamp.append(msgcmts[j]['modified_at'])
                session['thesecmts'].append({'cmts':cmts, 'cmtauth':cmtauth,'cmttimestamp':cmttimestamp})
    return render_template('wall.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/message', methods=['post'])
def send_message():
    wallmsg = request.form['message']
    fromid = session['user'][0]['id']
    toid = session['wall'][0]['id']
    query = "INSERT INTO messages (message, from_id, to_id, created_at, modified_at) VALUES (:message, :fromid, :toid, NOW(), NOW())"
    data = {'message':wallmsg, 'fromid': fromid, 'toid':toid}
    mysql.query_db(query,data)
    return redirect('/wall/{}'.format(session['wall'][0]['username']))

@app.route('/comment', methods=['post'])
def add_comment():
    msgid = request.form['msgid']
    cmt = request.form['cmt']
    fromid = session['user'][0]['id']
    to_id = mysql.query_db("SELECT from_id FROM messages WHERE id = {}".format(msgid))
    toid = session['wall'][0]['id']
    query = "INSERT INTO comments (message_id, comment, from_id, to_id, created_at, modified_at) VALUES (:messageid, :comment, :fromid, :toid, NOW(), NOW())"
    data = {'messageid': msgid, 'comment': cmt,'fromid': fromid, 'toid':toid}
    mysql.query_db(query,data)
    return redirect('/wall/{}'.format(session['wall'][0]['username']))

app.secret_key = 'key'
app.run(debug=True)
