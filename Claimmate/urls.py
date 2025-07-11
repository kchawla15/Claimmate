from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('register/', core_views.register, name='register'),
    path('logout/', core_views.force_logout, name='logout'),
    path('upload/', core_views.upload_warranty, name='upload_warranty'),
    path('budget-dashboard/', core_views.budget_dashboard, name='budget_dashboard'),  # <-- ADD THIS LINE
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
