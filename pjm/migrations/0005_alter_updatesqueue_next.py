# Generated by Django 3.2.3 on 2022-02-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pjm', '0004_auto_20220216_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatesqueue',
            name='next',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
    ]