# Generated by Django 3.2.3 on 2021-06-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0010_acer_alllaptops_apple_asus_dell_hp_msi_razerblade'),
    ]

    operations = [
        migrations.CreateModel(
            name='lenovo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forwardlink', models.URLField(default='')),
                ('photolink', models.URLField(default='')),
                ('laptopname', models.TextField(default='', max_length=150)),
                ('price', models.IntegerField(blank=True, default=None, null=True)),
                ('site', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
