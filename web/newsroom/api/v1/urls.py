from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet, basename='News')
urlpatterns = router.urls
