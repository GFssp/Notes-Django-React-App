# Generated by Django 4.1.7 on 2023-03-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_created_notes_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]