
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'))
    re_path(r'^uploads/products/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#if settings.DEBUG:
#urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS[0])
#urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)