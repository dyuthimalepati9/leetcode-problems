class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        if len(trees) == 1:
            return trees
        trees = sorted(trees)
        def wedge(origin, limit, tree):
            return (limit[0] - origin[0]) * (tree[1] - origin[1]) - (limit[1] - origin[1]) * (tree[0] - origin[0])
        lowerFence = []
        for tree in trees:
            while len(lowerFence) >= 2 and wedge(lowerFence[-2], lowerFence[-1], tree) < 0:
                lowerFence.pop()
            lowerFence.append(tree)
        upperFence = []
        for tree in reversed(trees):
            while len(upperFence) >= 2 and wedge(upperFence[-2], upperFence[-1], tree) < 0:
                upperFence.pop()
            upperFence.append(tree)
        fence = lowerFence[:-1] + upperFence[:-1]
        visited = set()
        fenceCoords = []
        for x, y in fence:
            if (x, y) not in visited:
                visited.add((x, y))
                fenceCoords.append([x, y])
        return fenceCoords