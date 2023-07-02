from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main.views import *

# Один список urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls')),
]

# Додаємо шляхи URL до списку urlpatterns
urlpatterns += i18n_patterns(
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('projects/', projects, name="projects"),
    path('products/<slug:post_slug>/', show_product, name="show_product"),
    path('products/', products, name="products"),
    path('projects/<slug:case_slug>/', show_case, name="show_case"),

    prefix_default_language=False,


)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
