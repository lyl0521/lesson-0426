from lesson.day05.built_in_test import multi_return

print(multi_return(1,2))


def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Error...')
    if x > 0 :
        return x
    else:
        return -x


print(my_abs(-1))


def fn_append(array = []):  #default argument value is mutable
    array.append('END')
    return array


print(fn_append([1,2,3]))

print(fn_append())
print(fn_append())