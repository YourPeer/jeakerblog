# Generated by Django 2.0.2 on 2018-02-24 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Say',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-post_date',),
            },
        ),
    ]
