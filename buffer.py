import arcpy

arcpy.env.workspace = r"D:\SEM III\Programming_3\P1_run_Python_Scripts\Practical_1_ProProject\Practical_1_ProProject\01_Running_Python_Scripts.gdb"


arcpy.analysis.Buffer("Wilson_Schools","Wilson_School_Buffer", "500 meters")
print("process complete")