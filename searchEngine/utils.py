import re
import os

from django.templatetags.static import static

from searchEngine.models import News


def engine(word):
    sentences = News.objects.filter(post_name__search=word.lower)
    # template = rf"\b{word.lower()}\b"
    res = [" "]
    # res.extend([sentence for sentence in sentences if re.search(template, sentence.lower())])
    res.extend(sentences)
    return res

