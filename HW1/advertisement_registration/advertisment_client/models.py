from django.db import models

class Advertisement(models.Model):
    id=models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    email = models.EmailField()
    caregory=models.CharField(max_lentgh=50)
    state=models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title