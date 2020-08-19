# python-keyword-scraper-email-notification
This Python script scrapes a list of urls, checks for keywords and will allow you through email about changes.

# Github Repo:
https://github.com/djerrund/python-keyword-scraper-email-notification

# Instructions
1. Download the Keywordscraper.py file.
2. Install the dependencies.
3. Download the Chrome Driver here: https://chromedriver.chromium.org/ 
4. Setup an email client to use. Easy instructions can be found here: https://realpython.com/python-send-email/
5. Find the Xpaths of the elements that you want to check for changes. Easy instructions can be found here: https://towardsdatascience.com/how-to-use-python-and-xpath-to-scrape-websites-99eaed73f1dd  
6. Implement your email info and Xpaths in the script.
7. Set the keywords, for instance a status of a product on a website can be "non available", this should then be your keyword. If this status changes you will get an email.
8. Run script. 
9. Use Cronjob to run script every x minutes. Easy instructions can be found here: https://medium.com/better-programming/how-to-execute-a-cron-job-on-mac-with-crontab-b2decf2968eb 
