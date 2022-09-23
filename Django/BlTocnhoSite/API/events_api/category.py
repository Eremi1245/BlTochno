
from rest_framework import serializers, viewsets
from events.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category=serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        read_only=True,
        lookup_field='category'
    )
    class Meta:
        model = Category
        fields = ['name','category']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer