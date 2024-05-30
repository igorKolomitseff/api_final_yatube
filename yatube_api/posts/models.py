from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

TEXT_LENGTH = 50


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.following}'


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Индификатор')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return (
            f'{self.title[:TEXT_LENGTH]}. | '
            f'{self.description[:TEXT_LENGTH]}.'
        )


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Картинка'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        ordering = ('pub_date',)
        default_related_name = 'posts'
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return (
            f'{self.text[:TEXT_LENGTH]} ... | '
            f'{self.pub_date.strftime("%d.%m.%Y %H:%M")} | '
            f'От автора {self.author} '
            f'в группе {self.group}'
        )


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Публикация'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий от {self.author}: {self.text[:TEXT_LENGTH]}...'
