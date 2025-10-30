#!/usr/bin/env python
"""
Gap Analysis Visualization
Creates professional charts showing education vs market demand gap

Author: Roadmap Resources Repository
Date: October 30, 2025
Version: 1.0

This script generates a grouped bar chart comparing university curriculum 
coverage versus market demand for 8 critical data science skills in Morocco.

Usage:
    python gap_analysis_charts.py

Input:
    - CSV file: ../Morocco_Market_Analysis_2025/04_Skills_Gap_Detailed.csv
    - Required columns: Skill_Category, University_Coverage, Market_Demand

Output:
    - PNG file: ../images/charts/skills_gap_analysis.png (300 DPI, 1400x700px)

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

def create_gap_analysis_chart():
    """
    Creates and saves a grouped bar chart comparing university coverage 
    vs market demand for critical data science skills.
    """
    
    # Set professional style
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (14, 8)
    plt.rcParams['font.size'] = 10
    
    # Load data
    csv_path = '../Morocco_Market_Analysis_2025/04_Skills_Gap_Detailed.csv'
    
    try:
        df = pd.read_csv(csv_path)
        print(f"✅ Data loaded: {len(df)} skills analyzed")
    except FileNotFoundError:
        print(f"❌ Error: File not found at {csv_path}")
        print("   Make sure you're in the Visualization_Scripts directory")
        return False
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Extract numeric values (remove % sign)
    try:
        uni_coverage = df['University_Coverage'].astype(str).str.rstrip('%').astype(int)
        market_demand = df['Market_Demand'].astype(str).str.rstrip('%').astype(int)
    except Exception as e:
        print(f"❌ Error processing data: {e}")
        return False
    
    # Prepare bar positions
    x = np.arange(len(df))
    width = 0.35
    
    # Create bars
    bars1 = ax.bar(x - width/2, uni_coverage, width, 
                   label='University Coverage', 
                   color='#3498db', 
                   alpha=0.8,
                   edgecolor='black',
                   linewidth=0.5)
    
    bars2 = ax.bar(x + width/2, market_demand, width,
                   label='Market Demand', 
                   color='#e74c3c', 
                   alpha=0.8,
                   edgecolor='black',
                   linewidth=0.5)
    
    # Customize chart
    ax.set_xlabel('Skills', fontsize=13, fontweight='bold')
    ax.set_ylabel('Percentage (%)', fontsize=13, fontweight='bold')
    ax.set_title('Morocco: University Coverage vs Market Demand for Data Science Skills (2025)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(df['Skill_Category'], rotation=45, ha='right', fontsize=10)
    ax.legend(fontsize=11, loc='upper left')
    ax.set_ylim(0, 105)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    def add_value_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}%',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    add_value_labels(bars1)
    add_value_labels(bars2)
    
    # Add gap annotations for critical gaps (>50%)
    for i, (uni, market) in enumerate(zip(uni_coverage, market_demand)):
        gap = market - uni
        if gap > 50:
            ax.text(i, market + 3, f'Gap: {gap}%', 
                   ha='center', fontsize=8, color='#c0392b', fontweight='bold')
    
    # Adjust layout
    plt.tight_layout()
    
    # Create output directory if it doesn't exist
    os.makedirs('../images/charts', exist_ok=True)
    
    # Save figure
    output_path = '../images/charts/skills_gap_analysis.png'
    try:
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✅ Chart saved: {output_path}")
        print(f"   Size: 1400x700 pixels, 300 DPI")
    except Exception as e:
        print(f"❌ Error saving chart: {e}")
        return False
    
    plt.show()
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("📊 Generating Gap Analysis Chart...")
    print("=" * 60)
    
    success = create_gap_analysis_chart()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ Gap Analysis Chart Generated Successfully!")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ Failed to generate chart. Check errors above.")
        print("=" * 60)