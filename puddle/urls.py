from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', include(('item.urls', 'item'), namespace='items')),
    path('users/', include('users.urls', namespace='users')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('notadmin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
