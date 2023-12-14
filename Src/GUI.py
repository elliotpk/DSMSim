from flask import Flask,url_for,render_template
import webbrowser
import os

# Creates Flask application named "app" and pass it the __name__,  which holds the name
# of the current python module, flask needs it for some work behind the scenes
app = Flask(__name__) 
    
@app.route('/') # Tells python it will work with a web browser (HTTP client)

def hello():
    return render_template('index.html')

htmlLocation = 'http://127.0.0.1:5000'

webbrowser.open_new_tab(htmlLocation)

# Skriv i powershell:
# DSMSimGrupp92023/.venv/Scripts/Activate.ps1
# python -m flask --app .\Src\GUI.py run
# Länk för guide: https://medium.com/@dipan.saha/managing-git-repositories-with-vscode-setting-up-a-virtual-environment-62980b9e8106