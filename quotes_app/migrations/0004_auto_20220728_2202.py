# Generated by Django 3.2.4 on 2022-07-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0003_auto_20220728_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
