import datetime
import re
from typing import List, Optional
import time
import requests
import dateutil.relativedelta as rd

class GoogleSearchClient():
    def __init__(
            self, 
            api_key: str, 
            search_engine_id: str, 
            language: Optional[str] = None, 
            country: Optional[str] = None, 
            delay_between_requests: int = 1, 
            max_results: int = 100
        ):
        self.api_key = api_key
        self.search_engine_id = search_engine_id
        self.language = language
        self.country = country
        self.delay = delay_between_requests
        self.max_results = max_results
        self.base_url = "https://www.googleapis.com/customsearch/v1"


    def _build_query(
            self, 
            query: str, 
            start_date: str, 
            month_count: int = 3
        ) -> str:
        """
            A helper method to build query with restricted dates. 
            ## Params
            query: the searched phrase
            start_date: date string in YYYY_MM format 
            month_count: the amount of months to search through; search resolution
            ## Motivation
            The basic dateRestrict parameter can only search for the LAST x days, weeks, months, years.
            However, we need more granularity and a workaround that allows that is to directly edit the search query.
            ## Example
            For query="Artificial Intelligence", start_date: "2020_05", the method will return "Artificial Intelligence after:2020-05-01 before:2020-07-31".
        """
        year: int
        month: int
        day: int = 1

        start: datetime.date
        end: datetime.date

        def _validate_start_date_format(start_date: str) -> bool:
            pattern: re.Pattern
            is_valid: bool

            pattern = re.compile("\d{4}_\d{2}")
            is_valid = pattern.fullmatch(start_date) is not None
            
            return is_valid
        
        if not _validate_start_date_format(start_date): raise ValueError("Provided start date is wrongly formatted. The correct format is YYYY_MM, e.g. 2020_05.")
        
        year, month = (int(num) for num in start_date.split('_'))

        if not 1 <= month <= 12: raise ValueError(f"Provided start date month ({month=}) is incorrect. This value must be between 1 and 12 (inclusive).")

        start = datetime.date(year=year, month=month, day=day)
        end = start + rd.relativedelta(months=month_count, days=-1) # the last day of the end month

        if end > datetime.date.today(): raise ValueError(f"Provided start date ({start_date=}) results in an end date that cannot be searched for ({end=: %Y-%m-%d}).")
        
        return f"{query} after:{start: %Y-%m-%d} before:{end: %Y-%m-%d}"
    
    def search(
        self,
        query: str,
        start_date: str,
        month_count: int = 3
    ) -> List[str]:
        all_titles: List[str] = []
        start_index: int = 1
        results_per_page: int = 10

        formatted_query: str 
        params: dict[str, str | int]
        title: str

        formatted_query = self._build_query(query, start_date, month_count)
        params = {
            'q': formatted_query,
            'key': self.api_key,
            'cx': self.search_engine_id,
            'num': results_per_page
        }
        if self.language: params['lr'] = self.language
        if self.country: params['cr'] = self.country

        while start_index <= self.max_results:
            params['start'] = start_index

            response = requests.get(self.base_url, params=params)
            if response.status_code != 200:
                print(f"Error {response.status_code}: {response.text}")
                break

            data = response.json()
            items = data.get("items", [])
            if not items: break

            for item in items:
                title = item.get("title")
                if title:
                    all_titles.append(title)

            start_index += results_per_page
            time.sleep(self.delay)

        return all_titles

