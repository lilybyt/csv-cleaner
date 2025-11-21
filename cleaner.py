import pandas as pd
import os

def clean_csv(input_file, output_file="cleaned_output.csv"):
    print(f"📂 Reading file: {input_file}...")
    
    # Check if file exists first
    if not os.path.exists(input_file):
        print(f"❌ Error: The file '{input_file}' was not found.")
        return

    # 1. Load CSV
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return

    # 2. Remove completely empty rows
    print("🧹 Removing empty rows...")
    df.dropna(how="all", inplace=True)

    # 3. Remove duplicate rows
    print("dup Removing duplicates...")
    df.drop_duplicates(inplace=True)

    # 4. Trim whitespace from text columns (fixing " Bob " -> "Bob")
    # This looks at every column; if it's text, it strips space.
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # 5. Save the new file
    print(f"💾 Saving cleaned data to: {output_file}")
    df.to_csv(output_file, index=False)
    print("✅ Done! Cleaning complete.")

# --- THIS IS THE START BUTTON ---
if __name__ == "__main__":
    # This line actually runs the function we defined above
    clean_csv("sample_input.csv")
