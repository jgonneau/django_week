# Generated by Django 2.2.5 on 2019-09-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={},
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]