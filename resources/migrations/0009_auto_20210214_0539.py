# Generated by Django 3.1.4 on 2021-02-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_auto_20210214_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='organization',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepagesection',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]