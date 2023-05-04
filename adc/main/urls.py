from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('projects', views.projects, name="projects"),
    path('products', views.products, name="products"),
    path('projects/<slug:case_slug>/', views.show_case, name="show_case"),
    path('<slug:post_slug>/', views.show_product, name="show_product"),


]
