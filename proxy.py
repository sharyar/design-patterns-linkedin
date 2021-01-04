import time

class Producer:
    '''Define the "resource-intensive" object to instantiate'''
    def produce(self):
        print('Producer is working hard!')
    
    def meet(self):
        print('Producer will meet you now!')
    
class Proxy:
    ''' Define the 'relatively less expensive' proxy to instantiate as a middleman'''
    def __init__(self):
        self.occupied = False
        self.producer = None
        
    def produce(self):
        '''Checks if producer is available'''
        print('Artist is checking if producer is available')
        
        if not self.occupied:
            # If the producer is available, create a producer object:
            self.producer = Producer()
            time.sleep(2)
            
            # make the producer meet the guest
            self.producer.meet()
        else:
            # otherwise, don't instantiate a producer
            time.sleep(2)
            print('Producer is busy')

p = Proxy()

# make the proxy! -> Artist will produce the producer if available -> In this case yes. 
p.produce()

# change status to occupied
p.occupied = True

# make the proxy produce:
p.produce()