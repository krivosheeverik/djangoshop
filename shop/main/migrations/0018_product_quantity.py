# Generated by Django 2.1 on 2019-08-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20190815_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
