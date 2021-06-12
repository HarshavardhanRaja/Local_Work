
# what is pip ?
"""
pip is a package-management system written in Python used to install and manage software packages. 
It connects to an online repository of public packages, called the Python Package Index. 
pip can also be configured to connect to other package repositories, provided that they comply to Python Enhancement Proposal 503
"""


# pip -h
# pip help [specific command]
# pip search [package name]         to find the package and return it's description
# pip install [package name]        to install the package
# pip list                          lists all the packages that we installed
# pip uninstall [package name]      to uninstall a package
# pip list -o (--outdated)          lists all outdated packages
# pip install -U [package name]     To update a package 
# pip freeze --local | grep -v '^\-e' | cut -d = f 1 | xargs -n1 pip install -U         To update all outdated packages



# pip freeze > requirements.txt     Outputs all the packages into an requrements.txt file
# pip install -r requirements.txt   Installs all the packages present in the requirements.txt file
