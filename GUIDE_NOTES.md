GUIDE

Creating a live app in python/django for free.

####
Useful links
https://c9.io/site/blog/2013/08/django-workspace-type
####

#### Some notes from a similar project ####

Github, Cloud9, NodeJS & Heroku: develop & deploy a web(socket) application

http://charless.org/?p=283

Github - web-based hosting service for software development projects that use the Git revision control system.
Cloud9 - state-of-the-art IDE that runs in your browser and lives in the cloud, allowing you to run, debug and deploy applications from anywhere, anytime.
Django - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
Heroku - cloud application platform

Github - store code - version control
Cloud9 - write code - IDE
Django - language   - Python/Django
Heroku - deploy it  - deploy the app

#### Cloud9 to Github development ####

http://lepidllama.net/blog/how-to-push-an-existing-cloud9-project-to-github/

all normal, but push with:

git push -u origin master

# finally got github, cloud9 and my local repositories at the same place.

Had to delete the devel branch from cloud9 then push that to github, then pull that to local.
Sweet, so now I have two develpment environments.
1. Cloud9
2. Local

So when I go to another laptop, I can just pull down the repo and setup and environment 
and then carry on working on my project.

################################
################################

Github Everyday workflow
	git fetch (allows you to see new remote branches)
-Go to branch you want to work on
	git pull
-Make changes
	git commit -a -m "message details of changes"
-push commits to remote
	git push


################################
################################

GitHub workflow:
## Update master and devel from github:
(master) git pull origin master
(master) git push
(master) git checkout devel
(devel) git pull origin devel

## Create or change to your working branch.
(devel) git checkout -b "branch-name"

make your changes
git add "file-changed.txt"
git commit -m "commit message"
git push origin branch-name

then continue development

Design a feature, with criteria for acceptance.
Test your feature, to see if meets those criteria.
When it works (or you make good progress), commit your work.


################################
################################


#### Git Reset to Github Version ####

### To hard pull from github origin/master

git reset --hard origin/master
git push

### To hard push to github origin/master

git push origin master --force

################################
################################


#### Branches:

master -- only for use in cloud9
devel -- for testing new features in cloud 9



#### Revert branch to old commit
	git revert --no-commit 1e6bd23e629df7211c6b91b5338f3fe120c0408d
	git commit

#### Rename branch as master
	git branch -m master old-master
	git branch -m seotweaks master
	git push -f origin master

#### List all Branches ( first list in local, second list is remote )
	git branch -a

#### Remove branch
	git branch -d branchname

	for remote	
		git push origin --delete yourbranchname
	for local
		git branch -d yourbranchname
		git branch -D yourbranchname

#### Remove untracked files
	git clean -f

#############################


#### Using 'South' to sync DB ####

How does all this work with migrations?

Think I have to make migrations on every computer I am using the db.
ie. since I hard rest the app on Cloud 9 i think i have to reapply the migration.
20150708

###########################################################################################
###########################################################################################
###########################################################################################


#### Caution: keep python package versions ####

I have updated my local django to 1.8,
but the cloud9 django is 1.7

May need to clone root env then replace root environment 

### Conda Environments
## List all environments
			conda info --envs 

## Create an environment
			conda create --name Env_Python276_Django171 python=2.7.6 django=1.7.1

## Change environments (activate/deactivate)
	#Linux, OS X: 
			source activate Env_Python276_Django171

	#Windows: 
			activate Env_Python276_Django171
			deactivate Env_Python276_Django171
			
## Remove an environment
			conda remove --name Env_Python276_Django171 --all


## Install Specific Verison of package
			conda install django=1.7.1

## Check versions of packages
			conda list

## Clone root env
	conda create -n Env_Original_root --clone root

## Replace root env
	# Create .bashrc file
		echo -n > ~/.bashrc
	# Edit file
		echo "~/anaconda/envs/Env_Python276_Django171/bin" >> .bashrc


#### Development Process ####

Develop using Cloud9 to release master, 
Github to store code, 
Local to develop new features.

## Master: Live version running on Cloud9 "anything in the master branch is always deployable"
			Can only be updated from devel and only after devel is working on cloud9
			## When you're ready to push a feature to master
				on C9:
				git checkout devel
				git pull
				-- check app
				git checkout master
				git reset --hard origin/devel
				git push

## Devel: For testing features

## Branch: Feature branch where you can create new stuff.
				Commit messages are important, especially since Git tracks your changes and 
				then displays them as commits once they're pushed to the server.

## Pull Requests: You can open a Pull Request at any point during the development process: 
						when you have little or no code but want to share some screenshots or general ideas, 
						when you're stuck and need help or advice, 
						or when you're ready for someone to review your work

## Merging Branch:  If you want to test things before merging in the repository on GitHub, you can perform the merge locally first

###########################################################################################
###########################################################################################
###########################################################################################

