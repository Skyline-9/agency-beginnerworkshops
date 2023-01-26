
<p align="center">
  <img src="./assets/Agency Logo.png" width="180">
</p>

# About

Hello! This is a series of "workshops" designed to give a gentle introduction to deep learning. Each workshop is a Jupyter notebook that walks through some concepts and provides coding exercises along the way to test your knowledge. Learning about neural networks is not easy, so we include detailed diagrams and explanations to make learning as smooth as possible. We have also included answer keys to check your implementations. These will walk you through implementing a basic neural network from scratch (without an ML framework), and then learning the basics of using ML frameworks (PyTorch).


<p align="center">
  <img src="./assets/wkshp2_preview.png" width="400">
  <img src="./assets/wkshp3_preview.png" width="400">
</p>


Feel free to work through these workshops alone, or come visit [Agency tuesday meetings](https://gtagency.github.io/) if you have questions or want help. We hold an open session where members can work through the workshops, and Agency officers will help with all questions, ranging from installation of the workshops to providing in-depth explanations of neural network topics. We may also walk through a particular worksheet depending on the level of interest on the day. It is very much a relaxed, but productive learning environment.

# Installation

Simply fork the repository or download a zip of the code. It is important to keep all the workshops in the correct folder, otherwise images won't load properly.

## Pre-requisites

Make sure you have the following dependencies
- [ ] [Python](https://www.python.org/downloads/)
- [ ] Anaconda (any version will do, I suggest [Miniconda](https://docs.conda.io/en/main/miniconda.html)
- [ ] [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

If you have git, you can run
```git
git clone https://github.com/Skyline-9/agency-beginnerworkshops.git
```

## Setting up a Python virtual environment

All of the required dependencies are listed in requirements.txt. This can also be used directly with pip to install all dependencies directly into your virtual environment.

If you are using Anaconda (which is recommended), you can create an environment directly using the provided yml file with the following command

	conda env create -f workshops.yml
	conda activate workshops

If the above command DOES NOT WORK, then you can try running the following commands
```bash
conda create -n workshops #replace "workshops" with desired name
conda activate workshops #activate your environment, use same name as before
conda install numpy ipykernel jupyter notebook
```

Once you reach the pytorch section of workshops, you can reconfigure pytorch for your personal specs at https://pytorch.org/. For example, on macOS it is
```bash
conda install pytorch torchvision torchaudio -c pytorch
```
	
If you are done coding, you can deactivate your environment with 

	conda deactivate
	
Make sure to activate your environment before doing anything in the workshops, or before calling 
	
	jupyter notebook
	
in the source directory to open the workshops, and deactivate once you are done!

## Installing and Preparing the MNIST Dataset

We have provided two scripts to install and prepare the MNIST dataset. From the source directory, navigate to the data folder with 

	cd data
	
Now, run the script to install the data from online

	sh get_data.sh
		
If the script is not working for you, you can alternatively go to [Yann LeCun's Website](http://yann.lecun.com/exdb/mnist/) and simply click on the 4 links at the top to download the dataset. Move these files into the data directory, and make sure to unzip them. 

Once you have the data downloaded, we will reformat it. You can do this by running

	python mnist_to_csv.py
	
This should add two csv files to your data directory. Now you're ready to write a neural network for this dataset!