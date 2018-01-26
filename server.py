from flask import Flask, request, jsonify, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
import post_controller
import team_controller
import login_controller
from user_model import User
from bson import ObjectId

app = Flask(__name__)
app.secret_key = 'super secret string'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.route('/')
def index():
    return 'Hello world'

@login_manager.user_loader
def load_user(user_id):
    return login_controller.get_user(user_id)

@app.route('/signup', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return '''
        <html><body><form method="POST">
        Name: <input type="text" name="name"/><br/>
        Teams: <input type="text" name="teams"/><br/>
        Username: <input type="text" name="username"/><br/>
        Password: <input type="password" name="password"/><br/>
        <input type="submit" name="submit" value="Signup"/>
        </form></body></html>
        '''
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    teams = request.form['teams']
    team_list = teams.split(',')
    user = User(name=name, username=username, password=password)
    for team in team_list:
        user.teams.append(ObjectId(team))
    user.save()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return '''
        <html><body><form method="POST">
        Username: <input type="text" name="username"/><br/>
        Password: <input type="password" name="password"/><br/>
        <input type="submit" name="submit" value="Login"/>
        </form></body></html>
        '''
    username = request.form['username']
    password = request.form['password']
    user = login_controller.authenticate(username, password)
    if user:
        login_user(user)
        next = request.args.get('next')
        return redirect(next or url_for('index'))
    else:
        print "could not auth"
        return redirect(url_for('login'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return '<p>Logged out</p>'

@app.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
    if request.method == 'POST':
        return post_controller.create_a_post(request.get_json())
    elif request.method == 'GET':
        return post_controller.get_all_posts(current_user)

@app.route('/teams', methods=['POST'])
def post_team():
    return team_controller.create_a_team(request.get_json())

@app.route('/teams', methods=['GET'])
@login_required
def get_teams():
        return team_controller.get_all_teams(current_user)

app.run(host='0.0.0.0', port=5000, debug=True)
