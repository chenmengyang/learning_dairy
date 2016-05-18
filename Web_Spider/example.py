# This is an example of web spider using python + bs4
# https://www.youtube.com/watch?v=3xQTJi2tqgk
# we are going to scrape the yellowpages.com, search coffee near Los Angeles, CA

# First we are checking the source code of that web page, using chorme, right click the item and choose inspect
# and we found that the interesting data are located in the  <div class="info"> tag

# Second install needed libraries:
# 1. sudo pip install requests --upgrade
# 2. sudo pip install beautifulsoup4 --upgrade

import requests
from bs4 import BeautifulSoup

# It will take a seconds
url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url)

# This will show all the html codes, but not useful, so that's why beautifulsoap comes in
# r.content

# Now it can be much better to read the html
soup = BeautifulSoup(r.content, "html5lib")
print soup.prettify()

# How to get all urls in that page?
links = soup.find_all("a")
for link in links:
  print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
