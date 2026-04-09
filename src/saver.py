import os
import pandas as pd
from src.settings import OUTPUT_FILE

COLUMNS = ["name", "company", "url", "email", "phone", "score"]

def save(data):
    df = pd.DataFrame(data, columns=COLUMNS)
    if "email" in df.columns:
        df.drop_duplicates(subset=["email"], inplace=True)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
