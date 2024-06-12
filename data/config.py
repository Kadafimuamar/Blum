# api id, hash
API_ID = 11450128
API_HASH = '0384518e3ba0d967a1509afd4d53b729'

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'PLAY': [5, 15],   # delay between play in seconds
    'ERROR_PLAY': [60, 180],    # delay between errors in the game in seconds
    'CLAIM': [600, 1800]   # delay in seconds before claim points every 8 hours
}
# points with each play game; max 280
POINTS = [240, 280]

# proxy type for tg client
PROXY_TYPE = "socks5"  # "socks4", "socks5" and "http" are supported

# title blacklist tasks (do not change)
BLACKLIST_TASKS = ['Farm points', 'Invite 5 frens']

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30
