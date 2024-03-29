# Generated by Django 4.2.7 on 2023-11-19 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial_settings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tagcomment',
            name='comment',
            field=models.ManyToManyField(related_name='tagComment', related_query_name='tags', to='blog.comment'),
        ),
        migrations.AlterField(
            model_name='tagpost',
            name='post',
            field=models.ManyToManyField(related_name='tagPost', related_query_name='tags', to='blog.post'),
        ),
    ]
