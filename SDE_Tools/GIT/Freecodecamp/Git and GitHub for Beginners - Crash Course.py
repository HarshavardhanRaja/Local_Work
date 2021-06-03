# https://www.youtube.com/watch?v=RGOj5yH7evk&t=851s


"""
What is Git?
=> Free & Open Source Version control system.


What is Version Control System?
=> The management of changes to documents, computar programs, large websites and other collections of information.

"""


"""
Important Terms:
    => Directory                -> Folder
    => Terminal/Command Line    -> Interface for text commands 
    => CLI                      -> Command Line Interface
    => cd                       -> change directory
    => Code Editor              -> Word processor for writing code
    => Repository               -> Project or the folder/place where your code is kept
    => Github                   -> A website to host your repositories online
"""


# IMP GIT Commands
"""
clone -> Bring a repository that is hosted somewhere like Github into a folder on your local machine.
add -> Track your files and changes in it.
commit -> Save your files in GIT.
push -> Upload git commits to remote repo, like Github.
pull -> Download changes from remote repo to your local machine, the opposite of push.

"""




# Github workflow
# Local Git workflow

# Workflow1
"""

-> git clone [repo_link]    this will clone the repo from github to local machine
-> cd [repo_name]
-> ls -la                   List everything including hidden folders and files

Now all files from repo are copied to your local machine.
Make the changes you want in that copied folder/repo.

-> git status               Shows all of the files that are updated/created/deleted
-> git add .                tell git to track newly created file before saving it 
-> git commit -m "add the comments about the commit"  this saves the changed/modified files to local repo
-> git push origin master                when you are running it first time you have to create a ssh key and add it in github
-> 

"""




# Workflow-2
"""

-> git init         initialize git repository for this current folder

now add/remove/modifiy files as you want

-> git status
-> git add .
-> git status
-> git commit -m "message"

As we didnot cloned this from any github repository we cannot directly push this
First create an empty git repo in github or other git providers
copy the clone link for this empty repo

-> git remote add origin [empty repo_link]
-> git remote -v

-> git push origin master


"""


# Git Branching
"""
Master Branch: A naming convention for main or default branch of a repository

-> git branch       to know which branch you are working on

-> git checkout -b [name_of_the_branch] 

-> git checkout [branch_name]       git checkout is used to swith between branche but by adding '-b' flag it is used to create new branch

now this branch repo act as a repo and we can make all the things that we do with/to master branch
After making changes and commiting the changes to this branch repo we have to merge it to master branch
first go to master branch

-> git checkout master
-> git diff [branch_name]       shows the differences between the branches
-> git merge [branch_name]

-> git push -u origin [branch_name]     creates a new branch/ updates the branch



-> git pull             To pull changes made to master branch while we are working on code

-> git branch -d [branch_name]      to delete the branch
"""

# What is a Pull Request(PR)?
"""
It's basically a request to have your code pulled into other branch
    make a PR from child branch to master branch
    once we made a PR anyone can review our code, comment on it, ask us to make changes   
    After PR is succefull we generally delete the child branch
"""



# Merge Conflicts
"""
when you were working on makeing changes as per your task other people/developers will also be doing their
tasks paralelly on their branches and master is being updated from multiple developers


we have to manually handle these kind of conflicts

 
"""
 

 # Undoing 
"""
what if we accidently made some changes to master?


-> git reset HEAD~1
    Here HEAD refers to last commit made
    ~1 => last but one commit

-> git log          to see the logs/ commit history
"""


# Forking
"""
Fork: makes complete copy of the repository
    used for saving other peoples repo and play with it



"""