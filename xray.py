import arcpy


class Checker:
    def __init__(self, wrkspc):
        self._wrkspc = wrkspc


    @property
    def gdb_elements(self):

        elements = list(map(self.describe_elements, arcpy.Describe(self._wrkspc).children))
        return elements

    def describe_elements(self, el, sufix=''):
        data = {'Name' + sufix: el.name,
                'DataType' + sufix: el.dataType,
                'Children' + sufix: None}
        if data['DataType' + sufix] == 'FeatureDataset':
            n = len(el.children)
            subset = list(map(self.describe_elements, el.children, ['_child'] * n))
            data['Children'] = subset

        elif data['DataType' + sufix] == 'FeatureClass':
            fields = ', '.join([field.name for field in arcpy.ListFields(el.catalogPath)])
            data['fields' + sufix] = fields

        elif data['DataType' + sufix] == 'Table':
            fields = ', '.join([field.name for field in arcpy.ListFields(el.catalogPath)])
            data['fields' + sufix] = fields

        elif data['DataType' + sufix] == 'RelationshipClass':
            data['Origin' + sufix] = el.originClassNames[0]
            data['Destination' + sufix] = el.destinationClassNames[0]

        return data
