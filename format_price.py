def format_price(price):
    try:
        float_price = round(float(price), 2)
        if float_price - int(float_price) != 0:
            return '{:,.2f}'.format(float_price).replace(',', ' ')
        else:
            return '{:,}'.format(int(float_price)).replace(',', ' ')
    except (ValueError, TypeError):
        return None


if __name__ == '__main__':
    print(format_price(None))
