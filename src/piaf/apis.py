from random import randint
import json

from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ParagraphBatch, Paragraph


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
            "is_certified",
        )


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)


@method_decorator(csrf_exempt, name="dispatch")
class ParagraphView(APIView):
    permission_classes = [IsAuthenticated]

    # Provide a randomly picked pending article.
    def get(self, request, *args, **kwargs):
        theme = request.GET.get("theme")
        qs = ParagraphBatch.objects.filter(status="pending")
        # Limit display by audience
        if getattr(request.user, "is_certified", False):
            qs_certified = qs.filter(paragraphs__article__audience="restricted")
            if qs_certified.count():
                qs = qs_certified
        else:
            qs = qs.filter(paragraphs__article__audience="all")

        # Limit by theme
        if theme:
            qs = qs.filter(paragraphs__article__theme=theme)
        if not qs.count():
            return Response({})
        # Pick one batch, randomly
        batch = qs[randint(0, qs.count() - 1)]
        article = batch.article
        paragraph = batch.paragraphs.filter(status="pending").first()
        data = {
            "id": paragraph.id,
            "theme": article.theme,
            "text": paragraph.text,
            "title": article.name,
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        paragraph = Paragraph.objects.get(pk=data["paragraph"])
        paragraph.complete(data["data"], request.user)
        return Response(status=201)
