import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
#---------------------PLOT POPULATION VS SECONDS PER DAY---------------------
# Manual data
data = {
    'Population': [2000, 8000, 8000, 10000, 16000, 20000],
    'Seconds': [3, 118, 137, 161, 263, 313]
}

# Create DataFrame
df = pd.DataFrame(data)
df = df.sort_values(by='Population')

# Calculate time for each day (each simulation is 28 days)
df['Seconds_per_Day'] = df['Seconds']

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Population'], df['Seconds_per_Day'], color='blue', alpha=0.7, label="Data Points")
plt.plot(df['Population'], df['Seconds_per_Day'], color='blue', linestyle='-', marker='o', label="Trend Line")

# Add the dashed regression line with data values
m, q = np.polyfit(df['Population'], df['Seconds_per_Day'], 1)
x_reg = np.linspace(df['Population'].min(), df['Population'].max(), 100)
y_reg = m * x_reg + q
plt.plot(x_reg, y_reg, color='red', linestyle='--', label=f"Fit: y = {m:.2f}x + {q:.2f}")

plt.title("Population vs Seconds per Day", fontsize=14)
plt.xlabel("Population", fontsize=12)
plt.ylabel("Seconds/Days", fontsize=12)
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig("10 prov/population_time_plot_with_regression.png", dpi=300)
plt.show()

# Y = 0.02x - 16.54
"""

"""
#---------------------CALCULATE LINEAR REGRESSION LINE---------------------
import numpy as np

# Data (replace with yours)
x = np.array([2000, 8000, 8000, 10000, 16000, 20000])
y = np.array([3, 118, 137, 161, 263, 313])

# Calculate the coefficients for the line y = mx + q
m, q = np.polyfit(x, y, 1)

# Generate line values
x_reg = np.linspace(min(x), max(x), 100)  # Points for the line
y_reg = m * x_reg + q

# Plot the data and the regression line
plt.scatter(x, y, color='red', label='Data')
plt.plot(x_reg, y_reg, color='blue', label=f'Line: y = {m:.2f}x + {q:.2f}')
plt.legend()
plt.show()

# Print the equation
print(f"Line equation: y = {m:.2f}x + {q:.2f}")
"""

"""
#------------CODE TO PLOT POPULATION CHANGE GRAPH WITH 10 PROVINCES-------------
import numpy as np
from scipy.stats import linregress

# Manual data
data = {
    'Population': [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000],
    'Seconds': [123, 488, 1594, 2278, 4852, 5138, 6988, 14440]
} # Add new data for 40000 here

# Create DataFrame
df = pd.DataFrame(data)
df = df.sort_values(by='Population')

# Calculate time for each day (each simulation is 28 days)
df['Seconds_per_Day'] = df['Seconds'] / 28

# Calculate the regression line
m, q = np.polyfit(df['Population'], df['Seconds_per_Day'], 1)

# Generate points for the regression line
x_reg = np.linspace(df['Population'].min(), df['Population'].max(), 100)
y_reg = m * x_reg + q

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Population'], df['Seconds_per_Day'], color='blue', alpha=0.7, label="Data Points")
plt.plot(df['Population'], df['Seconds_per_Day'], color='blue', linestyle='-', marker='o', label="Trend Line")

# Add the dashed regression line
plt.plot(x_reg, y_reg, color='red', linestyle='--', label=f"Fit: y = {m:.2f}x + {q:.2f}")

plt.title("Population vs Seconds per Day", fontsize=14)
plt.xlabel("Population", fontsize=12)
plt.ylabel("Seconds/Days", fontsize=12)
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig("10 prov/population_time_plot.png", dpi=300)
plt.show()
"""

"""
#---------CODE FOR SEITRS 6-CURVE CHART-------
# Load the CSV file (change 'your_file.csv' to the correct name)
file_path = "SEITRS_T4.csv"
data = pd.read_csv(file_path)

# Extract the required columns
days = data["Day"]
columns = ["classS", "classE", "classI", "classT3", "classT4", "classR", "Deaths"]
labels = ["S", "E", "I", "J3", "J4", "R", "Deaths"]

# Create the chart
plt.figure(figsize=(12, 6))

# Draw a curve for each class
for col, label in zip(columns, labels):
    plt.plot(days, data[col], label=label)

# Configure the chart
plt.title("Class Cardinality Over Days", fontsize=16)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Population", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save the plot
plt.savefig("SEITRS/class_cardinality.png", dpi=300)

# Show the plot
plt.show()
"""

"""
#---------CODE FOR SEITRS 4-CURVE CHART-------
# Load the CSV file (change 'your_file.csv' to the correct name)
file_path = "SEITRS_T4.csv"
data = pd.read_csv(file_path)

# Extract the required columns
days = data["Day"]
columns = ["classE", "classI", "classT3", "classT4", "Deaths"]
labels = ["E", "I", "J3", "J4", "Deaths"]

# Define colors
colors = ["orange", "green", "red", "purple", "pink"]

# Create the chart
plt.figure(figsize=(12, 6))

# Draw a curve for each class
for col, label, color in zip(columns, labels, colors):
    plt.plot(days, data[col], label=label, color=color)

# Configure the chart
plt.title("Class Cardinality Over Days", fontsize=16)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Population", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save the plot
plt.savefig("SEJIRS/4_class_cardinality.png", dpi=300)

# Show the plot
plt.show()
"""

#---------CODE FOR SPP 4-CURVE CHART-------
"""
def create_multi_line_chart(csv_files, labels, title, x_label, y_label, output_filename, output_dir):
    plt.figure(figsize=(12, 8))

    # Draw the main curves
    for csv_file, label in zip(csv_files, labels):
        data = pd.read_csv(csv_file)
        x = data['Day']
        y = data['Deaths'] / 12000 * 100
        plt.plot(x, y, linewidth=2, label=label)

    # Configure the chart
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)
    plt.tight_layout()

    # Save the chart
    output_path = os.path.join(output_dir, f"{output_filename}.png")
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Chart saved in: {output_path}")

# Example of usage
csv_files = [
    "variando F/F star 0.1/simulation_12000_7_365___20250528_135037.csv",
    "variando F/F star 0.01/simulation_12000_7_365___20250527_141151.csv",
    "variando F/F star 0.001/simulation_12000_7_365___20250526_190017.csv",
]
labels = ["F* = 0.1", "F* = 0.01", "F* = 0.001"]
title = "Deaths at varying F*"
x_label = "Days"
y_label = "Deaths"
output_filename = "F_prevalence_multi_simulation"
output_dir = "variando F"

create_multi_line_chart(csv_files, labels, title, x_label, y_label, output_filename, output_dir)
"""
"""
#---------CODE FOR QUARANTINE 3-CURVE CHART-------
def create_multi_line_chart(csv_files, labels, title, x_label, y_label, output_filename, output_dir):
    plt.figure(figsize=(12, 8))

    # Draw the main curves
    for csv_file, label in zip(csv_files, labels):
        data = pd.read_csv(csv_file)
        x = data['Day']
        y = data['Deaths'] / 25000 * 100
        plt.plot(x, y, linewidth=2, label=label)

    # Add horizontal lines
    plt.hlines(y=-0.008, xmin=50, xmax=70, color='green', linestyle='--', linewidth=2)
    plt.hlines(y=-0.008, xmin=90, xmax=110, color='green', linestyle='--', linewidth=2)
    plt.hlines(y=-0.008, xmin=130, xmax=150, color='green', linestyle='--', linewidth=2)
    plt.hlines(y=-0.005, xmin=50, xmax=110, color='orange', linestyle='--', linewidth=2)

    # Configure the chart
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)
    plt.tight_layout()

    # Save the chart
    output_path = os.path.join(output_dir, f"{output_filename}.png")
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Chart saved in: {output_path}")

# Example of usage
csv_files = [
    "variando PP/0.9 PP - base/simulation_25000_12_365___20250118_014844.csv",
    "variando quarantene/50-110/simulation_25000_12_365___20250119_025018.csv",
    "variando quarantene/50-70, 90-110, 130-150/simulation_25000_12_365___20250120_131900.csv"
]
labels = ["No quarantine", "One quarantine", "Splitted quarantine"]
title = "Deaths Over Days (%) at varying quarantine"
x_label = "Days"
y_label = "Deaths (%)"
output_filename = "Quarantine_deaths_multi_simulation"
output_dir = "variando quarantene"

create_multi_line_chart(csv_files, labels, title, x_label, y_label, output_filename, output_dir)
"""

"""
#---------CODE FOR PP 5-CURVE CHART-------
def create_multi_line_chart(csv_files, labels, title, x_label, y_label, output_filename, output_dir):
    plt.figure(figsize=(12, 8))

    for csv_file, label in zip(csv_files, labels):
        # Read the CSV
        data = pd.read_csv(csv_file)

        x = data['Day']
        y = data['Deaths'] / 25000 * 100

        # Add the curve to the chart
        plt.plot(x, y, linewidth=2, label=label)

    # Add title and axes
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)
    plt.tight_layout()

    # Save the chart
    output_path = os.path.join(output_dir, f"{output_filename}.png")
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Chart saved in: {output_path}")

csv_files = [
    "variando PP/0.25 PP/simulation_25000_12_365___20250114_114954.csv",
    "variando PP/0.5 PP/expanded_data.csv",
    "variando PP/0.75 PP/modified_data_075.csv",
    "variando PP/0.9 PP - base/simulation_25000_12_365___20250118_014844.csv",
    "variando PP/1 PP/modified_data_1.csv",
]
labels = ["PP = 0.25", "PP = 0.5", "PP = 0.75", "PP = 0.9", "PP = 1"]
title = "Deaths Over Days (%) at varying PP"
x_label = "Days"
y_label = "Deaths (%)"
output_filename = "PP_deaths_multi_simulation"
output_dir = "variando PP"

create_multi_line_chart(csv_files, labels, title, x_label, y_label, output_filename, output_dir)
"""

"""
#----------CODE TO SUM TIMES------------
# TODO: times
csv_file = "10 prov/simulation_40000_10_28___20250216_195029.csv"  # Replace with your file name
try:
    df = pd.read_csv(csv_file)
    if "Seconds" not in df.columns:
        raise ValueError("The column 'Seconds' is not present in the CSV file.")
    sum_seconds = df["Seconds"].sum()
    print(f"The sum of the values in the 'Seconds' column is: {sum_seconds:.2f}")
except FileNotFoundError:
    print(f"Error: The file '{csv_file}' was not found.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
"""

'''
#----------CODE TO CREATE POPULATION/SPEED CHART----------
# Read the Excel file
file_path = "simulazioni migliori/Tempi.xlsx"  # Change to the correct file name
df = pd.read_excel(file_path)

df = df.sort_values(by='Population')

# Calculate the Seconds/Days ratio
df['Ratio'] = df['Seconds'] / df['Days']

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.plot(df['Population'], df['Ratio'], color='blue', marker='o', linestyle='-')
plt.title("Population vs Seconds per Day", fontsize=14)
plt.xlabel("Population", fontsize=12)
plt.ylabel("Seconds/Days", fontsize=12)
plt.grid(True)

# Save the chart as an image
plt.savefig("simulazioni migliori/linear_time_plot.png", dpi=300)  # Change to "scatter_plot.jpg" if you prefer JPG
plt.show()
'''

"""
#------------CODE TO PLOT 10 FRA CHARTS FOR PROVINCE CHANGE AND THEIR TIME-------------
# Manual data
data = {
    'Province': [2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Seconds': [4754, 3686, 2844, 2522, 2204, 2459, 2123, 2249, 1923]
}

# Create DataFrame
df = pd.DataFrame(data)
df = df.sort_values(by='Province')

# Calculate time for each day (each simulation is 50 days)
df['Seconds_per_Day'] = df['Seconds'] / 50

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Province'], df['Seconds_per_Day'], color='blue', alpha=0.7, label="Data Points")
plt.plot(df['Province'], df['Seconds_per_Day'], color='blue', linestyle='-', marker='o', label="Trend Line")

plt.title("Province vs Seconds per Day", fontsize=14)
plt.xlabel("Provinces", fontsize=12)
plt.ylabel("Seconds/Days", fontsize=12)
plt.grid(True)

# Save the chart
plt.savefig("Simulazioni Fra Prov/province_time_plot.png", dpi=300)
plt.show()
"""

"""
#------------CODE TO PRINT INFECTED AND DEATHS CHARTS-------------
# CSV file path
csv_filename = "dati_percentuali_Veneto.csv"

# Read the CSV file
try:
    data = pd.read_csv(csv_filename, sep=',')
except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")
    exit()

# Create a sequential column for days
data["giorno"] = range(1, len(data) + 1)

# Verify that the necessary columns exist in the dataset
required_columns = ["data", "deceduti", "nuovi_positivi", "totale_positivi"]
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    print(f"Error: The following columns are missing in the file: {missing_columns}")
    exit()

# Create directory for the charts
output_dir = "grafici_Veneto"
os.makedirs(output_dir, exist_ok=True)

# Function to create a line chart
def create_line_chart(x, y, title, x_label, y_label, base_filename, output_dir):
    filename = f"{base_filename}.png"  # Chart file name
    output_file = os.path.join(output_dir, filename)  # Full file path
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue', linewidth=2)
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(output_file)  # Save the chart
    plt.close()  # Close the figure to avoid overlapping

# Create the charts
# Chart 1: Days vs Deaths
create_line_chart(
    x=data["giorno"],  # Days column
    y=data["deceduti"],  # Deaths column
    title="Deaths over days (%) In Veneto",
    x_label="Days",
    y_label="Deaths (%)",
    base_filename="deceduti_line_chart",
    output_dir=output_dir
)

# Chart 2: Days vs New Positives
create_line_chart(
    x=data["giorno"],  # Days column
    y=data["nuovi_positivi"],  # New positives column
    title="New Daily Cases Over Days (%) In Veneto",
    x_label="Days",
    y_label="New Daily Cases (%)",
    base_filename="nuovi_positivi_line_chart",
    output_dir=output_dir
)

# Chart 3: Days vs Total Positives
create_line_chart(
    x=data["giorno"],  # Days column
    y=data["totale_positivi"],  # Total positives column
    title="Prevalence Over Days (%) In Veneto",
    x_label="Days",
    y_label="Prevalence (%)",
    base_filename="totale_positivi_line_chart",
    output_dir=output_dir
)

print("The charts have been generated and saved in the 'grafici_Veneto' directory.")
"""

"""
#------------CODE TO TRANSFORM COLUMNS INTO PERCENTAGES-------------
# Variable for Lombardy's population
lombardy_population = 5000000  # About 10 million
# Original file name and generated file name
input_file = "dati_filtrati_Veneto.csv"
output_file = "dati_percentuali_Veneto.csv"

# Read the CSV file
df = pd.read_csv(input_file, sep='\t')

# Specify the columns to normalize
columns_to_normalize = [
    "ricoverati_con_sintomi", "terapia_intensiva", "totale_ospedalizzati", 
    "totale_positivi", "variazione_totale_positivi", "nuovi_positivi", 
    "deceduti", "totale_casi"
]  # Example: modify based on the actual column names

# Normalize the specified columns
for column in columns_to_normalize:
    if column in df.columns:
        df[column] = (df[column] / lombardy_population) * 100

# Save the new CSV file
df.to_csv(output_file, index=False)
print(f"File '{output_file}' generated with percentage values.")
"""

"""
#------------CODE TO SLICE LOMBARDY CSV, EXTRACT ITS PEAK AND COMPARE IT WITH MY CSV----------
# Load data from the first CSV and select rows from 550 to 915
file_path1 = "dati_percentuali_Veneto.csv"
data_veneto = pd.read_csv(file_path1)

# Filter the data and create an explicit copy
filtered_data_veneto = data_veneto.iloc[570:935].copy() # 300:381 with 8000 2 90, 550:915 with 365 days

# Fix the "giorno" column
filtered_data_veneto["giorno"] = range(1, len(filtered_data_veneto) + 1)

# Calculate the number of deaths on day 0 (new starting point)
initial_deaths = filtered_data_veneto["deceduti"].iloc[0]

# Subtract the initial value from all values in the deaths column
filtered_data_veneto["deceduti"] = filtered_data_veneto["deceduti"] - initial_deaths

# Load data from the second CSV
file_path2 = "simulazioni migliori/365 gg 6%/simulation_12000_7_365___20250527_162439.csv"
data_simulation = pd.read_csv(file_path2)
data_simulation["Prevalence (%)"] = (data_simulation["Prevalence"] / 12000) * 100
data_simulation["Deaths (%)"] = (data_simulation["Deaths"] / 12000) * 100

# Create the chart with two lines
plt.figure(figsize=(10, 6))
plt.plot(filtered_data_veneto["giorno"], filtered_data_veneto["totale_positivi"],
         label="Veneto Prevalence", color='blue', linewidth=2)
plt.plot(data_simulation["Day"], data_simulation["Prevalence (%)"],
         label="Simulation Prevalence", color='orange', linewidth=2)

# Customize the chart
plt.title("Prevalence Over Days (%) In Veneto vs Simulation", fontsize=16)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Prevalence (%)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.tight_layout()

# Save the chart
output_file = os.path.join("prevalence_combined_line_chart_tesi2.png")
plt.savefig(output_file)
plt.close()

# Create the deaths chart with two lines
plt.figure(figsize=(10, 6))
plt.plot(filtered_data_veneto["giorno"], filtered_data_veneto["deceduti"],
         label="Veneto Deaths", color='blue', linewidth=2)
plt.plot(data_simulation["Day"], data_simulation["Deaths (%)"],
         label="Simulation Deaths", color='orange', linewidth=2)

# Customize the chart
plt.title("Deaths Over Days (%) In Veneto vs Simulation", fontsize=16)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Deaths (%)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.tight_layout()

# Save the chart
output_file = os.path.join("deaths_combined_line_chart_tesi2.png")
plt.savefig(output_file)
plt.close()

print(f"Charts saved in '{output_file}'")
"""

"""
#------------CODE TO CLEAN DB REGION BY REGION-----------
# CSV file name
csv_file = "no_note_dpc-covid19-ita-regioni.csv"

# Select only the columns of interest
columns_of_interest = [
    "data", "ricoverati_con_sintomi", "terapia_intensiva", "totale_ospedalizzati", 
    "totale_positivi", "variazione_totale_positivi", "nuovi_positivi", 
    "deceduti", "totale_casi"
]

# Load the CSV file
df = pd.read_csv(csv_file, sep=',')
df.columns = df.columns.str.strip()
selected_df = df[columns_of_interest + ["denominazione_regione"]]

# Filter only the rows with denominazione_regione == "Veneto"
filtered_df = selected_df[selected_df["denominazione_regione"] == "Veneto"]

# Remove the 'denominazione_regione' column
final_df = filtered_df.drop(columns=["denominazione_regione"])

# Save the result in a new CSV file
final_df.to_csv("dati_filtrati_Veneto.csv", index=False, sep="\t")
print("Data cleaning completed. File saved as 'dati_filtrati_Veneto.csv'.")
"""

'''
#-------------CODE TO IMPORT FROM GITHUB--------------
# GitHub repository URL
repo_url = "https://github.com/pcm-dpc/COVID-19.git"  # Change to the repository URL
local_folder = "repo_clonato"  # Name of the folder where the repository will be cloned
csv_folder = "dati-regioni"  # Change to the relative path of the CSV folder inside the repo
region_of_interest = "Lombardia"  # Change to your region of interest

# Clone the GitHub repository if it's not already present
if not os.path.exists(local_folder):
    print("Cloning the repository...")
    git.Repo.clone_from(repo_url, local_folder)
else:
    print("The repository has already been cloned.")

# Full path of the CSV folder
csv_folder_path = os.path.join(local_folder, csv_folder)

# Check if the folder exists
if not os.path.exists(csv_folder):
    raise FileNotFoundError(f"The folder {csv_folder} does not exist. Check the path.")

# List to collect all data
merged_data = []

# Scan all .csv files in the folder
for filename in sorted(os.listdir(csv_folder_path)):
    if filename.endswith(".csv"):
        file_path = os.path.join(csv_folder_path, filename)
        
        # Read the .csv file
        df = pd.read_csv(file_path, sep="\t")
        
        # Filter the data for the region of interest
        filtered_df = df[df["denominazione_regione"] == region_of_interest]
        
        # Add the filtered data to the list
        if not filtered_df.empty:
            merged_data.append(filtered_df)
        else:
            print(f"No data found for the region {region_of_interest} in {filename}")

# Combine all merged data
final_df = pd.concat(merged_data, ignore_index=True)

# Save the final DataFrame to a new .csv file
final_df.to_csv("dati_accorpati_regione.csv", index=False, sep="\t")
print("Merge completed: 'dati_accorpati_regione.csv'")
'''


#---------CODE TO PLOT STOCHASTICITY OF SEIJRS CLASSES (SUBPLOTS)-------
'''
# 1. Insert the names of your 3 CSV files
csv_files = [
    "simulation_25000_12_200___20260319_102855.csv",
    "simulation_25000_12_200___20260319_090958.csv",
    "simulation_25000_12_200___20260319_074913.csv"
]

# Total population for percentage calculation (adjust if your simulation changes)
total_population = 25000

# Read data from the 3 files
dfs = [pd.read_csv(file) for file in csv_files]
days = dfs[0]["Day"] # Use the days from the first simulation

# Define the columns to analyze and their colors
columns = ["classS", "classE", "classI", "classT3", "classT4", "classR"]
labels = ["S", "E", "I", "J3", "J4", "R"]
colors = ["blue", "orange", "green", "red", "purple", "brown"]

# 2. Create a SINGLE image containing a 2x3 grid (2 rows, 3 columns)
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()  # Flatten the grid into a list for easier iteration

# 3. Draw each class in its dedicated subplot
for idx, (col, label, color) in enumerate(zip(columns, labels, colors)):
    ax = axes[idx] # Select the current subplot

    # Extract the data and convert it directly to percentage: (value / total) * 100
    class_data = np.array([(df[col].values / total_population) * 100 for df in dfs])
    mean_data = class_data.mean(axis=0) # Calculate the mean of the percentages

    # Draw the 3 individual simulations (thin and semi-transparent lines)
    for i, sim_data in enumerate(class_data):
        sim_label = "Individual Runs" if i == 0 else ""
        ax.plot(days, sim_data, color=color, alpha=0.3, linewidth=1, label=sim_label)

    # Draw the mean line (thick and opaque line)
    ax.plot(days, mean_data, color=color, alpha=1.0, linewidth=2.5, label="Mean")

    # Configure the individual subplot
    ax.set_title(f"Class {label}", fontsize=14)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(fontsize=10, loc="best")

    # Add axes labels (Y label only on the left column, X label only on the bottom row)
    if idx % 3 == 0:
        ax.set_ylabel("Percentage (%)", fontsize=12)
    if idx >= 3:
        ax.set_xlabel("Days", fontsize=12)

# 4. Final configurations for the entire image
plt.suptitle("Cardinality of SEJIRS model over days (%)", fontsize=18)
plt.tight_layout() # Optimize spacing to avoid overlapping text

# 5. Save the generated image
output_dir = "stochasticity_plots"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "seijrs_stochasticity_subplots_percentage.png")
plt.savefig(output_path, dpi=300)

print(f"Chart successfully saved in: {output_path}")
plt.show()


#---------CODE TO PLOT STOCHASTICITY OF PREVALENCE AND DEATHS (PP & SPP)-------


def plot_stochastic_grid(base_dir, sub_dirs, labels, metric, grid_rows, grid_cols, title_prefix, output_filename, total_population=25000):
    # Create the grid
    fig, axes = plt.subplots(grid_rows, grid_cols, figsize=(16, 10))
    axes = axes.flatten()

    for idx, (sub_dir, label) in enumerate(zip(sub_dirs, labels)):
        ax = axes[idx]
        folder_path = os.path.join(base_dir, sub_dir)

        # Automatically find all CSV files
        try:
            csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
        except FileNotFoundError:
            print(f"Warning: Folder '{folder_path}' not found. Skipping...")
            continue

        if len(csv_files) == 0:
            print(f"Warning: No CSV files found in {folder_path}. Skipping...")
            continue

        # Read data from the files
        dfs = [pd.read_csv(f) for f in csv_files]

        # --- FIX FOR INHOMOGENEOUS SHAPE ---
        # Find the minimum number of rows among the simulations to avoid shape errors
        min_len = min(len(df) for df in dfs)
        days = dfs[0]["Day"].values[:min_len]

        # Extract the requested metric, slice to min_len, and convert to percentage
        class_data = np.array([(df[metric].values[:min_len] / total_population) * 100 for df in dfs])

        # Calculate Mean
        mean_data = class_data.mean(axis=0)

        # Draw the 3 individual simulations (Gray, semi-transparent, medium thickness)
        for i, sim_data in enumerate(class_data):
            sim_label = "Individual Runs" if i == 0 else ""
            ax.plot(days, sim_data, color="gray", alpha=0.6, linewidth=1.5, label=sim_label)

        # Draw the mean line on top (Red, solid, clear thickness)
        ax.plot(days, mean_data, color="red", alpha=1.0, linewidth=2.0, label="Mean")

        # Configure the individual subplot
        ax.set_title(label, fontsize=14)
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend(fontsize=10, loc="best")
        ax.set_xlabel("Days", fontsize=12)
        ax.set_ylabel(f"{metric} (%)", fontsize=12)

    # Hide any extra empty subplots
    for i in range(len(sub_dirs), len(axes)):
        fig.delaxes(axes[i])

    # Final configurations
    plt.suptitle(f"{title_prefix} - {metric} (%)", fontsize=18)
    plt.tight_layout()

    # Save the generated image right next to the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_directory, "stochasticity_plots")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Chart successfully saved in: {output_path}")

# ==========================================
# Get the exact absolute path of this python script
# ==========================================
script_dir = os.path.dirname(os.path.abspath(__file__))

# ==========================================
# 1. EXECUTE FOR PP (5 subfolders -> 2x3 grid)
# ==========================================
# ATTENZIONE: Controlla bene che questi nomi corrispondano esattamente a quelli sul tuo PC!
sub_dirs_pp = [
    "PP 1 SPP 0.8",
    "PP 0,9 SPP 0.8",
    "PP 0,75 SPP 0.8",
    "PP 0,5 SPP 0.8",
    "PP 0,25 SPP 0.8"
]
labels_pp = ["PP = 1", "PP = 0.9", "PP = 0.75", "PP = 0.5", "PP = 0.25"]

# Plot Prevalence for PP
plot_stochastic_grid(script_dir, sub_dirs_pp, labels_pp, "Prevalence", 2, 3, "Prevalence over days at varying PP", "PP_prevalence_stochasticity.png")
# Plot Deaths for PP
plot_stochastic_grid(script_dir, sub_dirs_pp, labels_pp, "Deaths", 2, 3, "Deaths over days at varying PP", "PP_deaths_stochasticity.png")

# ==========================================
# 2. EXECUTE FOR SPP (4 subfolders -> 2x2 grid)
# ==========================================
sub_dirs_spp = [
    "PP 0,9 SPP 1",
    "PP 0,9 SPP 0.8",
    "PP 0,9 SPP 0.5",
    "PP 0,9 SPP 0"
]
labels_spp = ["SPP = 1", "SPP = 0.8", "SPP = 0.5", "SPP = 0"]

# Plot Prevalence for SPP
plot_stochastic_grid(script_dir, sub_dirs_spp, labels_spp, "Prevalence", 2, 2, "Prevalence over days at varying SPP", "SPP_prevalence_stochasticity.png")
# Plot Deaths for SPP
plot_stochastic_grid(script_dir, sub_dirs_spp, labels_spp, "Deaths", 2, 2, "Deaths over days at varying SPP", "SPP_deaths_stochasticity.png")

'''


#---------CODE TO PLOT STOCHASTICITY OF PREVALENCE AND DEATHS (SINGLE CHART)-------

'''

def plot_stochastic_single_chart(base_dir, sub_dirs, labels, metric, title, output_filename, total_population=25000):
    # Create a single large figure
    plt.figure(figsize=(12, 8))
    
    # Define a color palette for the different parameters
    colors = ["blue", "orange", "green", "red", "purple"]

    for idx, (sub_dir, label) in enumerate(zip(sub_dirs, labels)):
        folder_path = os.path.join(base_dir, sub_dir)
        color = colors[idx % len(colors)] # Assign a specific color to this parameter
        
        # Automatically find all CSV files
        try:
            csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
        except FileNotFoundError:
            print(f"Warning: Folder '{folder_path}' not found. Skipping...")
            continue
            
        if len(csv_files) == 0:
            print(f"Warning: No CSV files found in {folder_path}. Skipping...")
            continue

        # Read data from the files
        dfs = [pd.read_csv(f) for f in csv_files]
        
        # --- FIX FOR INHOMOGENEOUS SHAPE ---
        min_len = min(len(df) for df in dfs)
        days = dfs[0]["Day"].values[:min_len]

        # Extract the requested metric, slice to min_len, and convert to percentage
        class_data = np.array([(df[metric].values[:min_len] / total_population) * 100 for df in dfs])
        
        # Calculate Mean
        mean_data = class_data.mean(axis=0)

        # Draw the individual simulations (Thin and semi-transparent)
        for sim_data in class_data:
            # We don't add a label here to avoid cluttering the legend
            plt.plot(days, sim_data, color=color, alpha=0.2, linewidth=1)

        # Draw the mean line on top (Thick and fully opaque)
        plt.plot(days, mean_data, color=color, alpha=1.0, linewidth=2.5, label=f"Mean {label}")

    # Configure the chart
    plt.title(title, fontsize=16) # <-- QUI ABBIAMO INSERITO IL TITOLO ESATTO SENZA AGGIUNTE
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=12, loc="best")
    plt.xlabel("Days", fontsize=14)
    plt.ylabel(f"{metric} (%)", fontsize=14)
    plt.tight_layout()

    # Save the generated image right next to the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_directory, "stochasticity_plots")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)
    plt.savefig(output_path, dpi=300)
    plt.close() # Close the figure to free up memory

    print(f"Chart successfully saved in: {output_path}")

# ==========================================
# Get the exact absolute path of this python script
# ==========================================
script_dir = os.path.dirname(os.path.abspath(__file__))

# ==========================================
# 1. EXECUTE FOR PP (Overlapped in a single chart)
# ==========================================
sub_dirs_pp = [
    "PP 1 SPP 0.8", 
    "PP 0,9 SPP 0.8", 
    "PP 0,75 SPP 0.8", 
    "PP 0,5 SPP 0.8", 
    "PP 0,25 SPP 0.8"
]
labels_pp = ["PP = 1", "PP = 0.9", "PP = 0.75", "PP = 0.5", "PP = 0.25"]

# Plot Prevalence for PP
plot_stochastic_single_chart(script_dir, sub_dirs_pp, labels_pp, "Prevalence", "Prevalence over days (%) at varying PP", "PP_prevalence_combined.png")
# Plot Deaths for PP
plot_stochastic_single_chart(script_dir, sub_dirs_pp, labels_pp, "Deaths", "Deaths over days (%) at varying PP", "PP_deaths_combined.png")

# ==========================================
# 2. EXECUTE FOR SPP (Overlapped in a single chart)
# ==========================================
sub_dirs_spp = [
    "PP 0,9 SPP 1", 
    "PP 0,9 SPP 0.8", 
    "PP 0,9 SPP 0.5", 
    "PP 0,9 SPP 0"
]
labels_spp = ["SPP = 1", "SPP = 0.8", "SPP = 0.5", "SPP = 0"]

# Plot Prevalence for SPP
plot_stochastic_single_chart(script_dir, sub_dirs_spp, labels_spp, "Prevalence", "Prevalence over days (%) at varying SPP", "SPP_prevalence_combined.png")
# Plot Deaths for SPP
plot_stochastic_single_chart(script_dir, sub_dirs_spp, labels_spp, "Deaths", "Deaths over days (%) at varying SPP", "SPP_deaths_combined.png")

'''

#---------CODE TO PLOT STOCHASTICITY OF LOCKDOWNS (SINGLE CHART WITH PADDING)-------
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_lockdown_single_chart(base_dir, sub_dirs, labels, metric, title, output_filename, total_population=25000):
    # Create a single large figure
    plt.figure(figsize=(12, 8))
    
    # Define a color palette: Blue (Base), Orange (60-day), Green (3x20-day)
    colors = ["blue", "orange", "green"]

    # First pass: read all data to find the global maximum length (e.g., 800 days)
    all_dfs = []
    global_max_len = 0
    master_days = None
    
    for sub_dir in sub_dirs:
        folder_path = os.path.join(base_dir, sub_dir)
        try:
            csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
            dfs = [pd.read_csv(f) for f in csv_files]
            all_dfs.append(dfs)
            for df in dfs:
                if len(df) > global_max_len:
                    global_max_len = len(df)
                    master_days = df["Day"].values
        except FileNotFoundError:
            print(f"Warning: Folder '{folder_path}' not found. Skipping...")
            all_dfs.append([])

    # Second pass: Plotting with intelligent Padding (Zero or Edge)
    for idx, (dfs, label) in enumerate(zip(all_dfs, labels)):
        if not dfs:
            continue
            
        color = colors[idx % len(colors)]
        class_data = []

        # Process each simulation and pad if it's shorter than the maximum length
        for df in dfs:
            val = (df[metric].values / total_population) * 100
            if len(val) < global_max_len:
                if metric == "Deaths":
                    # For cumulative metrics (Deaths), we carry forward the last recorded value
                    val = np.pad(val, (0, global_max_len - len(val)), mode='edge')
                else:
                    # For active metrics (Prevalence), we pad with 0s
                    val = np.pad(val, (0, global_max_len - len(val)), mode='constant', constant_values=0)
            class_data.append(val)
            
        class_data = np.array(class_data)
        
        # Calculate Mean
        mean_data = class_data.mean(axis=0)

        # Draw the individual simulations (Thin and semi-transparent)
        for sim_data in class_data:
            plt.plot(master_days, sim_data, color=color, alpha=0.2, linewidth=1)

        # Draw the mean line on top (Thick and fully opaque)
        plt.plot(master_days, mean_data, color=color, alpha=1.0, linewidth=2.5, label=f"{label} (Mean)")

    # Add the horizontal dashed lines for lockdown periods at the bottom
    plt.hlines(y=-0.008, xmin=50, xmax=70, color='green', linestyle='--', linewidth=2)
    plt.hlines(y=-0.008, xmin=90, xmax=110, color='green', linestyle='--', linewidth=2)
    plt.hlines(y=-0.008, xmin=130, xmax=150, color='green', linestyle='--', linewidth=2)
    plt.hlines(y=-0.005, xmin=50, xmax=110, color='orange', linestyle='--', linewidth=2)

    # Configure the chart
    plt.title(title, fontsize=16)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=12, loc="best")
    plt.xlabel("Days", fontsize=14)
    plt.ylabel(f"{metric} (%)", fontsize=14)
    plt.tight_layout()

    # Save the generated image
    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_directory, "stochasticity_plots")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Chart successfully saved in: {output_path}")

# ==========================================
# Get the exact absolute path of this python script
# ==========================================
script_dir = os.path.dirname(os.path.abspath(__file__))

# ==========================================
# 3. EXECUTE FOR LOCKDOWNS
# ==========================================
# Check if these exact folder names match your directories
sub_dirs_lockdowns = [
    "PP 0,9 SPP 0.8", 
    "60 day lockdown - 400 days", 
    "3 20 day lockdown - 800 days"
]
labels_lockdowns = ["No lockdown", "60 day lockdown", "3x20 day lockdown"]

# Plot Prevalence for Lockdowns
plot_lockdown_single_chart(script_dir, sub_dirs_lockdowns, labels_lockdowns, "Prevalence", "Prevalence over days (%) at varying lockdowns", "Lockdown_prevalence_combined.png")

# Plot Deaths for Lockdowns
plot_lockdown_single_chart(script_dir, sub_dirs_lockdowns, labels_lockdowns, "Deaths", "Deaths over days (%) at varying lockdowns", "Lockdown_deaths_combined.png")
