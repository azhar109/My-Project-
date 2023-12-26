from django.db import models


class Apply(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30)
    campus = models.CharField(max_length=30)
    previousEducation = models.TextField(max_length=300)
    extracurricularActivities = models.TextField(max_length=100)
    password = models.CharField(max_length=30, default=1)
    confirm_password = models.CharField(max_length=30, default=1)

    def __str__(self):
        return self.firstname

    @staticmethod
    def email_get(email):
        try:
            email = Apply.objects.get(email = email)
        except:
            return False

    def email_check(self):
        if Apply.objects.filter(email = self.email):
            return True
        else:
            return False

    def check_phone(self):
        if Apply.objects.filter(phone = self.phone):
            return True
        else:
            return False