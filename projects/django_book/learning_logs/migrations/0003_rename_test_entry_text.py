# Generated by Django 5.1.3 on 2024-11-07 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='test',
            new_name='text',
        ),
    ]