import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, send_file, render_template, flash, redirect, url_for
import pickle
import urllib.request
import os,sys
from test import get_parser, main
from werkzeug.utils import secure_filename


from PIL import Image
#from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './templates/static/uploads/'
SAVE_FOLDER = './templates/static/removal/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


# app
app = Flask(__name__, static_folder=os.path.abspath('./templates/static'))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
#app.config.from_object(os.environ['APP_SETTINGS'])
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['DEBUG']=True
from model import Result, db

from flask_cors import CORS
CORS(app)
# routes


#@app.route('/', methods=['POST','GET'])
def home():
	print('yo')
	if request.method=='GET':
		return render_template('index.html')
	#return "WELCOME TO SHADOWSIGHT"

#@app.route('/predict', methods=['POST','GET'])
def predict(impath,fname):
	if request.method=='GET':
		return render_template('index.html')
	#data = request.get_json(force=True)
	print('hi2')

	parser, unknown = get_parser().parse_known_args()
	parser.image_path=impath
	parser.load = '1500'
	res = main(parser)
	#os.system('python test.py -l 1500 -i "./bb.png"')
	#output = {'results': int(result[0])}
	print('hi')
	# return data
	#return jsonify(results=output)
	#res.save('temp.png')
	pix = np.array(res)
	output = {'results': pix.tolist()}


	# return data
	#return jsonify(results=output)

	# CONVERSION TO IMAGE
	im = output['results']

	im_new = np.array(im)
	removal_im = Image.fromarray(im_new.astype('uint8'), 'RGB')
	predname = fname.split('.')[0]+'_removed.'+fname.split('.')[1]
	spath=SAVE_FOLDER+predname
	removal_im.save(spath)
	fname='./removal_rec.png'
	#return send_file('./removal_rec.png')
	#return render_template('index.html', fpath=spath)
	return predname

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	
	return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload_image():
	print(os. getcwd())

	file = request.files['file']
	print(file)
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		print('upload_image filename: ' + filename)

		spath = predict(UPLOAD_FOLDER+filename, filename)

		return render_template('index.html', fname=str(spath),filename=str('/static/uploads/'+filename),predpath=str('/static/removal/'+spath))
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>', methods=['GET', 'POST'])
def display_image(filename):
	print('display_image filename: ' + filename)
	#return redirect(url_for('./templates/static', filename=filename), code=301)
	return send_file(os.path.join(SAVE_FOLDER,filename),as_attachment=True)



if __name__ == '__main__':
	#db.init_app(app)
	app.run(port=8889, debug=True)	
	#app.run(debug=True)