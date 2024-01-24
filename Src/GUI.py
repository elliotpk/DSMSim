from flask import Flask,url_for,render_template
import webbrowser
import pymongo

# Creates Flask application named "app" and pass it the __name__,  which holds the name
# of the current python module, flask needs it for some work behind the scenes
app = Flask(__name__) 
    
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

y = []
for x in mycol.find():
  y.append(list(x.values()))

a = y[0]
b = y[1]

@app.route('/') # Tells python it will work with a web browser (HTTP client)
def index():
    return render_template('index.html')


companyNames = ['Company 1','Company 2','Company 3']
@app.route('/result')
def result():
    return render_template("result.html", names = companyNames, data = a, data2 = b)


@app.route('/config')
def config():
    return render_template("config.html")


htmlLocation = 'http://127.0.0.1:5000'
webbrowser.open_new_tab(htmlLocation)

app.run()



# Skriv i powershell:
# DSMSimGrupp92023/.venv/Scripts/Activate.ps1
# python -m flask --app .\Src\GUI.py run
# Länk för guide: https://medium.com/@dipan.saha/managing-git-repositories-with-vscode-setting-up-a-virtual-environment-62980b9e8106