#Sweepstakes

Sweepstakes is a program written in Python that searches for Twitter tweets that contain certain keywords relating to contests. It processes and filters out tweets until it finds a list of credible original contests that offer the opportunity to win a prize if you retweet. Looping through the list found, it retweets and follows if necessary each tweet in order to be entered into various giveaways and contests.

##Setup

Sweepstakes was developed using Python v2.7.6. Some dependencies that Sweepstakes uses are Scrapy for web crawling, Selenium for user simulation, and Python-twitter for searching and requesting tweets. Run the following commands to clone the repo and install dependencies.

```sh
$ git clone https://github.com/AnthonyBobsin/sweepstakes.git
$ pip install scrapy selenium python-twitter
```

Selenium requires that you have a web driver installed. I use the Chrome driver which you can download [here](http://chromedriver.storage.googleapis.com/index.html?path=2.16/). If you wish to use a different web driver, install it, then change the initialize method in `Sweep/spiders/status.py` to match your driver.

In order for this program to use your specific Twitter account, you must create your own config file based on the one I provided. In order to do so run the following command in the project folder, then edit in your own credentials to the new file.

```sh
$ cp Sweep/spiders/config.example.py Sweep/spiders/config.py
```

Once you have completed the previous steps, you are good to run the program and let it crawl and retweet. To do this, you must run the command below. That will find appropriate tweets, launch the web driver, log you in to twitter, and navigate to each found tweet url retweeting and following accordingly.

```sh
$ python Sweep/sweep.py
```

Good luck with the many contests you will be entered in!