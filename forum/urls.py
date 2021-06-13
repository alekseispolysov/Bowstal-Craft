from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.urls import path
from . import views
from django.urls import path, include

app_name = 'forum'

urlpatterns = [
	path('', views.ForumIndexPage.as_view(), name="forum-index-page"),
	path('create/', views.CreateForumPost.as_view(), name="forum-create-post"),
	path('update/<str:pk>/', views.UpdateForumPost.as_view(), name="forum-update-post"),
	path('delete/<str:pk>/', views.DeleteForumPost.as_view(), name="forum-delete-post"),
	path('post/<str:pk>/', views.DetailForumPage.as_view(), name='forum-detail-page'),
	path('search/', views.fullSearch.as_view(), name='forum-search'),
]


