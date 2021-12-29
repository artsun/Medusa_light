from django.urls import path, include

urlpatterns = [
    path('v1/', include('newsroom.api.v1.urls'))
]
