from common import config
from xray import Checker

import pandas as pd
import arcpy

_config = config()
wrkspc = _config['gdb_path']

arcpy.env.workspace = wrkspc

df_children = pd.json_normalize(Checker(wrkspc).gdb_elements, 'Children', ['Name', 'DataType',])
df_base = pd.json_normalize(Checker(wrkspc).gdb_elements, max_level=1)[['Name', 'DataType', 'fields',]]

df = pd.concat([df_base, df_children[['Name', 'DataType', 'Name_child', 'DataType_child', 'fields_child',
                                      'Origin_child', 'Destination_child',]], ], ignore_index=True)

with pd.ExcelWriter('Resultado.xlsx') as writer:
    df.to_excel(writer, sheet_name='Xray', index=False)
