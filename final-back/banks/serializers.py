from rest_framework import serializers
from .models import *


class DepositBaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositBase
        fields = '__all__'


class DepositOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'



class SavingBaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavingBase
        fields = '__all__'

class SavingOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'



# 
class DepositListSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositBase
        fields = '__all__'

# 
class SavingListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavingBase
        fields = '__all__'
        



class ExchangeRateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'
        