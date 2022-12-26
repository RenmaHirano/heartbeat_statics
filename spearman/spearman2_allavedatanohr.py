from scipy.stats import spearmanr
from csv import reader
import numpy as np

#それぞれの被験者から20種類取ってきて、相関を取っている。
#phiとf（50hzを除く）の変化で5*4 = 20 となっている

with open('heartbeat_affectgrid_allavedatanohr.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_columns = np.array(list(csv_reader))
    list_of_rows = list_of_columns.T.tolist()
    waveShift_list = [int(v) for v in list_of_rows[0]]
    frequency_list = [int(v) for v in list_of_rows[1]]
    heartRate_list = [int(v) for v in list_of_rows[2]]
    ave_z_valence_list = [float(v) for v in list_of_rows[3]]
    ave_z_arousal_list = [float(v) for v in list_of_rows[4]]

correlation2, pvalue2 = spearmanr(frequency_list, ave_z_valence_list)
correlation5, pvalue5 = spearmanr(frequency_list, ave_z_arousal_list)

correlation = [correlation2,correlation5]
pvalue = [pvalue2, pvalue5,]

print(correlation)
print(pvalue)
