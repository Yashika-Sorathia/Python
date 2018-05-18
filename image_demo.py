import random
import urllib.request

#downloading image throug url
def Image(url):
    name = random.randrange(1, 1000)
    file_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,file_name)

Image("http://cdn.goodshomedesign.com/wp-content/uploads/2016/07/Kakksauttanen-Resort-3.jpg")
