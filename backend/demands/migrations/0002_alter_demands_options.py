# Generated by Django 4.0.1 on 2022-01-29 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demands', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demands',
            options={'ordering': ['-date'], 'verbose_name': 'demand'},
        ),
    ]