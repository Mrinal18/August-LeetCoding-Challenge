"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
"""


from collections import deque
class Logger:
    """
    Algorithm

First of all, we use a queue as a sort of sliding window to keep all the printable messages in certain time frame (10 seconds).

At the arrival of each incoming message, it comes with a timestamp. This timestamp implies the evolution of the sliding windows. Therefore, we should first invalidate those expired messages in our queue.

Since the queue and set data structures should be in sync with each other, we would also remove those expired messages from our message set.

After the updates of our message queue and set, we then simply check if there is any duplicate for the new incoming message. If not, we add the message to the queue as well as the set.


    """
    #Approch 1
   
   
    def __init__(self):
        
        self.msg_set = set()
        self.msg_q = deque()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        
        while self.msg_q:
            msg, tsp = self.msg_q[0]

            if timestamp - tsp >= 10:
                self.msg_q.popleft()
                self.msg_set.remove(msg)

            else:
                break
            
        
        if message not in self.msg_set:
            self.msg_set.add(message)
            self.msg_q.append((message, timestamp))
            return True
        else:
            return False
   
        
    """
        Approch 2: Hashable/ Dictionary 
        
        Algorithm

We initialize a hashtable/dictionary to keep the messages along with the timestamp.

At the arrival of a new message, the message is eligible to be printed with either of the two conditions as follows:

case 1). we have never seen the message before.

case 2). we have seen the message before, and it was printed more than 10 seconds ago.

In both of the above cases, we would then update the entry that is associated with the message in the hashtable, with the latest timestamp.
        
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        
        if message not in self.msg_dict:
            
            #case 1. add the message to print
            self.msg_dict[message] = timestamp
            return True
        
        if timestamp - self.msg_dict[message] >=10:
            #case 2. update the timestamp of the message
            
            self.msg_dict[message] = timestamp
            return True
        else:
            return False

        ##Time Complexity:O(1)
        #Space Complexity: O(N)
            
        
    
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
