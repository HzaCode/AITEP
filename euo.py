import pandas as pd

def parse_strength(strength):
    parts = strength.lower().split('|')
    if len(parts) == 2:
        drug, amount_unit = parts
        try:
            amount, unit = amount_unit.split(' per ')
            amount_value = float(amount.replace('mg', '').strip())
            if 'ml' in unit:
                amount_value *= 5
                unit = '5ml'
            if amount_value.is_integer():
                amount = str(int(amount_value)) + 'mg'
            else:
                amount = str(amount_value).rstrip('0').rstrip('.') + 'mg'
            return f"{drug}|{amount}", f"per {unit}"
        except ValueError:
            return "not in the specified format", None
    else:
        return "not in the specified format", None

def read_excel_process_format(filename):
    df = pd.read_excel(filename)
    print("| reg_no | Standardized Strength | Unit |")
    for index, row in df.iterrows():
        reg_no = row['reg_no']
        strengths = eval(row['Strength of each API'])
        
        standardized_strengths = []
        units = set()
        for strength in strengths:
            standardized_strength, unit = parse_strength(strength)
            standardized_strengths.append(standardized_strength)
            if unit:
                units.add(unit)
        
        unit = units.pop() if len(units) == 1 else "N/A"
        
        standardized_strength_str = ', '.join([f'"{item}"' for item in standardized_strengths])
        print(f"| {reg_no} | [{standardized_strength_str}] | {unit} |")

filename = 'path/to/your/excel/file.xlsx'
read_excel_process_format(filename)
