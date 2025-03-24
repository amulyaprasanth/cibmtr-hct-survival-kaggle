import sweetviz as sv
import pandas as pd

# Load the dataframe
train_dataset = pd.read_csv("data/train.csv")

report = sv.analyze(train_dataset, target_feat="efs_time")
report.show_html("index.html", layout=vertical)
