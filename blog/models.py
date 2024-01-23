from django.db import models, migrations
import django.db


class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author', blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author', blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=212)
    email = models.EmailField(null=True, blank=True)
    website = models.TextField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=212)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0008_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]
