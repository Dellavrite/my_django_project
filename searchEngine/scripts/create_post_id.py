import os
import csv

from djangoProject.settings import BASE_DIR
from searchEngine.models import News


def run():
    post_ids = News.objects.values_list("post_id", flat=True)
    with open(os.path.join(BASE_DIR, 'static', "post_ids.csv"), "w") as post_ids_file:
        post_ids_writer = csv.writer(post_ids_file, delimiter='~')
        post_ids_writer.writerow(post_ids)
