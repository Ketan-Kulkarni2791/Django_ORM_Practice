from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True, default=100)
    department_name = models.CharField(max_length=100, blank=False, null=False)
    
    class Meta:
        db_table = 'dev_schema"."department'
    
    def __str__(self) -> str:
        return self.department_name
