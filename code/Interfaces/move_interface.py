class MoveInterface: 
    def get_position(self) -> 'tuple[int, int]':
        '''*Abstract Function*\n
        Retorna a posição X, Y do objeto
        '''
        pass

    def move(self, pos: 'tuple[int, int]') -> None:
        '''*Abstract Function*\n
        Move o objeto para a posição especificada. Pode implementar verificações que
        permitam ou não a movimentação.'''
        pass