def c3_linearize(cls):
    linearized = [cls]
    for base in cls.__bases__:
        print('#',base)
        linearized.extend(c3_linearize(base))

    # C3 merge
    result = []
    while linearized:
        current = linearized[0]
        if all(current not in tail.__bases__ for tail in linearized[1:]):
            result.append(current)
            linearized.remove(current)
        else:
            linearized.append(linearized.pop(0))

    return result

# 示例用法
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

linearization = c3_linearize(D)
print(linearization)
