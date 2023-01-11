from rest_framework import serializers
from .models import Department, Personnel

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ("id", "name", "personal_count")
        
    def get_personal_count(self, obj):
        return obj.personals.count()
class DepartmentPersonalSerializer(serializers.ModelSerializer):
    personals = PersonnelSerializer(many=True, required=False)
    personal_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ("id", "name", "personal_count", "personals")
        
    def get_personal_count(self, obj):
        return obj.personals.count()
        
        
