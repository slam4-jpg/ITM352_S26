#Sidney Lam
#Rick Kazman
#04/01/2026

import pandas as pd
import numpy as np
import pyarrow
import time
import sys
import ssl

# Allows pandas to read the CSV file from Google Drivessl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context = ssl._create_unverified_context

# Makes the DataFrame output easier to read when printed
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:.2f}".format)

# URL for the sales data CSV on Google Drive
SALES_DATA_URL = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

# Columns needed for the dashboard analysis.
# Used to check that required data exists before running each menu option.
# Helps prevent errors if some columns are missing.

REQUIRED_COLUMNS = [
    "order_number",
    "employee_id",
    "employee_name",
    "job_title",
    "sales_region",
    "order_date",
    "order_type",
    "customer_type",
    "customer_name",
    "customer_state",
    "product_category",
    "product_number",
    "product_name",  
    "quantity",
    "unit_price",
    "sales",
]

# Convert mixed-format date strings "10/6/18" or "11/06/2015" into datetime values.
# NOTE (AI assistance):
# Handles different date formats in the order_date column.
# The dataset includes dates like "10/6/18" and "11/06/2015".
# This function converts them into a consistent datetime format.
# Invalid or missing values are returned as NaT.
def parse_order_date(value):
    # Treat 0 or NaN as missing dates
    if value == 0 or pd.isna(value):
        return pd.NaT

    s = str(value).strip()
    if not s:
        return pd.NaT

    # Split on "/" to inspect the last piece as the "year"
    parts = s.split("/")
    year_part = parts[-1] if parts else ""

    try:
        if len(year_part) == 4:
            # Format like 15/02/2019 -> day/month/4-digit-year
            return pd.to_datetime(s, format="%d/%m/%Y", errors="coerce")
        else:
            # Format like 9/2/19 -> month/day/2-digit-year
            return pd.to_datetime(s, format="%m/%d/%y", errors="coerce")
    except Exception:
        # If parsing fails, treat as missing date
        return pd.NaT

# Individual requirement #9:
# "Instead of replacing missing data in the pivot table with zeroes, replace it with the mean value for that column."
# NOTE (AI assistance):
# I wasn't sure the cleanest way to code aloop through only numeric 
# columns in a DataFrame and fill NaNs with the column mean.
# I asked Claude 
# "help fix my code so its a simple function that takes a pandas pivot table
# and fills NaN values in numeric columns with the column mean."
# I used the structure it suggested and adjusted names and comments.
def fill_pivot_missing_with_means(pivot_df):
    if pivot_df is None:
        return None

    # Work on a copy so we don’t change the original pivot
    filled = pivot_df.copy()

    # Only fill numeric columns with their column mean
    for col in filled.columns:
        if pd.api.types.is_numeric_dtype(filled[col]):
            mean_val = filled[col].mean()
            filled[col] = filled[col].fillna(mean_val)

    return filled

# Individual requirement #1:
# "For each result, ask the user if they want the results exported to an 
# Excel file (that can be read directly into Excel). Ask the user what filename they want."
# NOTE (AI assistance):
# I used Claude to help me structure this function
# I wasn’t sure how to let users type a filename and then export a pandas DataFrame to Excel safely.
# My prompt was: 
# “Show me a simple Python function that exports a pandas DataFrame
# to Excel with a user-provided filename and basic error handling.”
def maybe_export_to_excel(df, default_filename="dashboard_output.xlsx"):
    # If nothing to export, just return
    if df is None or df.empty:
        return

    choice = input("Do you want to export these results to an Excel file? Enter 'y' or 'n': ").strip().lower()
    if choice != "y":
        return

    # Ask user for a filename, with a default suggestion
    filename = input(f"Enter a filename (default {default_filename}): ").strip()
    # If user just hits Enter, fall back to the default filename
    if not filename:
        filename = default_filename
    # If the user forgot to add ".xlsx", automatically append it so Excel can open the file
    if not filename.lower().endswith(".xlsx"):
        filename += ".xlsx"

    try:
        # Write DataFrame to an Excel file in the current working directory
        df.to_excel(filename, index=True)
        print(f"Results saved to '{filename}'.")
    except Exception as e:
        # Catch any file-related issues (permissions, invalid path, etc.)
        print(f"Could not save file: {e}")


# R1: Load the sales CSV into a DataFrame with error handling.
# This function handles file errors, parses dates, creates derived columns, 
# and validates that we got usable data.
def load_csv(file_path):
    print(f"\nReading CSV file from {file_path}...")
    start_time = time.time()

    try:
        # Read CSV from Google Drive, skipping bad lines instead of failing.
        df = pd.read_csv(file_path, engine="pyarrow", on_bad_lines="skip")

        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {df.columns.tolist()}")

        # Convert order_date to datetime (handles both 9/2/19 and 15/02/2019)
        if "order_date" in df.columns:
            df["order_date"] = df["order_date"].apply(parse_order_date)

        # Replace ANY missing data with 0 (R1 requirement)
        df.fillna(0, inplace=True)

        # Create a 'sales' column if quantity and unit_price are available
        if "quantity" in df.columns and "unit_price" in df.columns:
            df["sales"] = df["quantity"] * df["unit_price"]
        else:
            print("Warning: Could not create 'sales' column because 'quantity' or 'unit_price' is missing.")

        # Check which required columns are missing for the dashboard
        missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing_columns:
            print("\nWarning: The following columns required for some analytics are missing:")
            print(" ", missing_columns)
            print("Some dashboard options may not work correctly.\n")
        else:
            print("\nAll required columns for the dashboard are present.\n")

        # Simple assertions to confirm we have a non-empty DataFrame
        # (defensive programming + testing requirement)
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0

        return df

    # Handle the most common file problems gracefully instead of crashing.
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        sys.exit(1)
    except pd.errors.ParserError as e:
        print(f"Error: There was a parsing error while reading {file_path}. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while loading CSV: {e}")
        sys.exit(1)


# Extra credit #2:"When the sales data is loaded, display a summary of the data 
# (total orders, number of employees, sales regions, dates range of orders, 
# number of unique customers, product categories, unique states, total sales amount, 
# total quantities of products sold). If some data is not available (missing columns) for a 
# pre-defined analytic, remove that analytic from the menu options."
def summarize_data(data):
    # Print a simple summary of the loaded sales data
    print("\n--- Sales Data Summary ---")

    # Total orders = total rows
    print(f"Total orders: {len(data)}")

    # Number of unique employees
    if "employee_id" in data.columns:
        print(f"Number of employees: {data['employee_id'].nunique()}")

    # Sales regions and how many there are
    if "sales_region" in data.columns:
        regions = data["sales_region"].unique()
        print(f"Sales regions ({len(regions)}): {', '.join(sorted(map(str, regions)))}")

    # Date range of orders (ignore bad/missing dates)
    if "order_date" in data.columns:
        dates = pd.to_datetime(data["order_date"], errors="coerce")
        valid_dates = dates.dropna()
        if not valid_dates.empty:
            print(f"Order date range: {valid_dates.min().date()} to {valid_dates.max().date()}")

    # Number of unique customers
    if "customer_name" in data.columns:
        print(f"Number of unique customers: {data['customer_name'].nunique()}")

    # Count of product categories
    if "product_category" in data.columns:
        print(f"Product categories: {data['product_category'].nunique()}")

    # Number of unique states
    if "customer_state" in data.columns:
        print(f"Unique states: {data['customer_state'].nunique()}")

    # Total sales amount
    if "sales" in data.columns:
        print(f"Total sales amount: {data['sales'].sum():.2f}")

    # Total quantity sold
    if "quantity" in data.columns:
        print(f"Total quantity sold: {data['quantity'].sum():.0f}")


# R3 - Menu option 1: Show first n rows of sales data.
# Uses a loop and validation to make sure the user enters a valid choice.
def show_first_rows(data):
    max_rows = len(data)

    while True:
        print("\nEnter the number of rows to display:")
        print(f" - Enter a number 1 to {max_rows}")
        print(" - To see all rows, enter 'all'")
        print(" - To skip preview, press Enter")
        choice = input("Your choice: ").strip().lower()

        if choice == "":
            print("Skipping preview.")
            return

        if choice == "all":
            # Reset index so rows are numbered from 1..N instead of 0..N-1
            preview = data.copy()
            preview = preview.reset_index(drop=True)
            preview.index = range(1, len(preview) + 1)
            print("\nDisplaying all rows:\n")
            print(preview)
            maybe_export_to_excel(preview, "sales_all_rows.xlsx")
            return

        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= max_rows:
                # Only show the first n rows, renumbered 1..n for nicer display
                preview = data.head(num).copy()
                preview = preview.reset_index(drop=True)
                preview.index = range(1, len(preview) + 1)
                print(f"\nDisplaying the first {num} rows:\n")
                print(preview)
                maybe_export_to_excel(preview, f"sales_first_{num}_rows.xlsx")
                return

        print("Invalid input. Please try again.")


# Helper: check that required columns exist for an analytic.
# This supports defensive programming and is also used by the menu to hide
# analytics that cannot run on the current dataset.
def check_columns(data, required_cols, verbose=True):
    # Build a list of missing columns
    missing = [c for c in required_cols if c not in data.columns]
    if missing:
        if verbose:
            print("Cannot perform this analytic. Missing columns:", missing)
        return False
    return True


# R3 - Menu option 2: Total sales by region and order_type
def total_sales_by_region_and_order_type(data):
    required = ["sales_region", "order_type", "sales"]
    if not check_columns(data, required):
        return

    # Pivot by region (rows) and order_type (columns)
    pivot = pd.pivot_table(
        data,
        index="sales_region",
        columns="order_type",
        values="sales",
        aggfunc="sum",
    )

    pivot = fill_pivot_missing_with_means(pivot)

    print("\nTotal Sales by Region and Order Type:\n")
    print(pivot)

    maybe_export_to_excel(pivot, "total_sales_by_region_and_order_type.xlsx")
    return pivot


# R3 - Menu option 3: Average sales by region, state, and sale type
def average_sales_by_region_state_type(data):
    required = ["sales_region", "customer_state", "order_type", "sales"]
    if not check_columns(data, required):
        return

    # Pivot shows mean sales grouped by region, then by (state, order_type)
    pivot = pd.pivot_table(
        data,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
    )

    pivot = fill_pivot_missing_with_means(pivot)

    print("\nAverage Sales by Region, State, and Order Type:\n")
    print(pivot)

    maybe_export_to_excel(pivot, "average_sales_by_region_state_type.xlsx")
    return pivot


# R3 - Menu option 4: Sales by customer type and order type by state
def sales_by_customer_type_and_order_type_by_state(data):
    required = ["customer_state", "customer_type", "order_type", "sales"]
    if not check_columns(data, required):
        return

    # Group by (state, customer_type, order_type) and sum sales
    pivot = pd.pivot_table(
        data,
        index=["customer_state", "customer_type", "order_type"],
        values="sales",
        aggfunc="sum",
    )

    pivot = fill_pivot_missing_with_means(pivot)

    print("\nSales by Customer Type and Order Type by State:\n")
    print(pivot)

    maybe_export_to_excel(pivot, "sales_by_customer_type_and_order_type_by_state.xlsx")
    return pivot


# R3 - Menu option 5: Total sales quantity and price by region and product
# Extra credit #8: add percentage of quantity and sales
# NOTE (AI assistance):
# For the percentage columns, I asked Claude something like:
# "Given a pandas pivot table with total quantity and total sales, how can I add
# columns that show each row's share of the overall quantity and sales as percentages?"
# I then added that idea here and formatted the values with two decimals and a % sign.
def total_qty_and_sales_by_region_and_product(data):
    required = ["sales_region", "produce_name", "quantity", "sales"]
    if not check_columns(data, required):
        return

    # Sum quantity and sales by region + product
    pivot = pd.pivot_table(
        data,
        index=["sales_region", "produce_name"],
        values=["quantity", "sales"],
        aggfunc="sum",
    )

    pivot = fill_pivot_missing_with_means(pivot)

    # Extra credit #8: 
    #Add an analytic that shows sales by region and product, showing the percentage of the quantity and total sales per region and product.  
    #This percentage should be a new column in the pivot table.
    total_qty = pivot["quantity"].sum()
    total_sales = pivot["sales"].sum()

    if total_qty > 0:
        qty_pct = (pivot["quantity"] / total_qty) * 100
    else:
        qty_pct = 0

    if total_sales > 0:
        sales_pct = (pivot["sales"] / total_sales) * 100
    else:
        sales_pct = 0

    # Round and format as strings with % sign (e.g., "2.34%")
    pivot["quantity_pct"] = qty_pct.round(2).astype(str) + "%"
    pivot["sales_pct"] = sales_pct.round(2).astype(str) + "%"

    print("\nTotal Quantity and Sales by Region and Product (with percentages):\n")
    print(pivot)

    maybe_export_to_excel(pivot, "total_qty_and_sales_by_region_and_product.xlsx")
    return pivot

# R3 - Menu option 6: Total sales quantity and price by customer type
def total_qty_and_sales_by_customer_type(data):
    required = ["customer_type", "order_type", "quantity", "sales"]
    if not check_columns(data, required):
        return

    # Group by customer_type and order_type, sum quantity and sales
    pivot = pd.pivot_table(
        data,
        index=["customer_type", "order_type"],
        values=["quantity", "sales"],
        aggfunc="sum",
    )

    pivot = fill_pivot_missing_with_means(pivot)

    print("\nTotal Quantity and Sales by Customer Type and Order Type:\n")
    print(pivot)

    maybe_export_to_excel(pivot, "total_qty_and_sales_by_customer_type.xlsx")
    return pivot


# R3 - Menu option 7: Max and min sales price by category
def max_min_sales_price_by_category(data):
    price_col = "unit_price"
    required = ["product_category", price_col]
    if not check_columns(data, required):
        return

    # Show max and min price per product_category
    pivot = pd.pivot_table(
        data,
        index="product_category",
        values=price_col,
        aggfunc=[np.max, np.min],
    )

    pivot = fill_pivot_missing_with_means(pivot)

    print(f"\nMax and Min {price_col} by Product Category:\n")
    print(pivot)

    maybe_export_to_excel(pivot, "max_min_sales_price_by_category.xlsx")
    return pivot


# R3 - Menu option 8: Number of unique employees by region
def number_of_employees_by_region(data):
    required = ["sales_region", "employee_id"]
    if not check_columns(data, required):
        return

    # Use nunique to count unique employee_id per region
    pivot = pd.pivot_table(
        data,
        index="sales_region",
        values="employee_id",
        aggfunc=pd.Series.nunique,
    )

    # Rename column to something readable
    pivot.columns = ["Number of Employees"]
    pivot = fill_pivot_missing_with_means(pivot)

    print("\nNumber of Unique Employees by Region:\n")
    print(pivot)

    maybe_export_to_excel(pivot, "number_of_employees_by_region.xlsx")
    return pivot


# Helper function that validates user input for menu selections.
# Ensures users enter valid numbers and allows multiple selections using commas.
def get_user_selection(options, prompt, allow_empty=False):
    if not options:
        print("No available options.")
        return []

    while True:
        # Show the prompt text and then list each option with a number
        print("\n" + prompt)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        # User types something like "1, 3" or "2"
        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()

        # If empty input is allowed (for optional columns) and user just presses Enter, return an empty list
        if choice == "" and allow_empty:
            return []

        if choice == "":
            print("You must select at least one option.")
            continue

        # Split on commas and keep only pieces that are purely digits
        parts = [c.strip() for c in choice.split(",") if c.strip().isdigit()]
        if not parts:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        # Convert each piece to an integer index
        indices = [int(p) for p in parts]
        # Check that every chosen index is between 1 and the number of options
        if any(i < 1 or i > len(options) for i in indices):
            print("One or more selections are out of range. Please try again.")
            continue

        # Map the valid indices back to the actual option values
        selected = [options[i - 1] for i in indices]
        return selected

# R4: Custom Pivot Table Generator.
# NOTE (AI assistance):
# This function was built with help from Claude after I asked:
# "Help me implement a custom pivot table generator where the user
# picks rows, columns, values, and an aggregation function, but only from a small
# fixed list like the assignment example."
# I adapted the final list of options and comments to match my assignment text.
def generate_custom_pivot_table(data):
    print("\n--- Custom Pivot Table Generator ---")

    # Rows: Which field(s) should group the data
    row_options = ["employee_name", "sales_region", "product_category"]
    rows = get_user_selection(row_options, "Select rows:", allow_empty=False)

    # Columns (optional): order_type, customer_type
    col_options = ["order_type", "customer_type"]
    cols = get_user_selection(
        col_options,
        "Select columns (optional): (press Enter for no grouping)",
        allow_empty=True,
    )

    # Values: numeric fields to analyze (quantity, sales)
    value_options = ["quantity", "sales"]
    values = get_user_selection(value_options, "Select values:", allow_empty=False)

    # Aggregation function: sum, mean, count
    agg_options = ["sum", "mean", "count"]
    agg_choice = get_user_selection(agg_options, "Select aggregation function:", allow_empty=False)

    # Just use the first aggregation function chosen
    agg_func = agg_choice[0]

    try:
        # Build the pivot table using the user’s choices
        pivot = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func,
        )

        # Individual requirement #9: replace missing values in the pivot with the column mean
        pivot = fill_pivot_missing_with_means(pivot)

        print("\nCustom Pivot Table:\n")
        print(pivot)

        # Individual requirement #1: ask to export to Excel
        maybe_export_to_excel(pivot, "custom_pivot_table.xlsx")
        return pivot

    except Exception as e:
        print(f"Error creating custom pivot table: {e}")
        return None


# Menu option: Exit the program cleanly.
def exit_program(data):
    print("Exiting the program. Goodbye!")
    sys.exit(0)


# Simple test helper (Testing requirement).
def run_basic_tests(data):
    print("\nRunning basic tests...")

    # Data must be a non-empty DataFrame
    assert isinstance(data, pd.DataFrame), "Data is not a DataFrame."
    assert len(data) > 0, "DataFrame is empty."

    # Check that sales = quantity * unit_price for a small sample
    if {"sales", "quantity", "unit_price"}.issubset(data.columns):
        sample = data.head(10)
        calculated = sample["quantity"] * sample["unit_price"]
        assert np.allclose(sample["sales"], calculated), "Sales column does not match quantity * unit_price."

    print("Basic tests passed.\n")


# Extra credit #2: menu definitions with required columns for each analytic.
# NOTE (AI assistance):
# I asked ChatGPT something like:
# "How can I define a menu for my analytics in one place, including which
# columns each analytic requires, so I can dynamically build the menu later?"
# It suggested using a list of tuples (label, function, required_columns),
# which I implemented here and customized for my functions.
MENU_DEFINITIONS = [
    ("Show the first n rows of sales data", show_first_rows, []),
    ("Total sales by region and order_type", total_sales_by_region_and_order_type,
     ["sales_region", "order_type", "sales"]),
    ("Average sales by region with average sales by state and sale type",
     average_sales_by_region_state_type,
     ["sales_region", "customer_state", "order_type", "sales"]),
    ("Sales by customer type and order type by state",
     sales_by_customer_type_and_order_type_by_state,
     ["customer_state", "customer_type", "order_type", "sales"]),
    ("Total sales quantity and price by region and product",
     total_qty_and_sales_by_region_and_product,
     ["sales_region", "produce_name", "quantity", "sales"]),
    ("Total sales quantity and price by customer type",
     total_qty_and_sales_by_customer_type,
     ["customer_type", "order_type", "quantity", "sales"]),
    ("Max and min sales price of sales by category",
     max_min_sales_price_by_category,
     ["product_category", "unit_price"]),
    ("Number of unique employees by region",
     number_of_employees_by_region,
     ["sales_region", "employee_id"]),
    ("Create a custom pivot table", generate_custom_pivot_table, []),
    ("Exit", exit_program, []),
]


# R2: Display menu and dispatch to the right function.
# The menu is built dynamically using MENU_DEFINITIONS and check_columns,
# so users never see options that cannot run on the current data.
# I asked Clause a prompt like:
# "Given a list of (label, function, required_columns), show only the options
# where all required columns are present in a DataFrame, and call the chosen function."
def display_menu(data):
    # Build the visible menu based on which analytics can actually run
    menu_options = []
    for label, func, req_cols in MENU_DEFINITIONS:
        # If there are no required columns, or all required columns exist, include it
        if not req_cols or check_columns(data, req_cols, verbose=False):
            menu_options.append((label, func))

    print("\n--- Sales Data Dashboard ---")
    for i, (label, _) in enumerate(menu_options, start=1):
        print(f"{i}. {label}")

    try:
        # Ask the user which menu option they want to run
        choice = int(input(f"Select an option (1-{len(menu_options)}): ").strip())
        if 1 <= choice <= len(menu_options):
            # Call the chosen function with the data
            action = menu_options[choice - 1][1]
            action(data)
        else:
            print("Invalid choice. Please select a number from the menu.")
    except ValueError:
        # Catch non-numeric input for the menu selection
        print("Invalid input. Please enter a number.")


# Main loop: load data, sanity-check it, show a summary, then repeatedly show the menu.
def main():
    # Load data once at the start
    sales_data = load_csv(SALES_DATA_URL)

    # Run basic checks on the data
    run_basic_tests(sales_data)

    # Extra credit #2: show a summary of the data
    summarize_data(sales_data)

    # Keep showing the menu until the user chooses Exit
    while True:
        display_menu(sales_data)


if __name__ == "__main__":
    main()