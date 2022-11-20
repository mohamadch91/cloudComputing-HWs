# Generated by Django 4.0.6 on 2022-11-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]