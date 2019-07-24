from rest_framework import serializers

from .models import *

class EquipmentInfoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentInfoItems
        fields = '__all__'


class EquipmentInfoSerializer(serializers.ModelSerializer):
    Equipments_items = EquipmentInfoItemSerializer(many=True,read_only=True)
    class Meta:
        model = EquipmentInfo
        fields = '__all__'


class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentCategory
        fields = '__all__'


class FavoriteEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteEquipment
        fields = '__all__'


class MagazineInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineInfo
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    equipments_info = EquipmentInfoSerializer(many=True,read_only=True)
    category = EquipmentCategorySerializer(many=False, read_only=True)
    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentUsefulSerializer(serializers.ModelSerializer):
    equipments_info = EquipmentInfoSerializer(many=True,read_only=True)
    class Meta:
        model = EquipmentUseful
        fields = '__all__'


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

