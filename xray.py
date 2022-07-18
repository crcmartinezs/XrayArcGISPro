import arcpy

wrkspc = r'D:\OneDrive - Esri NOSA\Consultoria\LES\ELAS\FAC\Proyectos\INFRAESTRUCTURA DIFRA\Infraestructura DIFRA\DIFRA_GDB_SQL_15AGO2019.gdb'

arcpy.env.workspace = wrkspc
datasets =  arcpy.ListDatasets() + ['']
print(datasets)
for dataset in datasets:
    for feature_class in arcpy.ListFeatureClasses(feature_dataset=dataset):
        fields = [field.name for field in arcpy.ListFields(feature_class)]
        print(feature_class, fields)

for table in arcpy.ListTables():
    fields = [field.name for field in arcpy.ListFields(feature_class)]
    print(table, fields)


def detectRelationship():
    rc_list = [c.name for c in arcpy.Describe(wrkspc).children if c.datatype == "RelationshipClass"]
    rc_list

    # List the names, origin, and destination of the relationship class
    for rc in rc_list:
        des_rc = arcpy.Describe(rc)
        origin = des_rc.originClassNames
        destination = des_rc.destinationClassNames
        print (rc, origin, destination)

detectRelationship()
