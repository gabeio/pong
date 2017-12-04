from flask import Flask
from flask import request
from time import localtime, strftime

app = Flask(__name__)

@app.route('/<path>', methods=['POST'])
def all(**kwargs):
	with open("asdf", "a") as file:
		file.write('{{"time":"{}",'.format(strftime("%d-%m-%Y %H:%M:%S", localtime())))
		for key in request.form.keys():
			file.write('"{}": "{}",'.format(key, request.form[key]))
		file.write("}\n")
	return "OK"