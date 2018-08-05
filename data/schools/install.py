import os
import pandas as pd
import sqlite3
import stringcase


def mapper(str):
    return stringcase.snakecase(str).replace('__', '_').replace('g_i_s', 'gis').\
        replace('e_i_', 'ei_').replace('n_a_s', 'nas').replace('e_mail', 'email').\
        replace('province_c_d', 'province_cd').replace('type_do_e', 'type_doe').\
        replace('ward_i_d', 'ward_id')


dir = os.path.dirname(__file__)

conn = sqlite3.connect(os.path.join(dir, 'operational-ordinary-school.db'))

df = pd.read_excel(os.path.join(dir, 'Operational_ Ordinary School.xlsx'),
                   sheet_name='Operational Ordinary School')

df = df.rename(mapper=mapper, axis='columns')

df.to_sql('schools', con=conn, if_exists='replace')
