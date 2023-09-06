from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('projects', views.projects, name="projects"),

    path('projects/<slug:case_slug>/', views.show_case, name="show_case"),
    path('products/<slug:post_slug>/', views.show_product, name="show_product"),
    # path('news/<slug:post_slug>/', views.news_product, name="news_product"),
    path('products', views.products, name="products"),



]
