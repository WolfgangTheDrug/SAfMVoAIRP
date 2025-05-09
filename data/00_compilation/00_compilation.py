import pandas as pd

oecd: pd.DataFrame
lngs: pd.DataFrame
lrs: pd.DataFrame
hls: pd.DataFrame
gls: pd.DataFrame
crs: pd.DataFrame

oecd = pd.read_csv("./data/00_compilation/raw/OECD_countries.csv")
lngs = pd.read_csv("./data/00_compilation/raw/language_data.csv")
lrs = pd.read_csv("./data/00_compilation/raw/Google_acceptable_lr.csv")
hls = pd.read_csv("./data/00_compilation/raw/Google_acceptable_hl.csv")
gls = pd.read_csv("./data/00_compilation/raw/Google_acceptable_gl.csv")
crs = pd.read_csv("./data/00_compilation/raw/Google_acceptable_cr.csv")

oecd \
.merge(lngs, on="Country") \
.merge(lrs, on="Language") \
.merge(hls, on="Language") \
.merge(gls, on="Country") \
.merge(crs, on="Country") \
.sort_values(by='Country', axis=0) \
.to_csv("./data/00_compilation/00_joined_filetered_country_language_input.csv")
