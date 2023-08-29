import arcpy

# Path to arcpy
input_path = r"D:\SEM III\Programming_3\P1_run_Python_Scripts\Practical_1_ProProject\01_Running_Python_Scripts.gdb\Wilson_Schools"

# Path to output
output_path = r"D:\SEM III\Programming_3\P1_run_Python_Scripts\Practical_1_ProProject\output.gdb\buffer_2"

#buffer distance
distance = '500 meters'

arcpy.analysis.Buffer(input_path,output_path,distance);

print("process completed")