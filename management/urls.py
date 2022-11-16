# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(
    'SnippetViewSet', SnippetViewSet)
router.register(
    'SnippetSerializerLink', SnippetSerializerLink
)

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
    path('SnippetList', SnippetList.as_view(), name= 'SnippetList'),
    path('SnippetDetail/<int:pk>/', SnippetDetail.as_view()),  
    path('', include(router.urls)),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
