# Generated by Django 2.0.5 on 2018-05-08 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180507_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'managed': False,
            },
        ),
    ]