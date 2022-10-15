from .models import Url
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import redirect
import re
from .services import UrlService


@csrf_exempt
class ShortenUrl(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    @csrf_exempt
    def post(self, request):
        body = request.POST.dict()
        long_url = body.get("long_url")

        if not long_url:
            return JsonResponse({"message": "URL Not found"}, status=400)

        if not UrlService.is_absolute(long_url):
            return JsonResponse({"message": "URL is not fully formed."}, status=400)

        url = Url(long_url=body.get("long_url"))
        url.save()
        return JsonResponse({"short_url": url.short_url}, status=200)

    def get(self, request, short_url):
        queryset = Url.objects.all()
        url = get_object_or_404(queryset, pk=short_url)
        url.visits += 1
        url.save()
        return redirect(url.long_url)
