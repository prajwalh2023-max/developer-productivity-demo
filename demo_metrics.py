
def calculate_demo_metrics(merged_prs, review_hours):
    """Calculate simple demo metrics for the dashboard."""
    average_review_hours = (
        sum(review_hours) / len(review_hours)
        if review_hours else 0
    )

    return {
        "merged_pull_requests": merged_prs,
        "average_review_hours": round(average_review_hours, 2),
    }


if __name__ == "__main__":
    metrics = calculate_demo_metrics(5, [2, 4, 6, 8])
    print(metrics)
  
