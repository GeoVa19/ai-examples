from tree import tree

def minimax(node, maxPlayer):
    # base case of recursion: returns when node is of int type
    if isinstance(node, int):
        return node

    if maxPlayer: # MAX player
        value = -999 # an arbitrary low value
        for child in node:
            v = minimax(child, False)
            value = max(value, v)
        print("MAX best value:", value)
        return value
    else: # MIN player
        value = 999 # an arbitrary high value
        for child in node:
            v = minimax(child, True)
            value = min(value, v)
        print("MIN best value:", value)
        return value

print("Final value:", minimax(tree, True))
