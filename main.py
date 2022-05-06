from pycentral.base import ArubaCentralBase
from central_info import central_info
import xlrd
from create_users import create_user

data = xlrd.open_workbook('users.xlsx')
table = data.sheet_by_index(0)

# 行数
nrows = table.nrows

# 列数，去掉最后一行备注
ncols = table.ncols - 1

# 列表推导式生成
users = [[table.cell_value(row, col) for col in range(ncols)] for row in range(2, nrows)]
if len(users):
    # 登陆central
    ssl_verify = True
    token_store = {
        "type": "local",
        "path": "temp"
    }
    central = ArubaCentralBase(central_info=central_info,
                               token_store=token_store,
                               ssl_verify=ssl_verify)
else:
    print('No user exist!')

if __name__ == '__main__':
    create_user(central_conn=central, users=users)
