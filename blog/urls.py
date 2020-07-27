from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.contact_form, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
