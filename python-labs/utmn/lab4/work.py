# import glob
#
# txt_files = glob.glob('news/*.txt')
#
#
# def read_first_line(file):
#     with open(file, 'rt', encoding='utf8') as fd:
#         first_line = fd.readline()
#     return first_line
#
#
# output_strings = [*map(read_first_line, txt_files)]
# print(output_strings)
import csv
import os
import re

texts = list()

for filename in os.listdir('news'):
    with open(os.path.join('news', filename), 'r', encoding='utf8') as f:
        texts.append(f.read()[1:].split('\n\n'))

for text in texts:
    for text_str in range(len(text)):
        text[text_str] = ' '.join(text[text_str].split('\n'))

fileName = 'MyCSV.csv'
identifier = 1
with open(fileName, 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(['Index', 'Title', 'Lid', 'Text', 'Ner', 'Language', 'URL', 'Date'])
    for text in texts:
        if re.match(r'^[а-яё\d\s!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~«»–—]+$', ' '.join(text[:-1]), re.I):
            lang = 'ru'
        elif re.match(r'^[a-z\d\s!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~«»–—]+$', ' '.join(text[:-1]), re.I):
            lang = 'en'
        else:
            lang = 'ru-en'
        try:
            writer.writerow([identifier,
                             text[0][:-1],
                             text[1],
                             ' '.join(text[1:-1]),
                             1 if re.findall(r'([А-ЯЁA-Z]{2,}|[^!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~«»–—]\s[А-ЯЁA-Z][а-яёa-z]+'
                                             r'|[А-ЯЁA-Z][а-яёa-z]+(\s[А-ЯЁA-Z][а-яёa-z]+)+)', ' '.join(text), ) else 0,
                             lang,
                             ''.join(text[-1:]),
                             '.'.join(re.search(r'\d{2}-\d{2}-\d{4}', ' '.join(text)).group(0).split('-'))])
        except AttributeError:
            writer.writerow([identifier,
                             text[0][:-1],
                             text[1],
                             ' '.join(text[1:-1]),
                             1 if re.findall(r'([А-ЯЁA-Z]{2,}|[^!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~«»–—]\s[А-ЯЁA-Z][а-яёa-z]+'
                                             r'|[А-ЯЁA-Z][а-яёa-z]+(\s[А-ЯЁA-Z][а-яёa-z]+)+)', ' '.join(text)) else 0,
                             lang,
                             ''.join(text[-1:]),
                             '-'])
        identifier += 1
