import random
import urllib.request

def get_image(url):
    number = random.randrange(1,1000)
    fullname = str(number) + '.jpg'
    urllib.request.urlretrieve(url,fullname)

get_image('https://pp.vk.me/c617828/v617828270/ccb2/4mXTgo918ho.jpg')
