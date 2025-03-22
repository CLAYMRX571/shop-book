# Generated by Django 5.1.7 on 2025-03-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
            ],
        ),
    ]
