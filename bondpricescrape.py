import requests, bs4, smtplib, ssl

URL = 'https://runescape.wiki/w/Bond#tradeable'

page = requests.get(URL)

soup = bs4.BeautifulSoup(page.text, 'html.parser')
bond_price = soup.select('.infobox-quantity-replace')
price = bond_price[0].text

price_int = int(price.replace(",", ""))

if(price_int >= 28000000):
    port = 465  # For SSL
    password = "bonds2themoon"
    sender_email = "bondbot4rs@gmail.com"
    receiver_email = "omarshaikh@outlook.com"
    message = """\
    Subject: BOND ALERT BY BONDBOT4RS

    Hi! \n the price of bonds have reached your limit and are currently at - """+ price + " gold pieces."

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("bondbot4rs@gmail.com", password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
else:
    print("Price lower then limit! :\(")
