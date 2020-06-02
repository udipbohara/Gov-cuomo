Analyzing support towards Gov Andrew Cuomo through the COVID-19 pandemic using tweets.
================

Overview
--------

In this project, I analyzed tweets that mentioned 'cuomo' over the months of the pandemic to see the response towards him. I used pre-trained library flair to get sentiments of all the tweets and visualized it.

The first case of COVID-19 in the U.S. state of New York during the pandemic was confirmed on March 1, 2020. I have used the tweets from 02/15/2020 to 05/18/2020 to run sentiment analysis on it. 

Scope of this project:
--------

I have __excluded__ retweets, replies and links as I believe, as a retweet/reply is more of a response to a tweet/article rather than a general sentiment towards Gov Cuomo. In doing so, I have also filtered out news articles as they are associated with links. Also, I have excluded tweets that contain 'chris' in them to avoid getting sentiments for Chris Cuomo (brother of Gov. Andrew Cuomo)


The following module from python is required to run the sentiments:

```
$ pip install flair
```

``` python
print('hello world!)
```

Part 1: Download Data
---------------------

The conventional tweeter API - [Tweepy](https://github.com/tweepy/tweepy) can be used to download the tweets. However, it is important to note limitations of the tweepy such as accessing historical tweets and rate limits. 

Other libraries such as [GetOldTweets3](https://github.com/Mottl/GetOldTweets3) and [twitterscraper](https://github.com/taspinar/twitterscraper) provide excellent alternatives, specially when downloading historical data. 

There are a few ways of downloading the tweets. They are all provided [here](https://github.com/udipbohara/Gov-cuomo/tree/master/scrapers). _Note_: Due to errors such as Request timeouts/handling errors, it is advisable to download batches of tweets (eg: one day at a time). 
Here is an example of a json object: Full raw data can be found in /data

``` json
[
   {
      "screen_name":"justice0123",
      "username":"@justice 4 All aka justice0123",
      "user_id":"1191989767",
      "tweet_id":"1256372347218599937",
      "tweet_url":"/justice0123/status/1256372347218599937",
      "timestamp":"2020-05-01T23:58:04",
      "timestamp_epochs":1588377484,
      "text":"Gov. Cuomo knew what he was doing when he told the nursing home u don't need 2 test these elderly ppl the nursing home responded & told him we don't have the man power or space mind you the Javits ctr was empty & so was the ship where he could have sent them their but he didn't",
      "text_html":"<p class=\"TweetTextSize js-tweet-text tweet-text\" data-aria-label-part=\"0\" lang=\"en\">Gov. <strong>Cuomo</strong> knew what he was doing when he told the nursing home u don't need 2 test these elderly ppl the nursing home responded &amp; told him we don't have the man power or space mind you the Javits ctr was empty &amp; so was the ship where he could have sent them their but he didn't</p>",
      "links":[

      ],
      "hashtags":[

      ],
      "has_media":false,
      "img_urls":[

      ],
      "video_url":"",
      "likes":0,
      "retweets":0,
      "replies":0,
      "is_replied":false,
      "is_reply_to":false,
      "parent_tweet_id":"",
      "reply_to_users":[

      ]
   }
```







Flair sentiment model:
```python
 Model config DistilBertConfig {
  "activation": "gelu",
  "architectures": [
    "DistilBertForMaskedLM"
  ],
  "attention_dropout": 0.1,
  "dim": 768,
  "dropout": 0.1,
  "hidden_dim": 3072,
  "initializer_range": 0.02,
  "max_position_embeddings": 512,
  "model_type": "distilbert",
  "n_heads": 12,
  "n_layers": 6,
  "pad_token_id": 0,
  "qa_dropout": 0.1,
  "seq_classif_dropout": 0.2,
  "sinusoidal_pos_embds": false,
  "tie_weights_": true,
  "vocab_size": 30522
}
```
__in terminal__:


twitterscraper "cuomo -chris" -bd 2020-02-15 -ed 2020-3-01 -o cuomofeb_part1.json

twitterscraper "cuomo -chris" -bd 2020-3-01 -ed 2020-3-15 -o cuomo_march_part1.json

twitterscraper "cuomo -chris" -bd 2020-3-15 -ed 2020-3-31 -o cuomo_march_part2.json



#doing with fixed one.

twitterscraper "cuomo -chris" -bd 2020-3-31 -ed 2020-4-15 -o cuomo_april_part2.json


#info about virus
On January 19, 2020, a 35-year-old man presented to an urgent care clinic in Snohomish County, Washington, with a 4-day history of cough and subjective fever.


jan15-31:
Found: 40188 tweets
Wrote: 4477 tweets

jan31-feb15:
Found: 49487 tweets
Wrote: 4943 tweets

feb-16-29
Found: 27079 tweets
Wrote: 3369 tweets

march-01-15
Found: 139582 tweets
Wrote: 9586 tweets
