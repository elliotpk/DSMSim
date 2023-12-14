from flask import Flask
import webbrowser
import os

# Creates Flask application named "app" and pass it the __name__,  which holds the name
# of the current python module, flask needs it for some work behind the scenes
app = Flask(__name__) 
    
@app.route('/') # Tells python it will work with a web browser (HTTP client)

def hello():
    return "<p>Hello, World!</p>"

htmlLocation = os.path.dirname(os.path.realpath(__file__)) + "\\" + 'test.html'

webbrowser.open_new_tab(htmlLocation)

# Skriv i powershell:
# DSMSimGrupp92023/.venv/Scripts/Activate.ps1
# python -m flask --app .\Src\GUI.py run
# Länk för guide: https://medium.com/@dipan.saha/managing-git-repositories-with-vscode-setting-up-a-virtual-environment-62980b9e8106