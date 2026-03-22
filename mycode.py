import pandas as pd
import os 

data={
  "Name":["Alice","Bob","Charlie"],
  "Age":[39,89,10],
  "City":["New York","Mumbai","Los Angeles"]
}

df=pd.DataFrame(data)
print(df.head())

#Creates data directory if exists
data_dir="data"
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,"sample_data.csv")

df.to_csv(file_path,index=False)
print(f"CSV file saved to {file_path}")