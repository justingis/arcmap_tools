#-------------------------------------------------------------------------------
# Name:        Find & Replace
# Purpose:     Finds all instances of a text pattern and updates the attribute
#    table accordingly
#
# Author:      Justin Hawley (justin@orcagis.com)
#
# Created:     07/03/2022
#
# Interpreter: C:\Python27\ArcGIS10.8\python.exe
#-------------------------------------------------------------------------------

import arcpy
import re

def find(pat, text):
    match = re.search(pat, text)
    if match:
        print(match.group())
    else:
        print('not found')

def main():
    #input_layer = arcpy.GetParameter(0)
    input_layer = arcpy.MakeFeatureLayer_management(r'C:\ws_consulting\gdb\input.gdb\USA_States_Generalized','USA_States_Generalized') # temporary, for dev only
    desc = arcpy.Describe(input_layer)
    field_list = desc.fields
    field_names = [f.name for f in field_list]

    with arcpy.da.UpdateCursor(input_layer, field_names) as cursor:
        for row in cursor:
            for field in field_list:
                if field.type == 'String':
                    index = field_names.index(field.name)
                    print(row[index])


if __name__ == '__main__':
    main()