import csv
import numpy as np
import plotly.express as px

with open("D:\Python\Correlation project\cups of coffee vs hours of sleep.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()
