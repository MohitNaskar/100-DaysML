from aem import app
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.posts_list,name='list'),
    path('new-post/', views.post_new, name='post_new'),
    path('<slug:slug>', views.post_page, name='posts_page'),
]