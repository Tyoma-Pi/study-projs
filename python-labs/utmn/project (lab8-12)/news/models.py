from django.db import models

# Create your models here.
class Rubric(models.Model):  # Рубрика
    name = models.TextField('Рубрика', blank=True, null=False)
    published = models.DateTimeField('Опубиковано', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['-published']


class Article(models.Model):  # Статья
    title = models.TextField('Название', blank=True, null=False)
    keywords = models.TextField('Ключевые слова', blank=True, null=False)
    annotation = models.TextField('Аннотация', blank=True, null=False)
    image = models.TextField('Изображение', blank=True, null=False)
    rubnum = models.ForeignKey(Rubric, on_delete=models.DO_NOTHING, verbose_name='Рубрика')
    published = models.DateTimeField('Опубиковано', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published']


class Hashtag(models.Model):  # Хештег
    name = models.TextField('Хештег', blank=True, null=False)
    published = models.DateTimeField('Опубиковано', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Хештег'
        verbose_name_plural = 'Хештеги'
        ordering = ['-published']


class ArticleHashtag(models.Model):
    fk_id_art = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    fk_id_ht = models.ForeignKey(Hashtag, on_delete=models.CASCADE, verbose_name='Хештег')
    published = models.DateTimeField('Опубиковано', auto_now_add=True, db_index=True)

    def __str__(self):
        return 'Article - Hashtag'

    class Meta:
        verbose_name = 'НовостьХештег'
        verbose_name_plural = 'НовостиХештеги'
        ordering = ['-published']


class MyUsers(models.Model):
    username = models.TextField('Имя пользователя', blank=True, null=False)
    email = models.TextField('Электронная почта', blank=True, null=False)
    password = models.TextField('Пароль', blank=True, null=False)
    role = models.TextField('Права доступа', blank=True, null=False)
    published = models.DateTimeField('Опубиковано', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-published']
