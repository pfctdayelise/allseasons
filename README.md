# Welcome to the PyCon Australia 2017 'practical testing with pytest' tutorial!

# Setup instructions

## Windows? Install git for windows

[Git for Windows download](https://git-for-windows.github.io/)

## Clone the git repo

Linux/Mac: In terminal, run `git clone https://github.com/pfctdayelise/allseasons.git`

Windows: Run git-bash and `git clone https://github.com/pfctdayelise/allseasons.git`

## Change directory

`cd allseasons`

## Install miniconda 

[Install the appropriate miniconda](https://conda.io/miniconda.html)

You can find out if your operating system is 32- or 64-bit by...

Linux/Mac: In a terminal window, `uname -m`

* x86_64 ==> 64-bit kernel
* i686   ==> 32-bit kernel

Windows: Run `cmd` and `wmic os get osarchitecture`

## Create a conda environment

Linux/Max: Run `setup.sh` 

Windows: Run `setup.bat`

## Activate the environment

Linux/Mac: `source activate allseasons`

Windows: `activate allseasons`


## Clean up at the end of the tutorial

Linux/Mac: `cleanup.sh` 

Windows: `cleanup.bat`
