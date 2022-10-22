import re
import os

from django.templatetags.static import static


def engine(word, file):
    with open(f"{os.getcwd()}{static(file)}") as f:
        text = f.read()
        split_re = re.compile(r"[.|?|!]")
        sentences = filter(lambda t: t, [t.strip() for t in split_re.split(text)])
        template = rf"\b{word.lower()}\b"
        res = [" "]
        res.extend([sentence for sentence in sentences if re.search(template, sentence.lower())])
        return res

