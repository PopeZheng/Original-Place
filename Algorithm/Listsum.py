 说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值，例如：
     >
     > 输入：1 -2 3 5 -3 2
     >
     > 输出：8
     >
     > 输入：0 -2 3 5 -1 2
     >
     > 输出：9
     >
     > 输入：-9 -2 -3 -5 -3
     >
     > 输出：-2

#My idea
def max_succession(list1):
     max_list = []
     for i in range(len(list1)):
          for j in range(i,len(list1)):
               total = 0
               for n in range(i,j+1):
                    total += list1[n]
               max_list.append(total)
     max_list.sort()
     return max_list[len(max_list) -1]
     
def get_infor():
    list1 = []
    current = input().split()
    for char in current:
        list1.append(int(char))
    return list1

def main():
    list1 = get_infor()
    print(max_succession(list1))
    
if __name__ == '__main__':
    main()



#------------------------------------------------------------------------



def main():
     items = list(map(int, input().split()))
     size = len(items)
     overall, partial = {}, {}
     overall[size - 1] = partial[size - 1] = items[size - 1]
     for i in range(size - 2, -1, -1):
          partial[i] = max(items[i], partial[i + 1] + items[i])
          overall[i] = max(partial[i], overall[i + 1])
     print(overall[0])
     
     
if __name__ == '__main__':
     main()
