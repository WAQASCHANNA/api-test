from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def change_language(request):
    if request.method == 'POST':
        language = request.data.get('language')
        # Implement language change logic here
        return Response({"message": f"Language changed to {language}"})
    elif request.method == 'GET':
        # Return the current language or other relevant information
        return Response({"message": "Current language is ..."})

