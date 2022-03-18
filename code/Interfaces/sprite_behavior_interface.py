class SpriteBehaviorInterface:
    def kill(self) -> None:
        '''*Abstract Function*\n
        Desfaz o comportamento'''
        pass

    def get_name(self) -> str:
        '''*Abstract Function*\n
        Retorna o nome do comportamento'''
        pass