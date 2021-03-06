

# OS module allows us to interact with the underlying operating system in several different ways
# we can navigate through file system, get file information, lookup & change environment variables

import os

#print(dir(os))      # Prints out all of the attributes and methods that we have access to within this module


print(os.getcwd())  # prinf current working directory

# os.chdir('path')      this will change the directory to provided path


"""
os.listdir()                            returns contents in the current directory
os.listdir('directory_path')            return contents in the provided directory


os.mkdir('new_directory_name')          creates a new directory/folder
os.makedirs('new_dir/sub_dir')          creates multiple nested directories/folders

os.rmdir()                              removes single provided directories
os.removedirs()                         removes multiple nested directories


os.rename('original_file_name', 'modified_file_name')           renames a file/folder
os.stat('dir or file name')             returns information about the file/folder


mod_time = os.stat('file_name').st_mtime
print(datetime.fromtimestamp(mod_time))


form root path/directory prints all of the directories and files in root directory as well as sub directories inside root.
for dirpath, dirnames, filenames in os.walk('directory_path'):
    print('current_path:', dirpath)
    print('Directories:', dirnames)
    print('Files', filenames)
    print()



os.environ                      prints all of the environment variables
os.environ.get('HOME')          To get value of particular environment variable

Create a file at required path:

filepath = os.path.join(os.environ.get('HOME'), 'test.txt')
with open(file_path, 'w') as f:
    pass


os.path.basename('path')            prints basename i.e base file name
os.path.dirname('path')             prints directory name
os.path.split('path')               returns a tuple with  directory name fisrt and filename second
os.path.exists('path')              To check if a path exists or not. Returns True/False
os.path.isdir('path')               To check if a path is directory
os.path.isfile('path')              To check if a path is file
os.path.splittext('path')           Splits file path and extension


"""
