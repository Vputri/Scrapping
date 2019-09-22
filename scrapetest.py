from urllib.request import urlopen
html=urlopen("https://vputriariyanti.blogspot.com/")
print(html.read())
