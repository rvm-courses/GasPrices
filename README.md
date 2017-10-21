These are data files transformed from XML for easier sessions.

## Price Files

* Delimiter is ;
* No header is provided

Fields are in this order:
- id pdv (point of sales),
- cp (zip code),
- pop (type of population, R: rural, A: urban, etc.)
- latitude
- longitude
- date
- id carburant (gas id)
- nom carburant (gas label)
- prix (price in millieuros)

## Stations Files

* Delimiter is |
* No header is provided

- id pdv,
- cp (zip code)
- pop (type of population, R: rural, A: urban, etc.)
- latitude
- longitude
- adresse (address)
- ville (city)

Note : may require to set PYTHONIOENCODING=utf-8 on Windows for special French characters.

## Services Files

* Delimiter is |
* No header is provided

Files are in this order:
- id_pdv (point of sales),
- cp_pdv (zip code),
- pop (type of population, R: rural, A: urban, etc.),
- latitude,
- longitude,
- services (as a string of services list in natural language)

Please see additional references at http://www.prix-carburants.gouv.fr/rubrique/opendata/
