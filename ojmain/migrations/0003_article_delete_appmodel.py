# Generated by Django 4.0.5 on 2022-07-07 10:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojmain', '0002_appmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AppModel',
        ),
    ]
