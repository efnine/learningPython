def report_status(scheduled_time, arrival_time):
    """
    (number, number) -> str

    Returns flight status(on time, early, late)

    Pre-condition: 0.0 <= scheduled_time < 24.0 and 
    0.0 <= arrival_time < 24.0
    
    >>> report_status(14.3, 14.3)
    on time
    >>> report_status(12.5, 11.5)
    early
    >>> report_status(9, 9.5)
    late
    """

    if scheduled_time == arrival_time:  
        return "on time"
    elif scheduled_time > arrival_time:
        return "early"
    else:
        return "delayed"
