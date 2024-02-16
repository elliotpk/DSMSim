from flask import Flask,url_for,render_template
import webbrowser
import pymongo

# Creates Flask application named "app" and pass it the __name__,  which holds the name
# of the current python module, flask needs it for some work behind the scenes
app = Flask(__name__) 
    
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
city = mydb["city"]

y = []
for x in mycol.find():
  y.append(list(x.values()))

a = y[0]
b = y[1]
c = y[2]

companyNames = ['Company 1','Company 2','Company 3']

z = []
for x in city.find():
  z.append(list(x.values()))
temp = []
for x in z:
    temp.append(x[1])
z = temp
    

@app.route('/') # Tells python it will work with a web browser (HTTP client)
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template("result.html", names = companyNames, data = y)

@app.route('/sortfairness')
def sortfairness():
    fair = []
    i = 0
    sort = []
    for x in y:
        fair.append(int(x[2]))
    for x in fair:
        sort.append(x)
    sort.sort(reverse=True)

    temp = []
    temp2=[]
    j = 0

    while(j < len(sort)):
        i = 0
        while(i < len(sort)):
            if(int(sort[j]) == int(fair[i])):
                temp+=[companyNames[i]]
                temp2+=[y[i]]
                i+=1
            else:
                i+=1
        y2 = temp2
        companyNames2 = temp
        j+=1

    return render_template("sortfairness.html", names = companyNames2, data = y)

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