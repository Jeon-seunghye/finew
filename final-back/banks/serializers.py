from rest_framework import serializers
from .models import *

def process_data(deposit_base_data, deposit_option_data):
    combined_data = []

    for base_item in deposit_base_data:
        for option_item in deposit_option_data:
            if base_item.id == option_item.depositbase_id:
                combined_data.append({
                    'base_id': base_item.id,
                    'base_field': base_item.some_field,
                    'option_id': option_item.id,
                    'option_field': option_item.some_field,
                    # 필요한 필드 추가 가능
                })

    return combined_data


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
    combined_data = serializers.SerializerMethodField()

    def get_combined_data(self, obj):
        deposit_base_data = DepositBase.objects.all()
        deposit_option_data = DepositOption.objects.all()
        combined_data = process_data(deposit_base_data, deposit_option_data)

        return combined_data


# 
class SavingListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavingBase
        fields = '__all__'
        



class ExchangeRateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'
        