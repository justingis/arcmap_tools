#run from ArcGIS Pro default py env: & "c:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe" c:/projects/poc_tabletop/py/schema.py

import arcpy, csv, os

def main():

    workspace = 'C:/projects/ga_power/gdb'
    output_folder = 'C:/Users/arcgis/Desktop/output/' #change to output folder

    for dirpath, dirnames, filenames in arcpy.da.Walk(workspace):
        for filename in filenames:
            desc = arcpy.Describe(os.path.join(dirpath, filename))
            featureclass = desc.catalogpath
            fields = arcpy.ListFields(featureclass)
            output_csv = os.path.join(output_folder, desc.name + '.csv')
            with open(output_csv, 'w', newline='') as csv_table:
                csv_writer = csv.writer(csv_table)
                for field in fields:
                    csv_writer.writerow([field.name, field.type, field.length])
            print(desc.name)

    print('\nFinished...')

if __name__ == '__main__':
    main()
