import py7zr
import requests
import pandas as pd
import numpy as np

# Function to read data from a source


def getData(url, sep):
    df = pd.read_csv(url, sep=sep)
    return df


# Function to interpret the data
def interpretData(df, column_names):
    df = df[column_names]
    return df


# Function to load data into a database
def load(table_name, sheet):
    sheet.to_sql(table_name, 'sqlite:///../data/Store.sqlite',
                 if_exists='replace', index=False)


#------------------------------------------------------------
# Disease Outbreaks data

url = "https://figshare.com/ndownloader/files/37887318"
response = requests.get(url)

# Save the file locally
with open('file.7z', 'wb') as f:
    f.write(response.content)

with py7zr.SevenZipFile('file.7z', mode='r') as z:
    z.extractall()

df2 = getData('./DiseaseOutbreaks/Outbreaks.csv', sep=',')

df2 = interpretData(df2, ["Country",
                          "iso3",
                          "Year",
                          "icd10n",
                          "icd104n",
                          "icd11l1",
                          "icd11l3",
                          "Disease"])

df2_before_2020 = df2.loc[df2['Year'] < 2020]




#------------------------------------------------------------

# PRIMAP data

df1 = getData(
    'https://zenodo.org/records/4723476/files/Guetschow-et-al-2021-PRIMAP-crf_2021-v1.csv?download=1',
    sep=',')

df1 = interpretData(df1, ["area (ISO3)",
                          "entity",
                          "unit",
                          "category (IPCC2006)",
                          "1996",
                          "1997",
                          "1998",
                          "1999",
                          "2000",
                          "2001",
                          "2002",
                          "2003",
                          "2004",
                          "2005",
                          "2006",
                          "2007",
                          "2008",
                          "2009",
                          "2010",
                          "2011",
                          "2012",
                          "2013",
                          "2014",
                          "2015",
                          "2016",
                          "2017",
                          "2018",
                          "2019",])


# Cleaning the data

df1_zero_category = df1.loc[df1['category (IPCC2006)'] == '0']
gases_in_consideration = ['CO2', 'CH4', 'N2O',
                          'HFCS (AR5GWP100)', 'PFCS (AR5GWP100)', 'SF6', 'NF3']
df1_filter_gases = df1_zero_category.loc[df1_zero_category['entity'].isin(
    gases_in_consideration)]
# Replace null values with min of the row
for index, row in df1_filter_gases.iterrows():
    # Calculate the minimum of non-NA/null values
    min_val = row.iloc[4:].min()
    # Replace NA/null values with the minimum value
    df1_filter_gases.loc[index, df1_filter_gases.columns[4:]] = row.fillna(min_val)
    

df1_filter_gases.reset_index(drop=True, inplace=True)
mask = df1_filter_gases['unit'].str.contains('(?<!k)t .* / yr', regex=True)
df1_filter_gases.loc[mask, df1_filter_gases.columns[4:]] = df1_filter_gases.loc[mask, df1_filter_gases.columns[4:]].apply(lambda x: x / 1000)


# Proceed with the filtered dataframes
load('PRIMAP', df1_filter_gases)
load('Diseases', df2_before_2020)