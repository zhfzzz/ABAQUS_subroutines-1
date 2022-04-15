import numpy as np
import matplotlib.pyplot as plt
#
def read_csv_file(filename):
    """
    Read the csv file from the ABAQUS post-processing script
    """
    # Open text file for reading
    fp = open(filename+'.csv','r')
    # Scroll through the lines in the file
    for line in fp:
        if line[0:1] == '*':
           # Extract the variable names from the first line of the file
           keys = [x.strip() for x in line.replace('*','').split(',')]
           # Create a dictionnary with a list for each variable/key
           dico = {}
           for key in keys:
               dico[key] = []
        else:
           # Store each value in the corresponding dictionnary key
           for key,value in zip(keys,line.split(',')):
               dico[key].append(float(value))
    # Scroll through the lines in the file
    fp.close()
    # Change the lists to arrays
    for key in list(dico.keys()):
        dico[key] = np.array(dico[key])
    return dico
##########################################################################################
# START OF THE SCRIPT
##########################################################################################
# Define files to be read
filenames = ['example_VUHARD_V1_data','example_UHARD_V1_data']
# Read csv files
results = {}
for filename in filenames:
    results[filename] = read_csv_file(filename)
# Plot results
plt.rcParams["figure.figsize"] = (8, 4)
fig,axs = plt.subplots(1,2)
k = 0
for key in list(results.keys()):
    axs[k].plot(results[key]['time'],results[key]['sig_rate'],label=key.split('_')[1]+' Visco-plastic')
    axs[k].plot(results[key]['time'],results[key]['sig_ref'],label=key.split('_')[1]+' Plastic')
    axs[k].set_xlabel('Time (s)')
    axs[k].set_ylabel('True stress (-)')
    axs[k].set_xlim([0.0,0.02])
    axs[k].set_ylim([0.0,400.0])
    axs[k].legend()
    axs[k].grid()
    k += 1
plt.tight_layout()
plt.savefig('UHARD_VUHARD_V1.pdf')
plt.show()
##########################################################################################
# END OF THE SCRIPT
##########################################################################################
exit()