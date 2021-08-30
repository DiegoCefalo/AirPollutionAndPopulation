import pandas as pd
import re
import requests

def remove_comma(string):
    """
    Esta función remueve las comas de las cifras de población scrapeadas
    Input: str
    output: str
    """
    string = string.replace(',','')
    return string
    
def get_info():
    """
    Esta función scrapea la población de estados unidos a través de los años:
    Inputs: Ninguno
    Ouputs: Data Frame
    """
    url = 'https://www.worldometers.info/world-population/us-population/'
    response = requests.get(url).content
    pop_year = re.findall('<tr> <td>(\d+)</td> <td><strong>(\d+,\d+,\d+)</strong></td>',str(response))
    del pop_year[18:]
    pop_year = pd.DataFrame(pop_year).rename(columns={0:'year',1:'population'})
    pop_year.year = pop_year.year.astype(int)
    pop_year.population = pop_year.population.apply(lambda x : x.replace(',',''))
    pop_year.population = pop_year.population.astype(int)
    return pop_year