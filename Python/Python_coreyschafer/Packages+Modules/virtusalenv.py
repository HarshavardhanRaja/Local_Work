

"""
Virtualenv is a way that we can seperate different python environments for different projects.
Provides an isolated environments for different projects with only the dependencies, packages and specific versions they need

"""

# pip install virtualenv                                Installs virtusal env
# virtualenv [environment_name]                         creates an virtual environment with the provided name
# source [envirnment_name]/bin/activate                 Activates the virtual environment
# which python                                          to know which environment working on
# pip freeze --local  > requirements.txt                to output dependencies from virtual env
# deactivate                                            to get out of virtual environment
# rm -rf [environment_name]                             to completely remove the environment
