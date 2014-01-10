from bs4 import BeautifulSoup
import urllib2
from placetoplay.models import Games
from django.db import models
import sys
sys.path.append('C:\Python27\Lib\site-packages\django-1.6-py2.7.egg\django\bin\product\placetoplay')

#This function is for populating the games table of the database
def get_games():
    print "--------populating games database---------"
    url = "http://www.boardgamegeek.com/xmlapi/collection/eekspider"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())

    xml_list = soup.findAll('item')
    #shortcut to getting a length of games to parse through going through a user's collection
    for id in xml_list:
        game_id = id['objectid']
        url = "http://www.boardgamegeek.com/xmlapi/boardgame/" + game_id +"?stats=1"
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())

        #checking if info exists before adding to DB
        name = soup.find('name')
        description = soup.find('description')
        maker = soup.find('boardgamepublisher')
        category = soup.find('boardgamecategory')
        mechanics = soup.find('boardgamemechanic')
        date_published = soup.find('yearpublished')
        rating = soup.find('average')
        amount_owned = soup.find('owned')
        playtime = soup.find('playingtime')
        optimal_age = soup.find('age')
        image_path = soup.find('image')

        #validating data before saving
        if name == None:
            game = Games(name = "No data")
            game.save()
        else:
            game = Games(name = unicode(name.string))
            print "Saving name"
            game.save()

        gg = Games.objects.get(id = game.id)

        if description == None:
            gg.description = "No data"
            gg.save()
        else:
            gg.description = unicode(description.string)
            gg.save()
            print "description saved"

        if category == None:
            gg.category = "No data"
            gg.save()
        else:
            gg.category = unicode(category.string)
            print "check1"
            gg.save()
            print "category saved"

        if mechanics == None:
            gg.mechanics = "No data"
            gg.save()
        else:
            gg.mechanics = unicode(mechanics.string)
            gg.save()
            print "mechanics saved"

        if date_published == None:
            gg.date_published = "No data"
            gg.save()
        else:
            gg.date_published = unicode(date_published.string)
            gg.save()
            print "publishing date saved"

        if rating == None or 0:
            gg.average_rating = "No data"
            gg.save()
        else:
            gg.average_rating = unicode(rating.string)
            gg.save()
            print "rating saved"

        if amount_owned == None:
            gg.amount_owned = "No data"
            gg.save()
        else:
            gg.amount_owned = unicode(amount_owned.string)
            gg.save()
            print "amount owned saved"

        if playtime == None or 0:
            gg.playtime = "No data"
            gg.save()
        else:
            gg.playtime = unicode(playtime.string)
            gg.save()
            print "playtime saved"

        if optimal_age == None or 0:
            gg.optimal_age = "No data"
            gg.save()
        else:
            gg.optimal_age = unicode(optimal_age.string)
            gg.save()
            print "age saved"

        if maker == None:
            gg.maker = "No data available"
            gg.save()
        else:
            gg.maker = unicode(maker.string)
            gg.save()
            print "maker saved"

        if image_path == None:
            gg.image_path = "No image avaliable"
            gg.save()
        else:
            gg.image_path = unicode(image_path.string)
            gg.save()
            print "image saved"
    print "-------------database populated--------------"