import imdlib as imd
import pandas as pd
import matplotlib.pyplot as plt
import xarray 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import seaborn as sns

file_dir=r'C:\Users\Nirdesh\Documents\Untitled Folder'
start_yr=2020
end_yr=2020
variable = 'rain'
data=imd.get_data(variable,start_yr,end_yr,'yearwise',file_dir)
data = imd.open_data(variable, start_yr, end_yr,'yearwise', file_dir)
ds = data.get_xarray()
min_lon = 91
min_lat = 26
max_lon = 95
max_lat = 26.25

mask_lon = (ds.lon >= min_lon) & (ds.lon <= max_lon)
mask_lat = (ds.lat >= min_lat) & (ds.lat <= max_lat)
cropped_ds = ds.where(mask_lon & mask_lat, drop=True)
df=cropped_ds.to_dataframe()
%matplotlib inline
ds=df.groupby(['time']).mean()
ds['date']=ds.index

df=ds[['date','rain']]
df['date'] = pd.to_datetime(df['date'])
plt.plot(df['date'],df['rain'])
plt.xlabel('date')
plt.ylabel('rain')
plt.show()
