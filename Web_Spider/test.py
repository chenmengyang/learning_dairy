__author__ = 'cmy'
import urllib
import os

u = urllib.urlopen("https://image.tmdb.org/t/p/w185/zSouWWrySXshPCT4t3UKCQGayyo.jpg")
data = u.read()

base_path = "/Users/cmy/Documents/web development/MovieSite/img"

id = 123

exists = os.path.exists(base_path+"/"+str(id))

if not exists:
    os.makedirs(base_path+"/"+str(id))
    filename = base_path+"/"+str(id) + "/1.jpg"
    f = open(filename, "wb")
    f.write(data)
    f.close()