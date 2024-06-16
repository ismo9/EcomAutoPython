from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('product/<int:pk>', views.product, name="product"),
    path('category/<str:foo>', views.category, name="category"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/submit_review/', views.submit_review, name='submit_review'),
    path('order/history/', views.order_history, name='order_history'),
]