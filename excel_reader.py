import pandas as pd

def read_excel(file):
    df = pd.read_excel(file)
    return df.to_string() 
