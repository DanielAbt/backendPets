# Generated by Django 3.2.8 on 2021-10-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]