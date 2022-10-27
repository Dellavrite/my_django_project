#!/bin/bash


while :
do
  python3 ~/Project/my_django_project/manage.py runscript create_post_id
  mv ~/Project/my_django_project/static/post_ids.csv ~/Project/temp

  cd ~/Project/News_Crawler/starters
  screen -S spyder_hi-tech_crawl -d -m  bash start_hi_tech_crawl.sh
  screen -S spyder_habr_news -d -m  bash start_habr_news.sh

  sleep 5

  last_screen_line=$(screen -ls | tail -1)
  while ! [ "${last_screen_line::1}" == "2" ]; do
      last_screen_line=$(screen -ls | tail -1)
      echo "Wait please"
      sleep 600
  done

  cd ~/Project/data/
  python3 ~/Project/News_Crawler/merge_csv.py
  mv merged.csv ~/Project/my_django_project/static/
  python3 ~/Project/my_django_project/manage.py runscript load

done