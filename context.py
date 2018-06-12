class ContextStorage:
    def __init__(self):
        self.context = {}

    def init_context(self, user_id):
        """
        Устанавливает пустой контекст
        :param user_id: ИД пользователя
        :return:
        """
        self.context[user_id] = {}
        self.context[user_id]['system_context'] = None

    def get_context(self, user_id):
        """
        Получение контекста указанного пользователя
        :param user_id: ИД пользователя
        :return: Словарь
        """
        if user_id not in self.context:
            self.init_context(user_id)
        return self.context[user_id]

    def set_context(self, user_id, context):
        """
        Получение контекста указанного пользователя
        :param user_id: ИД пользователя
        :param context: Контекст общий
        :return: Словарь
        """
        if user_id not in self.context:
            self.init_context(user_id)
        self.context[user_id] = context

    def clear_context(self, user_id):
        """
        Очистка контекста у пользователя
        :param user_id: ИД пользователя
        :return: None
        """
        self.init_context(user_id)

    def set_system_context(self, user_id, context):
        """
        Добавление системного контекста
        :param user_id: ИД пользователя
        :param context: Объект с системным контекстом
        :return: None
        """
        if user_id not in self.context:
            self.init_context(user_id)
        self.context[user_id]['system_context'] = context

    def get_system_context(self, user_id):
        if user_id not in self.context:
            self.init_context(user_id)

        return self.context[user_id]['system_context']



