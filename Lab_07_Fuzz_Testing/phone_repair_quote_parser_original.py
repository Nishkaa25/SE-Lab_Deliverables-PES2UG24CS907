def mask_imei(imei):
    """
    Removes dashes and spaces, then hides all but the last four digits.
    Assumes imei is a non-empty string.
    """
    imei = imei.replace('-', '').replace(' ', '')
    return '*' * (len(imei) - 4) + imei[-4:]

def parse_parts_order(text):
    """
    Parses 'screen x1; battery x2' into a {part: quantity} dictionary.
    Assumes every item is written as 'part xQTY'.
    """
    order = {}
    for item in text.split(';'):
        part, qty = item.split('x')
        order[part.strip()] = int(qty)
    return order

def parse_model(text):
    """
    Splits 'Brand Model name' into a (brand, model) tuple.
    Assumes text has at least two words.
    """
    brand, model = text.strip().split(' ', 1)
    return brand.title(), model.strip()

def main():
    print("==== Running mask_imei ====")
    value = input("Enter an IMEI number (e.g. 35-209900-176148-1): ")
    print("Masked IMEI:", mask_imei(value))

    print("\n==== Running parse_parts_order ====")
    value = input("Enter parts and quantities as PART xQTY separated by ; (e.g. screen x1; battery x2): ")
    print("Parts order:", parse_parts_order(value))

    print("\n==== Running parse_model ====")
    value = input("Enter the phone brand and model (e.g. Samsung Galaxy S23): ")
    print("Brand and model:", parse_model(value))

if __name__ == "__main__":
    main()
