from django.urls import path  

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the URLs from myapp
]
