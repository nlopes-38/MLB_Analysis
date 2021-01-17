"""
Scrape MLB yearly stats
"""
import numpy as np, pandas as pd, requests, re
from bs4 import BeautifulSoup

url = "https://www.baseball-reference.com/teams/"
year = 2020

r = requests.get(url = url)
soup = BeautifulSoup(r.content, "lxml")


