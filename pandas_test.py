import pandas as pd

data = {
    "Ism": ["Ali", "Vali", "Hasan"],
    "Yosh": [23, 21, 25],
    "Kasb": ["Dasturchi", "Talaba", "Buxgalter"]
}

df = pd.DataFrame(data)

print(df)