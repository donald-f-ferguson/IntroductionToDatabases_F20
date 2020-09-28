import pandas as pd
import pymysql
from sqlalchemy import create_engine
import os

base_dir = "/Users/donaldferguson/Dropbox/Columbia/W4111F2020/IntroductionToDatabases_F20/Data/lahman2019/"
engine = create_engine('mysql+pymysql://root:dbuserdbuser@localhost')
default_schema = "lahman2019raw"

def init_schema():
    con = engine.connect()
    con.execute("create schema if not exists lahman2019raw character set='utf8mb4'")
    con.close()


def load_and_create_table(file_name, table_name, schema_name=default_schema, repl="replace", engine=engine):
    df = pd.read_csv(file_name)
    df = df.astype(str)
    try:
        df.to_sql(table_name, engine, schema=schema_name, if_exists="replace", index=False)
    except Exception as e:
        print("Exception e = ", e)
        print("DF = ", df.head(10))


def get_load_files(load_dir, file_type):

    result = []

    dir_files = os.listdir(load_dir)
    file_suffix = "." + file_type

    for f in dir_files:
        if file_suffix in f:
            split_name = f.split(".")
            fn = f
            tn = split_name[0]
            result.append([fn, tn])

    return result


def load_csv_dir(base_dir):
    ff = file_to_use = get_load_files(base_dir, "csv")
    for f in ff:
        print("Loading file = ", f[0], "into table", f[1])
        load_and_create_table(base_dir + f[0], f[1])
        print("Loaded")
    print("Done!")





init_schema()
load_csv_dir(base_dir)


