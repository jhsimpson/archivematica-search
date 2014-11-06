how to set up the project

this will create a vm with ES 1.4 installed

vagrant up

this will create a virtualenv with python 3.4 and elasticsearch library installed

cd client 
virtualenv -p /usr/bin/python3.4 venv
source venv/bin/activate
pip install -r requirements.txt


The venv directory can be moved wherever you want, if it is inside this source tree
it will be ignored by git.


