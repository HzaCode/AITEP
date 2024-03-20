import pandas as pd
import re 

def extract_concentration(strength):
   
    match = re.search(r"(\d+\.?\d*)", strength)
    if match:
        return float(match.group(1))
    else:
        raise ValueError(f"Cannot extract numeric value from: {strength}")

def convert_ingredient_strength(ingredient, form):
    name, strength = ingredient.split('|')
    if 'w/w' in strength:
        concentration = extract_concentration(strength) * 10  
    elif 'w/v' in strength:
        concentration = extract_concentration(strength) * 50  
    else:
     
        concentration = extract_concentration(strength)
    return f"{name}|{concentration}mg"

def format_drug_info(row):
    reg_number = row['reg_no']
    dosage_form = row['dosage form']
    ingredients = eval(row['strength of each ingredients'])
    
    standardized_strength = [convert_ingredient_strength(ingredient, dosage_form) for ingredient in ingredients]
    
    if dosage_form in ['TABLET', 'CAPSULE']:
        unit = "per tablet" if dosage_form == 'TABLET' else "per capsule"
    elif dosage_form in ['SYRUP', 'SOLUTION', 'SUSPENSION']:
        unit = "per 5ml"
    elif dosage_form in ['SEMI-SOLID (CREAM / GEL / OINTMENT / LOTION / PASTE)', 'POWDER/ GRANULE']:
        unit = "per gram"
    else:
        unit = "N/A"
    
    return reg_number, standardized_strength, unit

def read_excel_process_format(filename):
    df = pd.read_excel(filename, engine='openpyxl')
    print("| Reg_number | Standardized Strength                                                                                              | Unit      |")
    print("|------------|--------------------------------------------------------------------------------------------------------------------|-----------|")
    for index, row in df.iterrows():
        try:
            reg_number, standardized_strength, unit = format_drug_info(row)
          
            standardized_strength_str = str(standardized_strength).replace("'", '"')  
            print(f"| {reg_number} | {standardized_strength_str} | {unit} |")
        except ValueError as e:
            print(f"Error processing row {index}: {e}")


excel_file = r'path.xlsx'
read_excel_process_format(excel_file)
