from rest_framework import serializers
from .models import Project,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_photo','bio','location','contact') 
        
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','url','description','technologies','cover_photo')
