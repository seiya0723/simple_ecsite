# Generated by Django 3.1.2 on 2020-11-12 04:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, verbose_name='カテゴリ名')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='商品名')),
                ('price', models.IntegerField(verbose_name='価格')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shopping.category', verbose_name='カテゴリ名')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
