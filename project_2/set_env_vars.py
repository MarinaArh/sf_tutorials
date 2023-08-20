import os

os.environ['SF_DB_USER'] = 'skillfactory'
os.environ['SF_DB_PASSWORD'] = 'cCkxxLVrDE8EbvjueeMedPKt'
os.environ['SF_DB_HOST'] = '84.201.134.129'
os.environ['SF_DB_PORT'] = '5432'
os.environ['SF_DB_NAME'] = 'skillfactory'

os.environ['SF_DB_URL'] = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'.format(
  user=os.environ['SF_DB_USER'],
  password=os.environ['SF_DB_PASSWORD'],
  host=os.environ['SF_DB_HOST'],
  port=os.environ['SF_DB_PORT'],
  dbname=os.environ['SF_DB_NAME']
)