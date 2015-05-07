# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Maintaner Name

# Add the application resources URL
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/ap\
t/sources.list

# Update the sources list
RUN apt-get update

# Install Python and Basic Python Tools
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential pkg-config
RUN apt-get install -y texlive-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra
RUN apt-get install -y python3 python3-dev python3-pip
RUN apt-get install -y libfreetype6-dev

# Application-Dependencies
RUN pip3 install django
RUN pip3 install xlrd
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install pylatex
RUN pip3 install git+https://github.com/jgru/training_monitoring.git

# Adding requiremetns
ADD /app /my_application

# Expose ports
EXPOSE 8000

# Set the default directory where CMD will execute
WORKDIR /my_application

# Set the default command to execute
# when creating a new container
# i.e. using CherryPy to serve the application
# to change the port use: python3 manage.py runserver 0.0.0.0:1234
CMD python3 manage.py runserver
