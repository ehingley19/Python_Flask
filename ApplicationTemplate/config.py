# Code taken from "The New and Improved Flask Mega-Tutorial (2024 Edition)" by Miguel Grinberg
import os

# This class is used to store application configuration variables
class Config:

    # Flask and some of its extensions use the value as a cryptographic key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'N0_S3cr3t_K3y_H4s_B33n_Cr34t3d!'