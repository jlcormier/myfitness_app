from django.contrib import admin
from goals import views as goals_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('', goals_views.index.as_view(), name='home'),
    path('api/goals/', goals_views.goals_details),
    path('api/goals/<int:pk>/', goals_views.goal_detail),
    path('api/goals/published/', goals_views.goal_detail_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)