# Generated by Django 4.2.7 on 2023-11-18 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0006_review_alter_title_max_lenth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant_name',
            field=models.CharField(max_length=35),
        ),
    ]
