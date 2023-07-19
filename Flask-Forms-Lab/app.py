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
			return render_template('home.html')
		else: return render_tamplate ('login.html')
	
	@app.route('home')
	def home():
		return render_template_('home.html')

'facebook_friends' = frfr
	return render_template('home.html, value = frfr')
	





if __name__ == "__main__":  # Makes sure this is the main process
	app.run(debug=True)

