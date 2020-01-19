#!/bin/bash
# install Open JDK 8
apt-get install -y openjdk-8-jre
# download jenkins install package
wget https://pkg.jenkins.io/debian/binary/jenkins_2.207_all.deb
# install jenkins
dpkg -i jenkins_2.207_all.deb
apt --fix-broken install -y
dpkg -i jenkins_2.207_all.deb
rm jenkins_2.207_all.deb
# start service
service jenkins start
exit 0