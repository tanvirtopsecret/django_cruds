from django.db import models


# Create your models here.
class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),

    )
    RELIGION = (
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Buddha', 'Buddha'),
        ('Cristian', 'Cristian'),
        ('Others', 'Others'),

    )
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('O+', 'O+'),

    )

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='prof_pic/', default='def.png')
    email = models.EmailField(max_length=25)
    phone_number = models.TextField(max_length=15)
    gender = models.CharField(choices=GENDER, max_length=8, default='----')
    address = models.TextField(max_length=40)
    religion = models.CharField(choices=RELIGION, max_length=8, default='----')
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=8, default='----')
    date_of_birth = models.DateField()
    is_alive = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.name
