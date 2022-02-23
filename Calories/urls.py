from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from FruitApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('image/upload/', views.ImageUploadTempView, name="image_upload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)