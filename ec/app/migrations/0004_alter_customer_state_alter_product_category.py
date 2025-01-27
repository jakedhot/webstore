# Generated by Django 4.1.4 on 2023-01-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customer_state_alter_product_category_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Visayas', 'Visayas'), ('Mindanao', 'Mindanao'), ('Luzon', 'Luzon')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CV', 'Civet'), ('RO', 'Robusta'), ('BA', 'Barako'), ('AR', 'Arabica'), ('MO', 'Mocha')], max_length=2),
        ),
    ]
