import pandas as pd
import numpy as np

def filter_inflated_forks(repos_df, activities_df):
    """
    Removes repositories that are forks of large non-crypto upstreams 
    where the contributor graph is inherited from the parent.
    """
    # Identify repos that are forks
    forks = repos_df[repos_df['is_fork'] == True]
    
    # Heuristic: If a repo has a very high dev count but very low stars, 
    # and it's a fork, it's likely inheriting the upstream graph.
    # Threshold: Devs > 100 AND Stars < 10 AND (Devs/Stars > 20)
    inflated_forks = forks[
        (forks['dev_count'] > 100) & 
        (forks['stars'] < 10) & 
        (forks['dev_count'] / (forks['stars'] + 1) > 20)
    ]
    
    return repos_df[~repos_df['repo_id'].isin(inflated_forks['repo_id'])]

def filter_contribute_to_earn(repos_df, activities_df):
    """
    Detects and flags 'contribute-to-earn' patterns:
    - High fork-to-star ratio
    - Uniform low commit counts per developer
    - High overlap of developers across low-star repos
    """
    # 1. Calculate Fork/Star ratio
    repos_df['fork_star_ratio'] = repos_df['forks'] / (repos_df['stars'] + 1)
    
    # 2. Analyze commit distribution per developer per repo
    dev_commits = activities_df.groupby(['repo_id', 'developer_id']).size().reset_index(name='commit_count')
    
    # Calculate variance of commits per dev per repo
    # Low variance around a small number (e.g., ~5 commits) is a red flag
    repo_stats = dev_commits.groupby('repo_id')['commit_count'].agg(['mean', 'std', 'count']).reset_index()
    
    # Heuristic for C2E: 
    # - Mean commits between 3 and 7
    # - Low standard deviation (uniformity)
    # - High fork/star ratio (> 40)
    c2e_repos = repo_stats[
        (repo_stats['mean'] >= 3) & 
        (repo_stats['mean'] <= 7) & 
        (repo_stats['std'] < 2.0)
    ]['repo_id']
    
    # Merge with repo data to apply the fork/star ratio filter
    c2e_final = repos_df[
        (repos_df['repo_id'].isin(c2e_repos)) & 
        (repos_df['fork_star_ratio'] > 40)
    ]['repo_id']
    
    return repos_df[~repos_df['repo_id'].isin(c2e_final)]
