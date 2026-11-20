def mask_imei(imei):
    """
    Removes dashes and spaces, then hides all but the last four digits.
    Handles invalid and unexpected inputs safely.
    """
    if not isinstance(imei, str):
        return ""

    imei = imei.replace('-', '').replace(' ', '')

    if len(imei) <= 4:
        return imei

    return '*' * (len(imei) - 4) + imei[-4:]


def parse_parts_order(text):
    """
    Parses 'screen x1; battery x2' into a {part: quantity} dictionary.
    Skips malformed items and invalid quantities.
    """
    if not isinstance(text, str):
        return {}

    order = {}

    for item in text.split(';'):
        parts = item.split('x')

        if len(parts) != 2:
            continue

        part, qty = parts
        part = part.strip()
        qty = qty.strip()

        if not part or not qty:
            continue

        try:
            quantity = int(qty)
        except ValueError:
            continue

        if quantity <= 0:
            continue

        order[part] = quantity

    return order


def parse_model(text):
    """
    Splits 'Brand Model name' into a (brand, model) tuple.
    Handles missing or invalid inputs safely.
    """
    if not isinstance(text, str):
        return ("", "")

    parts = text.strip().split(maxsplit=1)

    if len(parts) < 2:
        return ("", "")

    brand, model = parts

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