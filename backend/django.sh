#! /bin/bash

rm -rf /home/ubuntu/coding/django-terminal-backend

mv /home/ubuntu/backend/ /home/ubuntu/django-terminal-backend/

mv /home/ubuntu/django-terminal-backend/ /home/ubuntu/coding/

kill -9 `sudo lsof -i:8020`

rm /home/ubuntu/coding/django-terminal-backend/nohup.out

cd /home/ubuntu/coding/django-terminal-backend/

nohup python3 /home/ubuntu/coding/django-terminal-backend/manage.py runserver 0.0.0.0:8020 &

echo 'already rebuild! --  http://152.136.154.181:8020/api/test'
