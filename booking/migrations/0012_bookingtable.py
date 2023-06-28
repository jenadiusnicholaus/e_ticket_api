# Generated by Django 4.1 on 2023-06-23 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_seatstable_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_by', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('email_address', models.EmailField(max_length=20, null=True)),
                ('amount_paid', models.CharField(max_length=13, null=True)),
                ('pick_up', models.CharField(max_length=100, null=True)),
                ('drop_point', models.CharField(max_length=100, null=True)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.businfostable')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.seatstable')),
            ],
            options={
                'verbose_name': '4. Tickets',
                'verbose_name_plural': '4. Tickets',
            },
        ),
    ]