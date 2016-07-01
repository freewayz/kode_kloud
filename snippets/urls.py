from django.conf.urls import url
from snippets.views import api_fbv
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

        url(r'^snippets/$', api_fbv.snippet_list),
        url(r'^snippets/(?P<pk>[0-9]+)/$', api_fbv.snippet_detail)
]


#let make our api view render different content type
urlpatterns = format_suffix_patterns(urlpatterns)