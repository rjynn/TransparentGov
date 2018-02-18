from rest_framework import serializers

from main_search.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = [
            'pk',
            'title',
            'slug',
            'description',
            'committee',
            'category',
            'timestamp',
        ]
        read_only_fields = ['pk']


    def validate_title(self, value):
        qs = Meeting.objects.filter(title__iexact=value)
