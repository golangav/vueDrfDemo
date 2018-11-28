from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 999999.99
    pub_date = models.DateTimeField()  # "2012-12-12"
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)  # 级联删除
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.CharField(max_length=32)
    ad = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    addr = models.CharField(max_length=32)
    tel = models.IntegerField()

    # author=models.OneToOneField("Author",on_delete=models.CASCADE)
    def __str__(self):
        return self.addr


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
