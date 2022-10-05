from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from weight_logs import views as weight_views

urlpatterns = [
    path('', weight_views.index.as_view, name='home'),
    path('api/weight_logs', weight_views.weight_list),
    path('api/weight_logs/<int:pk>/', weight_views.weight_detail),
    path('api/weight_logs/published/', weight_views.weight_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)