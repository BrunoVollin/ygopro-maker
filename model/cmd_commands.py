import os
class Commands:
    def __init__(self, cmd_projectname):
            self.cmd_projectname = cmd_projectname

    def cmd_create_project(self):
        os.system("ygofab new " + self.cmd_projectname)
    def cmd_update_project(self):
        os.system("ygofab make ")
    def cmd_sync_project(self):
        os.system("ygofab sync ")
    def cmd_compose_project(self):
        os.system("ygofab compose ")