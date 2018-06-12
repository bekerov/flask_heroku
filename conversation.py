# -*- coding: utf-8 -*-

import os
import settings
from watson_developer_cloud import ConversationV1

WORKSPACE_ID = os.environ.get("CONVERSATION_API_WORKSPACE_ID")

conversation = ConversationV1(
    username=os.environ.get("CONVERSATION_API_USERNAME"),
    password=os.environ.get("CONVERSATION_API_PASSWORD"),
    version=os.environ.get("CONVERSATION_API_VERSION")
)


def get_intents():
    """
    Список интентов
    :return:
    """
    intents = conversation.list_intents(WORKSPACE_ID)['intents']
    return intents


def update_intens(intent, examples=[]):
    """
    Загрузка списка интентов в Watson Conversation
    :param intens: Список интентов
    :return:
    """
    conversation.update_intent(workspace_id=WORKSPACE_ID, intent=intent, new_examples=examples, new_description='Updated intent')


def send_message(text, context={}):
    """
    Отправка сообщения в Watson Conversation
    :param text: Текстовая строка
    :return:
    """

    response = conversation.message(
        workspace_id=WORKSPACE_ID,
        message_input={'text': text},
        context=context
    )

    return response


def get_entities(text):
    """
    Выделение сущностей через Watson Conversation
    Args:
        text:

    Returns:
    """
    response = conversation.message(
        workspace_id=WORKSPACE_ID,
        message_input={'text': text},
    )

    return response['context']
