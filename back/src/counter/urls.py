from django.contrib import admin
from django.urls import path, include
from counter.views import history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('history', history)
]
