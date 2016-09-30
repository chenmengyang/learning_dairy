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

create_sql = "create table if not exists tv_shows\
(tv_id int primary key\
,title varchar(100)\
,vote_average decimal(5,2)\
,release_year smallint\
,ranking smallint\
,genres varchar(100)\
,overview varchar(1000)\
,air_on varchar(50)\
,rating varchar(100)\
,show_type varchar(50)\
,show_status varchar(50)\
,runtime smallint\
,language varchar(100)\
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

cur.execute(create_sql)

# In total 1000 pages and about 20,000 results
url = "https://www.themoviedb.org/tv?page="
# but we don't need to get all data now, just first 10 pages' tv shows maybe enough
pages = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# set a path on local directory for storing images
base_path = "/Users/cmy/Documents/web development/MovieSite/tv_img/"

def save_img(img_url, id, path, filename):
    u = urllib.urlopen(img_url)
    data = u.read()
    exists = os.path.exists(path+str(id))
    if not exists:
        os.makedirs(path+str(id))
    f = open(path+str(id)+'/'+filename, "wb")
    f.write(data)
    f.close()

def load_tv_data(link, page):
    r = requests.get(link+str(page))
    soup = BeautifulSoup(r.content, "html5lib")
    # find all peoples
    all_cards = soup.find_all("div", {"class": "item poster card"})

    for card in all_cards:
        tid = int(card.find("a", {"class": "result"}).get("href").replace("/tv/", ""))
        title = card.find("a", {"class": "title result"}).text.replace("'", "''")
        vote_average = float(card.find_all("span", {"class": "vote_average"})[0].text)
        release_date = int(card.find_all("span", {"class": "release_date"})[0].text)
        rank = int(str(card.find("span", {"class": "hide popularity_rank_value"}).find("p").text).replace("Today: ", ""))
        genres = card.find_all("span", {"class": "genres"})[0].text
        overview = card.find_all("p", {"class": "overview"})[0].text.replace("'", "''")
        # print tid, title, vote_average, release_date, rank, genres, overview
        # now handle the detail information on the detail page
        detail_url = "https://www.themoviedb.org/tv/" + str(tid)
        r1 = requests.get(detail_url)
        soup1 = BeautifulSoup(r1.content, "html5lib")
        leftpanel = soup1.find("div", {"id": "leftCol"})
        attr_list = []
        for ele in leftpanel.find_all("p"):
            s = ele.text
            attr_list.append(s[s.find(':')+2:])
        # print attr_list
        air_on = attr_list[1]
        rating = attr_list[2]
        show_type = attr_list[3]
        status = attr_list[4]
        try:
            runtime = int(attr_list[5])
        except:
            runtime = 60
        lan = attr_list[6]
        img_url = leftpanel.find("img", {"class": "shadow"}).get("src")
        # save images to local system
        save_img(img_url, tid, base_path, "1.jpg")

        # print mid, title, vote_average, release_date, genres, img1
        insert_sql = "insert into tv_shows(tv_id,title,vote_average,release_year,ranking,genres,overview,air_on,rating,show_type,show_status,runtime,language) values(%d,'%s',%.1f,%d,%d,'%s','%s','%s','%s','%s','%s',%d,'%s');" % (tid, title, vote_average, release_date, rank, genres, overview, air_on, rating, show_type, status, runtime, lan)
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
    load_tv_data(url, p)

db.close()
#