
# Query params
QUERY_HASH = '45246d3fe16ccc6577e0bd297a5db1ab'
STORY_VARS = '{\
"reel_ids":["7370873214"],\
"tag_names":[],\
"location_ids":[],\
"highlight_reel_ids":[],\
"precomposed_overlay":false\
}'

# Cookies
SESSION_ID = 'IGSC95a09b81f9040bc819eb56d1aac92f9111eb94a5fd0e01499db033df13f6574c%3AM4TKLjKn2zOIPvHAjXy16y0VdSZkTEod%3A%7B%22_auth_user_id%22%3A7370873214%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%227370873214%3ASbnpE12ojNky0bGTCERM84OOVEB3HCjF%3Abfcd47e3fd241a7e017bef5148893c0e7d4c9c5a0f91717f7f80896b6250c4e8%22%2C%22last_refreshed%22%3A1526673126.9900562763%7D'
USER_ID = '7370873214'

# Instagram
INST_STORY_URL = 'https://www.instagram.com/graphql/query/?\
query_hash=%s&variables=%s' % (QUERY_HASH, STORY_VARS)

# Github
GITHUB_API_KEY = 'd3fe940e90266d2097d97a8396cd03e09618a741'
GITHUB_OWNER = 'geekodour'
GITHUB_REPO = 'geekodour.github.io'
GITHUB_API_URL = 'https://api.github.com/repos/%s/%s/issues?\
access_token=%s' % (GITHUB_OWNER, GITHUB_REPO, GITHUB_API_KEY)
