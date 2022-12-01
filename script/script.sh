#! /bin/bash
python3 /home/ubuntu/coding/weather-script/main.py >> /home/ubuntu/coding/weather-script/data.txt

# crontab -l
# 0 6,12,20 * * * . /home/ubuntu/coding/weather-script/script.sh