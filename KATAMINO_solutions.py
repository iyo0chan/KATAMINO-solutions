import matplotlib.pyplot as plt
import copy
import numpy as np

def mino_print(board_list):
    for i in range(len(board_list)):
        print(board_list[i])


def mino_check(board_list, mino_part, tar_num):
    row = len(board_list)
    column = len(board_list[0])
    tar_x = tar_num//row
    tar_y = tar_num%row

    for i in range (len(mino_part)):
        x = tar_x + mino_part[i][0]  
        y = tar_y + mino_part[i][1]
        if x <=-1 or y <=-1 or row <= y or column <= x:
            return False
        if board_list[y][x] != -1:
            return False

    return True 


def mino_set(board_list, mino_part, mino_num, tar_num):
    row = len(board_list)
    tar_x = tar_num//row
    tar_y = tar_num%row
    for i in range(len(mino_part)):
        x = tar_x + mino_part[i][0]
        y = tar_y + mino_part[i][1]
        board_list[y][x] = mino_num


def mino_list_check(mino_list, board_list):
    row = len(board_list)
    column = len(board_list[0])
    for i in range (column):
        for k in range (row):
            if board_list[k][i] == -1:
                return  k+i*row
            else: 
                mino_list[board_list[k][i]] = 1
    return row*column


def mino_all_dup_chuck(board_all_list, board_list):
    row = len(board_list)
    column = len(board_list[0])
    for i in range (len(board_all_list)):
        dif_cou = 0
        for j in range(column):
            for k in range(row):
                if board_all_list[i][k][j] != board_list[k][j]:
                    dif_cou+=1
        if dif_cou ==0:
            return False
    return True


def board_mino_balance_check(board_list,mino_num):
    mino_list = [0 for x in range(mino_num)]
    row = len(board_list)
    column = len(board_list[0])
    for i in range(row):
        for k in range(column):
            mino_list[board_list[i][k]] += 1
    for i in range (mino_num):
        if mino_list[i] != 5:
            print(mino_list)
            return False
    return True


def main_arrange(board_list, board_all_list,  mimo_part_list ,mino_num):
    row = len(board_list)
    column = len(board_list[0])
    mino_list = [-1 for x in range(mino_num)]
    tar_num = mino_list_check(mino_list,board_list)
    if tar_num == row*column:
        if mino_all_dup_chuck(board_all_list,board_list):
            board_all_list.append(board_list)
            board_drawing(board_list)
        del mino_list
        del board_list
        return

    for i in range (mino_num):
        if mino_list[i] == -1:
            for k in range (len(mino_part_list[i])):
                if mino_check(board_list, mino_part_list[i][k], tar_num):
                    next_board_list = copy.deepcopy(board_list)
                    mino_set(next_board_list, mino_part_list[i][k], i, tar_num)
                    main_arrange(next_board_list, board_all_list,  mimo_part_list ,mino_num)
                  
    del mino_list


def board_drawing(matrix):
    plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.gist_ncar)
    plt.xticks(np.arange(len(matrix[0])), range(len(matrix[0])), rotation=90)
    plt.yticks(np.arange(len(matrix)), range(len(matrix)))
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    dim_columns = 12
    dim_row = 5
    board_list = [[-1 for x in range(dim_columns)] for i in range(dim_row)]
    board_all_list = []

    mino_num = 12
    mino_list = [-1 for x in range(mino_num)]

    mino_part_list = [   
                        [[[0,0],[1,0],[2,0],[3,0],[4,0]],
                        [[0,0],[0,1],[0,2],[0,3],[0,4]]],

                        [[[0,0],[0,1],[1,0],[2,0],[3,0]],
                        [[0,0],[0,1],[0,2],[0,3],[1,3]],
                        [[0,0],[3,-1],[1,0],[2,0],[3,0]],
                        [[0,0],[1,0],[1,1],[1,2],[1,3]],
                        [[0,0],[0,1],[1,1],[2,1],[3,1]],
                        [[0,0],[1,0],[1,-1],[1,-2],[1,-3]],
                        [[0,0],[1,0],[2,0],[3,0],[3,1]],
                        [[0,0],[0,1],[1,0],[0,2],[0,3]]],
                        #2
                        [[[0,0],[1,1],[1,0],[2,0],[3,0]],
                        [[0,0],[0,1],[0,2],[0,3],[1,2]],
                        [[0,0],[2,-1],[1,0],[2,0],[3,0]],
                        [[0,0],[1,-1],[1,0],[1,2],[1,1]],
                        [[0,0],[1,0],[2,0],[3,0],[1,-1]],
                        [[0,0],[1,0],[1,-1],[1,1],[1,-2]],
                        [[0,0],[1,0],[2,0],[3,0],[2,1]],
                        [[0,0],[0,1],[1,1],[0,2],[0,3]]],
                        #3
                        [[[0,0],[2,1],[1,0],[2,0],[3,1]],
                        [[0,0],[0,1],[0,2],[1,0],[1,-1]],
                        [[0,0],[1,1],[1,0],[2,1],[3,1]],
                        [[0,0],[0,1],[1,0],[1,-1],[1,-2]],
                        [[0,0],[1,0],[2,0],[2,-1],[3,-1]],
                        [[0,0],[0,1],[1,1],[1,2],[1,3]],
                        [[0,0],[1,0],[1,-1],[2,-1],[3,-1]],
                        [[0,0],[0,1],[0,2],[1,2],[1,3]]],
                        #4
                        [[[0,0],[0,1],[1,0],[2,0],[0,2]],
                        [[0,0],[0,1],[0,2],[1,2],[2,2]],
                        [[0,0],[2,0],[1,0],[2,-1],[2,-2]],
                        [[0,0],[2,0],[1,0],[2,1],[2,2]]],
                        #5
                        [[[0,0],[1,1],[1,0],[0,1],[2,0]],
                        [[0,0],[0,1],[0,2],[1,1],[1,2]],
                        [[0,0],[2,0],[1,0],[2,-1],[1,-1]],
                        [[0,0],[0,1],[1,0],[1,1],[1,2]],
                        [[0,0],[1,0],[2,1],[1,1],[0,1]],
                        [[0,0],[1,0],[1,1],[0,1],[1,-1]],
                        [[0,0],[1,0],[2,0],[1,1],[2,1]],
                        [[0,0],[0,1],[1,0],[1,1],[0,2]]],

                        #6
                        [[[0,0],[0,1],[1,0],[2,0],[2,1]],
                        [[0,0],[0,1],[0,2],[1,0],[1,2]],
                        [[0,0],[2,0],[0,1],[1,1],[2,1]],
                        [[0,0],[1,0],[1,1],[1,2],[0,2]]],

                        #7
                        [[[0,0],[1,1],[1,0],[1,2],[2,2]],
                        [[0,0],[0,1],[1,0],[2,0],[2,-1]],
                        [[0,0],[1,0],[1,-1],[1,-2],[2,-2]],
                        [[0,0],[0,1],[1,1],[2,1],[2,2]]],

                        #8
                        [[[0,0],[1,1],[1,0],[2,1],[1,2]],
                        [[0,0],[0,1],[1,0],[2,0],[1,-1]],
                        [[0,0],[1,0],[1,-1],[1,1],[2,1]],
                        [[0,0],[1,0],[2,0],[2,-1],[1,1]],
                        [[0,0],[1,0],[1,-1],[1,-2],[2,-1]],
                        [[0,0],[1,0],[2,0],[1,-1],[2,1]],
                        [[0,0],[1,0],[1,1],[1,-1],[2,-1]],
                        [[0,0],[0,1],[1,1],[2,1],[1,2]]],

                        #9
                        [[[0,0],[1,1],[1,0],[2,0],[1,2]],
                        [[0,0],[0,1],[0,2],[1,1],[2,1]],
                        [[0,0],[1,0],[2,0],[1,-1],[1,-2]],
                        [[0,0],[1,0],[2,0],[2,1],[2,-1]]],

                        #10
                        [[[0,0],[1,1],[1,0],[2,1],[2,2]],
                        [[0,0],[0,1],[1,0],[1,-1],[2,-1]],
                        [[0,0],[0,1],[1,1],[1,2],[2,2]],
                        [[0,0],[1,0],[1,-1],[2,-1],[2,-2]]],

                        #11
                        [[[0,0],[1,0],[1,-1],[1,1],[2,0]]]
                                                                ]


    main_arrange(board_list, board_all_list,  mino_part_list ,mino_num)
    print("解の数 = ",len(board_all_list))
