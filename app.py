# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Afzal" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/f")

# define the route to mother webpage
@app.route("/m")

# define the route to friends webpage
@app.route("/fr")

# add other routes, if you want

# run the file
app.run(debug=True)
