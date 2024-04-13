# general idea is to do bfs, which works with initializing a start node and iterating through
# neighbors while keeping up with what you've already visited. first thing is finding the start node
# which at first I did inefficiently
# but then realized I could just call a function once I found the first instance of a 1
# from there i knew i needed to check to see if the neighbor == 0 (add to perimeter) or if the neighbor was out of bounds (also add to perimeter)
# i do this by doing r+1, c, r-1, c, r, c-1, and r, c+ 1
# the only other option is for it to be a one, and then i check to see if it's been visited already or if it's in the queue. if neither, i add it



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        # need to identify start node
        row = len(grid)
        col = len(grid[0])
        vis = set()
        q = []

        def bfs(r,c):
            peri = 0
            q.append((r,c))
            while q:
                r,c = q.pop(0)
                vis.add((r,c))
                for neigh in ((r+1,c), (r,c+1), (r-1,c), (r,c-1)): # checking four nearby neighbors
                    new_r, new_c = neigh
                    if new_r not in range(row) or new_c not in range(col): # out of bounds
                        peri+=1
                    elif grid[new_r][new_c] == 0:
                        peri+=1
                    elif (new_r, new_c) not in vis and (new_r, new_c) not in q:
                        q.append((new_r,new_c))                

            return peri



        

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return bfs(r,c)
        # nodes are [i,j]

                

        # after start node, need to do BFS

        # go to the grid




        
