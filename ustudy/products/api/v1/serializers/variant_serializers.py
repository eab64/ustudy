from rest_framework import serializers

from products.models.variant import Variant



class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'