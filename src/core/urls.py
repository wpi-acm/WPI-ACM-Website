from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

from core.views import *

urlpatterns = patterns('core.views',
    url(r'^$', TemplateView.as_view(template_name='core/index.html')),
    url(r'^join$', TemplateView.as_view(template_name='core/join.html')),
    url(r'^about$', TemplateView.as_view(template_name='core/about.html')),
    url(r'^contact$', TemplateView.as_view(template_name='core/contact.html')),
    url(r'^members$', 'members'),
)
