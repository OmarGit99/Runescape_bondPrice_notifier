# Runescape_bond_price_notifier
A simple bot script that can be scheduled to scrape bond price (for investing) and notify by Email using SMTP, can be configured to set limits for alerts.

How to set it up:
<li>
  Fix the path in the bash file
</li>
<li> Change the receiver email in the .py file to whatever email you are using </li>
<li> Add a cronjob on your pc (OR any scheduler) to run bash file or py file </li>
<li> Profit??</li>

To set limit alerts:
Just change the condition within the if statement in the .py file to whatever value you like 💰
