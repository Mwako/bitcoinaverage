API_DOCUMENT_ROOT = ''  # if empty - <main.py folder>/api used
API_DOCUMENT_ROOT_NOGOX = ''  # if empty - <API_DOCUMENT_ROOT>/no_mtgox used
WWW_DOCUMENT_ROOT = ''  # if empty - <main.py folder>/www used

LOG_PATH = ''  # if empty - <main.py folder>/runtime used
PROJECT_PATH = ''  # if empty - <main.py folder> used

API_INDEX_URL = 'http://api.ba.localhost/' #should be not empty
API_INDEX_URL_NOGOX = 'http://api.ba.localhost/no-mtgox/' #should be not empty

DEFAULT_API_QUERY_FREQUENCY_OVERRIDE = 60 #if present - overrides normal frequency of exchange APIs calls