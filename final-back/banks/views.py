from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.authentication import TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from .models import *
import requests


# 인증이 필요한 요소들에게 데코레이터 등록 (401)
## @authentication_classes([TokenAuthentication, BasicAuthentication])

# 권한 정책 설정 (403)
## @permission_classes([IsAuthenticated])


# open API 받아와서 저장
## 예금
@api_view(['GET'])
def deposit_save_data(request):
    DEPOSIT_API_KEY = '851fa6d368036fbfd4e57a633cccffd5'
    DEPOSIT_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={DEPOSIT_API_KEY}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(DEPOSIT_URL).json()   
    for i in response.get('result').get('baseList'):
        save_data = {
            'dcls_month': i.get('dcls_month'), # 공시제출월
            'kor_co_nm': i.get('kor_co_nm'),  # 금융회사명
            'fin_co_no': i.get('fin_co_no'),  # 금융회사코드
            'fin_prdt_nm': i.get('fin_prdt_nm'),    # 금융상품명
            'fin_prdt_cd': i.get('fin_prdt_cd'),    # 금융상품코드
            }
        if DepositBase.objects.filter(fin_prdt_cd = i.get('fin_prdt_cd')).exists():
            continue

        serializer = DepositBaseSerializers(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for j in response.get('result').get('optionList'):
        save_data = {
                'depositbase': DepositBase.objects.get(fin_prdt_cd = j.get('fin_prdt_cd')).id,
                'save_trm': j.get('save_trm'),   # 저축기간(month)
                'intr_rate': j.get('intr_rate'), # 금리
                'intr_rate2': j.get('intr_rate2') # 우대금리
        }
        if DepositOption.objects.filter(
                                        depositbase = DepositBase.objects.get(fin_prdt_cd = j.get('fin_prdt_cd')).id,
                                        save_trm = j.get('save_trm'),
                                        intr_rate = j.get('intr_rate'),
                                        intr_rate2 = j.get('intr_rate2')
                                        ).exists():
            continue
        serializer = DepositOptionSerializers(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({'message': 'okay'})



## 적금
@api_view(['GET'])
def saving_save_data(request):
    SAVING_API_KEY = '851fa6d368036fbfd4e57a633cccffd5'
    SAVING_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={SAVING_API_KEY}&topFinGrpNo=020000&pageNo=1'
    
    response = requests.get(SAVING_URL).json()   
    for i in response.get('result').get('baseList'):
        save_data = {
            'dcls_month': i.get('dcls_month'), # 공시제출월
            'kor_co_nm': i.get('kor_co_nm'),  # 금융회사명
            'fin_co_no': i.get('fin_co_no'),  # 금융회사코드
            'fin_prdt_nm': i.get('fin_prdt_nm'),    # 금융상품명
            'fin_prdt_cd': i.get('fin_prdt_cd'),    # 금융상품코드
        }
        if SavingBase.objects.filter(fin_prdt_cd = i.get('fin_prdt_cd')).exists():
            continue
        serializer = SavingBaseSerializers(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for j in response.get('result').get('optionList'):
        save_data = {
            'savingbase': SavingBase.objects.get(fin_prdt_cd = j.get('fin_prdt_cd')).id,
            'save_trm': j.get('save_trm'),   # 저축기간(month)
            'intr_rate': j.get('intr_rate'), # 금리
            'intr_rate2': j.get('intr_rate2') # 우대금리
        }
        if SavingOption.objects.filter(
                                    savingbase = SavingBase.objects.get(fin_prdt_cd = j.get('fin_prdt_cd')).id,
                                    save_trm = j.get('save_trm'),
                                    intr_rate = j.get('intr_rate'),
                                    intr_rate2 = j.get('intr_rate2')
                                    ).exists():
            continue
        serializer = SavingOptionSerializers(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message': 'okay'})

## 환율
@api_view(['GET'])
def exchange_rate_save_data(request):
    EXCHANGE_RATE_API_KEY = 'iwvzKxQP0RSUzyPFzjkrmTJ3WXFJZr3P'
    EXCHANGE_RATE_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={EXCHANGE_RATE_API_KEY}&searchdate=20180102&data=AP01'

    response = requests.get(EXCHANGE_RATE_URL).json()
    for i in response:
        save_data = {
            'cur_unit' : i.get('cur_unit'),   # 통화 코드
            'cur_nm' :  i.get('cur_nm'), # 국가/통화명
            'ttb' : i.get('ttb'),   # buying rate
            'tts' : i.get('tts'),   # selling rate
        }
        if ExchangeRate.objects.filter(
                                    cur_unit = i.get('cur_unit'),
                                    cur_nm =  i.get('cur_nm'),
                                    ).exists():
            continue
        serializer = ExchangeRateSerializers(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message': 'okay'})


# 예금 전체 조회
@api_view(['GET'])
def deposit_list(request):
    if request.method == 'GET':
        deposit = DepositListSerializers.objects.all()
        serializers = DepositListSerializers(deposit, many=True)
        return Response(serializers.data)

# 예금 상세 조회
@api_view(['GET'])
def deposit_detail(request, deposit_pk):
    if request.method == 'GET':
        deposit = DepositBase.objects.get(pk=deposit_pk)
        serializers = DepositBaseSerializers(deposit)
        return Response(serializers.data)

# 적금 전체 조회
def saving_list(request):
    if request.method == 'GET':
        saving = SavingBase.objects.all()
        serializers = SavingListSerializers(saving, many=True)
        return Response(serializers.data)
    
# 적금 상세 조회
@api_view(['GET'])
def saving_detail(request, saving_pk):
    if request.method == 'GET':
        saving = SavingBase.objects.get(pk=saving_pk)
        serializers = SavingBaseSerializers(saving)
        return Response(serializers.data)
    
# 환율 계산기 (환율 전체 json으로 받아오기)
@api_view(['GET'])
def exchange_rate(request):
    if request.method == 'GET':
        exchange_rate = ExchangeRate.objects.all()
        serializers = ExchangeRateSerializers(exchange_rate, many=True)
        return Response(serializers.data)