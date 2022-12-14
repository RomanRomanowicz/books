# Generated by Django 4.1.1 on 2022-09-06 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sfelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('year', models.IntegerField()),
                ('pic', models.FileField(upload_to='book_pic')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelf.author')),
            ],
        ),
    ]
