# Generated by Django 4.1 on 2022-09-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='30 caracteres max.', max_length=30)),
                ('lastname', models.CharField(help_text='30 caracteres max.', max_length=30)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('heartRate', models.IntegerField(help_text='Heart rate measured in Beats per minute/Pulses per minute')),
                ('bloodOxygenSaturation', models.IntegerField(help_text='Blood Oxygen Saturation')),
                ('stresslevel', models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High'), ('extreme', 'Extreme')], default='low', help_text='Stress level', max_length=20)),
            ],
        ),
    ]
