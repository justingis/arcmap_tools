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
    output_feature_class = arcpy.GetParameter(1)

def main():
    pass

if __name__ == '__main__':
    main()