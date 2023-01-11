from rest_framework import serializers
from .models import Department, Personnel

class PersonnelSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Personnel
        fields = ("id","create_user", "first_name", "last_name", "is_staffed", "title", "gender", "salary", "start_date", "department", "department_id")

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
        
        
