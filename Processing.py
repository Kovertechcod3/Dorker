def perform_keyword_search(results, keyword):
    matching_results = []
    for result in results:
        if keyword in result['snippet']:
            matching_results.append(result)
    return matching_results
