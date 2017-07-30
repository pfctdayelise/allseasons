# Setup instructions

## Windows? Install git for windows

[Git for Windows download](https://git-for-windows.github.io/)

## Clone the git repo

Windows: Run git-bash and `git clone ...`

Linux/Mac: In terminal, run `git clone ...`

## Change directory

`cd allseasons/allseasons`

## Install miniconda 

[Install the appropriate miniconda](https://conda.io/miniconda.html)

You can find out if you OS is 32 or 64 bit by...

Mac: In a terminal window, `uname -m`

* x86_64 ==> 64-bit kernel
* i686   ==> 32-bit kernel

Windows: Run `cmd` and `wmic os get osarchitecture`

## Create a conda environment

Run `setup.sh` on Linux/Mac, or `setup.bat` on Windows.

## Activate the environment

On Linux/Mac: `source activate allseasons`

On Windows: `activate allseasons`

## More instructions

...

## Clean up at the end of the tutorial

Run `cleanup.sh` on Linux/Mac, or `cleanup.bat` on Windows.
