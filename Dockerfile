# This sets up the container with python 3.10 installed.
FROM python:3.10-slim

# This copies everything in the current directory to the /app directory in the container.
COPY . /app

# This sets up the /app directory as the working directory for any RUN, CMD, ENTRYPOINT, or COPY instructions that follow.
WORKDIR /app

# This run pip install for all the packages listed in requirements.txt file.
RUN pip install -r requirements.txt

# This Docker to listen on port 80 at runtime. Port 80 is the standart port for HTTP.
EXPOSE 80

# This command creates a .streamlit directory in th home directory.
RUN mkdir ~/.streamlit

# This copies your streamlit configuration file into the .streamlit directory you just created.
RUN cp config.toml ~/.streamlit/config.toml

# Just like the previous step, this copies your streamlit credentials file into the .streamlit directory you just created.
RUN cp credentials.toml ~/.streamlit/credentials.toml

# This sets the default commands for the container to run the Streamlit app.
ENTRYPOINT ["streamlit", "run"]

# This command tells Streamlit to run you app.py script when the container starts.
CMD ["app.py"]