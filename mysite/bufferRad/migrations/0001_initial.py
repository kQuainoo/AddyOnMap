# Generated by Django 4.0.2 on 2022-05-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRadius',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uRadius_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='This is the date of request')),
            ],
        ),
    ]