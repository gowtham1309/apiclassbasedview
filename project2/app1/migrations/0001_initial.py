# Generated by Django 4.1.7 on 2023-06-08 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('PCID', models.IntegerField()),
                ('PCNAME', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.IntegerField()),
                ('PNAME', models.CharField(max_length=30)),
                ('PPRICE', models.IntegerField()),
                ('PDATE', models.DateField()),
                ('PCNAME', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product_category')),
            ],
        ),
    ]