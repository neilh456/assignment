from flask import Flask
import requests
#import json
#from flask import render_template

# Create Application
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to IP Location App"

@app.route("/hello")
def hello_world():
    return "Hello World"

@app.route("/country")
def get_country():
    ip = requests.get('https://api.ipify.org').text
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    country = response['country_name']
    return f"Hello from {country}"
    #return render_template('IPCountry.html', ip=ip,country=country)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=4000)

