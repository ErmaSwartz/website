import xarray as xr
import pandas as pd

# Define the full file path
file_path = "/Users/ermaswartz/Desktop/School/Spring_2025/Studio/Datasets/drought.nc"

# Open NetCDF file
ds = xr.open_dataset(file_path)

# Convert to Pandas DataFrame
df = ds.to_dataframe().reset_index()

# Save to CSV
output_csv_path = "/Users/ermaswartz/Desktop/School/Spring_2025/Studio/Datasets/drought_output.csv"
df.to_csv(output_csv_path, index=False)

print(f"NetCDF converted to CSV successfully! Saved at: {output_csv_path}")