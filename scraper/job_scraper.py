import requests
from bs4 import BeautifulSoup

def scrape_jobs(url):
    response = requests.get(url, "lxml")
    soup = BeautifulSoup(response.text, "lxml")
    
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    vagas = []

    for job in jobs:
        empresa = job.find("h3", class_="joblist-comp-name").text.strip()
        habilidades = job.find("span", class_="srp-skills").text.strip()
        data_publicacao = job.find("span", class_="sim-posted").text[7:].strip()
        
        vaga = {
            "empresa" : empresa,
            "habilidades" : habilidades,
            "data_publicacao" : data_publicacao
        }
        vagas.append(vaga)

    return vagas

