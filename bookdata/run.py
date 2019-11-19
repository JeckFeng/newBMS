from scrapy import cmdline
from PyQt5.QtWidgets import QApplication
import sys


class ScrapyRun():

    def __init__(self):
        cmdline.execute("scrapy crawl books".split())
