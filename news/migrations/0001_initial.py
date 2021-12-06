# Generated by Django 3.2.9 on 2021-11-15 09:35
# это файл миграции он описывает какую либо таблицу в базе данных

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('data', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
#тут говориться что будет создано таблица Articles и тут будет создано не 4 полей а 5
# мы тут создали файл миграции теперь можно провести миграцию python manage.py migrate