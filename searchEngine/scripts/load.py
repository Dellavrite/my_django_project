import csv
import os
from searchEngine.models import News


def run():
    with open('/data/merged.csv') as f:
        read_file = csv.reader(f)

        News.objects.all().delete()

        for news in read_file:
            News.objects.create(post_link=news[0], post_name=news[1], sender_name=news[2],
                                sender_link=[3], post_date=[4], post_id=[5])
