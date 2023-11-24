from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from banks.models import *





# User 커스텀 모델
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True) # 계정 로그인 ID
    nickname = models.CharField(max_length=255, blank=True, null=True, unique=True) # 별명
    email = models.EmailField(max_length=254, blank=True, null=True, unique=True)   # 이메일
    age = models.IntegerField(null=True, blank=True) # 나이
    money = models.IntegerField(null=True, blank=True)   # 재산(잔고)
    salary = models.IntegerField(null=True, blank=True)  # 연봉
    kor_co_nm = models.CharField(max_length=99, blank=True, null=True)  # 선호하는주거래 은행
    join_way = models.CharField(max_length=99, blank=True, null=True)   # 선호하는 가입 방법
    intr_rate_type_nm = models.CharField(max_length=99, blank=True, null=True)  #선호하는 금리 유형
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
        kor_co_nm = data.get("kor_co_nm")
        join_way = data.get("join_way")
        intr_rate_type_nm = data.get("intr_rate_type_nm")
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
        if kor_co_nm:
            user.kor_co_nm = kor_co_nm
        if join_way:
            user.join_way = join_way
        if intr_rate_type_nm:
            user.intr_rate_type_nm = intr_rate_type_nm

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
    

# 가입한 상품 모델
class FinancialProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposits = models.ForeignKey(DepositOption, on_delete = models.CASCADE, null=True)  # 가입한 예금 상품
    savings = models.ForeignKey(SavingOption, on_delete = models.CASCADE, null=True)    # 가입한 적금 상품
