from django.urls import path, include

urlpatterns = [
    path('', include('RegLoginApp.urls')),
    path('travelers/', include('TravelersLog.urls')),
]
