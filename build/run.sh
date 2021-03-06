( rpm -q docker-ce ) ||
	{
	curl -s https://raw.githubusercontent.com/ramjammigumpula/ansible-docker/master/plays | bash
	}


( rpm -q git ) || yum install git -y

git clone https://github.com/ramjammigumpula/jenkins.git

cd jenkins/build

test -f /bin/docker-compose  || { curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /bin/docker-compose ; chmod 777  /bin/docker-compose ; }

docker-compose build

docker-compose up -d cronjobs

sleep 20 

docker-compose up -d python

sleep 20

docker-compose up -d jenkins

sleep 20

mkdir -p /share/apache && chmod 777  /share/apache

docker-compose up -d apache




