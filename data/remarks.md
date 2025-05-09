# Data
These data files are attached for transparency and review purposes. 
Each file has been checked by the author of the study and corrected where needed.
The editorial process was to ensure propper dataframes' joining.

## Language and country (compilation no. 00)
Importantly, this results in several politically loaded simplifications: 
- the *de facto* official languages are treated equally to the *de jure* official languages;
- Koreas' North-South naming convention has been chosen;
- the Czech state's name has been standardized to "Czechia";
- the Slovak state's name has been standardized to "Slovak Repoublic";
- the Turkish state's name has been standardized to Türkiye;

Crucially, not all the items in each list have been standardized but mainly the vital ones for the study, i.e. the 38 OECD states with full parametric search support (cr, gl, hl, lr parameters) as for May 9, 2025.
Minor changes (like standardizing Portuguese language from Portugal to "Portuguese (Portugal)") have been ommitted in this documentationa as they do not require further explanation.

### Sources
These are the original sources of the data files.
| File   | Source |
| ---    | ---    |
|langugae_data.csv|[Oxfordshire County Council](https://portal.oxfordshire.gov.uk/content/public/LandC/SandPM/data/census/Countries_Languages.xls)|
|OECD_countries.csv|[OECD partners](https://www.oecd.org/en/about/members-partners.html)
|Google_acceptable_lr.csv|[Custom Search JSON API](https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list)
|Google_acceptable_cr.csv|[Programmable Search Engine International Values](https://developers.google.com/custom-search/docs/json_api_reference#international-values)|
|Google_acceptable_hl.csv|[Programmable Search Engine International Values](https://developers.google.com/custom-search/docs/json_api_reference#international-values)|
|Google_acceptable_gl.csv|[Programmable Search Engine International Values](https://developers.google.com/custom-search/docs/json_api_reference#international-values)|