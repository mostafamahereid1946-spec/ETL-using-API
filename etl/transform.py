def transform_data(df):
    # نختار الأعمدة المهمة بس
    df = df[["id", "name", "email", "address"]]

    # نفك address (nested JSON)
    df["city"] = df["address"].apply(lambda x: x["city"])
    df["street"] = df["address"].apply(lambda x: x["street"])

    df = df.drop(columns=["address"])

    return df
