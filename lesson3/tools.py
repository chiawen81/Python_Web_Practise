import requests

# 目標網址
url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=1000'



###### 下載UBike原始資料(完整版)
def  download_youbike_data_complete():
    try:
        response = requests.get(url)
        response.raise_for_status()
        '''NOTE:
            response.raise_for_status() 會檢查這次 HTTP 回應的狀態碼，只要不是 200～299 的成功碼，就會直接丟出 requests.HTTPError 例外。這可以讓你在請求失敗時立即跳出，方便在 try...except 裡處理錯誤，不用再自己判斷每種失敗狀況。
        '''

        try:
             data = response.json()
             print(f"取得資料:{data}")
             '''NOTE:
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
        except requests.exceptions.JSONDecodeError as err:
            raise Exception(f"發生轉換格式錯誤:{err}")

    # 錯誤訊息處理
    # 負責捕捉網路請求過程中所有 requests 可能拋出的異常。
    except requests.exceptions.HTTPError as err:
        raise Exception(f"發生 HTTP 錯誤: {err}")
    
    except requests.exceptions.Timeout as err:
        raise Exception(f"請求時間逾時: {err}")
    
    except requests.exceptions.ConnectionError as err:
        raise Exception(f"發生連線錯誤 (例如 DNS 查詢失敗、連線被拒): {err}")
        
    except requests.exceptions.RequestException as err:
        # 這是所有 requests 例外的父類別，可以用來捕捉其他未預期的錯誤
        raise Exception(f"網路請求失敗： {err}")
    
    except Exception as e:
        # 解析或其他非 requests 產生的例外
         print("程式執行出錯：", e)
    else:
        return data


###### 下載UBike原始資料(簡易版)
def  download_youbike_data_sample():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    
    # 錯誤訊息處理
    except requests.exceptions.RequestException as err:
        raise Exception(f"下載或解析失敗: {err}")
    
    except ValueError as err:
        raise Exception(f"JSON 解析失敗: {err}")



## 取得地區
def get_area(data)->list:
    areas = set()
    for item in data:
        areas.add(item['sarea'])
    return list(areas)


## 取得地區裡的地點
def get_sites_of_area(data,area)->list:
    sites = []
    for item in data:
        if item['sarea'] == area:
            sites.append(item)
    return sites