############################################################
# Developer stage: for running in vscode                   #
############################################################
FROM registry.access.redhat.com/ubi8/ubi:latest as developer

#Make a username. You can pass in a custom username
ARG USERNAME=developer 

ARG USER_UID=1000
ARG USER_GID=$USER_UID

USER root

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # add sudo support
    && yum update -y\
    && yum install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

RUN sudo yum install git -y
RUN sudo yum install wget -y
RUN sudo yum install make -y
RUN sudo yum install gcc -y
RUN sudo yum install python38 -y

COPY requirements.txt /req/requirements.txt
WORKDIR /req
RUN  pip3 install -r requirements.txt --user
RUN pip3 install uvicorn --user
RUN pip3 install pylint --user
WORKDIR /app
RUN sudo rm -rf /req

EXPOSE 5000
CMD ["sleep", "infinity"]

###############################################
# Production stage: for running in production #
###############################################
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY ./ /app
RUN rm -f /app/users.db
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
