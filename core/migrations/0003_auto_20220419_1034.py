# Generated by Django 3.2.3 on 2022-04-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220419_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=10),
        ),
    ]