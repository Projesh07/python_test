import unittest
from donation import Donate
class TestDonate(unittest.TestCase):
	card_charge=1.50

	def test_contributor(self):
		donor1=Donate('Projesh','Bhoumik',1000)
		donor2=Donate('Raza','Saheb',2000)

		self.assertEqual(donor1.contributor,'Projesh_Bhoumik@donor.marked')
		self.assertEqual(donor1.contributor,'Raza_Saheb@donor.marked')


	def donor_name(self):
		donor1=Donate('Projesh','Bhoumik',1000)
		donor2=Donate('Raza','Saheb',2000)

		self.assertEqual(donor1.donor_name,'Projesh Bhoumik')
		self.assertEqual(donor1.donor_name,'Raza Saheb')

	def donate(self):
		donor1=Donate('Projesh','Bhoumik',1000)
		donor2=Donate('Raza','Saheb',2000)


		self.assertEqual(donor1.donate,1000)
		self.assertEqual(donor1.donate,2000)

if __name__='__main__':
	unittest.main()	

