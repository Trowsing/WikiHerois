# Generated by Django 2.1.7 on 2019-03-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pagina", "0009_auto_20190303_0358"),
    ]

    operations = [
        migrations.AlterField(
            model_name="heroes",
            name="image",
            field=models.ImageField(default="", upload_to=""),
        ),
    ]