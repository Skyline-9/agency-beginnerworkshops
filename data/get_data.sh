#!/bin/bash

if which wget >/dev/null ; then
    echo "Downloading via wget..."
    wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
if which curl >/dev/null ; then
    echo "Downloading via curl..."
    curl -O -J http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
    curl -O -J http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
    curl -O -J http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
    curl -O -J http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
else
    echo "Cannot download, neither wget nor curl is available."
fi

gunzip train-images-idx3-ubyte.gz
gunzip train-labels-idx1-ubyte.gz
gunzip t10k-images-idx3-ubyte.gz
gunzip t10k-labels-idx1-ubyte.gz
