from django.urls import path

from . import views

app_name = 'vota'
urlpatterns = [
	path('home', views.logearse),
    path('index', views.IndexView.as_view(), name='index'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]