# Generated by Django 4.2.2 on 2023-07-02 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_bookingtable_safari_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[(0, 'BOOKED'), (1, 'CONFORMED'), (2, 'CANCELLED')], default=1)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_state', to='booking.bookingtable')),
            ],
            options={
                'verbose_name': '1. Booking state',
                'verbose_name_plural': '1. Booking state',
            },
        ),
    ]