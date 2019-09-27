from tree import tree

def alphabeta(node, alpha, beta, maxPlayer):
    # base case of recursion: returns when node is of int type
    if isinstance(node, int):
        return node

    if maxPlayer: # MAX player
        value = -999 # an arbitrary low value
        for child in node:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else: # MIN player
        value = 999 # an arbitrary high value
        for child in node:
            value = min(value, alphabeta(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

print("Final value:", alphabeta(tree, -999, 999, True))
