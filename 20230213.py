# Hi~ I'm vito.
# Today, I'm gonna introduce how to use git with vscode.
# 1. Install git to your PC (not portable version if you want to use vscode)
# 2. Click it, and it will link to your github, requesting login.
# 3. In your vscode terminal, enter the following commands after you have checked your repository (ex. this work folder):
#   3-1. git init
#   3-2. git add .
#   3-3. git commit -m "your commit"
#   3-4. git remote add origin https://github.com/vito-hsu/python_with_git.git
#   3-5. git push origin master
# Let's try it
# I just run the above commands again, and you can see the .py file has changed like this.
# Let's try it again.
# You can see the 3-4 command doesn't need to run if you just rerun again.






# In the second video about Git tutorial, I'll introduce the other common commands in Git.
# Before the pratice, we should know the purpose of branch in Git.
# The key is that "master" means the main file of our project.
# But if we want to develop other functions of our project, we should start other "branches".

# 1.    git status                      --- it indicates the change/status about your current folder files 
# 2.    git log                         --- as you see, in our project, we push five times and this command will indicate the update time and commit messages
# 3.    git branch                      --- because we have not built branches in our project, it just indicate the "master"
# 4.    git branch branch_1             --- new a branch from the master
# 5.    git push origin branch_1        --- push to the specific branch
# 6.    git branch -D branch_1          --- delete the specific branch

# But you can see it's not up-to-date, how could we update?
# And the last but not the least, how could we rapidly switch to master?

# 6-1.  git checkout branch_1           --- 
# 6-2.  git checkout master             --- 
