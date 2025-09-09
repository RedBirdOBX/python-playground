import config

# defined outside of the scope of the function
def demo():

    # reading a global variable from config
    print(config.APP_NAME)
    print(config.ENABLE_NOTIFICATIONS)
    print(config.ENABLE_ANALYTICS)

