from django.db import models

# 예금 베이스
class DepositBase(models.Model):
    dcls_month = models.TextField() # 공시제출월
    kor_co_nm = models.TextField()  # 금융회사명
    fin_co_no = models.TextField()  # 금융회사코드
    fin_prdt_nm = models.TextField()    # 금융상품명
    fin_prdt_cd = models.TextField()    # 금융상품코드
    
    join_member = models.TextField()    # 가입 대상
    join_way = models.TextField()   # 가입 방법
    spcl_cnd = models.TextField()   # 우대 조건
    etc_note = models.TextField()   # 기타 유의사항

# 예금 옵션
class DepositOption(models.Model):
    depositbase = models.ForeignKey(DepositBase, on_delete=models.CASCADE)
    save_trm = models.IntegerField()    # 저축기간(month)
    intr_rate_type_nm = models.TextField()  # 금리 유형 (단리 / 복리)
    intr_rate = models.FloatField() # 금리
    intr_rate2 = models.FloatField() # 우대금리

# 적금 베이스
class SavingBase(models.Model):
    dcls_month = models.TextField() # 공시제출월
    kor_co_nm = models.TextField()  # 금융회사명
    fin_co_no = models.TextField()  # 금융회사코드
    fin_prdt_nm = models.TextField()    # 금융상품명
    fin_prdt_cd = models.TextField()    # 금융상품코드
    join_member = models.TextField()    # 가입 대상
    join_way = models.TextField()   # 가입 방법
    spcl_cnd = models.TextField()   # 우대 조건
    etc_note = models.TextField()   # 기타 유의사항

# 적금 옵션
class SavingOption(models.Model):
    savingbase = models.ForeignKey(SavingBase, on_delete=models.CASCADE)
    save_trm = models.IntegerField()    # 저축기간(month)
    intr_rate_type_nm = models.TextField()  # 금리 유형 (단리 / 복리)
    intr_rate = models.FloatField() # 금리
    intr_rate2 = models.FloatField() # 우대금리

# 환율 정보
class ExchangeRate(models.Model):
    cur_unit = models.TextField()   # 통화 코드
    cur_nm = models.TextField() # 국가/통화명
    deal_bas_r = models.TextField() # 매매기준율