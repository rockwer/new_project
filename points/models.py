from django.db import models

# Create your models here.


class Point(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    photo = models.ForeignKey('Photo', on_delete=models.SET_NULL, null=True)
    description = models.TextField(default='')
    importence = models.ForeignKey('Importence', on_delete=models.SET_NULL, null=True, blank = True)
    facebook = models.URLField(max_length=200, blank = True)
    wiki = models.URLField(max_length=200, blank = True)
    trip_advisor = models.URLField(max_length=200, blank = True)
    coordinate = models.FileField(upload_to='uploads/coordinate', max_length=100, default='')
    adress = models.CharField(max_length=200, default='')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title+' (id: %s)' % self.create_time


class Importence(models.Model):
    title = models.FloatField()

    def __str__(self):
        return str(self.title)


class Type(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ForeignKey('Icon',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Icon(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/icons', max_length=100, default='')

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/Photos', max_length=100, default='')
    copyright = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='points/uploads/country flags', max_length=100, default='')

    def __str__(self):
        return self.title


class City (models.Model):
    title = models.CharField(max_length=100)
    country = models.ForeignKey('Country',  on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title