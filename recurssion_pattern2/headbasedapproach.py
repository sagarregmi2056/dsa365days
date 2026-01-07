# print N to 1 using tail based approach
# headbased (can be used for backtracking like dfs and bfs approach may be )

def printNto1(i,n):
    if i>n:
        return
    else:
        # always remember if we use tailbased approach then it will reverse
        printNto1(i+1,n)

        # execu
        print(i)

    

printNto1(1,4)