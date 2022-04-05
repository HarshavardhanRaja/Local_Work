

# Basic Commands for creating a repo from scratch
"""
git init        (creates a new git repository)
    => Running the git init command sets up all of the necessary files and directories that Git will use to keep track of everything. 
    => All of these files are stored in a directory called .git (notice the . at the beginning - that means it'll be a hidden directory on Mac/Linux). 
    => This .git directory is the "repo"! This is where git records all of the commits and keeps track of everything!

Here's a brief synopsis on each of the items in the .git directory:

config file - where all project specific configuration settings are stored.
From the Git Book:

Git looks for configuration values in the configuration file in the Git directory (.git/config) of whatever repository you’re currently using. These values are specific to that single repository.

For example, let's say you set that the global configuration for Git uses your personal email address. If you want your work email to be used for a specific project rather than your personal email, that change would be added to this file.

description file - this file is only used by the GitWeb program, so we can ignore it
hooks directory - this is where we could place client-side or server-side scripts that we can use to hook into Git's different lifecycle events
info directory - contains the global excludes file
objects directory - this directory will store all of the commits we make
refs directory - this directory holds pointers to commits (basically the "branches" and "tags")






git clone       (copies the contents of a remote repository to your local machine)
git status      (shows the status of the current directory)
"""



# Clone an existing repo
"""
clone => to make an identical copy

git clone "repo-url"
git clone "repo-url" dir_name

"""




# Determine  a repo status
"""
git status

"""