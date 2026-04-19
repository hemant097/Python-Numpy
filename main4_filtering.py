import numpy as np

ages = np.array([ [21,17,19,20,16,30,18,65],
                  [39,22,15,99,18,19,20,21]])

teenagers = ages[ages<20]
adults = ages[ (ages>=20) & (ages<65) ] #using & as numpy uses C like lang
seniors = ages[ages >= 65]
print(teenagers)
print(adults)
print(seniors)

evens = ages[ages%2 == 0]
print(evens)

#if we want to retain the original shape, as the above methods flatten the array
    # .where( condition, np_array_name, placeholder_for_failing_items)
legal_ages = np.where (ages>=18 , ages, 0)

print(legal_ages)

#where is slower, so use only when necessary
