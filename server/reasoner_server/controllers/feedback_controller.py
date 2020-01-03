import reasoner

def get_feedback_all():  # noqa: E501
    """Request a list of all feedback provided thus far

     # noqa: E501


    :rtype: List[Feedback]
    """
    return reasoner.get_feedback_all()

def get_feedback_expertise_levels():  # noqa: E501
    """Request a list of allowable expertise levels

     # noqa: E501


    :rtype: ExpertiseLevels
    """
    return reasoner.get_feedback_expertise_levels()

def get_feedback_ratings():  # noqa: E501
    """Request a list of allowable ratings

     # noqa: E501


    :rtype: Ratings
    """
    return reasoner.get_feedback_ratings()
