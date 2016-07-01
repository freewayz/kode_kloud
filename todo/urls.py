__author__ = 'peter'


from django.conf.urls import url
from views import TodoList, TodoDetail, TodoApiViewGetPost, kamba_view
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^todos/$', view=TodoList.as_view(), name="todo_list_create"),
    url(r'^board/$', view=kamba_view, name="kamba_board"),
    url(r'^todos/(?P<pk>[0-9])/$', view=TodoDetail.as_view(), name="todo_details"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
