import twitter

api = twitter.Api(consumer_key='FJJvQyFC05yCJK0OXJpTm3sDA',
    consumer_secret='v7XMILiw2Q0PvlBiA8qlYIj9D0SGAyCYETlHKYr7PyQp6RRrbd',
    access_token_key='3419005059-36mODCZWvCbE81NTjL2sSrjjOkNDkNbJuo6SsSH',
    access_token_secret='9WRTof9gkOiriwT0QjUPlDx0llHd91rgXVChhWo12qtWl')

api.VerifyCredentials()

{"created_at": "Wed Aug 12 23:47:48 +0000 2015", "default_profile_image": true, "description": "Aspiring DJ", "id": 3419005059,
"lang": "en", "location": "Toronto, Ontario", "name": "Vince Hardaway", "profile_background_color": "000000",
"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "profile_background_tile": false,
"profile_image_url": "https://abs.twimg.com/sticky/default_profile_images/default_profile_1_normal.png", "profile_link_color": "3B94D9",
"profile_sidebar_fill_color": "000000", "profile_text_color": "000000", "protected": false, "screen_name": "VinceHardaway",
"status": {"created_at": "Thu Aug 13 00:01:48 +0000 2015", "favorited": false, "id": 631616606108520453, "lang": "en", "retweet_count": 350,
"retweeted": true, "retweeted_status": {"created_at": "Mon Aug 10 21:21:44 +0000 2015", "favorite_count": 108, "favorited": false,
"id": 630851550156599296, "lang": "en", "retweet_count": 350, "retweeted": true, "source": "<a href=\"http://www.sprinklr.com\" rel=\"nofollow\">Sprinklr</a>",
"text": "The company formerly known as Google plans to create a new public holding company: Alphabet Inc.\nhttp://t.co/YVgBa0tQgL",
"truncated": false, "urls": {"http://t.co/YVgBa0tQgL": "http://onforb.es/1MlsTRh"}}, "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
"text": "RT @Forbes: The company formerly known as Google plans to create a new public holding company: Alphabet Inc.\nhttp://t.co/YVgBa0tQgL",
"truncated": false, "urls": {"http://t.co/YVgBa0tQgL": "http://onforb.es/1MlsTRh"}, "user_mentions": [{"id": 91478624, "name": "Forbes", "screen_name": "Forbes"}]},
"statuses_count": 1, "time_zone": "Eastern Time (US & Canada)", "utc_offset": -14400}

tweets = api.GetSearch(term='#contest', count=30) # ARRAY OF STATUSES

tweet = tweets[0]

tweet.text == "This is my first tweet"
tweet.GetRetweeted() == False

api.PostRetweet(status_id)