import requests
import time
import json


start = 1703643900
end = 1703655678
symbol = 'RPOWER'

url = 'https://groww.in/v1/api/charting_service/v2/chart/exchange/NSE/segment/CASH/{}?endTimeInMillis={}&intervalInMinutes=1&startTimeInMillis={}'.format(symbol,end,start)
header = {'Authorization' : 'Bearer eyJraWQiOiJXTTZDLVEiLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3MDM2NzYzMzgsImlhdCI6MTcwMzU2OTM1MSwibmJmIjoxNzAzNTY5MzAxLCJzdWIiOiJ7XCJlbWFpbElkXCI6XCJnaWxpZ2FpbHNAZ21haWwuY29tXCIsXCJwbGF0Zm9ybVwiOlwid2ViXCIsXCJwbGF0Zm9ybVZlcnNpb25cIjpudWxsLFwib3NcIjpudWxsLFwib3NWZXJzaW9uXCI6bnVsbCxcImlwQWRkcmVzc1wiOlwiMTY1LjEuMjM4LjIyOSxcIixcIm1hY0FkZHJlc3NcIjpudWxsLFwidXNlckFnZW50XCI6XCJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTE5LjAuMC4wIFNhZmFyaS81MzcuMzZcIixcImdyb3d3VXNlckFnZW50XCI6bnVsbCxcImRldmljZUlkXCI6XCJmZjNiNzIyNC01YjE1LTViN2QtYTVmNy1lZmMzOGJiMDYyMDBcIixcInNlc3Npb25JZFwiOlwiNjQxODFlYWQtMzJjZS00MzFlLWIzNWUtZTE2Y2IxYTQ2ODZjXCIsXCJzdXBlckFjY291bnRJZFwiOlwiQUNDODY4NDIxODM2MTUwMFwiLFwidXNlckFjY291bnRJZFwiOlwiQUNDODY4NDIxODM2MTUwMFwiLFwidHlwZVwiOlwiQVRcIixcInRva2VuRXhwaXJ5XCI6MTcwMzY3NjMzODQyOCxcInRva2VuSWRcIjpcImUxYTU5Y2Y1LWYyYmEtNDhkMC04ZjNmLTY0YzU3ODMwOWNhMFwifSIsImlzcyI6Imdyb3d3YmlsbGlvbm1pbGxlbm5pYWwifQ.jo1h_Ow7r_6ibPFspy2Zm7QueHIIPAyFgaA56hcn6ULNEGLvnKuB-xq5m3Kw73DnpW9IY3YKPjLnLZusk0pdpQ'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like

url = 'https://groww.in/v1/api/stocks_data/v1/tr_live_book/exchange/NSE/segment/CASH/IDEA/latest'



url = 'http://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={}&resolution=1&from={}&to={}&countback=3&currencyCode=INR'.format(symbol,start,end)

# https://groww.in/v1/api/stocks_data/v1/tr_live_prices/exchange/NSE/segment/CASH/IDEA/latest

# https://groww.in/v1/api/charting_service/v2/chart/exchange/NSE/segment/CASH/IDEA/daily?intervalInMinutes=1&minimal=true

r = requests.get(url, headers = headers, verify = False)
d = json.loads(r.text)['t']
print(r.text)
for i in d :
    print(time.gmtime(i))
    print(time.time())