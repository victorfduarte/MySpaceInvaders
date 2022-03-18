class MoveInterface: 
    def get_position(self) -> 'tuple[int, int]':
        '''*Abstract Function*\n
        Retorna a posição X, Y do objeto
        '''
        pass

    def set_position(self, pos: 'tuple[int, int]') -> None:
        '''*Abstract Function*\n
        Seta a posição X, Y do objeto
        '''
        pass