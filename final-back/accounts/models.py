from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # age = models.IntegerField() # 나이
    # money = models.IntegerField()   # 재산(잔고)
    # salary = models.IntegerField()  # 연봉
    # financial_product = models.TextField(null=True)  # 가입 상품