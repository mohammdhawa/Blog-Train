# Generated by Django 4.2 on 2024-10-10 21:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_author_category_alter_post_publish_date_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 10, 21, 35, 37, 936897, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
