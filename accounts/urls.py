from django.urls import path,include 
from rest_framework import routers
from . import views
from django.urls import re_path as url

router = routers.DefaultRouter()
router.register("users", views.UserView, basename='user')
router.register("anss", views.answerViewSet, basename='ans')
router.register("questions", views.questionViewSet, basename='question')
urlpatterns = [
    path('', views.homePage, name='index'),
    path('detail',views.profile, name='profile'),
    path('v1/', include(router.urls)),
    path('view_profile',views.view_profile, name='view_profile'),
    path('accounts/', include('allauth.urls')),

    path('base', views.base_view, name='home'), 
    path('all_questions/', views.all_questions, name = 'all_questions'),
    path('show_detailed_view_of_question/<int:pk>/', views.detailed_view_of_individual_question, name = 'detail_view'),
    path('show_answers/<int:pk>/', views.all_answers, name = 'show_answers'),
    path('show_searched_value', views.searched_vlaue, name='search_values'),
    path('ask_question/', views.ask_question, name='ask_question'),
    path('provide_your_answer/', views.provide_your_answer, name='provide_your_answer')
]