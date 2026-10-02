from src.data_pipeline.filters.repo_filters import filter_inflated_forks, filter_contribute_to_earn

def process_ecosystem_data(repos_df, activities_df):
    # ... existing preprocessing ...
    
    # Apply new filters to prevent developer count inflation
    print("Filtering inflated forks from non-crypto upstreams...")
    repos_df = filter_inflated_forks(repos_df, activities_df)
    
    print("Filtering contribute-to-earn program activity...")
    repos_df = filter_contribute_to_earn(repos_df, activities_df)
    
    # Filter activities to only include remaining valid repos
    activities_df = activities_df[activities_df['repo_id'].isin(repos_df['repo_id'])]
    
    # ... rest of the pipeline ...
    return repos_df, activities_df
