from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import Home, RobotsTxt

admin.autodiscover()

urlpatterns = patterns('')



urlpatterns += patterns('',
    (r'^$', Home.as_view(), {}, "home"),

    url(r'', include('partners.urls')),
    url(r'', include('bikes.urls')),

    (r'^mentions-legales\.html$', TemplateView.as_view(template_name="legal-mentions.html"), {}, "legal-mentions"),

    # sub menu shop
    (r'^presentation-du-magasin\.html$', TemplateView.as_view(template_name="shop/introduction.html"), {}, "shop-introduction"),

    #(r'^nous-contacter\.html$', TemplateView.as_view(template_name="shop/contact.html"), {}, "shop-contact"),

    # workshop
    (r'^les-services-reparation\.html$', TemplateView.as_view(template_name="workshop/introduction.html"), {}, "workshop-introduction"),
    (r'^location-de-box-reparation\.html$', TemplateView.as_view(template_name="workshop/workshop-box-rental-pending.html"), {}, "workshop-box-rental"),



    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^users/', include("users.urls")),
    url(r'', include("contact.urls")),
    #url(r'', include('password_reset.urls')),

    url(r'', include('sitemap.urls')),
    (r'^robots\.txt$', RobotsTxt.as_view()),

)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG: 
    if getattr(settings,'DISABLE_ROBOTS',False) is True:
        from django.http import HttpResponse
        urlpatterns += patterns('', 
                        url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
                        )


    urlpatterns += patterns('', 
                            url(r'^%s/(?P<path>.*)/?$' % settings.MEDIA_URL[1:-1] , 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT,}),
                            (r'^404$', TemplateView.as_view(template_name="404.html")),
                            (r'^500$', TemplateView.as_view(template_name="500.html")), 
                            )