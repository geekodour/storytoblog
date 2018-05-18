from os import getenv

# Query params
QUERY_HASH = getenv('QUERY_HASH')
STORY_VARS = getenv('STORY_VARS')

# Cookies
SESSION_ID = getenv('SESSION_ID')
USER_ID = getenv('USER_ID')

# Instagram
INST_STORY_URL = 'https://www.instagram.com/graphql/query/?\
query_hash=%s&variables=%s' % (QUERY_HASH, STORY_VARS)

# Github
GITHUB_API_KEY = getenv('GITHUB_API_KEY')
GITHUB_OWNER = getenv('GITHUB_OWNER')
GITHUB_REPO = getenv('GITHUB_REPO')

GITHUB_API_URL = 'https://api.github.com/repos/%s/%s/issues?\
access_token=%s' % (GITHUB_OWNER, GITHUB_REPO, GITHUB_API_KEY)
