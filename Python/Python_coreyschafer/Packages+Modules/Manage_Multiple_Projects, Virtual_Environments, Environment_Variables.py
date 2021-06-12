# https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
"""
When you are working on multiple project at once it's easy to get dependencies to mixed up 
and it's also hard to keep track of virtyal environments and environment variable


Create a directory for new project:
    mkdir [directory_name]  
    cd [directory_name]


Create a virtual environment and install required packages with their versions:
    conda create --name [environment_name] flask sqlalchemy numpy pandas
    source activate [environment_name]
    pip list / conda list


environment.yaml file that captures everything about our environment and can be used to build the same environment from scratch
    conda env export > environment.yaml
    cat environment.yaml

If you want recreate an environment using yaml file:
    conda env create -f environment.yaml



Environment variable: are used in many different projects to set,
    database urls, hold secret keys, set a python path etc
    These are used to access sensitive data without actually outting it into our project code 


    conda env list              copy the path of env you are working on
    cd [env_path]
    



"""

