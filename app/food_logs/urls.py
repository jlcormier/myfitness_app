from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from food_logs import views as foodlog_views

urlpatterns = [
    path('', foodlog_views.index.as_view, name='home'),
    path('api/food_logs', foodlog_views.foodlog_list),
    path('api/food_logs/<int:pk>/', foodlog_views.foodlog_detail),
    path('api/food_logs/published/', foodlog_views.foodlog_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)