from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from tour.views import tourpage, tour
from evento.views import evento
from django.conf.urls.static import static

urlpatterns = [
    path('tourpage', tourpage, name='tourpage'),
    path('tour', tour, name='tour'),
    path('tour/<slug:slug>/', evento, name='evento'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('', include('core_01.urls')),
    path('', include('newusers.urls')),
    path('', include("somusic.urls")),
    path('', include("worker.urls")),
    path('', include("contact_us.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)