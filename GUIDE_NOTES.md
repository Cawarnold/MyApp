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

then 