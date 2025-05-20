from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='%Y-%m-%d/')),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
