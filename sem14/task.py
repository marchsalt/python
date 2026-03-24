def hackers_funk(hackers:list, level: int ,levelup: int ) -> int:
    count = 0
    if len(hackers) == 0:
        print("0")
    else:
        for i in hackers:
            if level < i:
                count += 1
            else:
                level += levelup
    print(count)
hackers_funk([1,2,5,7,9,2,34,5], 5 ,1)