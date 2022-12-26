from scipy.stats import spearmanr
from csv import reader

with open('heartbeat_affectgrid_ver2.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    waveShift_list = [int(v) for v in list_of_rows[0]]
    frequency_list = [int(v) for v in list_of_rows[1]]
    heartRate_list = [int(v) for v in list_of_rows[2]]
    ave_z_valence_list = [float(v) for v in list_of_rows[3]]
    ave_z_arousal_list = [float(v) for v in list_of_rows[4]]

correlation1, pvalue1 = spearmanr(waveShift_list, ave_z_valence_list)
correlation2, pvalue2 = spearmanr(frequency_list, ave_z_valence_list)
correlation3, pvalue3 = spearmanr(heartRate_list, ave_z_valence_list)
correlation4, pvalue4 = spearmanr(waveShift_list, ave_z_arousal_list)
correlation5, pvalue5 = spearmanr(frequency_list, ave_z_arousal_list)
correlation6, pvalue6 = spearmanr(heartRate_list, ave_z_arousal_list)

correlation = [correlation1, correlation2, correlation3, correlation4, correlation5, correlation6]
pvalue = [pvalue1, pvalue2, pvalue3, pvalue4, pvalue5, pvalue6]

print(correlation)
print(pvalue)
