import string
import math
import random

class AdoptionCenter:
	"""
	The AdoptionCenter class stores the important information that a
	client would need to know about, such as the different numbers of
	species stored, the location, and the name. It also has a method to adopt a pet.
	"""
	def __init__(self, name, species_types, location):
		self.name=name
		self.location=location
		self.species_types=species_types

	def get_number_of_species(self, animal):
		return self.species_types.get(animal,0)

	def get_location(self):
		location=(int(self.location[0])*1.0,int(self.location[1])*1.0)
		return location 

	def get_species_count(self):
		localD={}
		for x in list(self.species_types.keys()):
			if self.species_types[x]!=0:
				localD[x]=self.species_types[x]
		return localD

	def get_name(self):
		return self.name

	def adopt_pet(self, species): 
		self.species_types[species]-=1


class Adopter:
	""" 
	Adopters represent people interested in adopting a species.
	They have a desired species type that they want, and their score is
	simply the number of species that the shelter has of that species.
	"""
	def __init__(self, name, desired_species):
		self.name=name
		self.desired_species=desired_species

	def get_name(self):
		return self.name

	def get_desired_species(self):
		return self.desired_species

	def get_score(self, adoption_center):
		return 1.0*adoption_center.get_number_of_species(self.desired_species)


class FlexibleAdopter(Adopter):
	"""
	A FlexibleAdopter still has one type of species that they desire,
	but they are also alright with considering other types of species.
	considered_species is a list containing the other species the adopter will consider
	Their score should be 1x their desired species + .3x all of their desired species
	"""
	def __init__(self,name,desired_species,considered_species):
		self.considered_species=considered_species
		Adopter.__init__(self,name,desired_species)

	def get_score(self,adoption_center):
		total_score=Adopter.get_score(self,adoption_center)
		#print Adopter.get_score(self,adoption_center)
		total=0
		for x in self.considered_species:
			total+=adoption_center.get_number_of_species(x)
		#	print adoption_center.get_number_of_species(x)
		res=total_score+(0.3*total)
		if res<0:
			return 0.0
		else:
			return 1.0*res

class FearfulAdopter(Adopter):
	"""
	A FearfulAdopter is afraid of a particular species of animal.
	If the adoption center has one or more of those animals in it, they will
	be a bit more reluctant to go there due to the presence of the feared species.
	Their score should be 1x number of desired species - .3x the number of feared species
	"""
	def __init__(self,name,desired_species,feared_species):
		self.feared_species=feared_species
		Adopter.__init__(self,name,desired_species)

	def get_score(self,adoption_center):
		#print Adopter.get_score(self,adoption_center),adoption_center.get_number_of_species(self.feared_species)
		res=(1.0*Adopter.get_score(self,adoption_center))-(0.3*adoption_center.get_number_of_species(self.feared_species))
		if res<0:
			return 0.0
		else:
			return 1.0*res


class AllergicAdopter(Adopter):
	"""
	An AllergicAdopter is extremely allergic to a one or more species and cannot
	even be around it a little bit! If the adoption center contains one or more of
	these animals, they will not go there.
	Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
	"""
	def __init__(self,name,desired_species,allergic_species):
		self.allergic_species=allergic_species
		Adopter.__init__(self,name,desired_species)

	def get_score(self,adoption_center):
		total=Adopter.get_score(self,adoption_center)
		for x in self.allergic_species:
			if adoption_center.get_number_of_species(x)>0:
				return 0.0
			else:
				continue
		return total


class MedicatedAllergicAdopter(AllergicAdopter):
	"""
	A MedicatedAllergicAdopter is extremely allergic to a particular species
	However! They have a medicine of varying effectiveness, which will be given in a dictionary
	To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
	To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
	Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
	"""
	def __init__(self,name,desired_species,allergic_species,medicine_effectiveness):
		self.medicine_effectiveness=medicine_effectiveness
		AllergicAdopter.__init__(self,name,desired_species,allergic_species)

	def get_score(self,adoption_center):
		total=Adopter.get_score(self,adoption_center)
		#print "Adopter base score",total
		m=1.0
		for x in list(self.medicine_effectiveness.keys()):
			#print "XXX",x,self.medicine_effectiveness[x],adoption_center.get_number_of_species(x),m
			if self.medicine_effectiveness[x]<m and adoption_center.get_number_of_species(x)>0:
				m=self.medicine_effectiveness[x]
		return m*total




class SluggishAdopter(Adopter):
	"""
	A SluggishAdopter really dislikes travelleng. The further away the
	AdoptionCenter is linearly, the less likely they will want to visit it.
	Since we are not sure the specific mood the SluggishAdopter will be in on a
	given day, we will asign their score with a random modifier depending on
	distance as a guess.
	Score should be
	If distance < 1 return 1 x number of desired species
	elif distance < 3 return random between (.7, .9) times number of desired species
	elif distance < 5. return random between (.5, .7 times number of desired species
	else return random between (.1, .5) times number of desired species
	"""
	def __init__(self,name,desired_species,location):
		self.location=location
		Adopter.__init__(self,name,desired_species)

	def get_linear_distance(self,to_location):
		return math.sqrt((self.location[0]-to_location[0])**2+(self.location[1]-to_location[1])**2)

	def get_score(self,adoption_center):
		d=self.get_linear_distance(adoption_center.get_location())
		if d<1:
			return 1.0*adoption_center.get_number_of_species(self.desired_species)
		elif d>=1 and d<3:
			return random.uniform(0.7,0.9)*adoption_center.get_number_of_species(self.desired_species)
		elif d>=3 and d<5:
			return random.uniform(0.5,0.7)*adoption_center.get_number_of_species(self.desired_species)
		elif d>=5:
			return random.uniform(0.1,0.5)*adoption_center.get_number_of_species(self.desired_species)


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
	"""
	The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
	"""
	lst=[]
	for x in list_of_adoption_centers:
		print [x,adopter.get_score(x),x.name]
		lst.append([x,adopter.get_score(x),x.name])
	lst=customSort(lst)
	newlst=[]
	for x in lst:
		newlst.append(x[0])
	print newlst
	return newlst


def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
	"""
	The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
	"""
	lst=[]
	for x in list_of_adopters:
		lst.append([x,x.get_score(adoption_center),x.name])
	lst=customSort(lst)
	newlst=[]
	for x in lst:
		newlst.append(x[0])
	#print lst[:n]
	#print newlst[:n]
	return newlst[:n]

def customSort(lst):
	#print lst
	lst=sorted(lst,key = lambda x: (x[2]))
	newlst=[]
	y=[x[1] for x in lst]
	#print y
	for i in range(len(lst)):
		z=max(y[:])
		newlst.append(lst[y.index(z)])
		lst.pop(y.index(z))
		y.pop(y.index(z))
	#print newlst
	return newlst

'''def customSort(lst):
	#print lst
	return sorted(lst,key = lambda x: (x[1], x[2]))'''

def getKey(item):
	return item[1]


adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])                            
# you can print the name and score of each item in the list returned