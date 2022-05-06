from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # 模型模块会自动创建id字段
    name = models.CharField(max_length=12)

    # 重写方法，显示内容
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

