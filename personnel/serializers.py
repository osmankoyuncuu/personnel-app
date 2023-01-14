from rest_framework import serializers
from .models import Department, Personnel

class PersonnelSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField(write_only=True)
    start_date = serializers.DateTimeField(write_only=True, required=False)
    days_since_joined = serializers.SerializerMethodField()
    create_user = serializers.StringRelatedField()
    create_user_id = serializers.IntegerField(required=False)
    
    class Meta:
        model = Personnel
        fields = ("id", "days_since_joined","create_user","create_user_id",  "first_name", "last_name", "is_staffed", "title", "gender", "salary", "start_date", "department", "department_id" )
        
    def get_days_since_joined(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.day - obj.start_date.day
    
    #! active user create
    def create(self, validated_data): 
        validated_data["create_user_id"] = self.context["request"].user.id
        instance = Personnel.objects.create(**validated_data)
        return instance
        
    
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
        
        
