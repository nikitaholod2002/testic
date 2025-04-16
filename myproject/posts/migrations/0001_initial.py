# Generated by Django 5.2 on 2025-04-09 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authorization', '0002_remove_user_id_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('full_text', models.TextField()),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authorization.user')),
            ],
        ),
    ]
