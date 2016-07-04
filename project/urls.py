"""globalevelo2 URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.base import TemplateView

from views import Home, RobotsTxt,Magasin, Mentions

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]



urlpatterns += [
    url(r'^$', Home.as_view(), {}, "home"),

    
    url(r'', include('bikes.urls')),

    url(r'^presentation-du-magasin\.html$', Magasin.as_view(), {}, "magasin"),
    url(r'^mentions-legales/$', Mentions.as_view(), {}, "mentions"),

    url(r'^partenaires/', include('partners.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include("contact.urls")),

    url(r'', include('sitemap.urls')),
    url(r'^robots\.txt$', RobotsTxt.as_view()),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    if getattr(settings,'DISABLE_ROBOTS',False) is True:
        from django.http import HttpResponse
        urlpatterns += [
                        url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
                        ]


    urlpatterns += [
                            url(r'^%s/(?P<path>.*)/?$' % settings.MEDIA_URL[1:-1] , 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT,}),
                            url(r'^404$', TemplateView.as_view(template_name="404.html")),
                            url(r'^500$', TemplateView.as_view(template_name="500.html")),
                            ]