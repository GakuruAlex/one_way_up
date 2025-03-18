from typing import List
def one_way_stairs(no_stairs: int, steps: List[int])-> List[int]:
    """_Find one combination up a stairs given a height and allowed steps at a time_

    Args:
        no_stairs (int): _Number of stairs_
        steps (List[int]): _Allowed steps at a time_

    Returns:
        List[int]: _A list of combination of steps up the stairs_
    """
    one_way_table: List[int] = [None for _ in range(no_stairs  + 1)]
    one_way_table[0] = []
    one_way_table[1] = [1]
    for index in range(1, no_stairs + 1):
        if one_way_table[index] != None:
            for step in steps:
                if index + step < len(one_way_table):
                     new =one_way_table[index][:]
                     new.append(step)
                     one_way_table[index + step] = new
    return one_way_table[no_stairs]

def main()-> None:
    steps: List[int] = [1,2]
    height: int = 5
    one_way: List[int] = one_way_stairs(no_stairs= height, steps= steps)
    print(f"One way up a stairs of height {height}, given the steps to take at a time can be either of {steps} is {one_way}")

if __name__ =="__main__":
    main()