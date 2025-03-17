from typing import List
def one_way_stairs(no_stairs: int, steps: List[int])-> List[int]:
    """_Find one combination up a stairs given a height and allowed steps at a time_

    Args:
        no_stairs (int): _Number of stairs_
        steps (List[int]): _Allowed steps at a time_

    Returns:
        List[int]: _A list of combination of steps up the stairs_
    """
    one_way_table: List[int] = [None for _ in range(no_stairs)]
    return one_way_table[no_stairs]