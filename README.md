# Deployment Process
![The deployment process](https://github.com/othmansamih/Deploying-a-Streamlit-app-as-a-Docker-container/blob/main/Images/img.png?raw=true)

## Testing the Streamlit on local
1. Install the required dependencies on local
```comandline
pip intall -r requirements.txt
```

2. Test the Streamlit app on local
``` commandline
streamlit run app.py
```


 ## Building the Docker image
 (Note: Run as administrator on Windows) <br>
 3. Make sure you have installed Docker on your PC (Docker Desktop if it's Windows)

 4. Start Docker (You can start Docker engine from Docker Desktop)

 5. Build the Docker image from the project directory (Create a sub directory that encapsulate the files that exist in this repository)
``` commandline
docker build -t Image_name:tag
```
(Note: Rerun the Docker build command if you want to make any changes to the code files and redeploy.)



## Running the container and removing it
-> List the built docker images
``` commandline
docker images
```

6. Start a container
``` commandline
docker run -p 80:80 Image_ID
```
-> List the running containers
``` commandline
sudo docker run -p 80:80 Image_ID
```

7. This will display the URL to access the Streamlit app (http://0.0.0.0:80). Note that this URL may not work on Windows. So, go to http://localhost/.

8. In a different terminal window, you can check the running containers with:
``` commandline
docker ps
```

9. Stop the container
   * Use `Ctrl + c` or stop it from Docker Desktop

10. Check all containers
``` commandline
docker ps -a
```

11. Delete all the containers if you're not going to run them again
``` commandline
docker container prune
```

## Pushing the Docker image to Docker Hub
12. Sign UP on Ducker Hub

13. Create a repository on Docker Hub

14. Log in to Docker Hub from the terminal. You can log in with your password or access token.
``` commandline
docker login
```

15. Tag your local Docker image to the Docker Hub repository
``` commandline
docker tag Image_ID username/repo-name:tag
```

16. Push the local Docker image to the Docker Hub repository
``` commandline
docker push username/repo-name:tag
```

17. Command to force delete an image (but don't do this yet)
``` commandline
docker rmi -f IMAGE_ID
```


