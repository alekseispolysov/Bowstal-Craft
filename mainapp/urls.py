from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
	path('', views.HomePage.as_view(), name='home-page'),
	path('news/', views.NewsPage.as_view(), name='news-page'),
	path('news/all/', views.NewsAllPage.as_view(), name='news-all'),
	path('about/', views.AboutPage.as_view(), name='about-page'),
	path('support/us/', views.SupportUs.as_view(), name='support-us-page'),
	path('download/', views.DownloadPage.as_view(), name='download-page'),
	path('post/<str:pk>/', views.PostDetailPage.as_view(), name='post-detail'),
	path('contact/', views.ContactPage.as_view(), name='contact-page'),
	path('contact/confirm', views.ConfirmPage.as_view(), name='confirm-contact-page'),
	path('security/report/bug', views.SecurityContactPage.as_view(), name='secutiry-report-bug'),
	path('security/success/', views.SuccessSecurityPage.as_view(), name='secutiry-report-success'),
]