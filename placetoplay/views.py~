from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django import forms
from placetoplay.forms import Userform, UserExtform, UserformEdit, UserformSignin, groupSignup
from placetoplay.models import UserExtension, Games, Groups
from django.contrib.auth.models import User
from django.contrib import auth, sessions
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Aggregate, Count
import Tkinter, tkMessageBox
import datetime
import urllib2
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


#function to process the landing page
def base(request):
    user = request.user
    #get most popular games
    game = Games.objects.all().order_by('-average_rating')
    if game:
        gamesPop = [game[0], game[1], game[2], game[3], game[4]]
    else:
	gamesPop = "None yet..."
    #get newest games
    publish = Games.objects.all().order_by('-date_published')
    if publish:
        gamesNew = [publish[0], publish[1], publish[2], publish[3], publish[4]]
    else:
	gamesNew = "None yet..."
    #get biggest groups
    group = Groups.objects.all().order_by('members')
    if group:
        group_big = [group[0], group[1], group[2]]
    else:
	group_big = "None yet..."
    #get poweruser
    userp = UserExtension.objects.all().order_by('friends')
    if userp:
        user_pop = userp[0]
    else:
	user_pop = "None yet..."
    return render(request, 'landing.html', {"user":user, "gamesPop":gamesPop, "gamesNew": gamesNew, "group": group_big, "userp": user_pop})


def test_view3(request, user_id=1):
    if not request.user.is_authenticated():
        tkMessageBox.showinfo("Log-in Error", "You have not logged in yet!")
        return redirect('/signin/?next=%s' % request.path)
    print "test3"
    return render(request, 'profile.html')

#function to render the search page
def search_home(request):
    if not request.user.is_authenticated():
        return redirect('/signin/?next=%s' % request.path)
    else:
        groups = Groups.objects.all()
        friends = request.user.extension.friends.all()
        #functionality to allow user to join different groups/request invite based on public group
        if request.POST:
            request.user.extension.group_link.add()
        return render(request, 'search.html', {"groups": groups, "friends": friends})

def test_view5(request):
    print "test5"
    return render(request, 'signup.html')




#function to authenticate and sign in to registered users
def signin_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user
        if user is not None and user.is_active:
            login(request, user)
            return redirect('placetoplay.views.profile')
        else:
            print "tkinter?"
            tkMessageBox.showerror("Log-in Error", "The username and password don't match.")
            return HttpResponseRedirect('/signin/')
    else:
        form = UserformSignin()
        return render(request, 'signin.html', {"form":form})

#log selected user out
def logout_view(request):
    logout(request)
    return redirect('placetoplay.views.base')#remember to change when you make the landing page view





# This is to display a profile page
def profile(request, user_id=None):
    if not request.user.is_authenticated():
        return redirect('/signin/?next=%s' % request.path)
    else:
        # Print id
        print user_id
        profile_user = None
        schedule = request.user.extension.group_link.all()
        if user_id == None:
            friends = request.user.extension.friends.all()
            profile_user = request.user
            friend_verification = True
            own_user = True
        else:
            get_user = User.objects.get(id=user_id)
            friends = get_user.extension.group_link.all()
            profile_user = get_object_or_404(User, pk=user_id)
            #friends = request.user.extension.friends.all()
            friend_verification = False
            own_user = False
            if request.user.extension.friends.filter(user_link=user_id).exists():
                friend_verification = True
        # Return the rendered tmpl
        return render(request, "profile.html", {
            'profile_user': profile_user,
            'friend_verification':friend_verification,
            "own_user": own_user,
            "schedule": schedule,
            "friends": friends
        })

#this allows the user to edit his profile information by retrieving the user's session data and allowing him to change it
def edit_profile(request):
    if not request.user.is_authenticated():
        return redirect('/signin/?next=%s' % request.path)
    form = UserformEdit(instance=request.user)
    formExt = UserExtform(instance=request.user.extension)
    print form.is_valid()
    #print formExt.is_valid()
    #saving any changes made
    if request.method == "POST":
        form = UserformEdit(request.POST, instance=request.user)
        formExt = UserExtform(request.POST, instance=request.user.extension)
        if form.is_valid():
            print form.is_valid()
            print formExt.is_valid()
            print form.errors
            print formExt.errors
            u = request.user
            ux = request.user.extension

            u.username = form.cleaned_data["username"]
            u.first_name = form.cleaned_data["first_name"]
            u.last_name = form.cleaned_data["last_name"]
            u.email = form.cleaned_data["email"]
            u.password = request.user.password
            u.save()#update_fields=['username', 'first_name', 'last_name', 'email'])
            #skipped over password change for now

            u.extension.city = formExt.cleaned_data["city"]
            ux.game_pref1 = formExt.cleaned_data["game_pref1"]
            ux.game_pref2 = formExt.cleaned_data["game_pref2"]
            ux.game_pref3 = formExt.cleaned_data["game_pref3"]
            ux.characteristics = formExt.cleaned_data["characteristics"]
            ux.skill = formExt.cleaned_data["skill"]
            ux.phone = formExt.cleaned_data["phone"]
            ux.image_path = formExt.cleaned_data["image_path"]
            ux.save()#update_fields=['city', 'game_pref1', 'game_pref2', 'game_pref3', 'characteristics', 'skill', 'phone'])

            return HttpResponseRedirect("/profile/")
        else:
            tkMessageBox.showerror("Log-in Error", "One or more fields are not valid.")
            print form.errors
            return HttpResponseRedirect('/editP/')
    else:
        return render(request, 'editP.html', {"edit":form, "editExt":formExt})






#function to initially sign people up
def signup_view(request):
    #not sure if I want to keep this...will any problems arise if people try to sign up while still logged in?
    if request.user.is_authenticated():
        logout_view(request)
        return redirect('/signup/')
    else:
        pass
    form = Userform()
    formExt = UserExtform()
    userReg = User()
    userExt = UserExtension()
    if request.method == "POST":
        print "check if runs through post"
        form = Userform(request.POST)
        formExt = UserExtform(request.POST)
        print form.errors
        print formExt.errors
        if form.is_valid() and formExt.is_valid():
            #first checking if any of these fields already exist in the DB
            print "check info"
            username = form.cleaned_data["username"]
            fname = form.cleaned_data["first_name"]
            email = form.cleaned_data["email"]
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                tkMessageBox.showinfo("Input Error", "The selected username/email was taken!")
                return HttpResponseRedirect("/signup/")
            #elif form.password != form.confirm_password:
            #    tkMessageBox.showinfo("Input Error", "The password fields do not match")
            #    return HttpResponseRedirect("/signup/")
            else:
                #if not, save the new user
                print "recording new user"
                userReg = User(
                    username=form.cleaned_data["username"],
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    email=form.cleaned_data["email"]
                )
                userReg.set_password(form.cleaned_data["password"])
                userReg.save()
                print "recording new user (cont)"
                userExt = UserExtension(
                    user_link=userReg,
                    city=formExt.cleaned_data["city"],
                    game_pref1=formExt.cleaned_data["game_pref1"],
                    game_pref2=formExt.cleaned_data["game_pref2"],
                    game_pref3=formExt.cleaned_data["game_pref3"],
                    characteristics=formExt.cleaned_data["characteristics"],
                    skill=formExt.cleaned_data["skill"],
                    phone=formExt.cleaned_data["phone"],
                    image_path=formExt.cleaned_data["image_path"]
                )
                userExt.save()
                #send to sign in page to log in
                return HttpResponseRedirect("/signin/")
        else:
            return HttpResponse("WRRRROOOOOONNNGGG")
    else:
        return render(request, "signup.html", {"form":form, "formExt":formExt})




#view to create groups
def group_signup(request):
    if not request.user.is_authenticated():
        return redirect('/signin/?next=%s' % request.path)
    form = groupSignup()
    if request.method == "POST":
        print "Check if posting"
        form = groupSignup(request.POST)
        print form.errors
        if form.is_valid():
            #check if group already exists
            group_name = form.cleaned_data["name"]
            if Groups.objects.filter(name=group_name).exists():
                tkMessageBox.showinfo("Input Error", "The selected username was taken!")
                return redirect("/group/create/")
            else:
                print "Creating new group"
                new_group = Groups(
                    name = form.cleaned_data["name"],
                    region = form.cleaned_data["region"],
                    address = form.cleaned_data["address"],
                    games = form.cleaned_data["games"],
                    special_rules = form.cleaned_data["special_rules"],
                    skill_level = form.cleaned_data["skill_level"],
                    email = form.cleaned_data["email"],
                    schedule_date = form.cleaned_data["schedule_date"],
                    schedule_time = form.cleaned_data["schedule_time"],
                    schedule_event = form.cleaned_data["schedule_event"],
                    private_group = form.cleaned_data["private_group"],
                    #image_path = form.cleaned_data["group_picture"],
                )
                new_group.save()
                if new_group.private_group == True:
                    print "private"
                    new_group.admin_id = request.user.id
                    new_group.save(update_fields=['admin_id'])
                else:
                    print "public"
                    new_group.admin_id = 0
                    new_group.save(update_fields=['admin_id'])
                request.user.extension.group_link.add(new_group)
                return redirect("placetoplay.views.group_view", group_id=new_group.id)
        else:
            return HttpResponse("Error: Form invalid")
    else:
        return render(request, 'group-create.html', {'form':form})

#view to search for groups
def group_search(request):
    if 'groupsearch' in request.GET and request.GET['groupsearch']:
        gs = request.GET['groupsearch']
        #gets us a list of groups who match the search terms
        groups = Groups.objects.filter(Q(name__icontains=gs) | Q(games__icontains=gs))
        friends = request.user.extension.friends.all()
        return render(request, 'group_search.html', {"query":gs, "groups":groups, "friends":friends})
    elif 'show_all' in request.GET and request.GET['show_all']:
        sa = "everything!"
        groups = Groups.objects.all()
        friends = request.user.extension.friends.all()
        return render(request, 'group_search.html', {"groups":groups, "query": sa, "friends":friends})
    else:
        tkMessageBox.showinfo("Invalid search", "Please enter a search query.")
        return redirect('placetoplay.views.search_home')

#view to render group pages
def group_view(request, group_id):
    if not request.user.is_authenticated():
        return redirect('/signin/?next=%s' % request.path)
    else:
        profile_group = get_object_or_404(Groups, pk=group_id)
        public_group = False
        string = profile_group.address
        location = string.replace(" ", "+")
        games = profile_group.games_link.all()
        members = profile_group.members.all()
        print request.user.extension.group_link.filter(pk=group_id)
        if profile_group.admin_id == 0:
            public_group = True
        else:
            #if private group, query if request.user is a member of said group; if s/he is a member public_group = True, else pass
            if request.user.extension.group_link.filter(pk=group_id).exists():
                public_group = True
            else:
                public_group = False
        if profile_group.admin_id == request.user.id:
            #give said user privilidge to boot people and invite/accept people into the group; passing for now
            pass
        else:
            pass
    # Return the rendered tmpl
    return render(request, "group-profile.html", {'profile_group': profile_group, "public_group":public_group, "location": location, "games":games, "members":members})

#adds members to public groups
def group_add(request, group_id):
    new_group = Groups.objects.get(id=group_id)
    if request.user.extension.group_link.filter(id=group_id).exists():
        print "Group already added"
        pass
    else:
        print "Adding new group"
        request.user.extension.group_link.add(new_group)
        print request.user.extension.group_link.all()
    return redirect("placetoplay.views.profile")




#function to view friends' list
def view_friends(request):
    if not request.user.is_authenticated():
        return redirect('/signin/?next=%s' % request.path)
    friends = request.user.extension.friends.all()
    return render(request, 'friends.html', {"friends":friends})

#function to search for friends
def friend_search(request):
    if 'friend_search' in request.GET and request.GET['friend_search']:
        fs = request.GET['friend_search']
        #gets us a list of users who match the search terms
        friends = User.objects.filter(username__icontains=fs)
        return render(request, 'friend_search.html', {"query":fs, "friends":friends})
    else:
        tkMessageBox.showinfo("Invalid search", "Please enter a search query.")
        return redirect('placetoplay.views.view_friends')

#function to actually add friends to current user's list
def friend_add(request, user_id):
    new_friend = User.objects.get(id=user_id)
    if request.user.extension.friends.filter(user_link=user_id).exists():
        print "Friend already added"
        pass
    else:
        print "o shit new friend"
        request.user.extension.friends.add(new_friend.extension)
    return redirect("placetoplay.views.view_friends")

#function to drop friends from current user's friend list
def friend_delete(request, user_id):
    bad_friend = User.objects.get(id=user_id)
    if request.user.extension.friends.filter(user_link=user_id).exists():
        print "Friend bout to get his ass dropped"
        request.user.extension.friends.remove(bad_friend.extension)
    else:
        print "o shit he ain't even hurr"
        pass
    return redirect("placetoplay.views.view_friends")




#function to render the games list page
def gamelist_view(request):
    if not request.user.is_authenticated():
        return redirect('/signin/?next=%s' % request.path)
    games = Games.objects.all()
    search = False
    paginator = Paginator(games, 10)
    page = request.GET.get('page')
    try:
        lst_game = paginator.page('page')
    except PageNotAnInteger:
        lst_game = paginator.page(1)
    except EmptyPage:
        lst_game = paginator.page(paginator.num_pages)
    if 'gamesearch' in request.GET and request.GET['gamesearch']:
        search = True
        gs = request.GET['gamesearch']
        search_game = Games.objects.filter(name__icontains=gs)
        return render(request, 'games.html', {"search_game": search_game, "search": search})
    else:
        pass
    return render(request, 'games.html', {"games": lst_game, "search": search})

#function to render the individual game pages
def game_view(request, game_id):
    game = Games.objects.get(id=game_id)
    string = game.description
    dic = {"<br/>":" ", "&quot;":""}
    description = replace_annoying(string, dic)
    print description
    return render(request, 'game_view.html', {"game": game, "description": description})

#helper function to parse out bad characters in description string
def replace_annoying(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
