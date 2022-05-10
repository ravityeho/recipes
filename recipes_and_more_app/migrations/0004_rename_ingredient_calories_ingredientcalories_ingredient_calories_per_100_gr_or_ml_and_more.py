# Generated by Django 4.0.3 on 2022-03-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_more_app', '0003_alter_ingredientcalories_alergens_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientcalories',
            old_name='ingredient_calories',
            new_name='ingredient_calories_per_100_gr_or_ml',
        ),
        migrations.RemoveField(
            model_name='ingredientcalories',
            name='alergens',
        ),
        migrations.AddField(
            model_name='ingredientcalories',
            name='optional_allergens',
            field=models.CharField(blank=True, choices=[('GLUTEN', 'Gluten'), ('EGGS', 'Eggs'), ('LACTOSE', 'lactose'), ('NUTS', 'Nuts'), ('PEANUTS', 'Peanuts'), ('SESAME SEEDS', 'Sesame Seeds'), ('SOY', 'Soy'), ('NON', 'Non')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='receiptingredient',
            name='amount_type',
            field=models.CharField(blank=True, choices=[('GRAM', 'Gram'), ('KG', 'Kg'), ('ML', 'Ml'), ('TEASPOON', 'Teaspoon'), ('TABLESPOON', 'Tablespoon'), ('CUP', 'Cup'), ('LEAF', 'Leaf'), ('SERVING PACKET', 'Serving Packet'), ('FLUID OUNCE (FL. OZ)', '(Fluid Ounce (fl. oz)'), ('QUART', 'Quart'), ('PINT', 'Pint')], max_length=128, null=True),
        ),
    ]