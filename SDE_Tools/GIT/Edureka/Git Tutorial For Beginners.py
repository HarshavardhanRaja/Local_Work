"""
What is Version Control?
What is GIT?
GIT Operations & Commands
Introduction to SSH keys
"""


"""
5 aspects of git operations
    setting up repositories
    Saving changes
    Inspecting repositories
    undoing change
    rewriting history

"""


# What is Version Control system?
"""

Version control is a system that records changes to a file or set of files over time so that you can recall
specific version later.
These versions are called repository and can be recalled from the same
There are Local, Centralized, Distributed Version control systems


Advantages:
    Collaboration       -> Shared workspace and realtime updates
    Manage version      -> All versions of code are preserved
    Roll backs          -> Easy rollback from current version
    Reduce Downtime     -> Reverse faulty update and save time
    Analyse Project     -> Analyze and compare versions
"""


# What is GIT?
"""
    
GIT:    
    -> Is one of the most used/ popular version control system
    -> Is a Distributed version control system that supports distributed non-linear workflows by providing 
        data assurance for developing quality software
    -> It lets you and your team of developers work together on the same project from anywhere
    -> Team members can work on files and easily merge their changes into source


What is a Repository?
    -> A repository or repo is a directory/storage space where projects can live.
    -> It can be local to a folder on your computer 
    -> or it can be a storage space on another online host (Github).
    -> you can keep code files, text files, image files, you name it, inside a repository.
"""



# Git commands & Operations
"""
Set up Repo:
    git init
        -> Creates a new or empty git repository
        -> It can be used to convert an existing, unprovisioned project to a git repository
        -> Most other git commands are not available outside of an initialized repository
        -> This is usually the first command you'll run in a new project
    git clone
        -> Used to target an existing repository and clone or copy the target repository to local machine
    git config
        -> Is a convenience function that is used to set git configuration values on a global or local project level
        -> Executing git config will modify the configuration text file 
        -> git config --global user.email "user@example.com"
    git alias
        -> Aliases are used to create shorter commands that map to longer commands. 
        -> They enable workflows by requiring fewer key strokes to execute a command.
            However, there isn't any direct command for an alias
        -> Aliases are created through the git config command
        -> git config --global alias.co checkout 

Save changes:
    git add
        -> Adds a change in the working directory to the staging area
        -> It tells git that you want to include updates to a particular file in the next commit
        -> git add <file_name> (for adding one file)
        -> git add . / git add -A(for adding all files created/modified/deleted in current directory)
    git commit
        -> Captures a snapshot of the project's currently staged changes
        -> git commit -m "message"
    git diff
    git stash

Inspect Repo:
    git status
        -> Displays the state of the working directory and the staging area 
        -> It lets you see which changes have been staged, which haven't and which files aren't tracked by GIT
        -> git status
    git log
        -> Only operates on commited history
        -> It displays commited snapshots
        -> It lets you list the project history, filter it and search for specific changes
        -> git log
    git tag
        -> Is used to capture(tag) a point in history that is used for marked version release (v.0.1)
        -> A tag is like a branch that doesn't change.
        -> Tags after being created have no further history of commits
        -> git tag <tag_name > 
    git blame
        -> Displays of author metadata attached to specific commited lines in a file.
        -> It is used to examine specific points of a file's history nd get context as to who the last author 
            was that modified the line
        -> git blame <file_name>

Parallel Development:
    git branch
        -> A git branch represents the tip of sereis of commits -it's not a container of commits
        -> Branching is an integral part of any version control system 
        -> Unlike other VCS git points to snapshots of the changes you have made in the system
        -> git branch <branch_name>
    git merge
        -> It is one of the two utilities that specializes in integrating the changes from one branch onto another
        -> It combines a sequence of commits to the old base commit.
        -> git merge <base>
    git rebase
        -> It commits sequence of commits to a new base commit.
        -> git rebase <base>



fetch changes from remote repository to local repository 
pust commits from local to remote

git pull
    -> Fetechs changes from remote repository to local repository
    -> basically it merges upstream changes in your local repository 
    -> git pull origin <repo_name>

git push
    -> Transfers commits from local repo to remote repo
    -> opposite of pull
    -> pulling will import the commits where as pushing will export commits to remote repo
    -> git push origin <repo_name>




Additional important commands

git archive
    -> used to acrchive your entire repository
    -> git archive master --format=zip -output=../name_of_file.zip

git bundle
    -> used to bundle your repository
    -> turns your entire repository into single file 
    -> git bundle create ../repo.bundler master

git stash
    -> Stashing uncommited changes
    ->  when you want to undo adding a feature or any kind of added data we can always stash 
        them temporarily
    -> git stash status
    -> git stash apply
"""




# Introduction to SSH Keys
"""
What is an ssh key?
    -> An SSH key is an access credential for the secure shell network protocol.
    -> This is authenticated and encrypted secure network protocol is used for remote communication between
        machines on an unsecured open network.
    -> SSH is used for remote file transfer, network management, remote os access
    ->  basically it is used to log into remote machine and execute the commands you want
    -> This also supports tunneling, forwarding tcp ports, and x11 conditions
    -> It can transfer files using associated ssh file transfer  or secure copy protocols


How to create ssh keys?
    -> ssh-keygen -t rsa -b 4096 -C "your_email@example.com" (create key using this command)
    -> Specifiy file location 
    -> Enter a secure passphrase twice
    -> add the new ssh-key to the ssh-agent (ssh -add)
"""