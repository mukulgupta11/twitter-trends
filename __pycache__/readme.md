# Twitter Trending Topics Scraper

This project uses Selenium to scrape the top 5 trending topics from Twitter's "What’s Happening" section. The scraped data, along with metadata, is stored in a MongoDB database and displayed on a simple HTML page. The project also integrates ProxyMesh to route each request through a new IP address.

---

## Features

1. **Scrape Twitter's Trending Topics**: Fetch the top 5 trends from the "What’s Happening" section.
2. **Proxy Integration**: ProxyMesh ensures each request is sent from a new IP address.
3. **MongoDB Storage**: Stores the results with a unique ID, trends, date, time, and IP address.
4. **Dynamic HTML Page**: A simple HTML interface to run the script and display results dynamically.
5. **Flask Backend**: Facilitates communication between the HTML frontend and Selenium script.

---

## Prerequisites

1. Python 3.x
2. Node.js (optional for hosting static HTML files)
3. MongoDB (running locally or hosted)
4. Google Chrome and ChromeDriver
5. ProxyMesh account for proxy rotation
6. Twitter account for login

---
## .env
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password

PROXYMESH_URL=your_proxymesh_url

MONGODB_URI=mongodb://localhost:27017/

FLASK_ENV=development
FLASK_DEBUG=1
