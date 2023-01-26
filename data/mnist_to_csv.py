#!/usr/bin/env python

import urllib.request
import shutil
import gzip
import os
import re


def gunzip_something(gzipped_file_name, work_dir):
    """gunzip the given gzipped file"""

    # see warning about filename
    filename = os.path.split(gzipped_file_name)[-1]
    filename = re.sub(r"\.gz$", "", filename, flags=re.IGNORECASE)

    with gzip.open(gzipped_file_name, 'rb') as f_in:  # <<========== extraction happens here
        with open(os.path.join(work_dir, filename), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def download():
    print('Downloading files...')
    urllib.request.urlretrieve("http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz", "train-images-idx3-ubyte.gz")
    urllib.request.urlretrieve("http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz", "train-labels-idx1-ubyte.gz")
    urllib.request.urlretrieve("http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz", "t10k-images-idx3-ubyte.gz")
    urllib.request.urlretrieve("http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz", "t10k-labels-idx1-ubyte.gz")

    shutil.register_unpack_format('gz', ['.gz', ], gunzip_something)

    print('Unpacking gz files...')
    shutil.unpack_archive('train-images-idx3-ubyte.gz', os.curdir, 'gz')
    shutil.unpack_archive('train-labels-idx1-ubyte.gz', os.curdir, 'gz')
    shutil.unpack_archive('t10k-images-idx3-ubyte.gz', os.curdir, 'gz')
    shutil.unpack_archive('t10k-labels-idx1-ubyte.gz', os.curdir, 'gz')


def cleanup():
    print('Cleaning up files...')
    try:
        os.remove('t10k-images-idx3-ubyte')
        os.remove('t10k-images-idx3-ubyte.gz')
        os.remove('t10k-labels-idx1-ubyte')
        os.remove('t10k-labels-idx1-ubyte.gz')
        os.remove('train-images-idx3-ubyte')
        os.remove('train-images-idx3-ubyte.gz')
        os.remove('train-labels-idx1-ubyte')
        os.remove('train-labels-idx1-ubyte.gz')
    except OSError as e:
        print("Error removing file: %s - %s." % (e.filename, e.strerror))


def convert(imgf, labelf, outf, n):
    print("Converting ", imgf)

    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)
        print_progress_bar(i + 1, n, prefix = "Reading Images:")

    for i, image in enumerate(images):
        o.write(",".join(str(pix) for pix in image)+"\n")
        print_progress_bar(i + 1, n, prefix = "Writing to CSV:")

    f.close()
    o.close()
    l.close()
    print()


# Print iterations progress
def print_progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


download()
convert("train-images-idx3-ubyte", "train-labels-idx1-ubyte","mnist_train.csv", 60000)
convert("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte","mnist_test.csv", 10000)
cleanup()