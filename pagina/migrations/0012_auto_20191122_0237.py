# Generated by Django 2.2.7 on 2019-11-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0011_auto_20190305_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroes',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
