from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import NewsSerializer
from newsroom.models import News


class NewsViewSet(ReadOnlyModelViewSet):
    queryset = News.objects.order_by('date')
    serializer_class = NewsSerializer
    pagination_class = None
