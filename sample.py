#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
SAMPLE_SIZE = 600

def plot_confusion_matrix(cm, title='Confusion matrix', target_names=['0','1'],cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

if __name__ == "__main__":
    all_mobiles = pd.read_csv('mobiles.txt',header=None)[0].values
    available_mobiles = pd.read_csv('可用号码_88587条.txt',header=None)[0].values
    disable_mobiles = np.setdiff1d(all_mobiles,available_mobiles)
    print "all: %d, available: %d, disable: %d." % (len(all_mobiles),len(available_mobiles),len(disable_mobiles))
    sample_available = np.random.choice(available_mobiles,SAMPLE_SIZE,replace=False)
    sample_disable = np.random.choice(disable_mobiles,SAMPLE_SIZE,replace=False)

    output = np.union1d(sample_available,sample_disable)
    output.tofile('recheck.txt',sep="\n")
    sample_available.tofile('available.txt',sep="\n")
    sample_disable.tofile('disable.txt',sep="\n")

    
