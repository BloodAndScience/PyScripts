import datetime

today = datetime.date.today()
out = today.isocalendar()[1]
text = 'Week{out}'.format(out=out)
print(text)
