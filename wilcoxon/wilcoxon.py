from csv import reader
from scipy import stats
import numpy as np

for i in range(1, 6):
    #print(i)
    output_arr = [[0 for n in range(5)] for m in range(5)]
    with open('experiment3_question' + str(i) + '.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        list_of_columns = np.array(list(csv_reader))
        list_of_rows = list_of_columns.T.tolist()
    
        for j in range(1,6):
            list1 = [int(v) for v in list_of_rows[j-1]]
            #print(list1)
            for k in range(1,6):
                #print(k)
                if j != k:
                    list2 = [int(v) for v in list_of_rows[k-1]]
                    result = stats.wilcoxon(list1, list2, mode='exact',alternative='two-sided')
                    output_arr[j-1][k-1] = result.pvalue
                else:
                    output_arr[j-1][k-1] = 100
        
        print("Result of question " + str(i) + " is")
        for p_value in output_arr:
            print(*p_value, sep=',')
