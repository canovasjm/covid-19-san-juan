![scraper-san-juan-gobierno](https://github.com/canovasjm/covid-19-san-juan/workflows/scraper-san-juan-gobierno/badge.svg)

# covid-19-san-juan

Este repositorio contiene un script en python para hacer scraping al "Módulo coronavirus" mantenido por el Gobierno de la Provincia de San Juan, Argentina. Link: https://sisanjuan.gob.ar/modulo-coronavirus

Este módulo muestra información sobre los casos de coronavirus en la Provincia de San Juan, Argentina. El scraper se ejecuta diariamente a la hora 09:00 UTC-3 usando GitHub Actions, toma la información y la guarda en un archivo csv.

Contenido: 

* `sj-gobierno.py`: script en python que hace el scraping y guarda los datos en un archivo csv.  

* `requirements.txt`: contiene un listado con las librerías que requiere el script en python para funcionar. Se usa para instalar estas librerías en el GitHub runner.

* `data/covid-san-juan.csv`: aquí se guardan los datos luego de cada ejecución.

Más detalles en mi blog: https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/

**2022-04-18 ACTUALIZACION:** El Consejo Federal de Salud anunció que a partir del martes 2022-04-19 los reportes sobre COVID-19 se difundirán una vez por semana todos los días martes (más detalles aquí: [link](https://sisanjuan.gob.ar/salud-publica/2022-04-18/40273-el-parte-de-covid19-se-difundira-los-dias-martes-por-decision-del-consejo-federal-de-salud)). Por esta razón, detuve la GitHub Action que corre el script de scraping.

# covid-19-san-juan  

This repository contains a python script to scrape the "Coronavirus Module" maintained by the Government of San Juan Province, in Argentina. Link: https://sisanjuan.gob.ar/modulo-coronavirus  

This module shows information about coronavirus cases in San Juan Province, Argentina. The scraper runs dialy at 09:00 UTC-3 using GitHub Actions, retrieves the information, and saves it to a csv file.

Content:  

* `sj-gobierno.py`: python script that performs the scraping and saves the data to a csv file.  

* `requirements.txt`: holds a list with the requiered libraries to run the python script. It is used to install these libraries in the GitHub runner.

* `data/covid-san-juan.csv`: new data is saved here after each daily run.

Full details in blogpost: https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/

**2022-04-18 UPDATE:** The Federal Health Council announced that starting on Tuesday 2022-04-19 COVID-19 reports will be published once a week every Tuesday (more details here: [link](https://sisanjuan.gob.ar/salud-publica/2022-04-18/40273-el-parte-de-covid19-se-difundira-los-dias-martes-por-decision-del-consejo-federal-de-salud)). For this reason, I stopped the GitHub Action running the scraping script.
