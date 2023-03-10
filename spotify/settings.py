from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# config_env = {
#     **dotenv_values(".env"),  # load local file development variables
# }

# CLIENT_ID = config_env.CLIENT_ID
# CLIENT_SECRET = config_env.CLIENT_SECRET

# print variables for testing
# print(config_env["CLIENT_ID"])
# print(config_env["CLIENT_SECRET"])