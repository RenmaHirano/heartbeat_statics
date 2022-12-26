from scipy.stats import spearmanr
from csv import reader

math    = [6, 4, 5, 10, 2, 8, 3, 9, 1, 7]
english = [10, 1, 4, 9, 3, 8, 6, 5, 2, 7]



with open('heartbeat_affectgrid.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    attenuation_list = [int(v) for v in list_of_rows[0]]
    gainRatio_list = [int(v) for v in list_of_rows[1]]
    waveShift_list = [int(v) for v in list_of_rows[2]]
    frequency_list = [int(v) for v in list_of_rows[3]]
    ave_z_valecnce_list = [float(v) for v in list_of_rows[4]]
    ave_z_arousal_list = [float(v) for v in list_of_rows[5]]

correlation1, pvalue1 = spearmanr(attenuation_list, ave_z_valecnce_list)
correlation2, pvalue2 = spearmanr(gainRatio_list, ave_z_valecnce_list)
correlation3, pvalue3 = spearmanr(waveShift_list, ave_z_valecnce_list)
correlation4, pvalue4 = spearmanr(frequency_list, ave_z_valecnce_list)
correlation5, pvalue5 = spearmanr(attenuation_list, ave_z_arousal_list)
correlation6, pvalue6 = spearmanr(gainRatio_list, ave_z_arousal_list)
correlation7, pvalue7 = spearmanr(waveShift_list, ave_z_arousal_list)
correlation8, pvalue8 = spearmanr(frequency_list, ave_z_arousal_list)

correlation = [correlation1, correlation2, correlation3, correlation4, correlation5, correlation6, correlation7, correlation8]
pvalue = [pvalue1, pvalue2, pvalue3, pvalue4, pvalue5, pvalue6, pvalue7, pvalue8]

print(correlation)
print(pvalue)
