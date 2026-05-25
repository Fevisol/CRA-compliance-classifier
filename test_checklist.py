import pandas as pd
from pathlib import Path

# Test reading the Excel file
checklist_path = Path(__file__).parent.parent / 'References' / 'Book1.xlsx'

print(f"Testing checklist file: {checklist_path}")
print(f"File exists: {checklist_path.exists()}")

if checklist_path.exists():
    try:
        df = pd.read_excel(checklist_path)
        print(f"\nExcel columns: {list(df.columns)}")
        print(f"Shape: {df.shape}")
        print(f"\nFirst 10 rows:")
        print(df.head(10).to_string())
        
        # Check for specific columns
        required_cols = ['ID', 'Question', 'Requirment', 'Legal Reference', 'Other Reference', 'Note', 'Check']
        print(f"\nColumn check:")
        for col in required_cols:
            has_col = col in df.columns
            print(f"  {col}: {'✓' if has_col else '✗'}")
            
    except Exception as e:
        print(f"Error reading Excel: {e}")
else:
    print("File not found!")
