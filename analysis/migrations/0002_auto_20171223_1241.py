# Generated by Django 2.1.dev20171206142534 on 2017-12-23 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=200)),
                ('datafile', models.FileField(upload_to='')),
                ('upload_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='data',
        ),
        migrations.AddField(
            model_name='data',
            name='basket_value',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='items',
            field=models.CharField(default=None, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='recency_days',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='sr',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='upload',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='analysis.Upload'),
            preserve_default=False,
        ),
    ]
