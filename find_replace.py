#-------------------------------------------------------------------------------
# Name:        Find & Replace
# Purpose:     Finds all instances of a regular expression text pattern 
# (in text fields) and updates the attribute table accordingly
#
# Author:      Justin Hawley (justin@orcagis.com)
#
# Created:     07/03/2022
#
# Interpreter: C:\Python27\ArcGIS10.8\python.exe
#-------------------------------------------------------------------------------

import arcpy
import re

# allows user to enter a regular expression pattern
def find(pat, text):
    match = re.search(pat, text)
    if match:
        return match.group()
    else:
        return None

def main():
    #input_layer = arcpy.GetParameter(0)
    input_layer = arcpy.MakeFeatureLayer_management(r'C:\ws_consulting\gdb\input.gdb\counties_test','counties_test') # temporary, for dev only
    find_val = 'Howard'
    replace_val = 'Zoward'
    desc = arcpy.Describe(input_layer)
    field_list = desc.fields
    
    # get list of fields name
    field_names = []
    for field in field_list:
        if field.type == 'String':
            field_names.append(field.name)

    with arcpy.da.UpdateCursor(input_layer, field_names) as cursor:
        for row in cursor:
            for name in field_names:
                index = field_names.index(name)
                field_val = row[index]
                found = find(find_val, field_val)
                if found:
                    field_val = field_val.replace(find_val, replace_val)
                    print(field_val)
                    
if __name__ == '__main__':
    main()