import reasoner

def get_message(message_id):  # noqa: E501
    """Request stored messages and results from reasoner

     # noqa: E501

    :param message_id: Integer identifier of the message to return
    :type message_id: int

    :rtype: Message
    """
    return reasoner.get_message(message_id)

def get_message_feedback(message_id):  # noqa: E501
    """Request stored feedback for this message from reasoner

     # noqa: E501

    :param message_id: Integer identifier of the message to return
    :type message_id: int

    :rtype: MessageFeedback
    """
    return reasoner.get_message_feedback(message_id)
