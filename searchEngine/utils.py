import re
import os
import pymorphy2
from django.contrib.postgres.search import SearchQuery
from django.templatetags.static import static

from searchEngine.models import News


def engine(word):
    morph = pymorphy2.MorphAnalyzer()
    res = [" "]
    morph_words = [x.word for x in morph.parse(word.lower())[0].lexeme]
    res.extend(News.objects.filter(post_name__search=" ".join(morph_words)))
    return res
