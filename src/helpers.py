from typing import List
from os import startfile

from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader

from models.token import TokenEntry
from models.error_entry import ErrorEntry, SintaxError
from models.token_enum import TypeToken


def process_file(tokens: List[TokenEntry], errs: List[ErrorEntry],
                 sintax_errs: List[SintaxError]):
    def extract_names(tokens: List[TypeToken]):
        return list(map(lambda t: t.name, tokens))

    env = Environment(loader=FileSystemLoader('src/templates'),
                      autoescape=select_autoescape(['html']))
    template = env.get_template('table_report.jinja2.html')

    html_file = open('reports.html', 'w+', encoding='utf-8')
    html_file.write(
        template.render(tokens=tokens,
                        errs=errs,
                        sintax_errs=sintax_errs,
                        extract_names=extract_names))
    html_file.close()
    startfile('reports.html')