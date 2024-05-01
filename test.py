from scipy import stats
import pandas as pd 
import numpy as np

# 單母體平均數 ：
# Eps*本益比 /  當月平均

# 單母體變異數：
# 台股變異數 / 個股變異數

# 雙母體平均：
# 台積電 / 大盤


# 雙母體變異：
# 台股 / 美股 or 台積電/大盤

###單母體平均數檢定
######## pe*eps = price
# 2023第四季 台積電
pe10 =  14.48
pe11 = 16.41
pe12 = 16.80
pe = (pe10 + pe11 + pe12) / 3
eps = 9.21

price_2330_2023Q4 = pd.read_csv('台積電.csv')


result = stats.ttest_1samp(price_2330_2023Q4['當日均價(元)'],pe*eps,alternative='two-sided')
pvalue = result[1]
print("t Statistic:", result[0])
print("P-value:", result[1])

if pvalue < 0.05:
    print(f'根據單母體平均數檢定台積電p value為{pvalue} 2023Q4跟用eps*本益比的股價 有顯著差異')
else:
    print(f'根據單母體平均數檢定台積電p value為{pvalue} 2023Q4跟用eps*本益比的股價 沒有顯著差異')
    
###單母體變異數檢定
# 台股變異數 / 0050個股變異數

index_df = pd.read_csv('台指_報酬率.csv')
index_df['日報酬率 %'] = index_df['日報酬率 %'].astype(float)*0.01

index_var = index_df['日報酬率 %'].var()

df_stock = pd.read_csv('0050_報酬率.csv')
df_stock['日報酬率 %'] = df_stock['日報酬率 %'].astype(float)*0.01


var_stock = df_stock['日報酬率 %'].var(ddof=1)

df = len(df_stock) - 1

# 計算卡方
chi_square = (df*var_stock)  /index_var

# 計算p value
pvalue = 1 - stats.chi2.cdf(chi_square,df)
 
print("x2 Statistic:", chi_square)
print("P-value:", pvalue)

if pvalue < 0.05:
    print(f'根據單母體變異數檢定0050 p value為{pvalue}  有顯著差異')
else:
    print(f'根據單母體變異數檢定0050 p value為{pvalue}  沒有顯著差異')
#######################
# 雙母體平均數檢定
index_df = pd.read_csv('台指_報酬率.csv')
df_stock = pd.read_csv('0050_報酬率.csv')

t,pvalue = stats.ttest_ind(index_df['日報酬率 %'],df_stock['日報酬率 %'],alternative='two-sided')[1]

print("t Statistic:", t)
print("P-value:", pvalue)

if pvalue < 0.05:
    print(f'根據雙母體平均數數檢定0050 p value為{pvalue}  有顯著差異')
else:
    print(f'根據雙母體平均數數檢定0050 p value為{pvalue}  沒有顯著差異')
    
#######################
# 雙母體變異數檢定
index_df = pd.read_csv('台指_報酬率.csv')
df_stock = pd.read_csv('0050_報酬率.csv')
f_statistic, p_value = stats.f_oneway(index_df['日報酬率 %'], df_stock['日報酬率 %'])

# 輸出結果
print("F Statistic:", f_statistic)
print("P-value:", p_value)

# 檢定
alpha = 0.05
if p_value < alpha:
    print(f"在信心水準 {alpha} 下，拒绝0050跟大盤的雙母體變異數檢定。" )
else:
    print(f"在信心水準 {alpha} 下，不拒絕0050跟大盤的雙母體變異數檢定。。" )

