#!/usr/bin/env python
"""
Job Market Visualization
Creates professional charts showing job distribution and salary analysis

Author: Roadmap Resources Repository
Date: October 30, 2025
Version: 1.0

This script generates two side-by-side visualizations:
1. Pie chart showing distribution of job positions by type
2. Bar chart showing average salaries by position

Usage:
    python job_market_visualization.py

Input:
    - CSV file: ../Morocco_Market_Analysis_2025/05_Job_Market_Morocco_2025.csv
    - Required columns: Job_Title, Job_Postings_Available, Avg_Monthly_Salary_MAD

Output:
    - PNG file: ../images/charts/job_market_analysis.png (300 DPI, 1400x700px)

Requirements:
    - pandas
    - matplotlib
    - seaborn
    - numpy
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_job_market_visualization():
    """
    Creates and saves job market distribution and salary analysis charts.
    """
    
    # Set professional style
    sns.set_style("whitegrid")
    plt.rcParams['font.size'] = 10
    
    # Load data
    csv_path = '../Morocco_Market_Analysis_2025/05_Job_Market_Morocco_2025.csv'
    
    try:
        df = pd.read_csv(csv_path)
        print(f"✅ Data loaded: {len(df)} job positions analyzed")
    except FileNotFoundError:
        print(f"❌ Error: File not found at {csv_path}")
        print("   Make sure you're in the Visualization_Scripts directory")
        return False
    
    # Create figure with 2 subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Extract data
    job_titles = df['Job_Title'].tolist()
    postings = df['Job_Postings_Available'].astype(int).tolist()
    salaries = df['Avg_Monthly_Salary_MAD'].astype(int).tolist()
    
    # Define colors
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c', '#e67e22']
    colors = colors[:len(job_titles)]
    
    # ===== SUBPLOT 1: PIE CHART (Job Distribution) =====
    wedges, texts, autotexts = ax1.pie(postings, 
                                         labels=job_titles,
                                         autopct='%1.1f%%',
                                         colors=colors,
                                         startangle=90,
                                         textprops={'fontsize': 9})
    
    # Make percentage text bold
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    ax1.set_title('Job Market Distribution by Position Type\n(% of Active Postings)', 
                  fontsize=12, fontweight='bold', pad=15)
    
    # ===== SUBPLOT 2: BAR CHART (Salary Comparison) =====
    bars = ax2.bar(range(len(job_titles)), salaries, color=colors, 
                   edgecolor='black', linewidth=0.5, alpha=0.8)
    
    # Add average line
    avg_salary = np.mean(salaries)
    ax2.axhline(y=avg_salary, color='red', linestyle='--', linewidth=2, 
                label=f'Average: {int(avg_salary):,} MAD', alpha=0.7)
    
    # Customize bar chart
    ax2.set_xlabel('Job Position', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Average Monthly Salary (MAD)', fontsize=11, fontweight='bold')
    ax2.set_title('Average Entry-Level Salaries by Position', 
                  fontsize=12, fontweight='bold', pad=15)
    ax2.set_xticks(range(len(job_titles)))
    ax2.set_xticklabels([title.replace(' ', '\n') for title in job_titles], 
                         rotation=0, ha='center', fontsize=9)
    ax2.legend(fontsize=10, loc='upper left')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    for bar, salary in zip(bars, salaries):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(salary):,} MAD',
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Format y-axis as thousands
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))
    
    # Adjust layout
    plt.tight_layout()
    
    # Create output directory if needed
    os.makedirs('../images/charts', exist_ok=True)
    
    # Save figure
    output_path = '../images/charts/job_market_analysis.png'
    try:
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✅ Chart saved: {output_path}")
        print(f"   Size: 1400x600 pixels, 300 DPI")
    except Exception as e:
        print(f"❌ Error saving chart: {e}")
        return False
    
    plt.show()
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("💼 Generating Job Market Analysis Charts...")
    print("=" * 60)
    
    success = create_job_market_visualization()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ Job Market Charts Generated Successfully!")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ Failed to generate charts. Check errors above.")
        print("=" * 60)