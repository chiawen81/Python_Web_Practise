import requests

###### 取得資料
url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=1000'

response = requests.get(url)

if response.status_code == 200:
    print("下載成功")
    print(response.json())
else:
    print("下載失敗")

'''
NOTE:
1. response 是 requests 套件中的 Response 物件（型別為 requests.models.Response）
2. 這個物件包含了：
    - 狀態碼：response.status_code
    - 回應標頭：response.headers
    - 回應內容：
        - 文字形式：response.text
        - JSON 形式：response.json()
    - 原始 bytes：response.content
    - Cookie、編碼等其他資訊
3. 所以要拿資料要寫成「response.json()」
'''




