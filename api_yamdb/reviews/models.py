from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

from .validators import validate_year


class Category(models.Model):
    """Модель категории."""
    name = models.CharField(max_length=256, verbose_name='Название категории')
    slug = models.SlugField(
        max_length=50,
        verbose_name='Слаг',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Genre(models.Model):
    """Модель жанра."""
    name = models.CharField(max_length=256, verbose_name='Название жанра')
    slug = models.SlugField(max_length=50, verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)


class Title(models.Model):
    """Модель тайтла."""
    name = models.CharField(
        max_length=256,
        verbose_name='Название произведения',
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=[validate_year]
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='categories',
        verbose_name='Категория',
        help_text='Категория произведения',
    )
    genre = models.ManyToManyField(
        Genre, through='GenreTitle'
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        default=None
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)


class GenreTitle(models.Model):
    """Связь жанра и тайтла."""
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.genre}'


class Review(models.Model):
    """Модель для отзыва+рейтинг."""

    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    score = models.PositiveIntegerField(
        verbose_name='Оценка',
        validators=(
            MinValueValidator(
                1,
                message='Оценка не может быть ниже',
            ),
            MaxValueValidator(
                10,
                message='Оценка не может быть выше',
            ),
        ),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Название произведения',
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_review',
            ),
        )

    def __str__(self):
        """Возвращает текст отзыва."""
        return self.text[:30]


class Comment(models.Model):
    """Модель добавления комментария."""

    text = models.TextField(verbose_name='текст комментария')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Aвтор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        """Возвращает текст комментария."""
        return self.text[:30]
