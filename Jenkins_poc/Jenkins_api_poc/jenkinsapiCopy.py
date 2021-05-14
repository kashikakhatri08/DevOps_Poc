import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='kashika', password='kashika08')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


#create job
"""
server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print(jobs)
"""

"""
my_job = server.get_job_config('jenkins_pipeline_test4')
print(my_job)
"""

"""
server.build_job('empty')
server.disable_job('empty')
server.copy_job('empty', 'empty_copy')
server.enable_job('empty_copy')
server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)
"""

"""
server.delete_job('empty')
server.delete_job('empty_copy')
"""


# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
"""
server.build_job('Jenkins_triggerTest', {'Building_String': 'Building', 'Testing_String': 'Testing', 'Deployment_String': 'Deployment'})
last_build_number = server.get_job_info('Jenkins_triggerTest')['lastCompletedBuild']['number']
build_info = server.get_build_info('Jenkins_triggerTest', last_build_number)
print(build_info)
"""

#get jb of a view
"""
jobs = server.get_jobs(view_name='My_view')
print(jobs)
"""

#Create a view
"""
server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)
view_config = server.get_view_config('EMPTY')
views = server.get_views()
server.delete_view('EMPTY')
print(views)
"""

#print a dictionary containing all the plugins that are installed on the Jenkins server.
"""
plugins = server.get_plugins_info()
print(plugins)
"""
#jenkins node
"""
server.create_node('slave1')
nodes = get_nodes()
print(nodes)
"""

