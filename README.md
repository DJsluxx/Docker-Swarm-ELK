# Docker-Swarm-ELK
Full deployment of ELK using Python on virtual machines.


Platforms :

*	Python (3.7.1)
*	Debian (9.9) (4 VMs)


Before  Running :
* Make sure to edit the configuration file and change the followings :
    * username
    * password
    * manager node
    * workers nodes
* Make sure you install the requirements from the requirements.txt file.
* This code runs with python 3.7, will work with other versions of python 3+.
* python 2.7 will not work since this code using deprecated formats.
* Don't forget to smile :)

RUN :
* pip install requirements.txt
* python elk_deploy.py


Next Update :

* Edit worker nodes to work in an Array so the code will be more generic and we will be able to add more workers easily.
* Deploy separate container for Cerebro and protect it with Nginx.
    * Insert it into the Docker-Composer.yml file.
* Curator settings to clean up Elasticsearch indexes older than 1 week.
    * Insert it into the Makefile.
    
    
For every question, feel free to communicate :)
Sluxx.
