from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, World!"

@app.route("/<name>")
def say_hello(name):
	return "Hello, %s!" % (name)

if __name__ == "__main__":
	app.run(host="0.0.0.0")

