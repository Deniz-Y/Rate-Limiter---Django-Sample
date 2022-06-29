from warnings import catch_warnings
from xmlrpc.client import boolean
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ratelimit.decorators import ratelimit
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from ratelimit.exceptions import Ratelimited

def handler403(request, exception=None):
    if isinstance(exception, Ratelimited):
        return HttpResponse('Sorry you are blocked', status=429)
    return HttpResponseForbidden('Forbidden')

@api_view()
@permission_classes([AllowAny])
@ratelimit(key='ip', rate = '5/2m', block=True)
def secondFunction(request):
    return Response({'message': "Hello from secondFunction"})

@api_view()
@permission_classes([AllowAny])
@ratelimit(key='header:x-ip', rate='10/m', block=True)
def thirdFunction(request):
    return Response({'message': "Hello from thirdFunction"})
