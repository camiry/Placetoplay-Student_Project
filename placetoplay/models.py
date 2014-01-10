from django.db import models
from django.contrib.auth.models import User

SKILL_CHOICES = (
        ("No prior experience", "No prior experience"),
        ("Novice", "Novice"),
        ("Intermediate", "Intermediate"),
        ("Skilled", "Skilled"),
        ("Expert", "Expert")
    )

class Games(models.Model):#all max_length and other limiters subject to change
    name = models.TextField(default="No name avaliable")
    description = models.TextField(default= "No description avaliable")
    maker = models.CharField(max_length=50, default=" ")
    category = models.CharField(max_length=50, default="No data")
    mechanics = models.TextField(default="No data")
    date_published = models.CharField(max_length=15, default=" ")#should I just change this to a string(charfield)?
    amount_owned = models.PositiveIntegerField(default="0")
    average_rating = models.DecimalField(max_digits=5, decimal_places=1, default=0.00000)
    comments = models.TextField(default="This game has no comments yet.")
    playtime = models.PositiveIntegerField(default="0")
    optimal_age = models.PositiveIntegerField(default="0")
    image_path = models.TextField(default="/static/mtg.jpeg")

class Groups(models.Model):
    name = models.CharField(max_length=90, verbose_name="group name")
    region = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=60, default="Placeholder address")
    games = models.TextField(default=" ", verbose_name="Games we play")
    special_rules = models.TextField(blank=True, verbose_name="house rules")
    skill_level = models.CharField(default="No skill level selected", max_length=30)
    #members = models.ManyToManyField(User, related_name="memberlist")
    email = models.EmailField(blank=True)
    phone = models.TextField(blank=True)
    schedule_date = models.DateField(auto_now=False, default='2013-10-13', verbose_name="event date")
    schedule_time = models.TimeField(auto_now=False, verbose_name="event time", default='00:00:00')
    schedule_event = models.TextField(default="Please check back soon for our first scheduled event!", verbose_name="event")
    image_path = models.CharField(default="/static/mtg.jpg", max_length=70, verbose_name="group picture", blank=True)
    private_group = models.BooleanField(default=False)
    games_link = models.ManyToManyField(Games, related_name="group games")
    admin_id = models.IntegerField(default=0)

class UserExtension(models.Model):
    user_link = models.OneToOneField(User, related_name="extension")
    friends = models.ManyToManyField('self')
    group_link = models.ManyToManyField(Groups, related_name="members")
    games_link = models.ManyToManyField(Games, related_name="link_to_games")
    city = models.CharField(max_length=30, blank=True)
    characteristics = models.TextField(max_length=255, blank=True)
    game_pref1 = models.CharField(max_length=30, verbose_name="Game preference")
    game_pref2 = models.CharField(max_length=30, blank=True, verbose_name="Second preference")
    game_pref3 = models.CharField(max_length=30, blank=True, verbose_name="Third preference")
    skill = models.CharField(blank=True, max_length=30, choices=SKILL_CHOICES, verbose_name="Experience")
    phone = models.CharField(blank=True, max_length=10)
    facebook = models.URLField(blank=True)
    image_path = models.CharField(default="/static/mtg.jpg", max_length=100, verbose_name="Profile picture")


#class User(models.Model)
    #extension = link back to all extended user fields

#DON'T FORGET ABOUT MANY-TO-MANY BETWEEN GROUPS AND GAMES
#DON'T FORGET ABOUT POSITIVE INTERGER FIELDS FOR LATER

