# Generated by Django 2.2.8 on 2019-12-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0011_auto_20191208_0755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='avatar1',
            new_name='avatar3',
        ),
        migrations.AlterField(
            model_name='post',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]
