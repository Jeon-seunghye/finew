from rest_framework import serializers
from .models import *




class DepositOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'

class DepositBaseSerializers(serializers.ModelSerializer):
    depositoption_set = DepositOptionSerializers(many=True, read_only=True)
    class Meta:
        model = DepositBase
        fields = '__all__'


class SavingOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'

class SavingBaseSerializers(serializers.ModelSerializer):
    savingoption_set = SavingOptionSerializers(many=True, read_only=True)
    class Meta:
        model = SavingBase
        fields = '__all__'



class ExchangeRateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'
        