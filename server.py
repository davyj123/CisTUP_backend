from flask import Flask,jsonify,request,send_from_directory,render_template
from flask_cors import CORS
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from vehicle_counting import detectVehicle


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

UPLOAD_FOLDER = 'static/uploaded/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload',methods=['POST'])
def res():
    file = request.files['file']
    errors = {}
    success = False

    if file and allowed_file(file.filename):
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        filename = dt_string+secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        detectVehicle(filename)
        success = True
        resp = jsonify({
            "message": 'File uploaded successfully',
            "status": 'success'  
        })
        return resp
    else:
        resp = jsonify({
            "message": 'File not uploaded',
            "status": 'failed'
        })
        return resp


@app.route('/api/listdata',methods=['GET'])
def listdata():
    
    files = os.listdir('static/uploaded')
    
    data = []
    url = request.host_url
    for filename in files:
        data.append({
            "name":filename,
            "original": url+"original/"+filename,
            "processed":url+"processed/"+filename
        })
        
    resp = jsonify({
        "data": data,
        "status": 'success'
    })
    return resp


@app.route('/original/<name>',methods=['GET'])
def show_img(name):
    file_exists = os.path.isfile(os.path.join("static/uploaded",name))
    
    if file_exists:
        # return send_from_directory("./uploaded",name,as_attachment=True)
        return render_template("index.html",src="uploaded/"+name)
    else:
        resp = jsonify({
            "data": "No file found",
            "status": "error"
        })
        return resp

@app.route('/processed/<name>',methods=['GET'])
def show_pimg(name):
    file_exists = os.path.isfile(os.path.join("static/processed",name))
    
    if file_exists:
        # return send_from_directory("./processed",name,as_attachment=True)
        return render_template("index.html",src="processed/"+name)
    else:
        resp = jsonify({
            "data": "No file found",
            "status": "error"
        })
        return resp

if __name__ == "__main__":
    app.run(host='127.0.0.2',port=5000,debug=True)