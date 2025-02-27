import county_demographics
import data
from data import CountyDemographics
from build_data import get_data

#Part 1: returns the total population of all counties in the given list using 2014 population data
def population_total(lst:list[CountyDemographics]):
    return sum(county.population.get('2014 Population') for county in lst)

#Part 2: returns a list of counties that belong to the specified state
def filter_by_state(lst: list[CountyDemographics], s:str):
    return [county for county in lst if county.state==s]

#Part 3: calculates the estimated number of people in the given list of counties
# who have are at the specified education, ethnicity, and poverty level
def population_by_education(lst:list[CountyDemographics], s:str):
    total = 0
    for county in lst:
        education_per = county.education.get(s)/100
        population = county.population.get("2014 Population")
        total += population*education_per
    return total

def population_by_ethnicity(lst:list[CountyDemographics], s:str):
    total = 0
    for county in lst:
        education_per = county.ethnicities.get(s)/100
        population = county.population.get("2014 Population")
        total += population*education_per
    return total

def population_below_poverty_level(lst:list[CountyDemographics], s:str):
    total = 0
    for county in lst:
        education_per = county.income.get(s)/100
        population = county.population.get("2014 Population")
        total += population*education_per
    return total

#Part 4: returns the percentage of the total population in the given list of counties that
# have reached the specified education level, ethnicity population, and poverty level
def percent_by_education(lst:list[CountyDemographics], s:str):
    return population_by_education(lst, s)/population_total(lst)

def percent_by_ethnicity(lst:list[CountyDemographics], s:str):
    return population_by_ethnicity(lst, s)/population_total(lst)

def percent_below_poverty_level(lst:list[CountyDemographics], s:str):
    return population_below_poverty_level(lst, s)/population_total(lst)

#Part 5: returns a list of counties where the percentage of the population within the given
# category are greater/lesser than or equal to the given threshold
def education_greater_than(lst:list[CountyDemographics], s:str, per:float):
    return [county for county in lst if percent_by_education([county],s) >= per]

def education_less_than(lst:list[CountyDemographics], s:str, f:float):
    return [county for county in lst if percent_by_education([county], s) <= f]

def ethnicity_greater_than(lst:list[CountyDemographics], s:str, f:float):
    return [county for county in lst if percent_by_ethnicity([county], s) >= f]

def ethnicity_less_than(lst:list[CountyDemographics], s:str, f:float):
    return [county for county in lst if percent_by_ethnicity([county], s) <= f]

def below_poverty_level_greater_than(lst:list[CountyDemographics], s:str, f:float):
    return [county for county in lst if percent_below_poverty_level([county], s) >= f]

def below_poverty_level_less_than(lst:list[CountyDemographics], s:str, f:float):
    return [county for county in lst if percent_below_poverty_level([county], s) <= f]


