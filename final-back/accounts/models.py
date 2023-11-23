from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from banks.models import *






class User(AbstractUser):
    # pass
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True) # 나이
    money = models.IntegerField(null=True, blank=True)   # 재산(잔고)
    salary = models.IntegerField(null=True, blank=True)  # 연봉
    deposit_options = models.ManyToManyField(DepositOption, through='FinancialProduct', related_name='users', blank=True)
    saving_options = models.ManyToManyField(SavingOption, through='FinancialProduct', related_name='users', blank=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

from allauth.account.adapter import DefaultAccountAdapter
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):

        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        deposit_options = data.get("deposit_options")
        saving_options = data.get("saving_options")


        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user,"first_name", first_name)
        if last_name:
            user_field(user,"last_name", last_name)
        if nickname:
            user_field(user,"nickname", nickname)
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        # if financial_product:
        #     financial_products = user.financial_products.split(',')
        #     financial_products.append(financial_product)
        #     if len(financial_products) > 1:
        #         financial_products = ','.join(financial_products)
        #     user_field(user,"financial_products", financial_products)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
    


class FinancialProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposits = models.ForeignKey(DepositOption, on_delete = models.CASCADE, null=True)
    savings = models.ForeignKey(SavingOption, on_delete = models.CASCADE, null=True)


class MyPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    kor_co_nm = models.TextField()
    join_way = models.TextField()
    intr_rate_type_nm = models.TextField()
