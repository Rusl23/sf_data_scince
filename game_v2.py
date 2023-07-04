import numpy as np

def random_predict(number:int=1) -> int:

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # number
        if number == predict_number:
            break # break cycle if we guess right 
    return(count)


def score_game(random_predict) -> int:
    """How many attempts we neded in mean for 1000 individual attempts

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: mean quantity of attempts
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воcпроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)