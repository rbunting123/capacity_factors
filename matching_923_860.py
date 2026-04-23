import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Question: How can I match Power Plant Generators between 923 and 860 datasets?
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import openpyxl
    import xlrd
    file_path = r"C:\Repository Folder\capacity_factors"
    return file_path, mo, pd


@app.cell
def _(file_path, pd):
    eia_923_2025 = pd.read_excel(file_path + r"\data\eia-923\2025\EIA923_Schedules_2_3_4_5_M_12_2025_20FEB2026.xlsx", sheet_name = 6, header = 4)
    eia_923_2024 = pd.read_excel(file_path + r"\data\eia-923\2024\EIA923_Schedules_2_3_4_5_M_12_2024_Final.xlsx", sheet_name = 6, header = 4)
    eia_923_2023 = pd.read_excel(file_path + r"\data\eia-923\2023\EIA923_Schedules_2_3_4_5_M_12_2023_Final_Revision.xlsx", sheet_name = 6, header = 4)
    eia_923_2022 = pd.read_excel(file_path + r"\data\eia-923\2022\EIA923_Schedules_2_3_4_5_M_12_2022_Final_Revision.xlsx", sheet_name = 6, header = 4)
    eia_923_2021 = pd.read_excel(file_path + r"\data\eia-923\2021\EIA923_Schedules_2_3_4_5_M_12_2021_Final_Revision.xlsx", sheet_name = 6, header = 4)
    eia_923_2020 = pd.read_excel(file_path + r"\data\eia-923\2020\EIA923_Schedules_2_3_4_5_M_12_2020_Final_Revision.xlsx", sheet_name = 6, header = 4)

    # eia_923_2019 = pd.read_excel(file_path + r"\data\eia-923\2019\EIA923_Schedules_2_3_4_5_M_12_2019_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2018 = pd.read_excel(file_path + r"\data\eia-923\2018\EIA923_Schedules_2_3_4_5_M_12_2018_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2017 = pd.read_excel(file_path + r"\data\eia-923\2017\EIA923_Schedules_2_3_4_5_M_12_2017_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2016 = pd.read_excel(file_path + r"\data\eia-923\2016\EIA923_Schedules_2_3_4_5_M_12_2016_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2015 = pd.read_excel(file_path + r"\data\eia-923\2015\EIA923_Schedules_2_3_4_5_M_12_2015_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2014 = pd.read_excel(file_path + r"\data\eia-923\2014\EIA923_Schedules_2_3_4_5_M_12_2014_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2013 = pd.read_excel(file_path + r"\data\eia-923\2013\EIA923_Schedules_2_3_4_5_2013_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2012 = pd.read_excel(file_path + r"\data\eia-923\2012\EIA923_Schedules_2_3_4_5_M_12_2012_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2011 = pd.read_excel(file_path + r"\data\eia-923\2011\EIA923_Schedules_2_3_4_5_2011_Final_Revision.xlsx", sheet_name = 0, header = 5)
    # eia_923_2010 = pd.read_excel(file_path + r"\data\eia-923\2010\EIA923 SCHEDULES 2_3_4_5 Final 2010.xls", sheet_name = 0, header = 5)
    # eia_923_2009 = pd.read_excel(file_path + r"\data\eia-923\2009\EIA923 SCHEDULES 2_3_4_5 M Final 2009 REVISED 05252011.XLS", sheet_name = 0, header = 5)
    # eia_923_2008 = pd.read_excel(file_path + r"\data\eia-923\2008\eia923December2008.xls", sheet_name = 0, header = 5)


    return (eia_923_2025,)


@app.cell
def _(eia_923_2025):
    eia_923_2025
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
