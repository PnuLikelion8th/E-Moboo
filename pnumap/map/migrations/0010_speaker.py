# Generated by Django 2.2.7 on 2020-03-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_tempcrawldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_content', models.CharField(max_length=50)),
            ],
        ),
    ]
