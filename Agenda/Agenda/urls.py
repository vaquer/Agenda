from django.conf.urls import patterns, include, url
from Agenda.Evento.views import Index,LogIn,Huevos,Error,Register
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Agenda.views.home', name='home'),
    # url(r'^Agenda/', include('Agenda.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Index),
    url(r'^login/$',LogIn),
    url(r'^error/$',Error),
    url(r'^huevos/$',Huevos),    
    url(r'^register/$',Register)
)
