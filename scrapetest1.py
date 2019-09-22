from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("https://vputriariyanti.blogspot.com/")
bsObj=BeautifulSoup(html.read());
print(bsObj.h1)
