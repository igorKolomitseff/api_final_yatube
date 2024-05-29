import base64

from django.core.files.base import ContentFile
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, encoded = data.split(';base64,')
        return super().to_internal_value(
            ContentFile(
                base64.b64decode(encoded), name='temp.' + format.split('/')[-1]
            )
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Ошибка: Вы уже подписаны на этого пользователя.'
            )
        ]

    def validate_following(self, following):
        if self.context['request'].user == following:
            raise serializers.ValidationError(
                'Ошибка: нельзя подписаться на самого себя.'
            )
        return following
