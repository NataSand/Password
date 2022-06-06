from django.db import models

# Create your models here.


class Example(models.Model):
    integer_field = models.IntegerField()
    positive_field = models.PositiveIntegerField()
    positive_small_field = models.PositiveSmallIntegerField()
    big_integer_field = models.BigIntegerField()
    float_field = models.FloatField()
    binary_field = models.BinaryField()
    boolean_field = models.BinaryField()
    char_field = models.CharField(max_length=5)
    text_field = models.TextField(max_length=20)
    date_field = models.DateField(auto_now=True)
    date_time_field = models.DateTimeField(auto_now_add=True)
    decimal_field = models.DecimalField(max_digits=8, decimal_places=2)
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='file')
    image_field = models.ImageField(upload_to='images')


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname


class Student(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name + ' ' + self.surname


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    time_create = models.DateTimeField(auto_now_add=False, blank=True)
    time_update = models.DateTimeField(auto_now=False, blank=True)
    is_published = models.BooleanField(default=True)
    price = models.IntegerField()
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'place {self.name}'


class Hotel(models.Model):
    place = models.OneToOneField('Place', on_delete=models.CASCADE, null=True)
    group = models.CharField(max_length=100)

    def __str__(self):
        return f'the hotel {self.place.name}'


class Manager(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} is manager of {self.hotel}'
