from django.urls import path

from collegeapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('create',views.create,name='create'),
    path('view',views.view,name='view'),
    path('update/<int:Todo_id>',views.update,name='update'),
    path('delete/<int:Todo_id>',views.delete,name='delete')
]