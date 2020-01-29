"""
     贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
     输入：
     20 6
     电脑 200 20
     收音机 20 4
     钟 175 10
     花瓶 50 2
     书 10 1
     油画 90 9
     输出最佳盗窃方案
     """
#My idea
class Thing(object):
     def __init__(self,name,worth,weight):
          self.name = name
          self.worth = worth
          self.weight = weight
          self.value = self.worth / self.weight
     def __str__(self):
         return self.name

def get_infor():
     name,worth,weight = input().split()
     return name,int(worth),int(weight)

def main():
     things = []
     sorted_things = []
     max_carry,things_num = map(int,input().split())

     for i in range(things_num):
          new_thing = Thing(*get_infor())
          things.append(new_thing)

     for j in range(len(things)):
          max_value = things[0].value
          max_index = 0
          max_weight = things[0].weight
          for k in range(1,len(things)):
               if things[k].value > max_value or (things[k].value == max_value and things[k].weight < max_weight):
                    max_value = things[k].value
                    max_index = k
                    max_weight = things[k].weight
               else:
                    pass
          sorted_things.append(things[max_index])
          del things[max_index]
          
     '''for thing in sorted_things:
          print(thing,end = ' ')
     print(' ')'''
          
     carry = 0
     total = 0

     for thing in sorted_things:
          if carry + thing.weight <= max_carry:
               carry += thing.weight
               total += thing.worth
               print('Stolen',thing.name)
     print('Total is',total)

if __name__ == '__main__':
     main()

# ------------------------------------------------------------------------------------------
#key
class Thing(object):
         """物品"""
     
         def __init__(self, name, price, weight):
             self.name = name
             self.price = price
             self.weight = weight
     
         @property
         def value(self):
             """价格重量比"""
             return self.price / self.weight
     
     
     def input_thing():
         """输入物品信息"""
         name_str, price_str, weight_str = input().split()
         return name_str, int(price_str), int(weight_str)
     
     
     def main():
         """主函数"""
         max_weight, num_of_things = map(int, input().split())
         all_things = []
         for _ in range(num_of_things):
             all_things.append(Thing(*input_thing()))
         all_things.sort(key=lambda x: x.value, reverse=True)
         total_weight = 0
         total_price = 0
         for thing in all_things:
             if total_weight + thing.weight <= max_weight:
                 print(f'小偷拿走了{thing.name}')
                 total_weight += thing.weight
                 total_price += thing.price
         print(f'总价值: {total_price}美元')
     
     
     if __name__ == '__main__':
         main()