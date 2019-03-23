from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    # 필드명 설정
    class Meta:
        verbose_name_plural = "도서명"

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    introduction = models.TextField()

    # 필드명 설정
    class Meta:
        verbose_name_plural = "저자"

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    # 필드명 설정
    class Meta:
        verbose_name_plural = "출판사"

    def __str__(self):
        return self.name
