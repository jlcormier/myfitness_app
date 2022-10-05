from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from exercise_logs import views as exercise_views

urlpatterns = [
    path('', exercise_views.index.as_view, name='home'),
    path('api/exercise_logs', exercise_views.exercise_list),
    path('api/exercise_logs/<int:pk>/', exercise_views.excerise_detail),
    path('api/exercise_logs/published/', exercise_views.exercise_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)