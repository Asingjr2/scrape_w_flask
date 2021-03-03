# SCRAPE_ELEC

### Purpose
- Purpose of repo to to display return values from the python web scrapping library `scrapy`

### Background
- Flask is a python library that allows a users computer to act as webserver for web application development
- Scrapy is a python library that supports web page parsing and research.  This application is used for demonstration purposes only serving local webpages and sample api responses. 

### Requirements
- python => 3
- flask
- scrapy

### Implementation
- Update url value `'https://placeholder.com/'` in `backend\serato\serato\spiders\community_spider.py` with url of your choice
- Start local web server from `backend` root folder and run command python3 index.py

### Localhost Endpoints
- `/` - simulates web application homepage
- `/login` - simulates login page (form does not submit)
- `/bad_login` - simulates incorrect of fake user creds being passed and redirects user
- `/api/` - endpoints demonstrates sample api response values.  First reads local json file (try updating to see differences), second takes user parameter as part of `uri`, and third takes `uri` and creates custom json api response
- `/copy` - shows html from another page (demonstration purposes only)

### Documentation
- [Flask]('https://flask.palletsprojects.com/en/1.1.x/installation/')
- [Python]('https://www.python.org/downloads/')
- [Scrapy]('https://docs.scrapy.org/en/latest/intro/tutorial.html)"# scrape_w_flask" 
