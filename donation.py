
#Client class
class Donate:
	card_charge=1.50

	def __init__(self,first_name,last_name,donate):

		self.first_name=first_name
		self.last_name=last_name
		self.donate=donate

	@property
	def contributor(self):
		return '{}_{}@donor.marked'.format(self.first_name,self.last_name)

	@property	
	def donor_name(self):
		return '{} {}'.format(self.first_name,self.last_name)
	@property	
	def donate(self):
		self.donate=int(self.donate+self.card_charge)
				
