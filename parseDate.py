import time
import datetime
import re

OPT_TODAY = frozenset(['today'])
OPT_YESTERDAY = frozenset(['yesterday', 'previous day'])

def convertDate(date_string):
	today = datetime.date.today()
	date_string = date_string.strip().lower()
	#.replace('/',' ').replace('-', ' ').replace(',',' ')
	
	if date_string in OPT_TODAY:
		return datetime.date(today.year, today.month, today.day)
	elif date_string in OPT_YESTERDAY:
		return datetime.date(today.year, today.month, today.day) - datetime.timedelta(days=1)
	elif re.search(r'(\d{1,5}|a) days? ago', date_string):
		return n_days(date_string)
	else:
		return date(date_string)

def n_days(date_string):
    """
    date_string string in format "(number|a) day(s) ago"
    """
    today = datetime.date.today()
    match = re.match(r'(\d{1,5}|a) days? ago', date_string)
    groups = match.groups()
    if groups:
        decrement = groups[0]
        if decrement == 'a':
            decrement = 1
        return today - datetime.timedelta(days=int(decrement))
    return None


def date(date_string):
    # %b = abbreviated month name
	# %B = full month name
	# %d = day of the month as a decimal number[01,31]
	# %m = month as a decimal number[01,12]
	# %y = year without century as a decimal number [00,99]
	# %Y = year with century as a decimal number
	date_formats_with_year = ['%m %d %Y', '%Y %m %d', '%B %d %Y', '%b %d %Y',
	'%m %d %y', '%y %m %d', '%B %d %y', '%B %d %y']

	date_formats_without_year = ['%m %d', '%d %B', '%B %d', '%d %b', '%b %d']

	for format in date_formats_with_year:
		try:
			result = time.strptime(date_string, format)
			return datetime.date(result.tm_year, result.tm_mon, result.tm_mday)
		except ValueError:
			pass

	for format in date_formats_without_year:
		try:
			result = time.strptime(date_string, format)
			year = datetime.date.today().year
			return datetime.date(year, result.tm_mon, result.tm_mday)
		except ValueError:
			pass

	return None


