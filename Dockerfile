#took a base image for the app according to enviroment(python,js)
FROM python:3.7

#created a working directory
WORKDIR /app

#copied the file(src code) from local to the working directory 
COPY . .

#install the required library if not required dont install


#finally running the app
ENTRYPOINT ["python","main.py"]



