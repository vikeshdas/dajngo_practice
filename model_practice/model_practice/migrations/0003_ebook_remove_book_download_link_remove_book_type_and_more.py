# Generated by Django 4.0.2 on 2024-03-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_practice', '0002_book_download_link_book_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(help_text='in cents')),
                ('download_link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='download_link',
        ),
        migrations.RemoveField(
            model_name='book',
            name='type',
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(help_text='in cents'),
        ),
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.PositiveIntegerField(help_text='in grams'),
        ),
    ]
