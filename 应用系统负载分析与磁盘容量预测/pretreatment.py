#数据预处理部分
import pandas as pd
data_file = '/Users/Mac/Desktop/discdata.xls'
data = pd.read_excel(data_file)
data1 = data[data['TARGET_ID'] == 184].copy()
C_data = data1[data1['ENTITY'] == 'C:\\'].copy()
D_data = data1[data1['ENTITY'] == 'D:\\'].copy()
change_data = pd.DataFrame({'SYS_NAME': C_data['SYS_NAME'].reset_index(drop=True),
                            'CWXT_DB:184:C': C_data['VALUE'].reset_index(drop=True),
                            'CWXT_DB:184:D': D_data['VALUE'].reset_index(drop=True),
                            'COLLECTTIME': C_data['COLLECTTIME'].reset_index(drop=True)},
                          columns=['SYS_NAME', 'CWXT_DB:184:C', 'CWXT_DB:184:D', 'COLLECTTIME'])
change_data.to_excel('/Users/Mac/Desktop/discdata.xls')
