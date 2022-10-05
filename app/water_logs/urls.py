from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from water_logs import views as water_views

urlpatterns = [
    path('', water_views.index.as_view, name='home'),
    path('api/water_logs', water_views.water_list),
    path('api/water_logs/<int:pk>/', water_views.water_detail),
    path('api/water_logs/published/', water_views.water_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)