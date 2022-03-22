import pandas as pd
import datetime

def send_Email():
    pass

if __name__ == "__main__":
    df=pd.read_excel("birthday_dates.xlsx")
    print(df)
    today=datetime.datetime.now()
    print(today)
    today=datetime.datetime.now().strftime("%d-%m")
    print(today)
    print(type(today))