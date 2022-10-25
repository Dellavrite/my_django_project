import re
import os
import pymorphy2
from django.templatetags.static import static

from searchEngine.models import News


def engine(word):
    morph = pymorphy2.MorphAnalyzer()
    res = [" "]
    for morph_word in [x.word for x in morph.parse(word.lower())[0].lexeme]:
        res.extend(News.objects.filter(post_name__search=morph_word))
    return res

