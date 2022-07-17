# ArcMap Tools
Geoprocessing toolbox for ArcMap. Feel free to download and use these tools at your conveniance. And if you wish, contribute to the repo to make it better. The following tools are included:
1. Add Coordinates: Adds XY, and or LAT LONG coordinate fields or updates existing fields.  If no update fields are selected, new additional fields will be added to the point layer.  
2. Export Attachments: Exports attachments (stored as a blob field) to a specified folder location.  
3. Export to XLSX: Exports a layer or table to .XLSX format.  User may select which fields to include in the export.
4. ID Generator: Calculates unique ID's for a given input layer, field, start value, prefix, suffix, and pad value.
5. Export Field Properties: Exports field properties to a CSV file which include field name, alias, type, length, editable, required, scale, precision, nullable, domain, and percent complete (percentage of records that have a value and are not blank or null)
6. Export Layer Properties: Exports layer properties to a CSV file which include layer name, type, description, credits, visible, source path, source format, geometry type, has M, has Z, spatial reference, definition query, and feature count. 
7. Workspace Reporter: Recursively walks through an input folder location or geodatabase (workspace) and generates a csv file of the schema (field name, field type, field length) for each file or feature class
8. Find & Replace: Finds all instances of a text pattern (regular expression) and updates the layers attribute table. If a text value is found, all instances of that text value are replaced in the record
9. Basic Erase: Allows for the same functionality as the built-in Erase tool without requiring the Advanced license (works with Basic license).

# System Requirements
1. Windows 10, 11
2. ArcMap 10.8.x, Basic, Standard, or Advanced license
3. Python 2.7.18.4 (default Python 2 environment installed with ArcMap - C:\Python27\ArcGIS10.8)
4. openpyxl - https://pypi.org/project/openpyxl/ (required for Export to XLSX)

# Installation
This process adds an additional package (openpyxl) to the default ArcMap Python environment. No new virtual environment is created.
1. Clone or download repository to local PC
2. Install openpyxl (only required for Export to XLSX):
  * Open Windows Command Prompt (CMD)
  * cd C:\Python27\ArcGIS10.8\Scripts
  * pip install openpyxl
3. Open ArcMap or ArcCatalog and navigate to the toolbox (.tbx file) in the repository. 
