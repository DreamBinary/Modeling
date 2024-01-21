import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_val_score

datas = pd.DataFrame([[13.85, 2.79,  7.80, 49.60],
                      [22.31, 4.67, 12.31, 47.80],
                      [28.82, 4.63, 16.18, 62.15],
                      [15.29, 3.54,  7.58, 43.20],
                      [28.29, 4.90, 16.12, 58.70],
                      [2.18,  1.06,  1.22, 20.60],
                      [3.85,  0.80,  4.06, 47.10],
                      [11.40, 0.00,  3.50,  3.00],
                      [3.66,  2.42,  2.14, 15.10],
                      [12.10, 0.00,  5.68,  0.00]], index=[1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
x0 = datas.values.astype(float)
y0 = datas.index.values.astype(float)
md = LDA()
print(cross_val_score(md, x0, y0, cv=5).mean())
