# Generated by Django 5.0.4 on 2024-04-30 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Foydalanuvchi', 'verbose_name_plural': 'Foydalanuvchilar'},
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category'),
        ),
    ]
