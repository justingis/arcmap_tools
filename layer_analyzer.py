#-------------------------------------------------------------------------------
# Name:        Layer Analyzer
# Purpose:     Output layer information to an XLSX
#
# Author:      Justin Hawley
#
# Created:     06/13/2022
#-------------------------------------------------------------------------------


# Output layer name (excel sheet name)
# List layer name, description, credits, visible, scale range, source, Display properties???, 
#   def query, joins and relates
# List each field in the layer with Field Properties (Name, Alias, Type, ect)
# Calc % complete and null or empty values
# Should be able to add multiple layers to create multiple sheets within an Excel doc
# Output to txt file or csv??

import arcpy

# this function could be better
def joinCheck(lyr):
  fList = arcpy.Describe(lyr).fields
  for f in fList:
    if f.name.find(lyr.datasetName) > -1:
      return True
  return False

def get_layer_info():
  layer_properties = {}
  field_properties = {}
  input_layer = arcpy.GetParameter(0)
  desc = arcpy.Describe(input_layer)

  layer_properties['layer_name'] = desc.name
  layer_properties['layer_type'] = desc.dataType
  layer_properties['layer_type'] = desc.dataType
  layer_properties['layer_desc'] = input_layer.description
  layer_properties['layer_credits'] = input_layer.credits
  layer_properties['layer_visible'] = input_layer.visible
  layer_properties['source_path'] = desc.catalogPath
  layer_properties['source_format'] = desc.dataElement.dataType
  layer_properties['geometry_type'] = desc.shapeType
  layer_properties['has_m'] = desc.hasM
  layer_properties['has_z'] = desc.hasZ
  layer_properties['spatial_reference'] = desc.spatialReference.name
  layer_properties['def_query'] = input_layer.definitionQuery
  layer_properties['has_join'] = joinCheck(input_layer)
  layer_properties['feature_count'] = arcpy.GetCount_management(input_layer)

  #for key, val in layer_properties.items():
    #arcpy.AddMessage('{}: {}'.format(key, val))

  field_list = desc.fields
  for field in field_list:
    field_properties['name'] = field.name 
      #field.aliasName,
      #field.type, 
      #field.length, 
      #field.editable, 
      #field.required, 
      #field.scale, 
      #field.precision,
      #field.isNullable,
      #field.domain

def main():
    get_layer_info()

if __name__ == '__main__':
    main()