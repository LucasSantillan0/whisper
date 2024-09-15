class Message:
    def __init__(self, **kwargs ) :
        self.role = kwargs.get('role', 'user')
        self.content = kwargs.get('content', '')
    def getText (self:'Message') -> str:
        return self.content