#!/usr/bin/env python
# coding: utf-8

# # TOP most Recent stocks

# In[1]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
Ma_url = "https://finance.yahoo.com/markets/stocks/most-active/?start=0&count=100"
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get(Ma_url)
rows = driver.find_elements("xpath", '//table[@class="yf-1onk3zf bd"]//tbody/tr')
all_rows = []
for row in rows:
    row_values = row.text.split("\n")
    if len(row_values) == 6:
        parts = row_values[3].split(" ")
        row_values = [row_values[0], row_values[1], row_values[2]] + parts + [row_values[4], row_values[5]]
    all_rows.append(row_values)
driver.quit()
columns = [
    "Symbol", "Name", "Last Price", "Change", "% Change", "Volume",
    "Avg Volume (30M)", "Market Cap", "PE Ratio (TTM)",
    "YTD % Change", "52W Low", "52W High"
]
Most_recent = pd.DataFrame(all_rows, columns=columns[:len(all_rows[0])])


# # top Gainers

# In[2]:


gainers_url="https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=100"
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get(gainers_url)
rows = driver.find_elements("xpath", '//table[@class="yf-1onk3zf bd"]//tbody/tr')
all_rows = []
for row in rows:
    row_values = row.text.split("\n")
    if len(row_values) == 6:
        parts = row_values[3].split(" ")
        row_values = [row_values[0], row_values[1], row_values[2]] + parts + [row_values[4], row_values[5]]
    all_rows.append(row_values)

driver.quit()
columns = [
    "Symbol", "Name", "Last Price", "Change", "% Change", "Volume",
    "Avg Volume (30M)", "Market Cap", "PE Ratio (TTM)",
    "YTD % Change", "52W Low", "52W High"
]
top_gainers = pd.DataFrame(all_rows, columns=columns[:len(all_rows[0])])


# # top loosers

# In[3]:


losers_url="https://finance.yahoo.com/markets/stocks/losers/?start=0&count=100"
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get(losers_url)
rows = driver.find_elements("xpath", '//table[@class="yf-1onk3zf bd"]//tbody/tr')
all_rows = []
for row in rows:
    row_values = row.text.split("\n")
    if len(row_values) == 6:
        parts = row_values[3].split(" ")
        row_values = [row_values[0], row_values[1], row_values[2]] + parts + [row_values[4], row_values[5]]
    all_rows.append(row_values)
driver.quit()
columns = [
    "Symbol", "Name", "Last Price", "Change", "% Change", "Volume",
    "Avg Volume (30M)", "Market Cap", "PE Ratio (TTM)",
    "YTD % Change", "52W Low", "52W High"
]
top_loosers = pd.DataFrame(all_rows, columns=columns[:len(all_rows[0])])


# In[4]:


from datetime import datetime
import pytz
karachi_time = datetime.now(pytz.timezone("Asia/Karachi"))
time_str = karachi_time.strftime("%Y-%m-%d")
Most_recent.to_csv(fr"C:\Users\ABC\OneDrive - Notley Green Primary School\Documents\data Analytics completed projects\Projects\Yahoo Finance Stock project\Most Recent\most_recent_{time_str}.csv", index=False)
top_gainers.to_csv(fr"C:\Users\ABC\OneDrive - Notley Green Primary School\Documents\data Analytics completed projects\Projects\Yahoo Finance Stock project\Top Gainers\top_gainers_{time_str}.csv", index=False)
top_loosers.to_csv(fr"C:\Users\ABC\OneDrive - Notley Green Primary School\Documents\data Analytics completed projects\Projects\Yahoo Finance Stock project\Top losers\top_losers_{time_str}.csv", index=False)


# In[5]:


driver.quit()


# In[ ]:





# In[ ]:




