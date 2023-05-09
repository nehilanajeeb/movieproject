from .import views
from django.urls import path
app_name='movieapp'

urlpatterns = [

    path('',views.demo,name='demo'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    #path('add/',views.addition,name='addition')
    #path('about/',views.about,name='about'),
    #path('contacts/',views.contacts,name='contacts')
]