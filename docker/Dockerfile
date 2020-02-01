FROM python:3

# add python script for setup
ADD ./setup.py ./setup.py

# update package list and install packages
RUN set -x && \
  apt-get update && \
  python ./setup.py install && \
  pip install pyyaml
