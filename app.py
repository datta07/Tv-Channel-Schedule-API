from sch import main_fun
from flask import Flask,send_file,current_app,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
	return "generic api services @garudadev.com"

@app.route('/getCategories')
def getCategories():
	return jsonify(main_fun.getCategories())

@app.route('/searchChannel')
def searchChannel():
	lang,cate=False,False
	if ("lang" in request.args):
		lang=request.args["lang"]
	if ("cate" in request.args):
		cate=request.args["cate"]
	try:
		return jsonify(main_fun.searchChannel(lang,cate))
	except Exception as e:
		print(str(e))
		return "failed:invalid parameters or no parameters,<br>search /getCategories"

@app.route('/TodaySchedule')
def TodaySchedule():
	channel=False
	offset=0
	if ("channel" in request.args):
		channel=request.args["channel"]
	return jsonify(main_fun.TodaySchedule(channel,offset))

@app.route('/Schedule')
def Schedule():
	channel=False
	offset=0
	if ("channel" in request.args):
		channel=request.args["channel"]
	if ("offset" in request.args):
		offset=request.args["offset"]
	return jsonify(main_fun.TodaySchedule(channel,offset))

@app.route('/GetTodaysMovies')
def GetTodaysMovies():
	lang=False
	offset=0
	if ("lang" in request.args):
		lang=request.args["lang"]
	if ("offset" in request.args):
		offset=request.args["offset"]
	return main_fun.GetTodaysMovies(lang,offset)

#app.run()
