tree = [[3,5], [6,9], [1,2], [0,-1]]

INF = float("inf")

def alphabeta(node, is_max, alpha, beta, level=0) :
    indent = "  " * level
    if not isinstance(node, list) :
        print(f"{indent}Leaf : {node}")
        return node

    if is_max :
        best = -INF
        for i, child in enumerate(node) :
            value = alphabeta(child, False, alpha, beta, level+1)
            best = max(best, value)
            alpha = max(alpha, best)
            print(f"{indent}Max : best={best}, alpha={alpha}, beta={beta}")
            if beta <= alpha :
                print(f"{indent}>>> PRUNED {len(node) - i - 1} branch(es)")
                break
        return best

    else :
        best = INF
        for i, child in enumerate(node) :
            value = alphabeta(child, True, alpha, beta, level+1)
            best = min(best, value)
            beta = min(beta, best)
            print(f"{indent}MIN : best={best}, alpha={alpha}, beta={beta}")
            if beta <= alpha :
                print(f"{indent}>>> PRUNED {len(node) - i - 1} branch(es)")
                break
        return best

if __name__ == "__main__" :
    print("Tree : ", tree, "\n")
    result = alphabeta(tree, True, -INF, INF)
    print("\nBest value for max at the root = ", result)