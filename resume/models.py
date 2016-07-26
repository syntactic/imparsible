from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()

class Resume(SingletonModel):
    name = models.CharField(max_length=40)


class Education(models.Model):
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    end_date = models.DateField(default=date.today())
    resume = models.ForeignKey(Resume)

    def __str__(self):
        return self.major + ", " + self.school + ", " + str(self.end_date)

class Experience(models.Model):
    company = models.CharField(max_length=50)
    resume = models.ForeignKey(Resume)

    def __str__(self):
        return self.company

