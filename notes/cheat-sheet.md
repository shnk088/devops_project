#devops cheat sheet 
## Git 
- git init - initialize git repository 
- git add .- stage all files 
- git commit -m "message" - save snapshot
## python
make a folder src under this python folder
## dockerfile
From python:3.10-slim ----base python image
WORKDIR/app           ----container ke andar ka folder
copy src/src/         --- for python code copy
CMD["python","src/app.py"]---container start hote
docker build -t devops-app .--- to build image
docker run --rm devops-app --- run 
docker tag devops-app sha088/devops-app:v1-- we use tag to provide adreess of docker hub
docker push sha088/devops-app:v1 ---- push image will upload to internet
