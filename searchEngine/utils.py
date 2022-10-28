import re
import os
import pymorphy2
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.templatetags.static import static

from searchEngine.models import News


def engine(word):
    word += " "
    morph = pymorphy2.MorphAnalyzer()
    morph_words = [f"'{x.word}'" for x in morph.parse(word.lower())[0].lexeme]
    vector = SearchVector("post_name")
    query = SearchQuery(f"({' | '.join(morph_words)})", search_type="raw")
    res = News.objects.annotate(search=vector).filter(search=query).order_by("post_date").reverse()
    return res
