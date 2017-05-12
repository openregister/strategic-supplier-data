# Strategic supplier register data

The data for a strategic-supplier register seeded from the
[Crown Representatives and strategic suppliers](https://www.gov.uk/government/publications/current-registered-providers-of-social-housing) list
kept and maintained by the [Crown Commercial Service](https://www.gov.uk/government/organisations/crown-commercial-service).

  * [data/strategic-supplier/strategic-supplier.tsv](data/strategic-supplier/strategic-supplier.tsv)

# Building

Use `make` to build register shaped data
— we recommend using a [Python virtual environment](http://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv -p python3 social-housing-data
    $ workon social-housing-data

    $ cd lists/ccs
    $ make init
    $ make

    $ cd ../..
    $ make init
    $ make

# Licence

The software in this project is covered by LICENSE file.

The data is [© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
