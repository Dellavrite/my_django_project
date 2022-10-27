import csv
import os

from djangoProject.settings import BASE_DIR
from searchEngine.models import News


def run():
    with open(os.path.join(BASE_DIR, 'static', 'merged.csv')) as f:
        read_file = csv.reader(f, delimiter="~")

        for news in read_file:
            News.objects.create(post_link=news[0], post_name=news[1], sender_name=news[2],
                                sender_link=news[3], post_date=news[4], post_id=news[5])