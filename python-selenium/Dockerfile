FROM python:3

# add python script for setup
ADD ./setup.py ./setup.py
ADD ./jenkins_install.sh ./jenkins_install.sh

# update package list and install packages
RUN set -x && \
  apt-get update && \
  python ./setup.py install && \
  pip install pyyaml

# install jenkins and change directory permissions
RUN chmod 765 ./jenkins_install.sh &&\
  ./jenkins_install.sh && \
  mkdir -p /script/allure-results/images/ &&\
  mkdir -p /tmp/allure_results/ &&\
  chmod 777 /script/allure-results/images/ &&\
  chmod 777 /tmp/allure_results/
