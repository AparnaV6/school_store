from django.db import models
from django.db.models import When, Value
from django.urls import reverse


#Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('schoolapp:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Student(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("T", "Transgender"),
        ("Do not wish to disclose", "Do not wish to disclose")
    )
    DEPARTMENT_CHOICES = (
        ("General Sciences", "General Sciences"),
        ("Commerce", "Commerce"),
        ("Arts", "Arts"),
        ("Astronomy", "Astronomy"),
        ("Computer Science", "Computer Science")
    )
    GS = "General Science"
    C = "Commerce"
    A = "Arts"
    AS = "Astronomy"
    CS = "Computer Science"
    COURSE_CHOISES = [
        (GS, (
            (11, "BSc.Chemistry"),
            (12, "BSc.Physics"),
            (13, "BSc.Mathematics")
        )),
        (C, (
            (21, "B.Com"),
            (22, "M.Com")
        )),
        (A, (
            (31, "BA"),
            (32, "MA"),
        )),
        (AS, (
            (41, "BSc.Earth and Space Science"),
            (42, "BSc.Astrophysics"),
        )),
        (CS, (
            (51, "BSc.Computer Science"),
            (52, "BCA"),
            (53, "MCA")
        )),
    ]
    PURPOSE_CHOICES = (
        ("Enquiry", "For Enquiry"),
        ("Order", "To Place Order"),
        ("Return", "Return"),
    )

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    phone = models.IntegerField()
    mail_id = models.EmailField(max_length=250, unique=True)
    address = models.TextField()
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    courses = models.Case(
        When(department="General Sciences", then=COURSE_CHOISES[0]),
        When(department="Commerce", then=Value(COURSE_CHOISES[1])),
        When(department="Arts", then=Value(COURSE_CHOISES[2])),
        When(department="Astronomy", then=Value(COURSE_CHOISES[3])),
        When(department="Computer Science", then=Value(COURSE_CHOISES[4])),
    )
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    materials = models.BooleanField()

    def __str__(self):
        return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     slug = models.SlugField(max_length=250, unique=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product', blank=True)
#     stock = models.IntegerField()
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def get_url(self):
#         return reverse('schoolapp:prodCatdetail', args=[self.category.slug, self.slug])
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'product'
#         verbose_name_plural = 'products'
#
#
#     def __str__(self):
#         return '{}'.format(self.name)
