def calculate_score(issues: list) -> float:
    """
    Start from 100 and deduct 20 points per issue.
    The minimum score is 0.
    """
    score = 100 - (len(issues) * 20)
    return float(max(0, score))


def calculate_confidence_score(issues: list) -> int:
    """
    Return an integer confidence score based on issue count.
    """
    score = 100 - (len(issues) * 20)
    return max(0, score)
