import py7zr
import requests
import pandas as pd

df1 = pd.read_csv(
    'https://zenodo.org/records/4723476/files/Guetschow-et-al-2021-PRIMAP-crf_2021-v1.csv?download=1',
    sep=','
)

df1 = df1[["area (ISO3)", 
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
           "2019",]]

df1=df1.dropna()
df_zero_category = df1.loc[df1['category (IPCC2006)'] == '0']

df_zero_category.to_sql('PRIMAP', 'sqlite:///../data/PRIMAP.sqlite',
           if_exists='replace', index=False)


url = "https://figshare.com/ndownloader/files/37887318"
response = requests.get(url)

# Save the file locally
with open('file.7z', 'wb') as f:
    f.write(response.content)

with py7zr.SevenZipFile('file.7z', mode='r') as z:
    z.extractall()

df2 = pd.read_csv('./DiseaseOutbreaks/Outbreaks.csv', sep=',')

df2 = df2[["Country", 
           "iso3", 
           "Year", 
           "icd10n",
           "icd104n", 
           "icd11l1", 
           "icd11l3", 
           "Disease"]]

df2_before_2020 = df2.loc[df2['Year'] < 2020]

df2_before_2020.to_sql('Diseases', 'sqlite:///../data/diseases.sqlite',
           if_exists='replace', index=False)
