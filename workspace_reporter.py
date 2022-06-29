#-------------------------------------------------------------------------------
# Name:        Workspace Reporter
# Purpose:     Recursively walks an input folder location or geodatabase (workspace) and generates 
#   a csv file of the schema (field name, field type, field length) for each file or feature class
#
# Author:      Justin Hawley (justin@orcagis.com)
#
# Created:     06/28/2022
#
# Interpreter: C:\Python27\ArcGIS10.8\python.exe
#-------------------------------------------------------------------------------

import arcpy, csv, os

def main():

    workspace = 'C:/Users/justinhawley/Desktop/input'
    output_folder = 'C:/Users/justinhawley/Desktop/output'

    for dirpath, dirnames, filenames in arcpy.da.Walk(workspace):
        for filename in filenames:
            desc = arcpy.Describe(os.path.join(dirpath, filename))
            featureclass = desc.catalogpath
            fields = arcpy.ListFields(featureclass)
            output_csv = os.path.join(output_folder, desc.name + '.csv')
            with open(output_csv, 'wb') as csv_table:
                csv_writer = csv.writer(csv_table)
                csv_writer.writerow(['Name', 'Type', 'Length'])
                for field in fields:
                    csv_writer.writerow([field.name, field.type, field.length])
            print(desc.name)

    print('\nFinished...')

if __name__ == '__main__':
    main()
