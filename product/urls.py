from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'product.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'placetoplay.views.base'),
    url(r'^games/$', 'placetoplay.views.gamelist_view'),
    #url(r'^games/(?P<page>\d+)/$', 'placetoplay.views.game_view'),
    url(r'^games/(?P<game_id>\d+)/$', 'placetoplay.views.game_view'),
    url(r'^profile/$', 'placetoplay.views.profile'),
    url(r'^profile/(?P<user_id>\d+)/$', 'placetoplay.views.profile'),
    url(r'^search/$', 'placetoplay.views.search_home'),
    url(r'^group_search/$', 'placetoplay.views.group_search'),
    url(r'^group_search/add/(?P<group_id>\d+)/$', 'placetoplay.views.group_add'),
    #url(r'^group_search/delete/(?P<group_id>\d+)/$', 'placetoplay.views.group_delete'),
    url(r'^group/(?P<group_id>\d+)/$', 'placetoplay.views.group_view'),
    url(r'^group/create/$', 'placetoplay.views.group_signup'),
    url(r'^signup/$', 'placetoplay.views.signup_view'),
    url(r'^signin/$', 'placetoplay.views.signin_view'),
    url(r'^logout/$', 'placetoplay.views.logout_view'),
    url(r'^editP/$', 'placetoplay.views.edit_profile'),
    url(r'^friends/$', 'placetoplay.views.view_friends'),
    url(r'^friend_search/$', 'placetoplay.views.friend_search'),
    url(r'^friend_search/add/(?P<user_id>\d+)/$', 'placetoplay.views.friend_add'),
    url(r'^friend_search/delete/(?P<user_id>\d+)/$', 'placetoplay.views.friend_delete')
    #url(r'^friends/(?P<user_id>\d+)/$', 'placetoplay.views.view_userfriends')#for other users <-- implement this later
)