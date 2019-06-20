import numpy as np
import sys

'''get the pacman location from the board'''
def get_pacman_location(board):
    return np.where(board==3)

'''not used, was written to make it more efficiant by saving place to exact number'''
def get_number_of_valid_vert(board):
    return np.count_nonzero(board==0)+np.count_nonzero(board==2)+1


def get_all_adj(board,point):
    n = np.shape(board)[0]-1
    m = np.shape(board)[1]-1


def main(board):
    for arg in sys.argv[1:]:
        print(arg)
        b2 = np.load(arg)

    n = np.shape(board)[0]-1
    m = np.shape(board)[1]-1
    '''vert=np.zeros(get_number_of_valid_vert(board))'''
    vert_visited=np.full(np.shape(board),-1, dtype=int)
    queue=[]
    dis=[]
    s=get_pacman_location(board)
    s_x=s[0][0]
    s_y=s[1][0]
    point=(s_x,s_y)
    vert_visited[s_x,s_y]=0
    queue.append((s_x,s_y))

    while(queue):
        s=queue.pop(0)
        s_x = s[0]
        s_y = s[1]
        if s_x>0:
            if board[s_x-1][s_y]!=1 and vert_visited[s_x-1][s_y]==-1:
                vert_visited[s_x - 1][s_y] = vert_visited[s_x][s_y] + 1
                queue.append((s_x - 1,s_y))
                if board[s_x-1][s_y]==2:
                    dis.append([(s_x-1,s_y),vert_visited[s_x - 1][s_y]])
        if s_x<n:
            if board[s_x+1][s_y]!=1 and vert_visited[s_x+1][s_y]==-1:
                vert_visited[s_x +1][s_y] =vert_visited[s_x][s_y] + 1
                queue.append((s_x + 1,s_y))
                if board[s_x+1][s_y]==2:
                    dis.append([(s_x+1,s_y),vert_visited[s_x + 1][s_y]])
        if s_y>0:
            if board[s_x][s_y-1]!=1 and vert_visited[s_x][s_y-1]==-1:
                vert_visited[s_x][s_y-1] =vert_visited[s_x][s_y] + 1
                queue.append((s_x,s_y-1))
                if board[s_x][s_y-1]==2:
                    dis.append([(s_x,s_y-1),vert_visited[s_x][s_y-1]])
        if s_y<m:
            if board[s_x][s_y+1]!=1 and vert_visited[s_x][s_y+1]==-1:
                vert_visited[s_x][s_y+1] =vert_visited[s_x][s_y] + 1
                queue.append((s_x,s_y+1))
                if board[s_x][s_y+1]==2:
                    dis.append([(s_x,s_y+1),vert_visited[s_x][s_y+1]])
    print(dis)
    return dis


'''example of board'''
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(arg)
        b = np.load(arg)
    '''BOARD = np.array([[0, 0, 0, 0], [2, 1, 1, 1], [2, 1, 1, 2], [0, 0, 1, 0], [0, 0, 1, 0], [0, 3, 0, 0], [0, 0, 1, 1]])'''
    main(b)

