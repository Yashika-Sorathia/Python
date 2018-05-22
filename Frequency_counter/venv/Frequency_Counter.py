import requests
from bs4 import BeautifulSoup
import operator

#function takes all the text from website and split it into words
def start(url):
    word_list = []
    src = requests.get(url).text
    soup = BeautifulSoup(src, "html.parser")
    for p in soup.findAll('a', {'class': '_2cLu-l'}):
        content = p.string
        words = content.lower().split()
        for every in words:
            word_list.append(every)
    clean_list(word_list)

#fucntion removes all the unwanted sybmoles
def clean_list(word_list):
    clean = []
    for word in word_list:
        sym = "!@#$%^&*()_+-={}[]:\";'<>?,./"
        for w in range(0, len(sym)):
            word = word.replace(sym[w], "")
        if len(word) > 0:
            clean.append(word)
    create_dic(clean)

#function creates dictionary along with its no. of occurance sorted by its values
def create_dic(clean):
    count = {}
    for word in clean:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    for key, value in sorted(count.items(), key=operator.itemgetter(1)):
        print(key, value)






start('https://www.flipkart.com/womens-clothing/western-wear/shirts-tops-tunics/pr?sid=2oq,c1r,ha6,cck&otracker=categorytree&otracker=nmenu_sub_Women_0_Top,%20T-Shirts%20and%20Shirts&otracker=nmenu_sub_Women_0_Top,%20T-Shirts%20and%20Shirts')