class MoveInterface:   
    def __move__(self, delta) -> None:
        pass

    def __move_right__(self) -> None:
        pass

    def __move_left__(self) -> None:
        pass

    def __move_up__(self) -> None:
        pass

    def __move_down__(self) -> None:
        pass

    def __stop_move__(self) -> None:
        pass

    def get_position(self) -> 'tuple[int, int]':
        pass

    def set_position(self, pos: 'tuple[int, int]') -> None:
        pass