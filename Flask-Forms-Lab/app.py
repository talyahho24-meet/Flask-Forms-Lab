from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "feivel"
password = "smallbabyboy"
facebook_friends=["fiona","Talyah","Curious George", "Teddy Bear", "Libi", "Celina"]


@app.route('/', methods = ['GET' , 'POST'] )  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form ['username']
		password = request.form ['password']
		if username == request.form ['username'] and password == request.form ['password'] :
			return redirect(url_for('home'))
		else: 
			return render_template ('login.html')
	
@app.route('/home', methods =['GET', 'POST'])
def home():
	return render_template('home.html' , frfr = facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run(debug=True)

@app.route ('/friend_exists/<string:name>', methods = ['GET', 'POST'])
def friend_exists(frfr, name):
	return render_template('friend_exists.html', frfr= 'facebook_friends', n = name)