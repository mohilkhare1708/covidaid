from django.shortcuts import render, redirect
from mainapp.forms import CityForm
import tweepy,json
from tweepy.streaming import StreamListener

access_token="717644539167526912-MFhr46JcY1XxJo7mXG8tYxxPn4E84Bs"
access_token_secret="yPcmazV805V8AYZTjBHPtGC4HBVjxEOz26WxCM0oQSss7"
consumer_key="o4J8U2DNIhRH28VwDO9RJIPpQ"
consumer_secret="HM6RMEKahZmswQ3hQzWKlQkB5PM100wiHcMftXISypkDXdorCL"


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
            print(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

def home_page(request):
    return render(request, 'mainapp/home.html', {'title': 'Home'})

def need_help(request):
    return render(request, 'mainapp/need_help.html', {'title': 'Home'})

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
        'title' : 'Help'
    }
    return render(request, 'mainapp/do_help.html', context)

def results(request, cityName, req):
    print(req, type(req))
    #req.append(cityName)
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(['remdesivir', 'corona', 'oxygen'])
    return render(request, 'mainapp/results.html', {'city' : cityName, 'req' : req})

