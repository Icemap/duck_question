import math

from numpy import random
import matplotlib.pyplot as plt


def get_random_point():
    """
    获取一个在x = [-1.0, 1.0], y = [-1.0, 1.0]上的点
    检查如果在以(0, 0)为圆心，半径为1的圆外，就递归重新生成随机点

    :return: int[2] 一个在(0, 0)为圆心，半径为1的圆内的点
    """
    point = random.rand(2) * 2.0 - 1.0

    if math.sqrt(point[0] ** 2 + point[1] ** 2) > 1:
        return get_random_point()
    return point


def left(point, vector) -> bool:
    """
    计算点是否在向量所在的直线的左边：
        left_sign > 0 时，在左边;
        left_sign < 0 时，在右边;
        left_sign = 0 时，在线上（忽略）;

    :param point: int[2] 一个在(0, 0)为圆心，半径为1的圆内的点
    :param vector: int[2][2] 两个在(0, 0)为圆心，半径为1的圆内的点所组成的向量
    :return: bool 是否在左边
    """

    x1, y1, x2, y2, x, y = vector[0][0], vector[0][1], vector[1][0], vector[1][1], point[0], point[1]
    left_sign = (y1 - y2) * x + (x2 - x1) * y + x1 * y2 - x2 * y1

    return left_sign > 0


def get_four_point():
    """
    :return: int[4][2] 四个在(0, 0)为圆心，半径为1的圆内的点的数组
    """
    return [get_random_point(), get_random_point(), get_random_point(), get_random_point()]


def get_vector():
    """
    :return: int[2][2] 两个在(0, 0)为圆心，半径为1的圆内的点所组成的向量
    """
    return [get_random_point(), get_random_point()]


def all_one_side() -> bool:
    """
    获取四个点，一个向量，查看是否都在向量同边

    # show_pic 可查看生成点/向量位置

    :return: bool 是否都在同边
    """
    point_array = get_four_point()
    vector = get_vector()

    # show_pic(point_array, vector)

    first_point_side = left(point_array[0], vector)
    for i in range(1, 3):
        if first_point_side != left(point_array[i], vector):
            return False

    return True


def show_pic(point_array, vector):
    """
    生成plt示意图
    :param point_array: int[4][2] 四个在(0, 0)为圆心，半径为1的圆内的点的数组
    :param vector: int[2][2] 两个在(0, 0)为圆心，半径为1的圆内的点所组成的向量
    """
    x = [point_array[0][0], point_array[1][0], point_array[2][0], point_array[3][0]]
    y = [point_array[0][1], point_array[1][1], point_array[2][1], point_array[3][1]]
    plt.scatter(x, y, color='g', marker='o')
    plt.plot([vector[0][0], vector[1][0]], [vector[0][1], vector[1][1]], color="red")
    plt.xlim(xmin=-1, xmax=1)
    plt.ylim(ymin=-1, ymax=1)
    plt.show()


def eval_probability() -> float:
    """
    计算times次，每10000次输出一次
    :return:
    """
    times = 1000000
    true_times = 0
    for i in range(times):
        if all_one_side():
            true_times += 1
        if i % 10000 == 0 and i != 0:
            print(f"current probability: {float(true_times) / float(i)}")

    return float(true_times) / float(times)


print(eval_probability())
