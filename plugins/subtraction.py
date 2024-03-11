import plugins


class SubtractionPlugin(plugins.Base):
    @classmethod
    def operation_name(cls):
        return "subtraction"

    @classmethod
    def execute(cls, x, y):
        return x - y
