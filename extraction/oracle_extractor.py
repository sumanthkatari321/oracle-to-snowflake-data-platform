import cx_Oracle
import pandas as pd
import yaml
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class OracleExtractor:

    def __init__(self, config_path):

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        self.connection = None

    def connect(self):

        try:
            oracle_cfg = self.config['oracle']

            dsn = cx_Oracle.makedsn(
                oracle_cfg['host'],
                oracle_cfg['port'],
                service_name=oracle_cfg['service']
            )

            self.connection = cx_Oracle.connect(
                user=oracle_cfg['username'],
                password=oracle_cfg['password'],
                dsn=dsn
            )

            logging.info("Connected to Oracle")

        except Exception as e:
            logging.error(f"Connection failed: {e}")
            raise

    def extract_incremental(self, table_name, watermark):

        query = f"""
        SELECT *
        FROM {table_name}
        WHERE LAST_UPDATED_TIMESTAMP > TO_TIMESTAMP('{watermark}',
        'YYYY-MM-DD HH24:MI:SS')
        """

        logging.info(f"Extracting data from {table_name}")

        df = pd.read_sql(query, self.connection)

        logging.info(f"{len(df)} rows extracted")

        return df

    def close(self):

        if self.connection:
            self.connection.close()
            logging.info("Oracle connection closed")
