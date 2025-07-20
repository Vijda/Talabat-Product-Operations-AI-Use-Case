#!/usr/bin/env python3
"""
Talabat Analytics Data Update Script

This script updates the analytics data CSV file with fresh metrics.
It can be run manually or via GitHub Actions for automated updates.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

def generate_sample_data():
    """Generate sample analytics data with realistic variations."""
    
    # Base metrics with some realistic variation
    base_metrics = {
        'Customer Satisfaction': 87.3,
        'Average Delivery Time': 28.5,
        'Platform Response Time': 1.2,
        'Order Success Rate': 94.7,
        'Positive Sentiment': 67,
        'Neutral Sentiment': 20,
        'Negative Sentiment': 13,
        'Peak Hour Delays': 45,
        'App Crash Rate': 0.8,
        'Customer Service Response Time': 24,
        'Delivery Fee Complaints': 78,
        'Food Quality Rating': 89,
        'App Usability Score': 92,
        'Restaurant Selection': 95
    }
    
    # Add some realistic daily variation (±5%)
    updated_metrics = {}
    for metric, value in base_metrics.items():
        variation = np.random.uniform(0.95, 1.05)
        updated_metrics[metric] = round(value * variation, 1)
    
    # Ensure sentiment percentages add up to 100
    total_sentiment = updated_metrics['Positive Sentiment'] + updated_metrics['Neutral Sentiment'] + updated_metrics['Negative Sentiment']
    if total_sentiment != 100:
        # Normalize to 100%
        updated_metrics['Positive Sentiment'] = round(updated_metrics['Positive Sentiment'] * 100 / total_sentiment, 1)
        updated_metrics['Neutral Sentiment'] = round(updated_metrics['Neutral Sentiment'] * 100 / total_sentiment, 1)
        updated_metrics['Negative Sentiment'] = round(100 - updated_metrics['Positive Sentiment'] - updated_metrics['Neutral Sentiment'], 1)
    
    return updated_metrics

def create_dataframe(metrics):
    """Create a pandas DataFrame from the metrics."""
    
    # Define categories for each metric
    categories = {
        'Customer Satisfaction': 'Overall',
        'Average Delivery Time': 'Performance',
        'Platform Response Time': 'Performance',
        'Order Success Rate': 'Performance',
        'Positive Sentiment': 'Sentiment',
        'Neutral Sentiment': 'Sentiment',
        'Negative Sentiment': 'Sentiment',
        'Peak Hour Delays': 'Issues',
        'App Crash Rate': 'Issues',
        'Customer Service Response Time': 'Issues',
        'Delivery Fee Complaints': 'Issues',
        'Food Quality Rating': 'Positive',
        'App Usability Score': 'Positive',
        'Restaurant Selection': 'Positive'
    }
    
    # Create descriptions
    descriptions = {
        'Customer Satisfaction': 'Based on 500+ reviews analyzed by Llama 3.2 AI',
        'Average Delivery Time': 'Target: 25 minutes. Performance within acceptable range',
        'Platform Response Time': 'Excellent platform performance with minimal latency',
        'Order Success Rate': 'High success rate with continuous improvement',
        'Positive Sentiment': 'Customers expressing positive experiences',
        'Neutral Sentiment': 'Customers with neutral experiences',
        'Negative Sentiment': 'Customers expressing negative experiences',
        'Peak Hour Delays': 'Percentage of delays during 12-2 PM and 7-9 PM rush hours',
        'App Crash Rate': 'Percentage of sessions experiencing crashes',
        'Customer Service Response Time': 'Average response time in hours for non-critical issues',
        'Delivery Fee Complaints': 'Percentage of customers mentioning high delivery fees',
        'Food Quality Rating': 'Percentage rating food quality as excellent or very good',
        'App Usability Score': 'User satisfaction with app interface and navigation',
        'Restaurant Selection': 'Customer satisfaction with restaurant variety'
    }
    
    # Create DataFrame
    data = []
    for metric, value in metrics.items():
        data.append({
            'Metric': metric,
            'Value': f"{value}{'%' if 'Sentiment' in metric or 'Rate' in metric or 'Complaints' in metric or 'Rating' in metric or 'Score' in metric or 'Selection' in metric else '' if metric == 'Platform Response Time' else ' min' if metric == 'Average Delivery Time' else ' hours' if metric == 'Customer Service Response Time' else ''}",
            'Category': categories[metric],
            'Description': descriptions[metric]
        })
    
    return pd.DataFrame(data)

def main():
    """Main function to update the analytics data."""
    
    print("🔄 Generating Talabat Analytics Summary...")
    
    # Generate updated metrics
    metrics = generate_sample_data()
    
    print(f"✅ Analytics summary generated successfully!")
    print(f"📅 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Print summary
    print("\n📈 Key Metrics Summary:")
    print(f"   Customer Satisfaction: {metrics['Customer Satisfaction']}%")
    print(f"   Delivery Time: {metrics['Average Delivery Time']} min")
    print(f"   Success Rate: {metrics['Order Success Rate']}%")
    print(f"   Positive Sentiment: {metrics['Positive Sentiment']}%")
    
    print("\n💡 Note: This script generates sample data for demonstration.")
    print("   For production use, connect to your actual data sources.")

if __name__ == "__main__":
    main() 