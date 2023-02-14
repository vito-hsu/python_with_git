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

#
#######################################################################################


# Review.
# In the last tutorial video, we've known the following commands could automatically push all our new files in this folder to the correspoding Git repository.
# git init ; git add . ; git commit -m "123" ; git remote add origin https://github.com/vito-hsu/python_with_git.git ; git push origin master
# Let's try again. Check the github content first.

# In the second video, I'll introduce the other common commands in Git.
# Before the pratice, we should know the purpose of branch in Git.
# The key is that "master" means the main file of our project.
# But if we want to develop other functions of our project, we should start other "branches".
# Because I just built the new branch called branch_1, now I will delete the branch first.


# 1.    git status                      --- check the status in the Git repository
# 2.    git log                         --- check the log in the Git repository
# 3.    git branch                      --- check the branch in the Git repository
# 4.    git branch branch_1             --- new a branch from the master
# 5.    git push origin branch_1        --- push to the specific branch
# 6.    git branch -D branch_1          --- delete the specific branch


# To push all files to the branch of the project, the whole commands are :
# git branch branch_1 ; git init ; git add . ; git commit -m "123" ; git push origin branch_1
# If you encounter this condition, do the following thing~~  and we try again
 
# And the last but not the least, how could we rapidly switch to master?
# Before do this, I suggest you update the master first.

# 7-1.  git checkout branch_1           --- 
# 7-2.  git checkout master             --- 

# If you encounter this condition "Everything up-to-date", delete the branch, and do it again.

# Ok~ hope you can get what you want in this video~~thx



#######################################################################################



# In the last tutorial video, we've known the branch commands:
# git branch branch_2 ; git init ; git add . ; git commit -m "123" ; git push origin branch_2
# If you encounter this condition "Everything up-to-date", delete the branch, and do it again.

# In the third video, we'll focus on the two commands:
# 1.    git merge branch_2              --- 
#       1)  git checkout branch_1
#       2)  git checkout branch_2
# 2.    git rebase branch_2             ---




#######################################################################################




# In the fourth video, we'll learn how to get the files from github repository to our local folder in two ways:
# 1. git pull origin master
# 2. git clone [url]
# Before today's practice, I suggest you should create two new folders outside this folder like these.
# And let's review the push command first.