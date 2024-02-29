from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET'])
def articles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True, context={ 'request': request })
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def articleById(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArticleSerializer(article, context={ 'request': request })
    return Response(serializer.data, status=status.HTTP_200_OK)
