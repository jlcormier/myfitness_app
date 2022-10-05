from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from foods import views as food_views

urlpatterns = [
    path('', food_views.index.as_view, name='home'),
    path('api/foods', food_views.food_list),
    path('api/foods/published/', food_views.food_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)