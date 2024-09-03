def solution(A):
    east_car_acc = 0
    pass_acc = 0
    for car in A:
        if car == 0:
            east_car_acc += 1
        elif car == 1:
            pass_acc += east_car_acc
        if pass_acc > 1_000_000_000:
            return -1
    return pass_acc