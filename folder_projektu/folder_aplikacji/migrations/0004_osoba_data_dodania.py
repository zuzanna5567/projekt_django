# Generated by Django 5.1.4 on 2024-12-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0003_stanowisko_osoba'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True, default='2024-12-10'),
            preserve_default=False,
        ),
    ]
