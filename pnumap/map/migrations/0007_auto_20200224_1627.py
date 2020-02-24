# Generated by Django 2.2.7 on 2020-02-24 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20200224_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='major',
            name='major',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='reviewdata',
            name='coursename',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.Course'),
        ),
        migrations.AlterField(
            model_name='reviewdata',
            name='star',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]