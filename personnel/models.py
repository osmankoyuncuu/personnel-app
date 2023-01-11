from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Personnel(models.Model):
    TITLE = (
        (1, 'Team Lead'),  # db, kullanıcı
        (2, 'Mid Lead'),
        (3, 'Junior')
    )
    GENDER = (
        (1, 'Female'),  # db, kullanıcı
        (2, 'Male'),
        (3, 'Other'),
        (4, 'Prefer Not Say'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staffed = models.BooleanField(default=False)
    title = models.SmallIntegerField(choices=TITLE, default=3)
    gender = models.SmallIntegerField(choices=GENDER, default=4)
    salary = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    create_user = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="personals")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.department}"
        
