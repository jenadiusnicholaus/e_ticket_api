# Generated by Django 4.1 on 2023-06-24 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_dropstable_pickupstable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dropstable',
            options={'verbose_name': '6. Drop points ', 'verbose_name_plural': '6. Drop points '},
        ),
        migrations.AlterModelOptions(
            name='pickupstable',
            options={'verbose_name': '5. Pick Up points', 'verbose_name_plural': '5. Pick Up points'},
        ),
    ]
