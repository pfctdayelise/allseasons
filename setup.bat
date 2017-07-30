@echo off
doskey conda_alias=%userprofile%\AppData\Local\Continuum\Miniconda3\Scripts\conda.exe
conda_alias update conda-build
conda_alias env create --force -f environment.yml
