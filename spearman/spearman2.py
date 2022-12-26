from scipy.stats import spearmanr
from csv import reader
import numpy as np

with open('heartbeat_for_phi_freq.csv', 'r') as csv_file:
    #それぞれの被験者から20種類取ってきて、相関を取っている。
    #phiとf（50hzを除く）の変化で5*4 = 20 となっている
    #それが10人分で20*10=200こ
    csv_reader2 = reader(csv_file)
    list_of_columns2 = np.array(list(csv_reader2))
    list_of_rows2 = list_of_columns2.T.tolist()
    waveShift_list = [int(v) for v in list_of_rows2[0]]
    frequency_list = [int(v) for v in list_of_rows2[1]]
    ave_z_valence_list2 = [float(v) for v in list_of_rows2[3]]
    ave_z_arousal_list2 = [float(v) for v in list_of_rows2[4]]

correlation3, pvalue3 = spearmanr(waveShift_list, ave_z_valence_list2)
correlation4, pvalue4 = spearmanr(waveShift_list, ave_z_arousal_list2)
correlation5, pvalue5 = spearmanr(frequency_list, ave_z_valence_list2)
correlation6, pvalue6 = spearmanr(frequency_list, ave_z_arousal_list2)

print("phie&valeace correlation:" + str(correlation3) + ", p-value:" + str(pvalue3))
print("phie&arousal correlation:" + str(correlation4) + ", p-value:" + str(pvalue4))
print("freq&valeace correlation:" + str(correlation5) + ", p-value:" + str(pvalue5))
print("freq&arousal correlation:" + str(correlation6) + ", p-value:" + str(pvalue6))

with open('heartbeat_forHR.csv', 'r') as csv_file:
    #それぞれの被験者から4種類取ってきて、相関を取っている。
    #R（40BPMを除く）の変化で4となっている
    #それが10人分で4*10=40こ
    csv_reader1 = reader(csv_file)
    list_of_columns1 = np.array(list(csv_reader1))
    list_of_rows1 = list_of_columns1.T.tolist()
    heartRate_list = [int(v) for v in list_of_rows1[2]]
    ave_z_valence_list1 = [float(v) for v in list_of_rows1[3]]
    ave_z_arousal_list1 = [float(v) for v in list_of_rows1[4]]

correlation1, pvalue1 = spearmanr(heartRate_list, ave_z_valence_list1)
correlation2, pvalue2 = spearmanr(heartRate_list, ave_z_arousal_list1)

print("heartrate&valeace correlation:" + str(correlation1) + ", p-value:" + str(pvalue1))
print("heartrate&arousal correlation:" + str(correlation2) + ", p-value:" + str(pvalue2))
