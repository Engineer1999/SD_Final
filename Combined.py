from helper import main
from FLV.Stream.streamToSegment import streamToSegment

import multiprocessing 
  
def func1(): 
    print('In func1')
    #streamToSegment()


def func2(): 
    print('In func2')
    #main()


if __name__ == "__main__": 
    p1 = multiprocessing.Process(target=func1) 
    p2 = multiprocessing.Process(target=func2) 

    p1.start() 
    p2.start() 
  
    p1.join() 
    p2.join() 
  
    print("Done!")