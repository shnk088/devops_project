#devops cheat sheet 
## Git 
- git init - initialize git repository 
- git add .- stage all files 
- git commit -m "message" - save snapshot
- git remote add origin <url>--
- git push -u origin main - pura project git pr 

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
docker stop - to stop container 
docker ps - to show container
- docker tag devops-app sha088/devops-app:v1-- we use tag to provide adreess of docker hub
- docker push sha088/devops-app:v1 ---- push image will upload to internet
- docker login -- docker hub m login 
#  Dockerfile is edited, not recreated; keep a single Dockerfile per project.

