from pathlib import Path
import tempfile
import traceback
import json
import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except Exception as e:
    print(e)
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = "29280344"
    api_hash = "824d1adea456ad2f2788e64cfe2fc917"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try: 
    # index_settings_str = os.environ["INDEX_SETTINGS"].strip()

    # index_settings = json.loads(index_settings_str)

    index_settings = {
      "index_all": True,
      "index_private":True,
      "index_group": True,
      "index_channel": True,
      "exclude_chats": [],
      "include_chats": []
    }
    
try:
    session_string = "1BVtsOLcBuyuLdj4pSNpPPBuMxGaL2bn-9JJzJCO06mA1FbJkXmbJ8INVvtfYMNp3ZnYIdvRb9RZGf1xjDLHsF0mgeRU1LKTHihvzl2ffJynWd75wQ_hGdgJAufXA1LqdpQHuWQ0jr9l3RrXhNTqzDWyHDtrMxTk-a1bWLx_LKCnzqR4Ff25XICNpaBPkPMrnFMaxYetCSagUoqpaueBlSFByH4cX7pUxPo3fuZruuH-JaDghwDbPn4skXYZqVPbAnqau5i8JVObTSuLmgkiMNTtnQdgDq9_9yCDRVxwV8zcUx3HJphmqhzzGf-86yQjTVfoYJF8yxqSL0OY-jBQigug-2EeSV7s="
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
block_downloads = bool(os.environ.get("BLOCK_DOWNLOADS"))
results_per_page = int(os.environ.get("RESULTS_PER_PAGE", "20"))
logo_folder = Path(os.path.join(tempfile.gettempdir(), "logo"))
logo_folder.mkdir(parents=True, exist_ok=True)
username = os.environ.get("TGINDEX_USERNAME", "")
password = os.environ.get("PASSWORD", "")
SHORT_URL_LEN = int(os.environ.get("SHORT_URL_LEN", 3))
authenticated = bool(username and password)
SESSION_COOKIE_LIFETIME = int(os.environ.get("SESSION_COOKIE_LIFETIME") or "60")
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
    if len(SECRET_KEY) != 32:
        raise ValueError("SECRET_KEY should be exactly 32 charaters long")
except (KeyError, ValueError):
    if authenticated:
        traceback.print_exc()
        print("\n\nPlease set the SECRET_KEY environment variable correctly")
        sys.exit(1)
    else:
        SECRET_KEY = ""
