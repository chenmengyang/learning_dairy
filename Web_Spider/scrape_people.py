# Since I am feeling so bad about using the moviedb API to get data, now we are going to scrape the data from this website: https://www.themoviedb.org/movie

# create table to store the data after scraping
# download images to local file system, separated by id

from bs4 import BeautifulSoup
import requests
import MySQLdb
import os
import urllib

# connect to db
db = MySQLdb.connect("localhost", "cmy", "", "moviedb", use_unicode=True, charset='utf8')
cur = db.cursor()
#
create_sql = "create table if not exists people\
(person_id int primary key\
,name varchar(100)\
,credit smallint\
,biography varchar(4000)\
,sex varchar(15)\
,known_fors varchar(200)\
,birthday varchar(20)\
,birthplace varchar(100)\
,attribute1 varchar(100)\
,attribute2 varchar(100)\
,attribute3 varchar(100)\
,attribute4 varchar(100)\
,attribute5 varchar(100)\
,attribute6 varchar(100)\
,attribute7 varchar(100)\
,attribute8 varchar(100)\
,attribute9 varchar(100)\
,attribute10 varchar(100)\
);"
#
cur.execute(create_sql)

# set a path on local directory for storing images
base_path = "/Users/cmy/Documents/web development/MovieSite/people_img/"

def save_img(img_url, id, path, filename):
    u = urllib.urlopen(img_url)
    data = u.read()
    exists = os.path.exists(path+str(id))
    if not exists:
        os.makedirs(path+str(id))
    f = open(path+str(id)+'/'+filename, "wb")
    f.write(data)
    f.close()

# In total 100 pages
url = "https://www.themoviedb.org/person?page="
# but we don't need to get all data now, just first 10 pages maybe enough
pages = [1,2,3,4,5,6,7,8,9,10]

def load_people_data(link, page):
    r = requests.get(link+str(page))
    soup = BeautifulSoup(r.content, "html5lib")
    # find all peoples
    all_tr = soup.find_all("tr")

    for p in all_tr:
        pid = int(p.find("a").get("href").replace("/person/", ""))
        detail_url = "https://www.themoviedb.org/person/" + str(pid)
        r1 = requests.get(detail_url)
        soup1 = BeautifulSoup(r1.content, "html5lib")
        name = soup1.find("span", {"id": "name"}).text
        try:
            biography = soup1.find("div", {"id": "biography"}).text.replace("'", "''")
        except:
            biography = ""
        known_fors = ""
        for movie in soup1.find_all("li", {"class": "w92"}):
            known_fors += movie.text.replace("\n", "").replace(" ", "")+";"
        known_fors = known_fors.replace("'", "''")
        leftpanel = soup1.find("div", {"id": "leftCol"})
        attr_list = []
        for ele in leftpanel.find_all("p"):
            s = ele.text
            attr_list.append(s[s.find(':')+2:])
        sex = attr_list[0]
        credit = int(attr_list[1])
        birthday = attr_list[2]
        birth_place = attr_list[3]
        img_url = leftpanel.find("img", {"class": "shadow"}).get("src")
        print img_url
        # save images to local system
        save_img(img_url, pid, base_path, "1.jpg")

        # print mid, title, vote_average, release_date, genres, img1
        insert_sql = "insert into people(person_id,name,credit,biography,sex,known_fors,birthday,birthplace) values(%d,'%s',%d,'%s','%s','%s','%s','%s');" % (pid, name, credit, biography, sex, known_fors, birthday, birth_place)

        try:
            cur.execute(insert_sql)
            print "ok "
            db.commit()
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)
            # print insert_sql
            db.rollback()

for p in pages:
    print "loading page: "+str(p)
    load_people_data(url, p)


db.close()
#