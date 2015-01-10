from django.db import models

class cultivation(models.Model):
	name = models.CharField(max_length=50)
	type = models.IntegerField(default=80)
	lifeOfTrees = models.IntegerField(default = 50)
	gestation = models.IntegerField(default = 50)
	varieties = models.CharField(max_length=50)
	plantingSeasonStart = models.CharField(max_length=50)
	plantingSeasonEnd = models.CharField(max_length=50)
	harvestManagementStart = models.CharField(maxlength=50) 
	harvestManagementEnd = 	models.CharField(max_length=50)

class plantingSpecification(models.Model)
	name = models.CharField(max_length=50)
	spacingLength = models.IntegerField(default=80)
	spacingBreadth = models.IntegerField(default=80)
	plantPopulationPerAcre = models.IntegerFied(default=80)
	plotSize = models.IntegerField(default=80)
	
class irrigation(models.Model)
	name = models.CharField(max_length=50)
	irrigationSystem = models.CharField(max_length=50)
	irrigationPerPlant = models.IntegerField(default=80)
	irrigationPerAcrePerDay = models.IntegerField(default=80)
	dischargePerDay =  models.IntegerField(default=80)

class plantProtection(models.Model)
	name = models.CharField(max_length=50)
	pests = models.CharField(max_length=50)
	diseases = models.CharField(max_length=50)

class priceLastThreeYears(models.Model)
	firstYear = models.IntegerField(default=80)
	secondYear = models.IntegerField(default=80)
	secondYear = models.IntegerField(default=80)




	


