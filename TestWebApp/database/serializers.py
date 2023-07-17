from rest_framework import serializers
from .models import Notes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'anons', 'full_text', 'date', 'category']
