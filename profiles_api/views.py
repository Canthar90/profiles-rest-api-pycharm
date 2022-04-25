from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test APi View"""


    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, powst, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over you application project',
            "Is mapped anually to URL's",
        ]

        return Response({'message': 'Hello', 'an_apivier': an_apiview})