## emojizebot

This bot is based off of [this tutorial](http://readwrite.com/2014/06/20/random-non-sequitur-twitter-bot-instructions/).
and consequently [@tommeagher's heroku_ebooks](https://github.com/tommeagher/heroku_ebooks)

This is a basic Python port of [@harrisj's](https://twitter.com/harrisj) [iron_ebooks](https://github.com/harrisj/iron_ebooks/) Ruby script. Using Heroku's scheduler, you can post to an _ebooks Twitter account based on the corpus of an existing Twitter at pseudorandom intervals. Currently, it is the magic behind [@adriennelaf_ebx](http://www.twitter.com/adriennelaf_ebx) and [@stevebuttry_ebx](http://www.twitter.com/stevebuttry_ebx).

## Local Settings

Set up the bot with the Twitter API by reading the links above. Rename local_settings_example.py to local_settings.py

## Debugging

If you want to test the script or to debug the tweet generation, adjust the `DEBUG` variable in `local_settings.py`.

```
DEBUG = True 
```

## Deploying

Commit the change and `git push heroku master`. Then run the command `heroku run worker` on the command line and watch what happens.
