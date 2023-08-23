from django.http import JsonResponse
from rest_framework.response import Response

from api.serializers import CategorySerializer
from main.models import Category
from rest_framework.views import APIView


class ApiCategory(APIView):
    def get(self, request):
        category = Category.objects.all()
        data = CategorySerializer(category, many=True)
        return Response(data.data)
