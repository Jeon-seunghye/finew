from rest_framework import serializers
from .models import *




class DepositOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'

class DepositBaseSerializers(serializers.ModelSerializer):
    options = DepositOptionSerializers(many=True, read_only=True)

    class Meta:
        model = DepositBase
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
        