"""
xing_scraping_helper.py
This module provides functions to fetch job data from the Xing API and extract relevant job details.
"""
import requests

API_URL = "https://www.xing.com/graphql/api"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Referer": "https://www.xing.com/jobs/search",
    "Origin": "https://www.xing.com",
}

def fetch_jobs(limit, offset):
    """
    Sends a POST request to the Xing API to fetch job data.

    Args:
        limit (int): Number of jobs per request.
        offset (int): Offset for pagination.

    Returns:
        list: List of job dictionaries (or empty list if request fails).
    """
    payload = {
        "operationName": "JobSearchByQuery",
        "variables": {
            "query": {
                "filter": {
                    "careerLevel": {"id": ["2.24d1f6", "3.2ebf16"]},
                    "country": {"id": ["de.02516e"]},
                    "discipline": {"id": ["1011.6cf3f7"]},
                    "employmentType": {"id": ["FULL_TIME.ef2fe9"]},
                    "industry": {"id": ["200300.efce6c", "90100.a8b7b7"]},
                    "salary": {"max": 189000, "min": 5000}
                }
            },
            "consumer": "loggedout.web.jobs.search_results.center",
            "sort": "date",
            "limit": limit,
            "offset": offset,
            "trackRecent": True,
            "searchMode": "NORMAL"
        },
            "query": "query JobSearchByQuery($query: JobSearchQueryInput!, $consumer: String!, $offset: Int, $limit: Int, $sort: String, $trackRecent: Boolean, $searchMode: SearchMode) {\n  jobSearchByQuery(\n    query: $query\n    consumer: $consumer\n    offset: $offset\n    limit: $limit\n    sort: $sort\n    searchMode: $searchMode\n    trackRecent: $trackRecent\n    returnAggregations: true\n    splitBenefit: true\n  ) {\n    total\n    searchQuery {\n      guid\n      body {\n        ...JobSearchQueryBodySplitBenefits\n        __typename\n      }\n      __typename\n    }\n    appliedFilters {\n      extractedFilters {\n        enabled {\n          ...ExtractedFiltersEnabled\n          __typename\n        }\n        disabled {\n          ...ExtractedFiltersDisabled\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    collection {\n      ...JobItemResult\n      __typename\n    }\n    aggregations {\n      employmentTypes {\n        ...EmploymentTypeAggregation\n        __typename\n      }\n      careerLevels {\n        ...CareerLevelAggregation\n        __typename\n      }\n      disciplines {\n        ...DisciplineAggregation\n        __typename\n      }\n      industries {\n        ...IndustryAggregation\n        __typename\n      }\n      benefitsEmployeePerk {\n        ...BenefitAggregation\n        __typename\n      }\n      benefitsWorkingCulture {\n        ...BenefitAggregation\n        __typename\n      }\n      countries {\n        ...CountryAggregation\n        __typename\n      }\n      cities {\n        ...CityAggregation\n        __typename\n      }\n      remoteOptions {\n        ...RemoteOptionAggregation\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CompanyFilter on JobFilterCompany {\n  company {\n    companyName\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment EmploymentTypeFilter on JobFilterEmploymentType {\n  employmentType {\n    localizationValue\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment CareerLevelFilter on JobFilterCareerLevel {\n  careerLevel {\n    localizationValue\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment DisciplineFilter on JobFilterDiscipline {\n  discipline {\n    localizationValue\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment IndustryFilter on JobFilterIndustry {\n  industry {\n    localizationValue\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment BenefitEmployeePerkFilter on JobFilterBenefitEmployeePerk {\n  benefitEmployeePerk {\n    localizationValue\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment BenefitWorkingCultureFilter on JobFilterBenefitWorkingCulture {\n  benefitWorkingCulture {\n    localizationValue\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment CountryFilter on JobFilterCountry {\n  country {\n    localizationValue\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment CityFilter on JobFilterCity {\n  city {\n    localizationValue: name\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment SalaryFilter on JobFilterSalary {\n  min\n  max\n  __typename\n}\n\nfragment RemoteOptionFilter on JobFilterRemoteOption {\n  remoteOption {\n    localizationValue\n    __typename\n  }\n  entityId\n  __typename\n}\n\nfragment JobSearchFilterCollectionSplitBenefits on JobFilterCollection {\n  ...CompanyFilter\n  ...EmploymentTypeFilter\n  ...CareerLevelFilter\n  ...DisciplineFilter\n  ...IndustryFilter\n  ...BenefitEmployeePerkFilter\n  ...BenefitWorkingCultureFilter\n  ...CountryFilter\n  ...CityFilter\n  ...SalaryFilter\n  ...RemoteOptionFilter\n  __typename\n}\n\nfragment Salary on Salary {\n  currency\n  amount\n  __typename\n}\n\nfragment SalaryRange on SalaryRange {\n  currency\n  minimum\n  maximum\n  __typename\n}\n\nfragment SalaryEstimate on SalaryEstimate {\n  currency\n  minimum\n  maximum\n  median\n  __typename\n}\n\nfragment VisibleJobCommon on VisibleJob {\n  id\n  slug\n  url\n  title\n  activatedAt\n  refreshedAt\n  globalId\n  location {\n    city\n    __typename\n  }\n  employmentType {\n    localizationValue\n    __typename\n  }\n  companyInfo {\n    companyNameOverride\n    company {\n      id\n      logos {\n        x1: logo96px\n        __typename\n      }\n      kununuData {\n        ratingAverage\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  salary {\n    ...Salary\n    ...SalaryRange\n    ...SalaryEstimate\n    __typename\n  }\n  __typename\n}\n\nfragment JobTeaserVisibleJob on VisibleJob {\n  ...VisibleJobCommon\n  userInteractions {\n    bookmark {\n      state\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment JobKeyfactV2 on JobMatchingHighlightsJobKeyfactV2 {\n  __typename\n  type\n  localization {\n    localizationValue\n    __typename\n  }\n  localizationA11y {\n    localizationValue\n    __typename\n  }\n  ... on JobMatchingHighlightsJobKeyfactSalaryV2 {\n    value {\n      ...Salary\n      ...SalaryRange\n      ...SalaryEstimate\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment JobMatchingHighlightsV2 on JobMatchingHighlightsV2 {\n  token\n  highlight {\n    type\n    localization {\n      localizationValue\n      __typename\n    }\n    localizationA11y {\n      localizationValue\n      __typename\n    }\n    __typename\n  }\n  matchingFacts {\n    ...JobKeyfactV2\n    __typename\n  }\n  nonMatchingFacts {\n    ...JobKeyfactV2\n    __typename\n  }\n  __typename\n}\n\nfragment JobSearchQueryBodySplitBenefits on JobSearchQueryBody {\n  keywords\n  location {\n    text\n    radius\n    city {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  filterCollection {\n    ...JobSearchFilterCollectionSplitBenefits\n    __typename\n  }\n  __typename\n}\n\nfragment ExtractedFiltersEnabled on JobExtractedFilterEnabledCollection {\n  ...CareerLevelFilter\n  ...EmploymentTypeFilter\n  ...SalaryFilter\n  ...RemoteOptionFilter\n  ... on JobFilterLocation {\n    location {\n      localizationValue\n      radius\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ExtractedFiltersDisabled on JobExtractedFilterDisabledCollection {\n  ...CareerLevelFilter\n  ...EmploymentTypeFilter\n  ... on JobFilterDisabledSalary {\n    salary\n    __typename\n  }\n  ...RemoteOptionFilter\n  ... on JobFilterLocation {\n    location {\n      localizationValue\n      radius\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment JobItemResult on JobItemResult {\n  trackingToken\n  position\n  descriptionHighlight\n  jobDetail {\n    ...JobTeaserVisibleJob\n    __typename\n  }\n  matchingHighlightsV2 {\n    ...JobMatchingHighlightsV2\n    __typename\n  }\n  __typename\n}\n\nfragment EmploymentTypeAggregation on JobAggregationEmploymentType {\n  count\n  id\n  employmentType {\n    localizationValue\n    __typename\n  }\n  __typename\n}\n\nfragment CareerLevelAggregation on JobAggregationCareerLevels {\n  count\n  id\n  careerLevel {\n    localizationValue\n    __typename\n  }\n  __typename\n}\n\nfragment DisciplineAggregation on JobAggregationDiscipline {\n  count\n  id\n  discipline {\n    localizationValue\n    __typename\n  }\n  __typename\n}\n\nfragment IndustryAggregation on JobAggregationIndustry {\n  count\n  id\n  industry {\n    localizationValue\n    __typename\n  }\n  __typename\n}\n\nfragment BenefitAggregation on JobAggregationBenefit {\n  count\n  id\n  benefit {\n    localizationValue\n    __typename\n  }\n  __typename\n}\n\nfragment CountryAggregation on JobAggregationCountry {\n  count\n  id\n  country {\n    localizationValue\n    __typename\n  }\n  __typename\n}\n\nfragment CityAggregation on JobAggregationCity {\n  count\n  id\n  city {\n    localizationValue: name\n    __typename\n  }\n  __typename\n}\n\nfragment RemoteOptionAggregation on JobAggregationRemoteOption {\n  id\n  remoteOption {\n    localizationValue\n    __typename\n  }\n  __typename\n}\n"
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("jobSearchByQuery", {}).get("collection", [])
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

def extract_job_data(job):
    """
    Extracts job details from the job dictionary.

    Args:
        job (dict): Job data from API response.

    Returns:
        dict: Extracted job details.
    """
    return {
        "title": job.get("jobDetail", {}).get("title", "N/A"),
        "refreshed_at": job.get("jobDetail", {}).get("refreshedAt", "N/A"),
        "location": job.get("jobDetail", {}).get("location", {}).get("city", "N/A"),
        "company": job.get("jobDetail", {}).get("companyInfo", {}).get("companyNameOverride", "N/A"),
        "min_salary": job.get("jobDetail", {}).get("salary", {}).get("min", "N/A"),
        "max_salary": job.get("jobDetail", {}).get("salary", {}).get("max", "N/A")
    }
