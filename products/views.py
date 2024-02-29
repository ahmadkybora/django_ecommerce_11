from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={ "request": request })
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def productById(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, context={ "request": request })
    return Response(serializer, status=status.HTTP_200_OK)