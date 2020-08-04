import scipy.io as sio
import mat73
import numpy as np


def load_conn(path='', mtrx_name='matrix', subject_dim=3, modality_dim=2):
    """loads matlab 4d connectivity matrix from matlab file"""
    try:
        matfile = sio.loadmat(path)
        mtrx = matfile[mtrx_name]
        mtrx = np.moveaxis(mtrx, [subject_dim, modality_dim], [0, 3])
    except:
        try:
            matfile = mat73.loadmat(path)
            mtrx = matfile[mtrx_name]
            mtrx = np.moveaxis(mtrx, [subject_dim, modality_dim], [0, 3])
        except:
            raise Exception('The format needs to be a mat file.')

    return mtrx
    
