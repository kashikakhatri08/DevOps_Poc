from flask import Flask,render_template,request
import json
import jenkins

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("trigger.html")
    
@app.route("/trigger", methods=['POST'])
def trigger():
    data=request.json
    print(data)
    print(type(data))
    server = jenkins.Jenkins('http://localhost:8080/', username='kashika',   password='kashika08')
    
    
    server.build_job(data['name'], parameters=data['parameter'], token=None)
    
    return json.dumps(data)
    
if __name__ == "__main__":
    app.run(debug=True)
    """
    {
    "name":"Jenkins_triggerTest",
    "parameter":{"Building_String":"Building",
    "Testing_String":"Testing",
    "Deployment_String":"Deployment"
    }
}
    
    """
