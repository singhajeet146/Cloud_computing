#I specify the parent base image which is the python version 3.7
FROM python:3.6.9


# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --no-cache-dir --upgrade pip

# set work directory
WORKDIR /src/app

# copy requirements.txt
ADD ./req.txt /src/app/req.txt

# Copy the models directory and server.py files
ADD ./model /src/app/model
ADD pred_script.py /src/app/pred_script.py
#ADD google-service-account-key.json /src/app/google-service-account-key.json

#RUN export GOOGLE_APPLICATION_CREDENTIALS="google-service-account-key.json"

# install project requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r req.txt

# # copy project
# COPY . .

# # Generate pikle file
# WORKDIR /src/app/ML_Model
# RUN python model.py

# # set work directory
# WORKDIR /src/app

# set app port
EXPOSE 5021

ENTRYPOINT [ "python" ]

# Run app.py when the container launches
CMD [ "pred_script.py","run","--host","0.0.0.0"]

# Dockerfile
