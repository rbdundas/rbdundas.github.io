import os
import re
import markdown
from bs4 import BeautifulSoup


def get_replacement_string(filename):
    filename = filename + '.html'
    file = open(filename, 'r').read()
    return file


def check_includes(temp_html):
    includes = re.finditer(r'<p>@include_content (.*?).html</p>', temp_html)
    for include in includes:
        pattern = '<p>@include_content ' + include.group(1) + '.html</p>'
        replacement = get_replacement_string(include.group(1))
        temp_html = re.sub(pattern, replacement, temp_html, count=0, flags=0)
    return temp_html


def md_convert():

    files = os.listdir('.')
    for file in files:
        if file.split('.')[1] == "md":
            with open(file, 'r') as f:
                temp_md = f.read()
                temp_html = markdown.markdown(temp_md)
                temp_html = check_includes(temp_html)
                soup = BeautifulSoup(temp_html, 'html.parser')
                new_filename = file.split('.')[0] + '.html'
                with open(f'../{new_filename}', 'w') as f2:
                    f2.write(soup.prettify())


if __name__ == '__main__':
    md_convert()
