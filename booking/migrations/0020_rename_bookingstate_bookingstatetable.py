# Generated by Django 4.2.2 on 2023-07-02 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_alter_routeorigintable_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookingState',
            new_name='BookingStateTable',
        ),
    ]