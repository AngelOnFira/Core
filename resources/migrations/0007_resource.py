# Generated by Django 3.1.4 on 2021-02-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20210103_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=150)),
                ('resource_type', models.CharField(choices=[('study', 'study'), ('award', 'award'), ('event', 'event')], max_length=5)),
                ('url', models.CharField(max_length=300)),
                ('found_date', models.DateField()),
                ('status', models.CharField(choices=[('s', 'suggested'), ('p', 'public'), ('e', 'expired')], max_length=1)),
            ],
        ),
    ]
