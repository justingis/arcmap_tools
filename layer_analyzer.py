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
    input_layer = arcpy.GetParameter(0)
    desc = arcpy.Describe(input_layer)
    layer_name = desc.name
    layer_type = desc.dataType #we may not use this
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
    layer_feature_count = arcpy.GetCount_management(input_layer)

    arcpy.AddMessage(layer_feature_count)

    field_list = desc.fields
    for field in field_list:
        field_info = '{}, {}, {}, {} {}, {}, {}, {}, {}, {}'.format(field.name, field.aliasName, \
            field.type, field.length, field.editable, field.required, field.scale, field.precision, \
                field.isNullable, field.domain)
        arcpy.AddMessage(field_info)


def main():
    get_layer_info()

if __name__ == '__main__':
    main()