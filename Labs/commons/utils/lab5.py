"""
Este archivo es generado automaticamente.

###### NO MODIFICAR #########

# cualquier alteración del archivo
# puede generar una mala calificación o configuracion
# que puede repercutir negativamente en la
# calificación del laboratorio!!!!!

###### NO MODIFICAR #########
"""

from .imports import *

# from sklearn.metrics import mean_absolute_error, accuracy_score, mean_squared_error, mean_absolute_percentage_error,r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.neural_network import MLPRegressor
from sklearn.impute import SimpleImputer
from sklearn.svm import SVR, SVC
import warnings
import subprocess

# import itertools
# from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

warnings.filterwarnings("ignore")


def generate_data(is_class=False, cols=2):
    yy = (
        np.random.choice(2, 30)
        if is_class
        else 2 * np.random.rand(60).reshape((int(60 / cols), cols))
    )
    xx = np.vstack([np.random.rand(15, 3), 2 * np.random.rand(15, 3)])
    return (xx, yy)


def part_1():
    GRADER = Grader("lab5_part1", num_questions=4)
    dataset = pd.read_csv(
        "Labs/commons/utils/data/international-airline-passengers.csv",
        usecols=[1],
        engine="python",
        skipfooter=3,
    )
    dataset.columns = ["passengers"]
    subprocess.run(["pip", "install", "torchview"], check=False)
    subprocess.run(["pip", "install", "statsmodels"], check=False)

    return (GRADER, dataset)


def part_2():
    GRADER = Grader("lab5_part2", num_questions=4)
    db = np.loadtxt(
        "Labs/commons/utils/data/AirQuality.data", delimiter="\t"
    )  # Assuming tab-delimiter
    db = db.reshape(9357, 13)
    db = db[0:2000, :]
    print("Dim de la base de datos original: " + str(np.shape(db)))

    return (GRADER, db)
