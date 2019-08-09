import heapq
from path_search_3dgrid import Node


# MAIN ALGORITHM
def find_path(field, source, dest):
    queue = []
    heapq.heapify(queue)

    Node.setup_grid(field)

    start = Node(source[0], source[1], source[2])
    start.age = Node.age
    Node.age += 1

    heapq.heappush(queue, (start.get_cost(dest), start.age, start))
    start.mark_visited()

    while len(queue) > 0:
        curr = heapq.heappop(queue)[2]

        if curr.is_dest(dest):
            break

        children = curr.get_children()
        for i in range(len(children)):
            children[i].age = Node.age
            Node.age += 1
            heapq.heappush(queue, (children[i].get_cost(dest), children[i].age, children[i]))
            children[i].mark_visited()

    return curr.ret_path_prize()  # remake of the best path
