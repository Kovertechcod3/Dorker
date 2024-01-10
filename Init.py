"""
My Application Package

Provides modules for scraping, processing, and deploying data.
"""

__version__ = "1.0.0"


from .preprocessing import preprocess_dorks
from .search import scrape_google_search
from .processing import perform_keyword_search
from .deployment import deploy_application, cleanup_deployment

__all__ = [
    'preprocess_dorks',
    'scrape_google_search',
    'perform_keyword_search',
    'deploy_application', 
    'cleanup_deployment'
]

def main():
    """Executes basic workflow example"""
    
    dorks = preprocess_dorks()
    search_results = scrape_google_search(dorks)
    keywords = perform_keyword_search(search_results)
    
    deploy_dir = 'website'
    deploy_application(deploy_dir)
    
    print(f"Version {__version__}")

if __name__ == '__main__':
    main()
