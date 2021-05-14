import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='kashika', password='kashika08')


jobs = server.get_all_jobs(folder_depth=None)
# list of all jobs available
#print(jobs)

# build job remotely
#name = jobs[0]['fullname']
server.build_job('JenkinsApi_test2', parameters=None, token=None)


