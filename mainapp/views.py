from django.shortcuts import render, redirect
from mainapp.forms import CityForm
import tweepy,json
from tweepy.streaming import StreamListener
from dotenv import load_dotenv
import os, json

load_dotenv()

access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')

class TwitterStreamer():
    def __init__(self):
        pass

    def stream_tweets(self, hash_tag_list):
        listener = StdOutListener()
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        stream = tweepy.Stream(auth, listener)
        stream.filter(track=hash_tag_list)

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            data = json.loads(data)
            print(data['text'])
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

def home_page(request):
    return render(request, 'mainapp/home.html', {'title': 'CovidAid - A helping hand to the help needers and providers'})

def need_help(request):
    return render(request, 'mainapp/need_help.html', {'title': 'Need help'})

def do_help(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            req = form.cleaned_data.get('required_help')
            cityName = form.cleaned_data.get('city_name')
            return redirect('results', cityName, req)
    else:
        form = CityForm()
    context = {
        'form' : form,
        'title' : 'Do help'
    }
    return render(request, 'mainapp/do_help.html', context)

def results(request, cityName, req):
    #req.append(cityName)
    req = req.strip('][').split(', ')
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(req)
    return render(request, 'mainapp/results.html', {'city' : cityName, 'req' : req})