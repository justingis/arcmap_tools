#-------------------------------------------------------------------------------
# Name:        Export Layer Properties
# Purpose:     Writes layer properties to a CSV file
#
# Author:      Justin Hawley
#
# Created:     06/13/2022
#-------------------------------------------------------------------------------


# Additional functionality that could be added
  # Field Count
  # Scale Range
  # Other display properties
  # Allow multiple input layers which could output multiple CSV files

import arcpy
import csv

# not correct when the layer has a field as the same name of the layer
def joinCheck(lyr):
  fList = arcpy.Describe(lyr).fields
  for f in fList:
    if f.name.find(lyr.datasetName) > -1:
      return True
  return False

def get_layer_properties():
  input_layer = arcpy.GetParameter(0)
  desc = arcpy.Describe(input_layer)

  layer_name = desc.name
  layer_type = desc.dataType
  layer_desc = input_layer.description
  layer_credits = input_layer.credits
  layer_visible = input_layer.visible
  source_path = desc.catalogPath
  source_format = desc.dataElement.dataType
  geometry_type = desc.shapeType
  has_m = desc.hasM
  has_z = desc.hasZ
  spatial_reference = desc.spatialReference.name
  def_query = input_layer.definitionQuery
  has_join = joinCheck(input_layer)
  feature_count = arcpy.GetCount_management(input_layer).getOutput(0)

  layer_properties = [layer_name, layer_type, layer_desc, layer_credits, layer_visible,\
    source_path, source_format, geometry_type, has_m, has_z, spatial_reference, def_query, 
    has_join, feature_count]
  return layer_properties


def write_to_csv():
  output_props_csv = arcpy.GetParameterAsText(1)
  my_props = get_layer_properties()

  output_props_fields = ('Name', 'Type', 'Description', 'Credits', \
    'Visible', 'Source', 'Format', 'Geom Type', 'Has M', 'Has Z', 'Spatial Ref', 'Def Query', 'Has Join', 'Feature Count')
  
  output_props_row = (my_props[0], my_props[1], my_props[2], my_props[3], \
    my_props[4], my_props[5], my_props[6], my_props[7], my_props[8], my_props[9], my_props[10], my_props[11], my_props[12], my_props[13])

  with open(output_props_csv, 'wb') as csv_file: 
    csvwriter = csv.writer(csv_file) 
    csvwriter.writerow(output_props_fields)
    csvwriter.writerow(output_props_row)

def write_to_screen(): #have option for layer properties and or field properties to write
  my_props = get_layer_properties()
  arcpy.AddMessage('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format('Name', 'Type', 'Description', 'Credits', \
    'Visible', 'Source', 'Format', 'Geom Type', 'Has M', 'Has Z', 'Spatial Ref', 'Def Query', 'Has Join', 'Feature Count'))

  arcpy.AddMessage('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(my_props[0], my_props[1], my_props[2], my_props[3], \
    my_props[4], my_props[5], my_props[6], my_props[7], my_props[8], my_props[9], my_props[10], my_props[11], my_props[12], my_props[13]))

def main():
  write_to_screen()
  write_to_csv()

if __name__ == '__main__':
    main()