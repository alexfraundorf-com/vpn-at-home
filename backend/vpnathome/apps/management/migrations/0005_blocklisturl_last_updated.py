# Generated by Django 2.1.2 on 2018-12-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_add_bad_domain_hosts_sources'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocklisturl',
            name='last_updated',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
