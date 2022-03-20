# Generated by Django 4.0.3 on 2022-03-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_more_app', '0002_recipe_total_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientcalories',
            name='alergens',
            field=models.CharField(blank=True, choices=[('GLUTEN', 'Gluten'), ('EGGS', 'Eggs'), ('LACTOSE', 'lactose'), ('NUTS', 'Nuts'), ('PEANUTS', 'Peanuts'), ('SESAME SEEDS', 'Sesame Seeds'), ('SOY', 'Soy'), ('ELSE', 'Else')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='receiptingredient',
            name='amount_type',
            field=models.CharField(blank=True, choices=[('GRAM', 'Gram'), ('KG', 'Kg'), ('ML', 'Ml'), ('TEASPOON', 'Teaspoon'), ('TABLESPOON', 'Tablespoon'), ('CUP', 'Cup'), ('LEAF', 'Leaf'), ('BAG', 'Bag'), ('FLUID OUNCE (FL. OZ)', '(Fluid Ounce (fl. oz)'), ('QUART', 'Quart'), ('PINT', 'Pint')], max_length=128, null=True),
        ),
    ]
