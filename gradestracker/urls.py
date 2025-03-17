from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from grades.views import custom_logout  # Import the custom logout view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('grades/', include('grades.urls')),
    path('', RedirectView.as_view(url='/grades/')),  # Redirect root URL to /grades/
    # Add this line for custom logout
    path('logout/', custom_logout, name='logout'),
]