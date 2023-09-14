from django.db import models
class E(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=20)
    econtact=models.CharField(max_length=20)
    class Meta:
        db_table="Em"