from decimal import Decimal

def calc_stab_fee(debt,days,ray):
	seconds = days*86400	
	time_rate = ((Decimal(ray)/Decimal(1e27))**Decimal(seconds))
	stab_fee = debt*time_rate
	return(stab_fee-debt)

debt = 100
days = 100
ray = 1000000000782997609082909351
stab_fee = calc_stab_fee(debt,days,ray)
print("The stability fee for a "+str(debt)+" dai debt, for "+str(days)+" days, at a ray of "+str(ray)+", should be approximately "+str(stab_fee)+" dai.")