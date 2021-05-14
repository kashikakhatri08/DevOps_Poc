import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='kashika', password='kashika08')

jobs = server.get_all_jobs(folder_depth=None)
print(jobs)

server.build_job('jenkins_freestyle_test1' ,parameters=None, token=None)

