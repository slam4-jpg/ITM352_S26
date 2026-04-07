import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

url = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

try:
    df = pd.read_csv(url, engine='pyarrow', on_bad_lines='skip')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['sales'] = df['quantity'] * df['unit_price']
    
    
    pivot_table_avg = df.pivot_table(df,
                                    values="sales",
                                    index="region",
                                    columns="order_type",
                                    aggfunc=[np.sum, np.mean],  # Includes both total and average sales
                                    margins=True  # Adds a totals row and column
)
    df.options.display.float_format = "${:,.2f}".format

    # Print pivot table
    print(pivot_table_avg)

except Exception as e:
    print(f"Error reading the file: {e}")