
def click_element(context, locator_type, locator_value):
    if locator_type == "xpath":
        context.click(locator_value)
    else:
        raise ValueError("Unsupported locator type: " + locator_type)

def send_keys(context, locator_type, locator_value, send_keys_value):
    if locator_type == "xpath":
        context.fill(locator_value,send_keys_value)
    else:
        raise ValueError("Unsupported locator type: " + locator_type)

def fetchURL(context):
    return context.url


