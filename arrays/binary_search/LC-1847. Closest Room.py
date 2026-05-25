# There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed to be unique.

# You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. The answer to the jth query is the room number id of a room such that:

# The room has a size of at least minSizej, and
# abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
# If there is a tie in the absolute difference, then use the room with the smallest such id. If there is no such room, the answer is -1.

# Return an array answer of length k where answer[j] contains the answer to the jth query.

 

# Example 1:

# Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
# Output: [3,-1,3]
# Explanation: The answers to the queries are as follows:
# Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
# Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
# Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.
# Example 2:

# Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
# Output: [2,1,3]
# Explanation: The answers to the queries are as follows:
# Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
# Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
# Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.
from typing import List
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        rooms.sort(key=lambda x: -x[1])
    
        # Step 2: attach index and sort queries
        queries_with_idx = [(pref, minSize, i) for i, (pref, minSize) in enumerate(queries)]
        queries_with_idx.sort(key=lambda x: -x[1])
        
        ans = [-1] * len(queries)
        
        valid_rooms = []  # this will stay SORTED manually
        i = 0
        
        # helper: binary search insert position
        def find_insert_pos(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        # helper: insert while keeping sorted
        def insert_sorted(arr, val):
            pos = find_insert_pos(arr, val)
            arr.insert(pos, val)
        
        # process queries
        for preferred, minSize, idx in queries_with_idx:
            
            # add valid rooms
            while i < len(rooms) and rooms[i][1] >= minSize:
                insert_sorted(valid_rooms, rooms[i][0])
                i += 1
            
            if not valid_rooms:
                ans[idx] = -1
                continue
            
            # find position using binary search
            pos = find_insert_pos(valid_rooms, preferred)
            
            candidates = []
            
            # ceiling
            if pos < len(valid_rooms):
                candidates.append(valid_rooms[pos])
            
            # floor
            if pos > 0:
                candidates.append(valid_rooms[pos - 1])
            
            # choose best
            best = min(candidates, key=lambda x: (abs(x - preferred), x))
            ans[idx] = best
        
        return ans