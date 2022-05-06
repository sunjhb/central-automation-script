# central-automation-script
基于pycentral的aruba central自动化脚本

## 实现功能
批量导入运维账号到central

## 如何使用
1. 下载脚本到本地
```
git clone https://github.com/sunjhb/central-automation-script
```
  或者手动下载.zip文件

2. 在脚本根目录启用虚拟环境 (参考： https://docs.python.org/zh-cn/3/library/venv.html)，确保Python3.x已经在系统里安装
```
$ python3 -m venv venv
```
3. 激活虚拟环境
```
$ source venv/bin/activate

```
4. 安装必要的python模块
```
pip3 install -r requiremnts
```

5. 在users.xlsx文件中根据示例创建账号数据
示例：

|  email    | firstname  |lastname| phone       |                          |
|  ----     | ----       |  ----  | ----        | ----                     |
| 123@qq.com| lj         |  li    | 13712345678 | example（不会写入central） |
| xx@xx.com | xx         |  xx    | 13xxxxxxxxx |  |

6. 在central_info.py配置central api 凭证

```
    central_info = {
        "username": "<aruba-central-account-username>",
        "password": "<aruba-central-account-password>",
        "client_id": "<api-gateway-client-id>",
        "client_secret": "<api-gateway-client-secret>",
        "customer_id": "<aruba-central-customer-id>",
        "base_url": "<api-gateway-domain-url>"
    }
```

7. 运行脚本
```
python3 main.py
```

## 注意
### 该操作有风险，本脚本仅为学习使用，不建议在生产环境中使用，如在生产环境中使用，自行承担风险！！
