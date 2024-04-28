from rest_framework.serializers import ModelSerializer
from main import models


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ['id']


class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Category


class RegionListSerializer(ModelSerializer):
    class Meta:
        model = models.Region
        exclude = ['id']


class RegionDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Region


class PostListSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        exclude = ['id', 'banner_img', 'date', 'author']
        depth=2


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields='__all__'
        depth=2
        

class CommentSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
        # depth=2
        