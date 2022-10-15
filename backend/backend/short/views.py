from backend.short.models import Url
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect


@csrf_exempt
class ShortenUrl(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    @csrf_exempt
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        url = Url(long_url=body.get("long_url"))
        url.save()
        return JsonResponse({"short_url": url.short_url}, status=200)

    @csrf_exempt
    def get(self, request, short_url):
        queryset = Url.objects.all()
        url = get_object_or_404(queryset, pk=short_url)
        return HttpResponseRedirect(url.long_url)
