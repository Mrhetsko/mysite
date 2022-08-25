from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.user_logout, name='logout'),
    path('test/', views.test, name='test'),
    path('test2/', views.send_my_mail, name='send-mail'),
    path('contact/', views.contact, name='contact'),
    # path('', views.index, name='home'),
    path('', views.HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', views.get_category, name='category'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', views.ViewNews.as_view(), name='view_news'),
    # path('news/add_news', views.add_news, name='add_news'),
    path('news/add_news', views.CreateNews.as_view(), name='add_news'),
]
