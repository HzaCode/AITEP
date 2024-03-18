import pandas as pd
import re

def parse_strength(strength):
    match = re.match(r"(.+?)\|(\d+\.?\d*)\s*(mg|g|ml|l|µg|µl)\s*per\s*(\d+\.?\d*)\s*(ml|g|l|µg|µl)", strength.lower())
    if match:
        ingredient = match.group(1)
        amount = match.group(2)
        amount_unit = match.group(3)
        per_amount = match.group(4)
        per_unit = match.group(5)
        
        if per_unit == "ml" and per_amount == "1":
            amount = str(float(amount) * 5)
            per_unit = "5ml"

        new_quantity = f"{amount}{amount_unit} per {per_unit}"
    else:
        ingredient = strength
        new_quantity = "not in the specified format"
        per_unit = "N/A"

    return ingredient, new_quantity, per_unit

def process_data(filepath):
    df = pd.read_excel(filepath)
    ingredients, quantities, units = [], [], []

    for index, row in df.iterrows():
        strength = row['strength']
        for s in eval(strength):
            ingredient, quantity, unit = parse_strength(s)
            ingredients.append(ingredient)
            quantities.append(quantity)
            units.append(unit)
        
    df['Ingredient'] = ingredients
    df['Quantity'] = quantities
    df['Unit'] = units
    
    return df

filepath = 'path.xlsx'

df_processed = process_data(filepath)

output_path = 'path.xlsx'
df_processed.to_excel(output_path, index=False)

print(df_processed.head())
