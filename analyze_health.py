import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def load():
    df = pd.DataFrame.from_csv("HKQuantityTypeIdentifierDistanceWalkingRunning.csv")
    df['creationDate'] = pd.to_datetime(df['creationDate']).dt.date
    groupped_df = df.groupby('creationDate').sum()
    print groupped_df.ix[groupped_df['value'].idxmax()]

load()