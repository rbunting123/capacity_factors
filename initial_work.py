import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import openpyxl
    import xlrd
    file_path = r"C:\Repository Folder\capacity_factors"

    return file_path, mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## This marimo notebook is part of inital work to combine the following datasets together:
    - EIA 860: https://www.eia.gov/electricity/data/eia860/
    - EIA 923: https://www.eia.gov/electricity/data/eia923/

    ### What is EIA 860? - WHo and What exists dataset:
    Basically this dataset tells us what the generator is
    - Power Plant Locations and IDS
    - Generator level info
    - Ownership and operators
    - Planned additions, retirements and changes
    - Status (operating, retires and proposed)

    #### Important infomation about 860!
    -


    ### What is EIA 923 - What actually happened dataset:
    This datasets tell us how well it performed
    - Monthly electricity generation
    - Fuel consumption
    - Fuel stocks and deliveries
    - Fuel costs and quality

    #### Important infomation about 923
    - A plant will appear multiple times, with the same Plant ID
    - They may have different Prime movers / Fuel types
    - E.g Plant ID 3 has 5 different rows
    - Data is available monthly do we want this yearly?
    - Between different year the names of the columns slightly change!!!


    #### Columns that are important from EIA (2025)
    - Plant ID -
    - Nuclear Unit ID - Some plants may have multiple nuclear units
    - Plant Name
    - Operator Name/ Operator ID ??
    - Plant State
    - Reported Prime mover - How electricity is generated
    - Reported Fuel Type Code - How the fuel is reported by the plant operator
    - MER Fuel Type Code - How the fuel is classified by the EIA
    - Net Generation
    - Fuel consumption

    ### What is our aim?
    - What is the capacity factor change for each power plant from year 0 - Today

    ### How will this be done?
    - Match the ID from EIA-860 with EIA-
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Start: select key fields from EIA 923
    Years that need to be selected:
    - 2025 - Done
    - 2024 - Done
    - 2023 - Done
    - 2022 - Done
    - 2022 - Done
    - 2021 - Done
    - 2020 - Done
    MER Fuel Type Code changes to AER fuel type code
    - 2008
    - 2007: Changes to EIA 906/920/923
    - 2006: Changes to EIA 906/920
    - 2003: Changes to EIA 906
    - 2000: Changes to Historical Data
    Utility: 1970-2000
    Non Utility:
    - 2000: EIA 906
    - 1999: EIA 906
    - 189-1998 EIA 867
    """)
    return


@app.cell
def _(file_path, pd):
    eia_923_2025 = pd.read_excel(file_path + r"\data\eia-923\2025\EIA923_Schedules_2_3_4_5_M_12_2025_20FEB2026.xlsx", sheet_name = 0, header = 5)
    eia_923_2024 = pd.read_excel(file_path + r"\data\eia-923\2024\EIA923_Schedules_2_3_4_5_M_12_2024_Final.xlsx", sheet_name = 0, header = 5)
    eia_923_2023 = pd.read_excel(file_path + r"\data\eia-923\2023\EIA923_Schedules_2_3_4_5_M_12_2023_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2022 = pd.read_excel(file_path + r"\data\eia-923\2022\EIA923_Schedules_2_3_4_5_M_12_2022_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2021 = pd.read_excel(file_path + r"\data\eia-923\2021\EIA923_Schedules_2_3_4_5_M_12_2021_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2020 = pd.read_excel(file_path + r"\data\eia-923\2020\EIA923_Schedules_2_3_4_5_M_12_2020_Final_Revision.xlsx", sheet_name = 0, header = 5)



    eia_923_2025.columns = (
        eia_923_2025.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )
    eia_923_2024.columns = (
        eia_923_2024.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2023.columns = (
        eia_923_2023.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2022.columns = (
        eia_923_2022.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2021.columns = (
        eia_923_2021.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2020.columns = (
        eia_923_2020.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    important_columns = (
        "Plant Id",
        "Nuclear Unit Id",
        "Plant Name",
        "Operator Id",
        "Plant State",
        "Reported Prime Mover",
        "Reported Fuel Type Code",
        "MER Fuel Type Code",
        "AER Fuel Type Code",
        "Total Fuel Consumption Quantity",
        "Total Fuel Consumption MMBtu",
        "Net Generation (Megawatthours)",
        "Year"

    )

    eia_923_2025_key_columns = eia_923_2025.loc[:, eia_923_2025.columns.isin(important_columns)]
    eia_923_2024_key_columns = eia_923_2024.loc[:, eia_923_2024.columns.isin(important_columns)]
    eia_923_2023_key_columns = eia_923_2023.loc[:, eia_923_2023.columns.isin(important_columns)]
    eia_923_2022_key_columns = eia_923_2022.loc[:, eia_923_2022.columns.isin(important_columns)]
    eia_923_2021_key_columns = eia_923_2021.loc[:, eia_923_2021.columns.isin(important_columns)]
    eia_923_2020_key_columns = eia_923_2020.loc[:, eia_923_2020.columns.isin(important_columns)]

    return (
        eia_923_2020,
        eia_923_2020_key_columns,
        eia_923_2021,
        eia_923_2022,
        eia_923_2023,
        eia_923_2024,
        eia_923_2025,
        important_columns,
    )


@app.cell
def _(eia_923_2020_key_columns):
    eia_923_2020_key_columns
    return


@app.cell
def _(file_path, important_columns, pd):
    eia_923_2019 = pd.read_excel(file_path + r"\data\eia-923\2019\EIA923_Schedules_2_3_4_5_M_12_2019_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2018 = pd.read_excel(file_path + r"\data\eia-923\2018\EIA923_Schedules_2_3_4_5_M_12_2018_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2017 = pd.read_excel(file_path + r"\data\eia-923\2017\EIA923_Schedules_2_3_4_5_M_12_2017_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2016 = pd.read_excel(file_path + r"\data\eia-923\2016\EIA923_Schedules_2_3_4_5_M_12_2016_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2015 = pd.read_excel(file_path + r"\data\eia-923\2015\EIA923_Schedules_2_3_4_5_M_12_2015_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2014 = pd.read_excel(file_path + r"\data\eia-923\2014\EIA923_Schedules_2_3_4_5_M_12_2014_Final_Revision.xlsx", sheet_name = 0, header = 5)



    eia_923_2019.columns = (
        eia_923_2019.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )
    eia_923_2018.columns = (
        eia_923_2018.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2017.columns = (
        eia_923_2017.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2016.columns = (
        eia_923_2016.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2015.columns = (
        eia_923_2015.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2014.columns = (
        eia_923_2014.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )


    eia_923_2019_key_columns = eia_923_2019.loc[:, eia_923_2019.columns.isin(important_columns)]
    eia_923_2018_key_columns = eia_923_2018.loc[:, eia_923_2018.columns.isin(important_columns)]
    eia_923_2017_key_columns = eia_923_2017.loc[:, eia_923_2017.columns.isin(important_columns)]
    eia_923_2016_key_columns = eia_923_2016.loc[:, eia_923_2016.columns.isin(important_columns)]
    eia_923_2015_key_columns = eia_923_2015.loc[:, eia_923_2015.columns.isin(important_columns)]
    eia_923_2014_key_columns = eia_923_2014.loc[:, eia_923_2014.columns.isin(important_columns)]

    return (
        eia_923_2014,
        eia_923_2014_key_columns,
        eia_923_2015,
        eia_923_2016,
        eia_923_2017,
        eia_923_2018,
        eia_923_2019,
    )


@app.cell
def _(eia_923_2014_key_columns):
    eia_923_2014_key_columns
    return


@app.cell
def _(file_path, important_columns, pd):
    eia_923_2013 = pd.read_excel(file_path + r"\data\eia-923\2013\EIA923_Schedules_2_3_4_5_2013_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2012 = pd.read_excel(file_path + r"\data\eia-923\2012\EIA923_Schedules_2_3_4_5_M_12_2012_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2011 = pd.read_excel(file_path + r"\data\eia-923\2011\EIA923_Schedules_2_3_4_5_2011_Final_Revision.xlsx", sheet_name = 0, header = 5)
    eia_923_2010 = pd.read_excel(file_path + r"\data\eia-923\2010\EIA923 SCHEDULES 2_3_4_5 Final 2010.xls", sheet_name = 0, header = 5)
    eia_923_2009 = pd.read_excel(file_path + r"\data\eia-923\2009\EIA923 SCHEDULES 2_3_4_5 M Final 2009 REVISED 05252011.XLS", sheet_name = 0, header = 5)
    eia_923_2008 = pd.read_excel(file_path + r"\data\eia-923\2008\eia923December2008.xls", sheet_name = 0, header = 5)



    eia_923_2013.columns = (
        eia_923_2013.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )
    eia_923_2012.columns = (
        eia_923_2012.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2011.columns = (
        eia_923_2011.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2010.columns = (
        eia_923_2010.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2009.columns = (
        eia_923_2009.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    eia_923_2008.columns = (
        eia_923_2008.columns
        .str.replace("\n", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )


    eia_923_2013_key_columns = eia_923_2013.loc[:, eia_923_2013.columns.isin(important_columns)]
    eia_923_2012_key_columns = eia_923_2012.loc[:, eia_923_2012.columns.isin(important_columns)]
    eia_923_2011_key_columns = eia_923_2011.loc[:, eia_923_2011.columns.isin(important_columns)]
    eia_923_2010_key_columns = eia_923_2010.loc[:, eia_923_2010.columns.isin(important_columns)]
    eia_923_2009_key_columns = eia_923_2009.loc[:, eia_923_2009.columns.isin(important_columns)]
    eia_923_2008_key_columns = eia_923_2008.loc[:, eia_923_2008.columns.isin(important_columns)]

    return (
        eia_923_2008,
        eia_923_2009,
        eia_923_2010,
        eia_923_2011,
        eia_923_2012,
        eia_923_2013,
    )


@app.cell
def _():
    # eia_923_key = {
    #     2008: eia_923_2008_key,
    #     2009: eia_923_2009_key,
    #     2010: eia_923_2010_key,
    #     2011: eia_923_2011_key,
    #     2012: eia_923_2012_key,
    #     2013: eia_923_2013_key,
    #     2014: eia_923_2014_key,
    #     2015: eia_923_2015_key,
    #     2016: eia_923_2016_key,
    #     2017: eia_923_2017_key,
    #     2018: eia_923_2018_key,
    #     2019: eia_923_2019_key,
    #     2020: eia_923_2020_key,
    #     2021: eia_923_2021_key,
    #     2022: eia_923_2022_key,
    #     2023: eia_923_2023_key,
    #     2024: eia_923_2024_key,
    #     2025: eia_923_2025_key,
    # }
    return


@app.cell
def _(
    clean_columns,
    eia_923_2008,
    eia_923_2009,
    eia_923_2010,
    eia_923_2011,
    eia_923_2012,
    eia_923_2013,
    eia_923_2014,
    eia_923_2015,
    eia_923_2016,
    eia_923_2017,
    eia_923_2018,
    eia_923_2019,
    eia_923_2020,
    eia_923_2021,
    eia_923_2022,
    eia_923_2023,
    eia_923_2024,
    eia_923_2025,
):
    eia_923_years = {
        2025: eia_923_2025,
        2024: eia_923_2024,
        2023: eia_923_2023,
        2022: eia_923_2022,
        2021: eia_923_2021,
        2020: eia_923_2020,
        2019: eia_923_2019,
        2018: eia_923_2018,
        2017: eia_923_2017,
        2016: eia_923_2016,
        2015: eia_923_2015,
        2014: eia_923_2014,
        2013: eia_923_2013,
        2012: eia_923_2012,
        2011: eia_923_2011,
        2010: eia_923_2010,
        2009: eia_923_2009,
        2008: eia_923_2008,
    }



    for _year in eia_923_years:
        eia_923_years[_year] = clean_columns(eia_923_years[_year])

    important_columns_923 = (
        "plant id",
        "plant name",
        "operator name",
        "operator id",
        "generator id",
        "net generation year to date"
    )

    eia_923_key_columns = {}


    for _year, _df in eia_923_years.items():
        eia_923_key_columns[_year] = _df.loc[:, _df.columns.isin(important_columns_923)]

    eia_923_2025_key_columns = eia_923_2025.loc[:, eia_923_2025.columns.isin(important_columns_923)]
    eia_923_2024_key_columns = eia_923_2024.loc[:, eia_923_2024.columns.isin(important_columns_923)]
    eia_923_2023_key_columns = eia_923_2023.loc[:, eia_923_2023.columns.isin(important_columns_923)]
    eia_923_2022_key_columns = eia_923_2022.loc[:, eia_923_2022.columns.isin(important_columns_923)]
    eia_923_2021_key_columns = eia_923_2021.loc[:, eia_923_2021.columns.isin(important_columns_923)]
    eia_923_2020_key_columns = eia_923_2020.loc[:, eia_923_2020.columns.isin(important_columns_923)]
    eia_923_2019_key_columns = eia_923_2019.loc[:, eia_923_2019.columns.isin(important_columns_923)]
    eia_923_2018_key_columns = eia_923_2018.loc[:, eia_923_2018.columns.isin(important_columns_923)]
    eia_923_2017_key_columns = eia_923_2017.loc[:, eia_923_2017.columns.isin(important_columns_923)]
    eia_923_2016_key_columns = eia_923_2016.loc[:, eia_923_2016.columns.isin(important_columns_923)]
    eia_923_2015_key_columns = eia_923_2015.loc[:, eia_923_2015.columns.isin(important_columns_923)]
    eia_923_2014_key_columns = eia_923_2014.loc[:, eia_923_2014.columns.isin(important_columns_923)]
    eia_923_2013_key_columns = eia_923_2013.loc[:, eia_923_2013.columns.isin(important_columns_923)]
    eia_923_2012_key_columns = eia_923_2012.loc[:, eia_923_2012.columns.isin(important_columns_923)]
    eia_923_2011_key_columns = eia_923_2011.loc[:, eia_923_2011.columns.isin(important_columns_923)]
    eia_923_2010_key_columns = eia_923_2010.loc[:, eia_923_2010.columns.isin(important_columns_923)]
    eia_923_2009_key_columns = eia_923_2009.loc[:, eia_923_2009.columns.isin(important_columns_923)]
    eia_923_2008_key_columns = eia_923_2008.loc[:, eia_923_2008.columns.isin(important_columns_923)]

    eia_923_2025_key_columns.rename(columns = {"net generation year to date": "net generation to data 2025"})
    eia_923_2024_key_columns.rename(columns = {"net generation year to date": "net generation to data 2024"})
    eia_923_2023_key_columns.rename(columns = {"net generation year to date": "net generation to data 2023"})
    eia_923_2022_key_columns.rename(columns = {"net generation year to date": "net generation to data 2022"})
    eia_923_2021_key_columns.rename(columns = {"net generation year to date": "net generation to data 2021"})
    eia_923_2020_key_columns.rename(columns = {"net generation year to date": "net generation to data 2020"})
    eia_923_2019_key_columns.rename(columns = {"net generation year to date": "net generation to data 2019"})
    eia_923_2018_key_columns.rename(columns = {"net generation year to date": "net generation to data 2018"})
    eia_923_2017_key_columns.rename(columns = {"net generation year to date": "net generation to data 2017"})
    eia_923_2016_key_columns.rename(columns = {"net generation year to date": "net generation to data 2016"})
    eia_923_2015_key_columns.rename(columns = {"net generation year to date": "net generation to data 2015"})
    eia_923_2014_key_columns.rename(columns = {"net generation year to date": "net generation to data 2014"})
    eia_923_2013_key_columns.rename(columns = {"net generation year to date": "net generation to data 2013"})
    eia_923_2012_key_columns.rename(columns = {"net generation year to date": "net generation to data 2012"})
    eia_923_2011_key_columns.rename(columns = {"net generation year to date": "net generation to data 2011"})
    eia_923_2010_key_columns.rename(columns = {"net generation year to date": "net generation to data 2010"})
    eia_923_2009_key_columns.rename(columns = {"net generation year to date": "net generation to data 2009"})
    eia_923_2008_key_columns.rename(columns = {"net generation year to date": "net generation to data 2008"})

    return eia_923_2014_key_columns, eia_923_2020_key_columns


@app.cell
def _(
    clean_columns,
    eia_860_2014,
    eia_860_2015,
    eia_860_2016,
    eia_860_2017,
    eia_860_2018,
    eia_860_2019,
    eia_860_2020,
    eia_860_2021,
    eia_860_2022,
    eia_860_2023,
    eia_860_2024,
):
    eia_860_years = {
        # 2025: eia_860_2025,
        2024: eia_860_2024,
        2023: eia_860_2023,
        2022: eia_860_2022,
        2021: eia_860_2021,
        2020: eia_860_2020,
        2019: eia_860_2019,
        2018: eia_860_2018,
        2017: eia_860_2017,
        2016: eia_860_2016,
        2015: eia_860_2015,
        2014: eia_860_2014#,
        # 2013: eia_923_2013,
        # 2012: eia_923_2012,
        # 2011: eia_923_2011,
        # 2010: eia_923_2010,
        # 2009: eia_923_2009,
        # 2008: eia_923_2008,
    }

    for _year in eia_860_years:
        eia_860_years[_year] = clean_columns(eia_860_years[_year])

    important_columns_860 = (
        "plant code",
        "plant name",
        "generator id",
        "utility name",
        "utility id",
        "nameplate capacity (mw)"
    )


    eia_860_2024_key_columns = eia_860_2024.loc[:, eia_860_2024.columns.isin(important_columns_860)]
    eia_860_2023_key_columns = eia_860_2023.loc[:, eia_860_2023.columns.isin(important_columns_860)]
    eia_860_2022_key_columns = eia_860_2022.loc[:, eia_860_2022.columns.isin(important_columns_860)]
    eia_860_2021_key_columns = eia_860_2021.loc[:, eia_860_2021.columns.isin(important_columns_860)]
    eia_860_2020_key_columns = eia_860_2020.loc[:, eia_860_2020.columns.isin(important_columns_860)]
    eia_860_2019_key_columns = eia_860_2019.loc[:, eia_860_2019.columns.isin(important_columns_860)]
    eia_860_2018_key_columns = eia_860_2018.loc[:, eia_860_2018.columns.isin(important_columns_860)]
    eia_860_2017_key_columns = eia_860_2017.loc[:, eia_860_2017.columns.isin(important_columns_860)]
    eia_860_2016_key_columns = eia_860_2016.loc[:, eia_860_2016.columns.isin(important_columns_860)]
    eia_860_2015_key_columns = eia_860_2015.loc[:, eia_860_2015.columns.isin(important_columns_860)]
    eia_860_2014_key_columns = eia_860_2014.loc[:, eia_860_2014.columns.isin(important_columns_860)]



    eia_860_2024_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2024", "plant code": "plant id"}, inplace = True)
    eia_860_2023_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2023", "plant code": "plant id"}, inplace = True)
    eia_860_2022_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2022", "plant code": "plant id"}, inplace = True)
    eia_860_2021_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2021", "plant code": "plant id"}, inplace = True)
    eia_860_2020_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2020", "plant code": "plant id"}, inplace = True)
    eia_860_2019_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2019", "plant code": "plant id"}, inplace = True) ## utility id maybe an issue due to type
    eia_860_2018_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2018", "plant code": "plant id"}, inplace = True)
    eia_860_2017_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2017", "plant code": "plant id"}, inplace = True)
    eia_860_2016_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2016", "plant code": "plant id"}, inplace = True)
    eia_860_2015_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2015", "plant code": "plant id"}, inplace = True)
    eia_860_2014_key_columns.rename(columns = {"nameplate capacity (mw)": "nameplate capacity (mw) 2014", "plant code": "plant id"}, inplace = True)## utility id maybe an issue due to type
    return


if __name__ == "__main__":
    app.run()
