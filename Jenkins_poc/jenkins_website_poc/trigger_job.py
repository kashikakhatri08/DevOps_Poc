from flask import Flask,render_template,request,json
import jenkins

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("trigger.html")
    
@app.route("/trigger",methods = ['POST'])
def trigger():
    server = jenkins.Jenkins('http://localhost:8080/', username='kashika',   password='kashika08')
    
# build job remotely
    
    server.build_job('Jenkins_triggerTest', parameters={'Building_String': 'Building','Testing_String':'Testing','Deployment_String':'Deployment'}, token=None)
    return render_template("trigger.html")
    
if __name__ == "__main__":
    app.run(debug=True)
