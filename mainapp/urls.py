from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('need_help/', views.need_help, name='need-help'),
    path('do_help/', views.do_help, name='do-help'),
    path('results/<str:cityName>/<str:req>', views.results, name='results')
]