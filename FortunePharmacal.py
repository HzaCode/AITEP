import pandas as pd
import ast

def preprocess_and_format_ingredients(ingredients_str):
    formatted_ingredients = []
    try:
        ingredients = ast.literal_eval(ingredients_str)
        if not isinstance(ingredients, list):
            raise ValueError
    except (ValueError, SyntaxError):
        day_night_label = ""
        for part in ingredients_str.split('\n'):
            part = part.strip()
            if part:
                if 'Day Tablet:' in part:
                    day_night_label = "（Day Tablet）"
                elif 'Night Tablet:' in part:
                    day_night_label = "（Night Tablet）"
                else:
                    if day_night_label:
                        if ' ' in part:
                            name, dose = part.rsplit(' ', 1)
                            formatted_ingredients.append(f"{name}{day_night_label}|{dose}")
                        else:
                            formatted_ingredients.append(f"{part}{day_night_label}")
                    else:
                        if ' ' in part:
                            name, dose = part.rsplit(' ', 1)
                            formatted_ingredients.append(f"{name}|{dose}")
                        else:
                            formatted_ingredients.append(part)
    return formatted_ingredients

def format_drug_info(row):
    reg_number = row['reg_no']
    ingredients_str = row['strength of each ingredients']
    formatted_ingredients = preprocess_and_format_ingredients(ingredients_str)
    unit = "per tablet"
    return reg_number, formatted_ingredients, unit

def read_excel_process_format(filename):
    df = pd.read_excel(filename, engine='openpyxl')
    print("| Reg_number | Standardized Strength | Unit |")
    for index, row in df.iterrows():
        try:
            reg_number, standardized_strength, unit = format_drug_info(row)
            standardized_strength_str = ', '.join([f'"{item}"' for item in standardized_strength])
            print(f"| {reg_number} | [{standardized_strength_str}] | {unit} |")
        except Exception as e:
            print(f"Error processing row {index}: {e}")

excel_file = 'path_to_your_excel_file.xlsx'
read_excel_process_format(excel_file)
