#encoding=utf-8

import numpy as np


def load_MNIST_images(filename):
	"""loadMNISTImages returns a 28x28x[number of MNIST images] matrix containing
	the raw MNIST images.
	"""
	
	f = open(filename, 'rb')

	assert f != -1, 'Could not open %s' % filename

	magic = np.fromfile(f, dtype='>i4', count=1)
	assert magic == 2051, 'Bad magic number in %s' % filename

	numImages = np.fromfile(f, dtype='>i4', count=1)
	numRows = np.fromfile(f, dtype='>i4', count=1)
	numCols = np.fromfile(f, dtype='>i4', count=1)

	images = np.fromfile(f, dtype='B')
	images = images.reshape(numImages, numCols, numRows)
	
	f.close()

	# Reshape to #pixels x #examples
	images = images.reshape(images.shape[0], images.shape[1]*images.shape[2])
	# Convert to double and rescale to [0,1]
	images = images.astype(np.double)/255.0

	return images
    

def load_MNIST_labels(filename):
	"""loadMNISTLabels returns a [number of MNIST images]x1 matrix containing
	the labels for the MNIST images
	"""

	f = open(filename, 'rb')
	assert f != -1, 'Could not open %s' % filename

	magic = np.fromfile(f, dtype='>i4', count=1)
	assert magic == 2049, 'Bad magic number in %s' % filename
	
	numLabels = np.fromfile(f, dtype='>i4', count=1)
	
	labels = np.fromfile(f, dtype='B')
	
	assert labels.shape[0] == numLabels, 'Mismatch in label count'
	
	f.close()
	
	return labels


def get_data(Only0=True, N=4000):
    """
    Only01=True: 只选取label=0或1的图像
    Only01=False: 所有0-9的图像
    N：训练数据长度，默认测试数据和训练数据一样长
    """
    images = load_MNIST_images('./data/train-images-idx3-ubyte')
    labels = load_MNIST_labels('./data/train-labels-idx1-ubyte')

    if Only0:
        """
        #普通实现
        images_01=[]
        labels_01=[]
        for i in xrange(labels.size):
            if labels[i]==0 or labels[i]==1:
                labels_01.append(labels[i])
                images_01.append(images[i,:])
                
        
        images_01 = np.asarray(images_01)
        labels_01 = np.asarray(labels_01)
        """
        
        # numpy实现
        index = np.where(labels<1)
        images_01 = images[index[0],:]
        labels_01 = labels[index[0]]
        
        assert (2*N)<images_01.shape[0], "N is too larger than data length"
        images_s = scale_n(images_01[:N+N, :])
        labels_s = labels_01[:N+N]         
    else:
        assert (2*N)<images.shape[0], "N is too larger than data length"
        images_s = scale_n(images[:N+N, :])
        labels_s = labels[:N+N] 
            
    X = np.insert(images_s, 0, 1, axis=1) 

    train_X = X[:N, :] #前400行为训练数据
    train_y = labels_s[:N]
    train_y.shape = (train_y.shape[0],1)

    test_X = X[N:, :]
    test_y = labels_s[N:]
    test_y.shape = (test_y.shape[0],1)

    return train_X,train_y,test_X,test_y


def scale_n(x):
    x = np.double(x)
    m = x.mean(axis=0)
    s = x.std(axis=0)+0.1
    return (x-m)/(s)

    