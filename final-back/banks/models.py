from django.db import models

# Create your models here.
class Deposit(models.Model):
    dcls_month = models.TextField(null=True) # 공시제출월
    kor_co_nm = models.TextField(null=True)  # 금융회사명
    fin_co_no = models.TextField(null=True)  # 금융회사코드
    fin_prdt_nm = models.TextField(null=True)    # 금융상품명
    fin_prdt_cd = models.TextField(null=True)    # 금융상품코드
    save_trm = models.IntegerField(null=True)    # 저축기간(month)
    intr_rate = models.FloatField(null=True) # 금리
    intr_rate2 = models.FloatField(null=True) # 우대금리


class Saving(models.Model):
    dcls_month = models.TextField(null=True) # 공시제출월
    kor_co_nm = models.TextField(null=True)  # 금융회사명
    fin_co_no = models.TextField(null=True)  # 금융회사코드
    fin_prdt_nm = models.TextField(null=True)    # 금융상품명
    fin_prdt_cd = models.TextField(null=True)    # 금융상품코드
    save_trm = models.IntegerField(null=True)    # 저축기간(month)
    intr_rate = models.FloatField(null=True) # 금리
    intr_rate2 = models.FloatField(null=True) # 우대금리


class Exchange_rate(models.Model):
    cur_unit = models.TextField()   # 통화 코드
    cur_nm = models.TextField() # 국가/통화명
    ttb = models.FloatField()   # buying rate
    tts = models.FloatField()   # selling rate