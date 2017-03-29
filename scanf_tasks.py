#!/home/tops/bin/python
import commands
import os
cgrulesConfigPath = '/etc/cgrules.conf'
match_format = {'bash':'.sh','python':'.py'}

def ExecuteCmd(cmd):
    code, stdout = commands.getstatusoutput(cmd)
    if code != 0:
        print "Execute cmd FAIL: " + cmd
        print code
        print stdout
        sys.exit(-1)
    return stdout

class CgrulesItem(object):
    def __init__(self):
	global cgrulesConfigPath
	self.conf_path = cgrulesConfigPath

    def get_item(self):
        if os.path.exists(self.conf_path):
	    with open(self.conf_path) as f:
	        for line in f.readlines():
		    if not line.strip() or line.startswith('#'):
			continue
		    #return line.strip().split()[:] 
		    yield line.strip().split()

    def tasks_distribute(self):
	pass 

	

if __name__=='__main__':
	for item in CgrulesItem().get_item():
		user,process,subsyslist,cgroup = item[0].split(':')[0],item[0].split(':')[1],item[1].split(','),item[2] 	
		print user,process,subsys,cgroup
		cmd="ps aux|grep %s"  %process
		str=ExecuteCmd(cmd)
		print str
