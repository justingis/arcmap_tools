#-------------------------------------------------------------------------------
# Name:        Basic Erase
# Purpose:     Allows for the same functionality as the built-in Erase tool without
#              requiring the Advanced license (works with Basic license) 
#
# Author:      Justin Hawley (justin@orcagis.com)
#
# Created:     07/15/2022
#
# Interpreter: C:\Python27\ArcGIS10.8\python.exe
#-------------------------------------------------------------------------------

import arcpy

def basic_erase():
    input_layer = arcpy.GetParameter(0)
    erase_layer = arcpy.GetParameter(1)
    output_feature_class = arcpy.GetParameter(2)

    # union input_layer and erase_layer
    union_layer = arcpy.Union_analysis(in_features="{} #;{} #".format(erase_layer, input_layer), out_feature_class=output_feature_class, join_attributes="ALL", cluster_tolerance="", gaps="GAPS")
    union_layer = arcpy.MakeFeatureLayer_management(union_layer,"union_layer")

    field_name = 'FID_{}'.format(erase_layer)
    where_clause = '{} > -1'.format(field_name)

    arcpy.SelectLayerByAttribute_management(in_layer_or_view=union_layer, selection_type='NEW_SELECTION', where_clause=where_clause)
    arcpy.DeleteRows_management(union_layer)

def main():
    basic_erase()

if __name__ == '__main__':
    main()