from django.db import models
import uuid

#カテゴリ
class Category(models.Model):

    class Meta:
        db_table    = "category"

    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name    = models.CharField(verbose_name="カテゴリ名",max_length=15)

    def __str__(self):
        return self.name

#商品
class Product(models.Model):
    class Meta:
        db_table    = "product"

    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category    = models.ForeignKey(Category,verbose_name="カテゴリ名",on_delete=models.PROTECT)
    name        = models.CharField(verbose_name="商品名",max_length=20)
    price       = models.IntegerField(verbose_name="価格")

    def __str__(self):
        return self.name

