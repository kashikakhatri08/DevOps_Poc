import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='kashika', password='kashika08')
print(server)
#version
print(server.get_version())


#jobs count
print(server.jobs_count())

#printalljobs
jobs = server.get_all_jobs(folder_depth=None)
# list of all jobs available
print(jobs)

#jon info
info = server.get_job_info('jenkins_pipeline_test4')
print(info)
# Passed
print(info['lastCompletedBuild'])
# Unstable
print(info['lastUnstableBuild'])
# Failed
print(info['lastFailedBuild'])

#job metadata
builds = info['builds']
for build in builds:
    print(server.get_build_info('jenkins_freestyle_test1', build['number'])) 
  
#job config
myJob=server.get_jobs('jenkins_pipeline_test4')
myConfig=server.get_job_config('jenkins_pipeline_test4')
print (myConfig)
#new = myConfig.replace('<string>clean</string>', '<string>string bean</string>')



