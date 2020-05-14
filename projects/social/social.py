import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        #Generate all possible friendship possibilities:
        possible_friendships = []
        #Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        #Shuffle the possible friendships
        random.shuffle(possible_friendships)

        #Create friendships for the first X pairs of the list
        # X is determind by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        Breadth-First Traversal -- QUEUE -- FIFO
            Returns a list containing the shortest path from start to finish

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue(user_id)

        #Key is friend's ID : Value is path
        #Path so far is the user id
        visited[user_id] = [user_id]

        # While the queue is not empty...
        while q.size() > 0:
            #Dequeue the first PATH
            user = q.dequeue()

            #Get current user's friends
            #friendships is also a dict, use user_id as key
            friends = self.friendships[user]

            #Loop through friends
            for friend in friends:
                #If not in visited...
                if friend not in visited:
                    #Add to dict with friend's id as Key, and path as Value
                    #path so far is what is in Visited's value thus far and current friend that we're on
                    visited[friend] = visited[user] + [friend]
                    #Add friend to queue
                    q.enqueue(friend)

    """
***** USED BFS as reference *****
     def bfs(self, starting_vertex, destination_vertex):

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            #Dequeue the first PATH
            path = q.dequeue()

                # Then add A PATH TO its neighbors to the back of the queue
                for next_vert in self.get_neighbors(last_ver):
                    # _COPY_ THE PATH                    
                    prev_path = list(path)
                    # APPEND THE NEIGHOR TO THE BACK                    
                    prev_path.append(next_vert)
                    q.enqueue(prev_path) 
    """      
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

"""
Questions

1.) To create 100 users with an average of 10 friends each, 
how many times would you need to call add_friendship()? Why?

Answer: 500. In our function, we call add_friendship based on the number of users * avrg friends and divide by 2.
(100 * 10) // 2 == 500

2.) If you create 1000 users with an average of 5 random friends each, 
what percentage of other users will be in a particular user's extended social network? 
What is the average degree of separation between a user and those in his/her extended network?

Answer: The percentage would be increasingly smaller. For 10 users with avrg of 2 friends,
 we usually see 80-90% of other users in a particular user's extended social network 
 (or 1-2 people not thier extended network). With 1000 users, we're increasing our users by times 100 and
 only increasing amount of averg friends by +3. 

"""