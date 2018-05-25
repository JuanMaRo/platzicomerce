from django.urls import path, include
from comments.views import create_comment

app_name='comments'

urlpatterns = [
    path('createcomment', create_comment, name='createcomment'),
]
