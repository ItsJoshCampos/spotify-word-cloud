from dotenv import dotenv_values

CONFIG_ENV = {
    **dotenv_values(".env"),  # load local file development variables
}
