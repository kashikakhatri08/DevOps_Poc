import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='kashika', password='kashika08')

info = server.get_info()
jobs = info['jobs']
totalBuildCount = 0
  


for job in jobs:
    jobName = job['name']
    
    #name of jobs
    
    jobinfo = server.get_job_info(jobName)

    #job info:
     #1.class,
     #2.description
     #3.actions
     #4.displayName
     #5.displayNameOrNull
     #6.fullDisplayName
     #7.fullName
     #8.url
     #9.buildable
     #10.builds
    
    builds = jobinfo['builds'] 
    #print(builds)

    #1.builds:
       #1.class
       #2.number
       #3.url
    
    print(jobName + " build count: " + str(len(builds)))

    #jenkins_freestyle_test1 build count: 15
    #jenkins_freestyle_test2 build count: 7
    #jenkins_freestyle_test3 build count: 11
    #jenkins_pipeline_test1 build count: 23
    #jenkins_pipeline_test2 build count: 10
    #jenkins_pipeline_test3 build count: 5
    #jenkins_pipeline_test4 build count: 2
    #jenkins_pipeline_test5 build count: 8
    #Jenkins_triggerTest build count: 82
    #JenkinsApi_test1 build count: 9
    #JenkinsApi_test2 build count: 2
    #ScriptTesting build count: 12
    
    totalBuildCount += len(builds)

print("Total build count: " + str(totalBuildCount))

#Total build count: 186


info_job = server.get_job_info('Jenkins_triggerTest_copy')
# Loop over builds
builds_job = info_job ['builds']
for build in builds_job:
    print(server.get_build_info('Jenkins_triggerTest_copy', 
                                    build['number'])) 
    
single_job_info = server.get_job_info('jenkins_freestyle_test1')  
print(server.get_build_info('jenkins_freestyle_test1',1, depth=0))   
    
    
    
    
"""   
workflow_info = server.get_workflow_info('Jenkins_triggerTest_copy',1)
print(workflow_info)
"""


