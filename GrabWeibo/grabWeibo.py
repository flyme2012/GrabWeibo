

import requests
from bs4 import BeautifulSoup
import time


def grabHtml(url):
    htmlContent = requests.get(url);
    print htmlContent.status_code
    print htmlContent.text