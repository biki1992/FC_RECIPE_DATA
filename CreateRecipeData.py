import pandas as pd
recipe_header = []
spec_maping = pd.read_excel("LEGACY_SPEC_MAP.xlsx")
bom_file = pd.read_excel("SF_GENERAL_RECIPE.xlsx")
##############Recipe Header Creation#######################
head_file = bom_file[bom_file["ITEM_TYPE"]=="Primary output"]
cols = [
    "LEGACY_SPEC",
    "PLM_SPEC",
    "ALT_NO",
    "RECIPE_TYPE",
    "VALID_FROM",
    "VALID_TO",
    "QTY_FROM",
    "QTY_TO",
    "UoM",
    "AUTH. GROUP",
    "ECN",
    "PLANT",
    "DESC",
    "RESP_PERSON"
]

for index, row in head_file.iterrows():
    rcp_type = ""
    legacy_spec = ""
    if row["SF_FP"] == "SF" :
        rcp_type = "ZRD_GENERAL"
    elif row["SF_FP"] == "FP":
        rcp_type = "ZRD_FP_GEN"
    
    legacy_spec = str(row["IDENTIFIER"]) + "_"  + row["MAT_TYPE"] 
    plm_spec = spec_maping[spec_maping["LEGACY_SPEC"] == legacy_spec]
    spec = str(plm_spec.iat[0,1])
        
    recipe_header.append({
        "LEGACY_SPEC": legacy_spec,
        "PLM_SPEC": spec,
        "ALT_NO": '00'+str(row['ALTERNATE']),
        "RECIPE_TYPE": rcp_type,
        "VALID_FROM": "01.05.2019",
        "VALID_TO": "31.12.2019",
        "QTY_FROM": "",
        "QTY_TO": "",
        "UoM": "",
        "AUTH. GROUP":row["Auth. Group"],
        "ECN":"500000000400",
        "PLANT": row["PLANT"],
        "DESC" : row["COMPONENT_DESC"],
        "RESP_PERSON":"SINGHB02"
    }
    )
     
recipe_df = pd.DataFrame(recipe_header, columns=cols)

recipe_df.to_excel("RECIPE_HEADER.xlsx")
###############End of Recipe header########################