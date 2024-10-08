# Generated by Django 5.0.7 on 2024-09-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2000, verbose_name='コメント')),
            ],
            options={
                'db_table': 'topic',
            },
        ),
    ]
