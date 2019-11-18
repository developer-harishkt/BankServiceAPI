from django.db import models

# Create your models here.
class Bank_Branches(models.Model):

    ifsc = models.CharField(max_length=11, null = False, primary_key = True)
    bank_id = models.CharField(max_length=100, blank=False, null=False)
    branch = models.CharField(max_length=74, blank=True, null=True)
    address = models.CharField(max_length=195, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=26, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.bank_id)


    class Meta:
        db_table = 'bank_branches'