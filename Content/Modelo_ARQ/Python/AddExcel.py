import unreal 
import pandas as pd
import openpyxl

datap = pd.read_csv("D:\\Unreal Projects\\PROGRUA_MOV\\VR_3DPC\\Content\\Python\\ProjectData.csv")

# print (datap)

# DT = unreal.DataTable()
# Comp = DT.import_key_field()

# Importar DataTable desde el content browser
# EAL = unreal.EditorAssetLibrary

# DataTablePath = EAL.list_assets('/Game/Python/')

# DataWall = EAL.load_asset('/Game/Python/DataWall')

# print (DataWall)

# Importar informacion desde cvs
CIT = unreal.CSVImportType

CIT.ECSV_DATA_TABLE()
# UDTFL = unreal.DataTableFunctionLibrary
# UDTFL.fill_data_table_from_csv_string(DataWall,"D:\\Unreal Projects\\PROGRUA_MOV\\VR_3DPC\\Content\\Python\\ProjectData.csv")
