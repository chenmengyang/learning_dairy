# Since I am feeling so bad about using the moviedb API to get data, now we are going to scrape the data from this website: https://www.themoviedb.org/movie

# create table to store the data after scraping
# How to store the picture in mysql? How to download to 
# download to local file system first?
# If only storing the image address, how to program on plane?
from bs4 import BeautifulSoup
import requests
import MySQLdb

# connect to db
db = MySQLdb.connect("localhost", "cmy", "", "moviedb", use_unicode=True, charset='utf8')
cur = db.cursor()

create_sql = "create table if not exists movies\
(id int primary key\
,title varchar(100)\
,vote_average decimal(5,2)\
,release_year smallint\
,ranking smallint\
,genres varchar(100)\
,overview varchar(1000)\
,poster_adr1 varchar(200)\
,poster_adr2 varchar(200)\
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

# In total 984 pages and about 20,000 results
url = "https://www.themoviedb.org/movie?page="
# but we don't need to get all data now, just first 10 pages maybe enough
pages = [1,2,3,4,5,6,7,8,9,10]



def load_movie_data(link, page):
    r = requests.get(link+str(page))
    soup = BeautifulSoup(r.content, "html5lib")
    # find all cards
    all_cards = soup.find_all("div", {"class": "item poster card"})

    for card in all_cards:
        # id
        mid = int(card.find_all("a", {"class": "title result"})[0].get("id").replace("movie_", ""))
        # title
        title = card.find_all("a", {"class": "title result"})[0].text.replace("'", "''")
        # vote_average
        vote_average = float(card.find_all("span", {"class": "vote_average"})[0].text)
        # ranking
        rank = int(str(card.find("span", {"class": "hide popularity_rank_value"}).find("p").text).replace("Today: ", ""))
        # release_date
        release_date = int(card.find_all("span", {"class": "release_date"})[0].text)
        # genres
        genres = card.find_all("span", {"class": "genres"})[0].text
        # overview
        overview = card.find_all("p", {"class": "overview"})[0].text.replace("'", "''")
        # poster_adr1
        imgs = str(card.find_all("img", {"class": "poster"})[0].get("srcset"))
        img1 = imgs[0:imgs.index(',')].replace(" ", "").replace("1x", "")
        img2 = imgs[imgs.index(',')+1:].replace(" ", "").replace("2x", "")

        # print mid, title, vote_average, release_date, genres, img1
        insert_sql = "insert into movies(id,title,vote_average,release_year,ranking,genres,overview,poster_adr1,poster_adr2) values(%d,'%s',%.1f,%d,'%s','%s','%s','%s','%s');" % (mid, title, vote_average, release_date, rank, genres, overview, img1, img2)

        try:
            cur.execute(insert_sql)
            print "ok " + str(rank)
            db.commit()
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)
            print insert_sql
            db.rollback()

for p in pages:
    load_movie_data(url, p)

db.close()
#