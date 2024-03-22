from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',UserList.as_view(),name='index'),
    path('create/',UserCreate.as_view(),name='create'),
    path('detail/<int:pk>',UserDetail.as_view(),name='detail'),
    path('update/<int:pk>',UserUpdate.as_view(),name='update'),
    path('delete/<int:pk>',UserDelete.as_view(),name='delete')

]
