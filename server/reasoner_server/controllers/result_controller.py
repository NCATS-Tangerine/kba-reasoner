import reasoner

def get_result(result_id):  # noqa: E501
    """Request stored result

     # noqa: E501

    :param result_id: Integer identifier of the result to return
    :type result_id: int

    :rtype: Result
    """
    return reasoner.get_result(result_id)

def get_result_feedback(result_id):  # noqa: E501
    """Request stored feedback for this result

     # noqa: E501

    :param result_id: Integer identifier of the result to return
    :type result_id: int

    :rtype: ResultFeedback
    """
    return reasoner.get_result_feedback(result_id)

def post_result_feedback(result_id, feedback):  # noqa: E501
    """Store feedback for a particular result

     # noqa: E501

    :param result_id: Integer identifier of the result to return
    :type result_id: int
    :param feedback: Comment information
    :type feedback: dict | bytes

    :rtype: FeedbackResponse
    """
    return reasoner.post_result_feedback(result_id, feedback)
