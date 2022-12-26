from scipy.stats import spearmanr
from csv import reader

ans1 = [4.5, 3.25, 1.25, .175, 4]
ans2 = [2.5 , 1.25, 2, 2, 2.25]
ans3 = [4,3,1.25,1,4.25]
ans4 = [1.7, 1.25, 2, 2, 1.75]
ans1_3 = [4.25, 3.125, 1.25, 1.375, 4.125]
ans2_4 = [2.125, 1.25, 2,2,2]
ans10 = [3, 2.2, 1.4, 1.4, 2.75]


correlation1, pvalue1 = spearmanr(ans1, ans3)
correlation2, pvalue2 = spearmanr(ans2, ans4)
correlation3, pvalue3 = spearmanr(ans1_3, ans10)
correlation4, pvalue4 = spearmanr(ans2_4, ans10)

correlation = [correlation1, correlation2, correlation3, correlation4]
pvalue = [pvalue1, pvalue2, pvalue3, pvalue4]

print(correlation)
print(pvalue)
