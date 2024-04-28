from main import models
from . import serializers
# from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.authtoken.models import Token


@api_view(['GET'])
def category_list(request):
    """Kategoriyalarning yani bo'limlarning ro'yxati"""
    context = serializers.CategoryListSerializer(models.Category.objects.all(), many=True)
    return Response(context.data)

@api_view(['GET'])
def category_detail(request, id):
    """Kategoriya yani bo'lim haqidagi batafsil ma'lumot"""
    context = serializers.CategoryDetailSerializer(models.Category.objects.get(id=id))
    return Response(context.data)

@api_view(['GET'])
def region_list(request):
    """Regionlarning yani hududlarning ro'yxati"""
    context = serializers.RegionListSerializer(models.Region.objects.all(), many=True)
    return Response(context.data)

@api_view(['GET'])
def region_detail(request, id):
    """Region yani hudud haqidagi batafsil ma'lumot"""
    context = serializers.RegionDetailSerializer(models.Region.objects.get(id=id))
    return Response(context.data)

@api_view(['GET'])
def post_list(request):
    """Postlarning yani yangiliklarning ro'yxati"""
    context = serializers.PostListSerializer(models.Post.objects.all(), many=True)
    return Response(context.data)

@api_view(['GET'])
def post_detail(request, id):
    """Post yani yangilik haqidagi batafsil ma'lumot"""
    context = serializers.PostDetailSerializer(models.Post.objects.get(id=id))
    return Response(context.data)


@api_view(['POST'])
def comment_create(request, id):
    """Kommentariya yaratish"""
    if request.method == 'POST':
        text = request.POST.get('text')
        post = models.Post.objects.get(id=id)
        comment = models.Comment.objects.create(
            post=post, 
            text=text
        )
        return Response(serializers.CommentSerializer(comment).data, status=201)


@api_view(['GET'])
def post_comment(request, id):
    """Post yani yangilikka tegishli kommentariyalarni filterlash"""
    comment_post = models.Comment.objects.filter(post__id=id)
    context = serializers.CommentSerializer(comment_post, many=True)
    return Response(context.data)


@api_view(['GET'])
def comment_detail(request, id):
    """Kommentariya yani fikr-mulohazani batafsil ko'rish"""
    comment = models.Comment.objects.get(id=id)
    context = serializers.CommentSerializer(comment)
    return Response(context.data)


@api_view(['GET'])
def category_post(request, id):
    """Postlarni yani yangiliklarni kategoriyaga ko'ra filterlash"""
    category = models.Category.objects.get(id=id)
    posts = models.Post.objects.filter(category=category)
    regions = models.Region.objects.all()
    categories = models. Category.objects.all()
    posts_serializer = serializers.PostListSerializer(posts, many=True)
    categories_serializer = serializers.CategoryListSerializer (categories, many=True)
    regions_serializer = serializers.RegionListSerializer(regions, many=True)
    return Response (
        {
        'posts':posts_serializer.data,
        'categorys':categories_serializer.data,
        'regions':regions_serializer.data,
        }
    )


# @api_view(["POST"])
# def log_in(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
#     if user:
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'token':token.key})
#     return Response


# @api_view(["POST"])
# def log_out(request):
#     token = Token.objects.get(user=request.user).delete()
#     return Response