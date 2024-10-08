# Generated by Django 5.1.1 on 2024-10-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dateblog', models.DateField(blank=True, null=True)),
                ('source', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, upload_to='blog/images')),
                ('description', models.TextField()),
            ],
        ),
    ]
