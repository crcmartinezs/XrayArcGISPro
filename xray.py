wrkspc = r'D:\OneDrive - Esri NOSA\Consultoria\LES\ELAS\FAC\Proyectos\INFRAESTRUCTURA DIFRA\Infraestructura DIFRA\DIFRA_GDB_SQL_15AGO2019.gdb'


import arcpy


class Checker:
    def __init__(self, wrkspc):
        arcpy.env.workspace = wrkspc

    @property
    def gdb_elements(self):

        elements = [{'Name': fc.name, 'Type': fc.dataType,
                     'Children': [{'Name': c.name, 'Type': c.dataType} for c in fc.children]}
                    for fc in arcpy.Describe(wrkspc).children]
        return elements



print(Checker(wrkspc).gdb_elements)

