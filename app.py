from flask import Flask, render_template, request,redirect


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods = ['POST','GET'])
def index():
     if request.method == 'POST':
         com = request.form["Company"]
         prod = request.form["Product"]
         type = request.form["TypeName"]
         inches = request.form["Inches"]
         sr = request.form["ScreenResolution"]
         cpu = request.form["Cpu Benchmark"]
         gpu = request.form["Gpu Benchmark"]
         ram = request.form["Ram"]
         mem = request.form["Memory"]
         os = request.form["OpSys"]
         we = request.form["Weight"]
         return render_template('result.html',a = com,b = prod ,c = type,d = inches,e = sr ,f = cpu ,
         g = gpu,h = ram,i = mem,j = os ,k= we)
    
if __name__ == '__main__':
    app.run(debug=True)     