# Generated by Django 2.2.1 on 2019-11-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0011_auto_20191115_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentdate',
            name='date',
            field=models.DateField(),
        ),
    ]
