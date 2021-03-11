from flask import Flask, render_template, request, redirect,send_file
from werkzeug.utils import secure_filename
from functions import split,transform
import io
import os
import pdfrw
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm,mm

space = 2.4*mm
space_q = (2.6*mm,4.5*mm)
max_h = 296.93*mm
w = -38.6*mm + 42.7*mm#-0.02*mm
h = (125.7*mm - 121.9*mm)#+1*mm
# print(h,w)
start_id = (35.7*mm, max_h-135.3*mm+0.45*mm)
start_q = (36.8*mm,max_h-208.3*mm+0.45*mm)
error = 0.25*mm
x_name = 110*mm
y_name = 175*mm

MAX_ITENS = 6
parameters = [space,space_q,max_h,w,h,start_id,start_q,error,x_name,y_name,y_name]

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/",methods=["POST", "GET"])
def upload_page():
    if request.method == "GET":
	    return render_template("index.html")
    else:
        uploaded_file = request.files['file']
        if uploaded_file != '':
            print(os.getcwd())
            arq = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
            print(arq)
            uploaded_file.save(arq)
        name= request.form["name"]
        page = int(request.form["page"])
        id = request.form["id"]
        quest = request.form["quest"]
        if quest == "":
            for i in range(1,MAX_ITENS+1):
                key = "customRadioInline"+str(i)
                try:
                    quest += request.form[key]
                except KeyError:
                    quest += "."
        print(quest)
        
        output = os.path.join(app.config['UPLOAD_FOLDER'],
        "Gabarito_"+"_".join(name.split()))
        split(arq, page, output+".pdf")
        transform(id,quest,output,name,parameters)
        return send_file(output+".pdf")#,mimetype = '.pdf')

    os.remove(output+".pdf")
    os.remove(arq)
if __name__ == "__main__":
    #app.run(debug=True, host= '0.0.0.0')
    app.run()