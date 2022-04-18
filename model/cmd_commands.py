import os
class Commands:
    def __init__(self, cmd_projectname):
            self.cmd_projectname = cmd_projectname

    def cmd_create_project(self):
        os.system("ygofab new " + self.cmd_projectname)
