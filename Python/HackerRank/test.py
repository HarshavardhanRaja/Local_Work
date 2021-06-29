import os


subdomains = ["Introduction",
            "Basic_Data_types",
            "Strings",
            "Sets",
            "Math",
            "Itertools",
            "Collections",
            "Date_and_time",
            "Errors_and_exceptions",
            "Classes",
            "Built-ins",
            "Python_Functionals",
            "Regex_and_parsing",
            "XML",
            "Closures_and_Decorators",
            "Numpy",
            "Debugging"
]

start = os.getcwd()

#for dirpath, dirnames, filenames in os.walk(os.getcwd()):
# os.walk('directoray+path') returns an generator object which is a tupels of,
# ('directory_path', [list of directories], [list of files])
directories = []
for a,b,c in os.walk(os.getcwd()):
    directories.append(b)

for directory in directories[0]:
    for subdomain in subdomains:
        os.mkdir(start+'/'+directory+'/'+subdomain)
    print(directory)

