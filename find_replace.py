#-------------------------------------------------------------------------------
# Name:        Find & Replace
# Purpose:     Finds all instances of a text pattern (regular expression) and 
# updates the layers attribute table.  If a text value is found, all instances 
# of that text value are replaced in the record.
#
# Author:      Justin Hawley (justin@orcagis.com)
#
# Created:     07/03/2022
#
# Interpreter: C:\Python27\ArcGIS10.8\python.exe
#-------------------------------------------------------------------------------

import arcpy
import re

# add option to ignore case?

# allows user to enter a regular expression pattern
def find(pat, text):
    match = re.search(pat, text)
    if match:
        return match.group()
    else:
        return None

def main():
    input_layer = arcpy.GetParameter(0)
    #input_layer = arcpy.MakeFeatureLayer_management(r'C:\ws_consulting\gdb\input.gdb\counties_test','counties_test') # temporary, for dev only
    find_val = arcpy.GetParameterAsText(1) # '.*Pow.*' may be a text value or regular expression
    replace_val = arcpy.GetParameterAsText(2)
    #ignore_case = False # not used yet
    update_layer = arcpy.GetParameter(3)
    row_update_count = 0

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
                    arcpy.AddMessage('Found instance of {}'.format(find_val))
                    if update_layer:
                        row[index] = field_val
                        cursor.updateRow(row)
                        row_update_count += 1
    arcpy.AddMessage('\nUpdated {} rows'.format(row_update_count))

if __name__ == '__main__':
    main()