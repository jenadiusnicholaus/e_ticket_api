# Generated by Django 4.1 on 2023-06-23 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_businfostable_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businfostable',
            old_name='root_origin',
            new_name='route_origin',
        ),
        migrations.AddField(
            model_name='businfostable',
            name='route_destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.routedestinationtable'),
        ),
    ]
