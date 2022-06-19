#-------------------------------------------------------------------------------
# Name:        Layer Reporter
# Purpose:     Writes layer properties and schema information to an xlsx, txt, or csv
#
# Author:      Justin Hawley
#
# Created:     06/13/2022
#-------------------------------------------------------------------------------


# Additional functionality that could be added
# Has Relates
# Scale Range
# Other display properties
# Allow multiple input layers which could output multiple CSV, TXT or sheets within an XLSX document

import arcpy

# this function could be better
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

def get_layer_fields():
  input_layer = arcpy.GetParameter(0)
  desc = arcpy.Describe(input_layer)
  feature_count = arcpy.GetCount_management(input_layer).getOutput(0)
  field_prop_list = []

  field_list = desc.fields
  for field in field_list:
    name = field.name
    alias = field.aliasName
    type = field.type
    length = field.length
    editable = field.editable
    required = field.required
    scale = field.scale
    precision = field.precision
    isNullable = field.isNullable
    domain = field.domain
    percent_complete = get_percent_complete(input_layer, name, feature_count)

    field_properties = (name, alias, type, length, editable, required, scale, precision, isNullable, domain, percent_complete)
    field_prop_list.append(field_properties)
  return field_prop_list
    

# does not check for whitespace
def get_percent_complete(input_layer, field_name, feature_count):
  false_vals_included = [0] # could add empty string here
  val_count = 0.0
  cursor = arcpy.da.SearchCursor(input_layer, [field_name])
  for row in cursor:
    row_val = row[0]
    if row_val or row_val in false_vals_included:
      val_count += 1
  return (val_count / float(feature_count)) * 100

def write_to_txt():
  pass

def write_to_csv():
  pass

def write_to_xlsx():
  pass

def write_to_screen(): #have option for layer properties and or field properties to write
  my_props = get_layer_properties()
  arcpy.AddMessage('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format('Name', 'Type', 'Description', 'Credits', \
    'Visible', 'Source', 'Format', 'Geom Type', 'Has M', 'Has Z', 'Spatial Ref', 'Def Query', 'Has Join', 'Feature Count'))

  arcpy.AddMessage('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(my_props[0], my_props[1], my_props[2], my_props[3], \
    my_props[4], my_props[5], my_props[6], my_props[7], my_props[8], my_props[9], my_props[10], my_props[11], my_props[12], my_props[13]))

  arcpy.AddMessage('\n')
  my_fields = get_layer_fields()
  arcpy.AddMessage('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format('Name', 'Alias', 'Type', 'Length', 'Editable', 'Required',\
    'Scale', 'Precision', 'Is Nullable', 'Domain', '% Complete'))
  for field in my_fields:
    arcpy.AddMessage('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(field[0], field[1], field[2], field[3], field[4], field[5], field[6],\
      field[7], field[8], field[9], field[10]))

def main():
  write_to_screen()

if __name__ == '__main__':
    main()