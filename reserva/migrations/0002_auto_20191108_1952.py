# Generated by Django 2.1.4 on 2019-11-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realstate',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
