import sys

temp = 'a'
workout: Dict[str, Type[Training]] = {RUN_TRAINING: Running,
                                  WALK_TRAINING: SportsWalking,
                                          SWIM_TRAINING: Swimming}
if dict.get(temp, False) == False:  # 5
    sys.exit('НЕ НАШЕЛ')
print('НАШЁЛ')




# b = dict.get('c', False) # False
# print(a, b)