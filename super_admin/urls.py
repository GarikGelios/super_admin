from django.urls import path, include

urlpatterns = [
    path('admin/', include('core.urls', namespace='admin'))
]
