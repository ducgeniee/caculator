import plugins


class MultiplicationPlugin(plugins.Base):
    @classmethod
    def operation_name(cls):
        return "multiplication"

    @classmethod
    def execute(cls,x, y):
        return x * y
