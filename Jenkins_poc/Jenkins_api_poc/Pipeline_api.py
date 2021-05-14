import requests

print("##.GET Pipeline job last build description.")
url= "http://localhost:8080/job/jenkins_pipeline_test2/9/wfapi/"
response = requests.request("GET", url)
data = response.json()
print (data['stages'])
print (data['name'])
print (data['id'])
print (data['status'])

print("#1.GET Pipeline job description")
url1 ="http://localhost:8080/job/Jenkins_triggerTest_copy/wfapi/"
response1 = requests.request("GET", url1)
data1 = response1.json()
print(data1)
print (data1['name'])
print (data1['runCount'])

print("#2.GET Pipeline job last build description.")
url2 = "http://localhost:8080/job/Jenkins_triggerTest_copy/lastBuild/wfapi/"
response2 = requests.request("GET", url2)
data2 = response2.json()
print (data2['stages'])
print (data2['name'])
print (data2['id'])
print (data2['status'])

print("#3.Pipeline job run History.")
url3= "http://localhost:8080/job/Jenkins_triggerTest_copy/wfapi/runs/"
response3= requests.request("GET", url3)
data3 = response3.json()
print(data3)
print (data3[0]['stages'])

print("#4.a single Workflow run.")
url4= "http://localhost:8080/job/Jenkins_triggerTest_copy/1/wfapi/describe"
response4= requests.request("GET", url4)
data4 = response4.json()
print(data4)
print (data4['status'])

print("#5.Get the pending input action details for a Pipeline run")
url5= "http://localhost:8080/job/Jenkins_triggerTest_copy/1/wfapi/pendingInputActions/"
response5= requests.request("GET", url5)
data5 = response5.json()
print(data5)

print("#6.Get the build artifacts for a Pipeline run.")
url6= "http://localhost:8080/job/Jenkins_triggerTest_copy/1/wfapi/artifacts/"
response6= requests.request("GET", url6)
data6 = response6.json()
print(data6)

print("#7.Get a description of a Pipeline node.")
url7 ="http://localhost:8080/job/Jenkins_triggerTest_copy/1/execution/node/16/wfapi/describe/"
response7= requests.request("GET", url7)
data7 = response7.json()
print(data7)
print(data7['id'])

print("#8.Get the log for a Pipeline node.")
url8= "http://localhost:8080/job/Jenkins_triggerTest_copy/1/execution/node/16/wfapi/log/"
response8= requests.request("GET", url8)
data8 = response8.json()
print(data8)
print(data8['nodeStatus'])





