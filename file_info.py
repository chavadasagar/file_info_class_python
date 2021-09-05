import os

print(os.path.exists("LICENSE.txt"))

class file_info:
    folder = []
    file = []

    no_of_file = 0
    no_of_dir = 0
    def __init__(this,cwd = os.getcwd()):
        for cwd,dir_name,file_name in os.walk(cwd):
            for d_name in dir_name:
                this.folder.append(d_name)
                this.no_of_dir +=1
            for f_name in file_name:
                this.file.append(f_name)
                this.no_of_file+=1
                
file = file_info(".")
