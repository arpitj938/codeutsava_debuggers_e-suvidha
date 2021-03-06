"""sulabh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from review.views import open_index,get_review,send_review
from location.views import near_location_json
from analysis.views import usage_graph,date_graph,send_all_location,usage_post_graph,date_graph,usage_post_graph,date_post_graph
from user_data.views import login,forgot_password


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_review$', get_review),
    url(r'^send_review$', send_review),
    url(r'^near_location$', near_location_json),
    url(r'^usage/(?P<value>.+)/$', usage_graph),
    url(r'^date/(?P<value>.+)/$', date_graph),
    url(r'^send_all_location$', send_all_location),
    url(r'^usage_post_graph$', usage_post_graph),
    url(r'^date_post_graph$', date_post_graph),
    url(r'^login$', login),
    url(r'^forgot$', forgot_password),


]

admin.site.site_header = "Sulabh"
admin.site.index_title = 'Sulabh'
admin.site.site_title = 'Sulabh'

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
