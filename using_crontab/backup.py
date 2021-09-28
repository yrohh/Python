import psycopg2
import pandas as pd
from datetime import datetime

db = psycopg2.connect(
    host='ip',
    dbname='스키마명',
    user='유저명',
    password='암호',
    port=포트번호
)

nowT = datetime.now()
nowT = nowT.strftime("%Y%m%d%I")

# munjin 테이블
df_munjin = pd.read_sql("""select * from munjin.munjin order by munjin_id""", db)
df_munjin.to_csv(f"./backup_folder/munjin_{nowT}.csv", encoding='cp949', index=None)


# pheno 테이블
df_pheno = pd.read_sql("""select * from munjin.pheno order by pheno_id""", db)
df_pheno.to_csv(f"./backup_folder/pheno_{nowT}.csv", encoding='cp949', index=None)