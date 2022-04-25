import socket
import getpass
import os
username = getpass.getuser()

hostname = socket.gethostname()
if os.path.isdir('/kaggle/input/mandible-dataset1/'):
    dataroot = '/kaggle/input/mandible-dataset1/'
    logroot = 'logs'
else:
    if hostname == 'yenchi-pc':
        dataroot = '/home/yenchi/generative_transformers/data'
        logroot = '/home/yenchi/generative_transformers/logs'
    elif hostname == 'u110459':
        dataroot= '/data/datasets/paritosh'
        logroot= '/data/paritosh/generative_transformers/logs'
        if username == 'yenchi':
            dataroot = '/data/yenchi/generative_transformers/data'
            logroot = '/data/yenchi/generative_transformers/logs'
    elif hostname == 'euclid':
        if username == 'yenchi':
            dataroot = '/data/yenchi/generative_transformers/data'
            logroot = '/data/yenchi/generative_transformers/logs'
    else:
        dataroot = '..'
        logroot = '../logs'