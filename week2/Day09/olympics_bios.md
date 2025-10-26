Here’s the markdown format from my earlier answer—the one you liked—with concise description and grouped commands, but without excessive inline comments, all as a single Markdown block:

-----------------------------------------------------
## Python & Pandas: Olympics Bios Sheet Workflow

**1. Load Data**
import pandas as pd

Excel sheet
bios = pd.read_excel("data/olympics_data.xlsx", sheet_name="bios")

or CSV
bios = pd.read_csv("data/olympics_bios.csv")

-----------------------------------------------------

**2. Inspect Data**
bios.head()
bios.tail()
bios.info()
bios.describe()

-----------------------------------------------------

**3. Filter Rows**
bios[bios["height_cm"] > 215]
bios[(bios["height_cm"] > 215) & (bios["born_country"] == "USA")]
bios[bios["name"].str.contains("Keith", case=False)]
bios.query("born_country == 'USA'")

-----------------------------------------------------

**4. Create New Columns**
bios_new = bios.copy()
bios_new["first_name"] = bios_new["name"].str.split().str
bios_new["born_date_time"] = pd.to_datetime(bios_new["born_date"])
bios_new["born_year"] = bios_new["born_date_time"].dt.year

-----------------------------------------------------

**5. Save Data**
bios_new.to_csv("bios_new.csv", index=False)

-----------------------------------------------------

**6. Advanced: Custom Functions & Categories**
bios_new["height_category"] = bios_new["height_cm"].apply(
lambda x: "short" if x < 165 else "average" if x < 185 else "tall"
)
def categorize_athlete(row):
# custom logic using height and weight
...
bios_new["weight_category"] = bios_new.apply(categorize_athlete, axis=1)

-----------------------------------------------------

**7. Merge with Regions**
noc = pd.read_csv("data/regions.csv")
bios_new = pd.merge(
bios_new, noc, left_on="born_country", right_on="NOC", how="left"
)
bios_new.rename(columns={"region": "born_country_full"}, inplace=True)

-----------------------------------------------------

**8. Aggregation & Analysis**
bios["born_city"].value_counts()
bios[bios["born_country"] == "USA"]["born_region"].value_counts()
bios.groupby("sport")["height_cm"].mean()
bios_new.groupby("born_year")["name"].count()

-----------------------------------------------------

**9. Sort & Rank**
bios["height_rank"] = bios["height_cm"].rank(ascending=False)
bios.sort_values("height_rank")

-----------------------------------------------------

**10. Plot Example**
import matplotlib.pyplot as plt
bios["height_cm"].plot.hist(logy=True)

-----------------------------------------------------

This keeps it clean, grouped, and reference-style for rapid learning/review—matching the version you preferred for your notes and workflow.