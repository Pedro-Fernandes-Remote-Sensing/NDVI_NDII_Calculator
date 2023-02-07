# SAPROG MCSIG G20201439 PEDRO FERNANDES 
import arcpy
import os
from arcpy.sa import *

# APRESENTAÇÃO DO SCRIPT
print("Welcome to the Satelite Index calculator.\n")
print("This script takes different satelite images representing different Frequency Bands and calculates different indexes such as NDVI and NBR.\n")
print("Please note that, in the case of Before/After fire studies, the path used to store the images must contain a 'BEFORE' folder and an 'AFTER' folder.\n")

# DEFINIÇÃO DO WORKSPACE E CONFIRMAÇÃO DO MESMO
def WS_DEF(): 
    workspace_input = input("Please enter the full path (copy adress as text) to the folders containing the satelite images:\n")
    print("\nIs this the correct path? {workspace_input}")
    def WS_CONF():
        workspace_confirmation = input("Y/N\n")
        while workspace_confirmation != "Y" and workspace_confirmation != "y":
            if workspace_confirmation == "N" or workspace_confirmation == "n":
                WS_DEF();
                break
            if workspace_confirmation != "N" and workspace_confirmation != "n":
                print("Please enter either 'Y' or 'N'.")
                WS_CONF();
                break
        if workspace_confirmation == "Y" or workspace_confirmation == "y":
            arcpy.env.workspace = workspace_input
            print(" \n{arcpy.env.workspace} was defined as the current workspace.")
    WS_CONF();
    
# LISTAGEM DOS FOLDERS E CONFIRMAÇÃO
def LIST_FOLDERS():
    Folder_List = arcpy.ListFiles()
    print("\nAre these the two folders (Before/After) you want to use?\n")
    for i in Folder_List:
        print("{i}")
    def FOLDER_CONF():
        Folder_Confirmation = input("\nY/N \n")
        while Folder_Confirmation != "Y" and Folder_Confirmation != "y":
            if Folder_Confirmation == "N" or Folder_Confirmation == "n":
                print("Please remake your folders and re-run this script.")
                sys.exit()
            if Folder_Confirmation != "N" and Folder_Confirmation != "n":
                print("Please enter either 'Y' or 'N'.")
                FOLDER_CONF();
                break
        if Folder_Confirmation == "Y" or Folder_Confirmation == "y":
                print("\nThe folders have been confirmed.")
    FOLDER_CONF();

# DEFINIÇÃO DE CÁLCULO ANTES/DEPOIS OU NÃO              
def BA_OR_NOT():
    def BA_CONF():
        global Ba_Conf
        Ba_Conf = input("\nAre you trying to calculate a before and after index?\nY/N \n")
        if Ba_Conf == "Y" or Ba_Conf == "y":
            LIST_FOLDERS();
            BEFORE_FOLDER();
            AFTER_FOLDER();
            LIST_FILES()
            return
        if Ba_Conf == "N" or Ba_Conf == "n":
            print("Normal calculation will proceed.\n")
            ANY_FOLDER();
            LIST_FILES()
            return
        if Ba_Conf != "N" or Ba_Conf != "n" or Ba_Conf != "Y" or Ba_Conf != "y":
            print("Please enter either 'Y' or 'N'.")
            BA_CONF();
            return
    BA_CONF();

# DEFINIÇÃO DA PASTA "ANTES"
def BEFORE_FOLDER():
    Before_Path_Input = input("\nPlease enter the path to the BEFORE folder (copy as text).\n")
    print("\nIs {Before_Path_Input} the correct path?")
    def BEFORE_CONF():
        before_confirmation = input("Y/N\n")
        while before_confirmation != "Y" and before_confirmation != "y":
            if before_confirmation == "N" or before_confirmation == "n":
                BEFORE_FOLDER();
                break
            if before_confirmation != "N" and before_confirmation != "n":
                print("Please enter either 'Y' or 'N'.")
                BEFORE_CONF();
                break
        if before_confirmation == "Y" or before_confirmation == "y":
            global Before_Path
            Before_Path = Before_Path_Input
            print(" \n{Before_Path} was defined as the BEFORE folder.\n")
    BEFORE_CONF();

# DEFINIÇÃO DA PASTA "DEPOIS"
def AFTER_FOLDER():
    After_Path_Input = input("\nPlease enter the path to the AFTER folder (copy as text).\n")
    print("\nIs {After_Path_Input} the correct path?")
    def AFTER_CONF():
        after_confirmation = input("Y/N\n")
        while after_confirmation != "Y" and after_confirmation != "y":
            if after_confirmation == "N" or after_confirmation == "n":
                AFTER_FOLDER();
                break
            if after_confirmation != "N" and after_confirmation != "n":
                print("Please enter either 'Y' or 'N'.")
                AFTER_CONF();
                break
        if after_confirmation == "Y" or after_confirmation == "y":
            global After_Path
            After_Path = After_Path_Input
            print("\n{After_Path} was defined as the AFTER folder.\n")
    AFTER_CONF();

# DEFINIÇÃO DA PASTA A UTILIZAR NO CASO DE NÃO HAVER ANTES/DEPOIS
def ANY_FOLDER():
    Path_Input = input("\nPlease enter the path to folder containing the files (copy as text).\n")
    print("\nIs {Path_Input} the correct path?")
    def PATH_CONF():
        path_confirmation = input("Y/N\n")
        while path_confirmation != "Y" and path_confirmation != "y":
            if path_confirmation == "N" or path_confirmation == "n":
                ANY_FOLDER();
                break
            if path_confirmation != "N" and path_confirmation != "n":
                print("Please enter either 'Y' or 'N'.")
                PATH_CONF();
                break
        if path_confirmation == "Y" or path_confirmation == "y":
            global Folder_Path
            Folder_Path = Path_Input
            print("\n{Folder_Path} was defined as the folder containing the files.\n")
    PATH_CONF();

# LISTAGEM DE FICHEIROS E CONFIRMAÇÃO      
def LIST_FILES():
    if Ba_Conf == 'Y' or Ba_Conf == 'y':
        File_List = arcpy.da.Walk(datatype="RasterDataset")
        print("\nAre these the files (Satelite Raster Datasets) that you want to use?\n")
        for dir_path, dir_names, file_names in File_List:
            for filename in file_names:
                print(filename)
        def FILE_CONF():
            Files_Confirmation = input("\nY/N \n")
            while Files_Confirmation != "Y" and Files_Confirmation != "y":
                if Files_Confirmation == "N" or Files_Confirmation == "n":
                    print("Please rename your files (or find some) and re-run this script.")
                    sys.exit()
                if Files_Confirmation != "N" and Files_Confirmation != "n":
                    print("Please enter either 'Y' or 'N'.")
                    FILE_CONF();
                    break
            if Files_Confirmation == "Y" or Files_Confirmation == "y":
                    print("\nThe files have been confirmed.")
        FILE_CONF();
    if Ba_Conf == 'N' or Ba_Conf == 'n':
        arcpy.env.workspace = Folder_Path
        File_List = arcpy.da.Walk(datatype="RasterDataset")
        print("\nAre these the files (Satelite Raster Datasets) that you want to use?\n")
        for dir_path, dir_names, file_names in File_List:
            for filename in file_names:
                print(filename)
        def FILE_CONF():
            Files_Confirmation = input("\nY/N \n")
            while Files_Confirmation != "Y" and Files_Confirmation != "y":
                if Files_Confirmation == "N" or Files_Confirmation == "n":
                    print("Please remake your folders and re-run this script.")
                    sys.exit()
                if Files_Confirmation != "N" and Files_Confirmation != "n":
                    print("Please enter either 'Y' or 'N'.")
                    FILE_CONF();
                    break
            if Files_Confirmation == "Y" or Files_Confirmation == "y":
                    print("\nThe files have been confirmed.")
        FILE_CONF();

# VERIFICAÇÃO DE LICENÇA ARCGIS 
def LICENSE_VERIFICATION():
    print("\nRaster analysis requires a 'Spatial Analyst' license. Verification will now be run.")
    if arcpy.CheckExtension("Spatial") == "Available":
        print("\nLicense has been verified.\n")
    else:
        print("\nLicense is unavailable. Purchase a Spatial Analyst License and re-run the script.\n")
        sys.exit()

# ESCOLHA DO ÍNDICE A CALCULAR
def INDEX_CHOICE():
    Index = input("\nWhich index do you want to calculate? NDVI, NBR\n")
    while Index not in {"NDVI","ndvi","NBR","nbr"}:
        Index = str.casefold(input("Please awnser with any of the indexes (NDVI, NBR):\n"))
    if Index == "NDVI" or Index == "ndvi":
        LICENSE_VERIFICATION()
        BA_OR_NOT();
        LOCATE_BANDS_NDVI();
        CHECKIN();
        CALC_NDVI();
        CHECKOUT();
    if Index == "NBR" or Index == "nbr":
        LICENSE_VERIFICATION()
        BA_OR_NOT();
        LOCATE_BANDS_NBR();
        CHECKIN();
        CALC_NBR();
        CHECKOUT();

# LOCALIZAÇÃO DAS BANDAS PARA CÁLCULO DE NDVI
def LOCATE_BANDS_NDVI():
    if Ba_Conf == 'Y' or Ba_Conf == 'y':
        print("NDVI calculation requires a Red frequency band and a Near Infrared frequency band file.")
        print("Remenber to please rename your files 'NIF' for Near Infrared Frequency and 'R' for Red frequency.\n")
        print("Temporarily changing workspace to {Before_Path} \n")
        arcpy.env.workspace = Before_Path
        print("Finding BEFORE NIF file.\n")
        File_List = os.listdir(Before_Path)
        for i in File_List:
            if i == 'NIF.tiff':
                global NIF_Before_Raster
                NIF_Before_Raster = os.path.join(Before_Path,i)
        print("Found {NIF_Before_Raster}\n")
        print("Finding BEFORE R file.\n")
        for i in File_List:
            if i == 'R.tiff':
                global R_Before_Raster
                R_Before_Raster = os.path.join(Before_Path,i)
        print("Found {R_Before_Raster}\n")
        print("Temporarily changing workspace to {After_Path} \n")
        arcpy.env.workspace = After_Path
        print("Finding AFTER NIF file.\n")
        File_List_2 = os.listdir(After_Path)
        for i in File_List_2:
            if i == 'NIF.tiff':
                global NIF_After_Raster
                NIF_After_Raster = os.path.join(After_Path,i)
        print("Found {NIF_After_Raster}\n")
        print("Finding AFTER R file.\n")
        for i in File_List_2:
            if i == 'R.tiff':
                global R_After_Raster
                R_After_Raster = os.path.join(After_Path,i)
        print("Found {R_After_Raster}\n")
    if Ba_Conf == 'N' or Ba_Conf == 'n':
        print("NDVI calculation requires a Red frequency band and a Near Infrared frequency band file.")
        print("Remenber to please rename your files 'NIF' for Near Infrared Frequency and 'R' for Red frequency.")
        print("Finding NIF file.\n")
        File_List_3 = os.listdir(Folder_Path)
        for i in File_List_3:
            if i == 'NIF.tiff':
                global NIF_Raster
                NIF_Raster = os.path.join(Folder_Path,i)
        print("Found {NIF_Raster}\n")
        print("Finding R file.\n")
        for i in File_List_3:
            if i == 'R.tiff':
                global R_Raster
                R_Raster = os.path.join(Folder_Path,i)
        print("Found {R_Raster}\n")
 
# CÁLCULO DO NDVI      
def CALC_NDVI():
    if Ba_Conf == 'Y' or Ba_Conf == 'y':
        print("Calculating BEFORE NDVI.\n")
        arcpy.env.workspace = Before_Path
        NDVI_Before_Raster = RasterCalculator([NIF_Before_Raster,R_Before_Raster],["x","y"],"(x-y)/(x+y)")
        NDVI_Before_Raster.save(os.path.join(Before_Path,"NDVI.tif"))
        print("BEFORE NDVI was calculated. It has been exported to {Before_Path}\n")
        print("Calculating AFTER NDVI.\n")
        arcpy.env.workspace = After_Path
        NDVI_After_Raster = RasterCalculator([NIF_After_Raster,R_After_Raster],["x","y"],"(x-y)/(x+y)")
        NDVI_After_Raster.save(os.path.join(After_Path,"NDVI.tif"))
        print("AFTER NDVI was calculated. It has been exported to {After_Path}\n")
    if Ba_Conf == 'N' or Ba_Conf == 'n':
        print("Calculating NDVI.\n")
        arcpy.env.workspace = Folder_Path
        NDVI_Raster = RasterCalculator([NIF_Raster,R_Raster],["x","y"],"(x-y)/(x+y)")
        NDVI_Raster.save(os.path.join(Folder_Path,"NDVI.tif"))
        print("NDVI was calculated. It has been exported to {Folder_Path}\n")

# LOCALIZAÇÃO DAS BANDAS PARA O CÁLCULO NBR        
def LOCATE_BANDS_NBR():
    if Ba_Conf == 'Y' or Ba_Conf == 'y':
        print("NBR calculation requires an SWIR image composite file and a Near Infrared frequency band file.")
        print("Remenber to please rename your files 'SWIR' for short wave infrared file and 'NIF' for Near Infrared frequency.")        
        print("Temporarily changing workspace to {Before_Path} \n")
        arcpy.env.workspace = Before_Path
        print("Finding BEFORE NIF file.\n")
        File_List = os.listdir(Before_Path)
        for i in File_List:
            if i == 'NIF.tiff':
                global NIF_Before_Raster
                NIF_Before_Raster = os.path.join(Before_Path,i)
        print("Found {NIF_Before_Raster}\n")
        
        print("Finding BEFORE SWIR file.\n")
        for i in File_List:
            if i == 'SWIR.tiff':
                global SWIR_Before_Raster
                SWIR_Before_Raster = os.path.join(Before_Path,i)
        print("Found {SWIR_Before_Raster}\n")
        
        print("Temporarily changing workspace to {After_Path} \n")
        arcpy.env.workspace = After_Path
        print("Finding AFTER NIF file.\n")
        File_List_2 = os.listdir(After_Path)
        for i in File_List_2:
            if i == 'NIF.tiff':
                global NIF_After_Raster
                NIF_After_Raster = os.path.join(After_Path,i)
        print("Found {NIF_After_Raster}\n")
        
        print("Finding AFTER SWIR file.\n")
        for i in File_List_2:
            if i == 'SWIR.tiff':
                global SWIR_After_Raster
                SWIR_After_Raster = os.path.join(After_Path,i)
        print("Found {SWIR_After_Raster}\n")
        
    if Ba_Conf == 'N' or Ba_Conf == 'n':
        print("NBR calculation requires an SWIR image composite file and a Near Infrared frequency band file.")
        print("Remenber to please rename your files 'SWIR' for short wave infrared file and 'NIF' for Near Infrared frequency.")
        print("Finding NIF file.\n")
        File_List_3 = os.listdir(Folder_Path)
        for i in File_List_3:
            if i == 'NIF.tiff':
                global NIF_Raster
                NIF_Raster = os.path.join(Folder_Path,i)
        print("Found {NIF_Raster}\n")
        
        print("Finding SWIR file.\n")
        for i in File_List_3:
            if i == 'SWIR.tiff':
                global SWIR_Raster
                SWIR_Raster = os.path.join(Folder_Path,i)
        print("Found {SWIR_Raster}\n")

# CÁLCULO DO ÍNDICE NBR    
def CALC_NBR():
    if Ba_Conf == 'Y' or Ba_Conf == 'y':
        print("Calculating BEFORE NBR.\n")
        arcpy.env.workspace = Before_Path
        global NBR_Before_Raster
        NBR_Before_Raster = RasterCalculator([NIF_Before_Raster,SWIR_Before_Raster],["x","y"],"(x-y)/(x+y)")
        NBR_Before_Raster.save(os.path.join(Before_Path,"NBR.tif"))
        print("BEFORE NBR was calculated. It has been exported to {Before_Path}\n")
        print("Calculating AFTER NBR.\n")
        arcpy.env.workspace = After_Path
        global NBR_After_Raster
        NBR_After_Raster = RasterCalculator([NIF_After_Raster,SWIR_After_Raster],["x","y"],"(x-y)/(x+y)")
        NBR_After_Raster.save(os.path.join(After_Path,"NBR.tif"))
        print("AFTER NBR was calculated. It has been exported to {After_Path}\n")
        Index = input("Would you like to calculate the difference between NBR? (NBR Before - NBR After)\nY/N\n")
        while Index not in {"Y","y","N","n"}:
            Index = str.casefold(input("Please awnser with 'Y' or 'N':\n"))
        if Index == 'Y' or Index == 'y':
            File_List = os.listdir(Before_Path)
            for i in File_List:
                if i == 'NBR.tiff':
                    NBR_Before_Raster = os.path.join(Before_Path,i)
            File_List = os.listdir(After_Path)
            for i in File_List:
                if i == 'NBR.tiff':
                   NBR_After_Raster = os.path.join(After_Path,i)
            NBR_Diff_Raster = RasterCalculator([NBR_Before_Raster,NBR_After_Raster],["x","y"],"(x-y)")
            NBR_Diff_Raster.save(os.path.join(After_Path,"NBR_Diff.tif"))
            print("NBR Diference was calculated. It has been exported to {After_Path}\n")
    if Ba_Conf == 'N' or Ba_Conf == 'n':
        print("Calculating NBR.\n")
        arcpy.env.workspace = Folder_Path
        NBR_Raster = RasterCalculator([NIF_Raster,SWIR_Raster],["x","y"],"(x-y)/(x+y)")
        NBR_Raster.save(os.path.join(Folder_Path,"NBR.tif"))
        print("NBR was calculated. It has been exported to {Folder_Path}\n")

# CHECKOUT DA LICENÇA ARCGIS
def CHECKOUT():
    arcpy.CheckOutExtension("Spatial")

# CHECKIN DA LICENÇA ARCGIS
def CHECKIN():
    arcpy.CheckInExtension("Spatial")

# FUNÇÃO PARA COMEÇAR O PROGRAMA
def START():
    WS_DEF()
    INDEX_CHOICE()
     
               

#START PROGRAM
if __name__=='__main__':
    START()
