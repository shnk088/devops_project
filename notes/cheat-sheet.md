#devops cheat sheet 
## Git 
- git init - initialize git repository 
- git add .- stage all files 
- git commit -m "message" - save snapshot
- git remote add origin <url>--
- git push -u origin main - pura project git pr 
- git show 
- git show head 
- git show head~2
- git branch 
- git blame 
## python
- make a folder src under this python folder
## dockerfile
skeleton 
============
From python:3.10-slim ----base python image
WORKDIR/app           ----container ke andar ka folder
copy src/src/         --- for python code copy
CMD["python","src/app.py"]---container start hote
command 
==================
- docker build -t devops-app .--- to build image
- docker run --rm devops-app --- run container m chalega broser m 
nhi port mapping nhi h
- docker stop - to stop container 
- docker ps - to show container
- docker tag devops-app sha088/devops-app:v1-- we use tag to provide adreess of docker hub
- docker push sha088/devops-app:v1 ---- push image will upload to internet
- docker login -- docker hub m login 
#  Dockerfile is edited, not recreated; keep a single Dockerfile per project.

==========================================================================
yml file = command + config ek jagh 
#skeleton
=============
version: "3.8"

services:
 web:
  image: devops-app
  ports:
   - "8080:8080"
   restart : always 
 - docker build - image bnata h
 - docker-compose up - to container chakata h 
 - docker-compose down - to removed 
 - docker-compose up -d -- deatch mode 
 - docker ps-a ------- show all images 
 - docker stop devops-web(container name ) -- manually stopped 
 - docker system prune -af 
 # restart policies
  restart :always
  ================  
 - container crash --restart 
 - Docker restart -- restart 
 - docker stop -- restart nhi hoga

 restart: unless stoped 
 =========================
 - user stop kiya -- docker restart ke baad bhi start nhi hoga 

 restart on-failure 
 =====================
 - sirf error pe --- restart 
 - normal exist/manual stop - nhi hoga 

# restar policiy manual stop ko overide nhi krti

env 
=====
environment: docker-compose me variables define karne ke liya hota h
docker exec -it devops-web env -- extra verify 
env file mai port change kiya + docker-compose restart = behaviour change without code modification.
env_file: variable container k andar jate h 
${port}:${port} - variable compose time pe susbstitute hota h
# jenkins
================================
docker run -d \ ----- image build k liye 
  -p 8080:8080 \----- Left 8080 → tumhara laptop (browser) Right 8080 → Jenkins container
  -p 50000:50000 \---- Jenkins ke agents / nodes ke liye port
  --name jenkins \----- Container ka naam set kar diya
  -v jenkins_home:/var/jenkins_home \ ---- Jenkins ka data yahan store hota hai:
jobs
plugins
users
Container delete ho jaye → data safe 
  jenkins/jenkins:lts---------- jenkins/jenkins → official image
   lts → long-term support (stable)