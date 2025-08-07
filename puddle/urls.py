from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import LandingPageView


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('shop/', include(('item.urls', 'item'), namespace='items')),
    # path('users/', include('users.urls', namespace='users')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
