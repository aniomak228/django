from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/admin/', admin.site.urls),
    path('news/create/admin/', admin.site.urls),
    path('news/<int:pk>/admin/', admin.site.urls),
    path('news/admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/login/admin/', admin.site.urls),
    path('accounts/signup/admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)