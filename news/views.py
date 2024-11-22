from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import News
from .serializers import NewsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsListView(APIView):
    def get(self, request):
        return Response({'message': 'Список новостей'})
def example_view(request):
    return HttpResponse("Hello, this is an example view!")