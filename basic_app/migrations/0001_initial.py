# Generated by Django 3.2 on 2021-04-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('desc', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Technology', 'Technology'), ('Enterpreneur', 'Enterpreneur'), ('Marketing', 'Marketing')], max_length=200)),
            ],
        ),
    ]