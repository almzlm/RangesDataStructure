"""
Author : Ali Mazloum
Date : Nov 27th 2022

Module to define the Ranges data structure. This structure holds a list of Ranges that can be altered via its functions

Classes:

    Range

Functions:

    ConvertToInt(fn(obj,obj)) -> fn(int,int)
    Add(int,int)
    Delete(int,int)
    Get(int,int) -> list[ list[int] ]
    GetV2(int,int) -> list[ list[int] ]  --> This is the implementation in case my assumption #2 was invalid

Assumptions :
    1 - We assume that our ranges are always SORTED in our data structure. Otherwise, we would have to sort them ourselves which would take O(nlogn) time
"""

class Ranges:
  """
  A class to represent a Ranges data structure.

  ...

  Attributes
  ----------
  ranges : list
      The internal ranges in the Ranges data structure


  Methods
  -------
  ConvertToInt(start,end)
      Converts the start, end input parameters to integer types
  Add(start,end):
      Adds a new range to the list of ranges
  Delete(start,end):
      Deletes a range from the list of ranges
  Get(start,end):
      Gets the list of ranges from the list of ranges that match the given range
  """

  def ConvertToInt(fn):
    """
    Converts input parameter to int
    """
    def wrapper(obj,start,end):
      return fn(obj,int(start),int(end))
    return wrapper
    
  def __init__(self,start:int=None,end:int=None):
    self.ranges = []
    if (start is None) and (end is None):
      self.ranges = []
    else:
      self.ranges.append([int(start),int(end)])


  def __str__(self):
    return (f"{self.ranges}")

  def ConvertToInt(fn):
    """
    Converts input parameter to int
    """
    def wrapper(obj,start,end):
      return fn(obj,int(start),int(end))
    return wrapper

  @ConvertToInt
  def Add(self,start:int,end:int):
    """ 
    Adds a new range to the data structure. 
    If the provided range overlaps existing ranges, they are merged together 
    Time Complexity : O(n) where n = number of ranges currently in the data structure
    Space complexity : O(n) where n = number of ranges currently in the data structure (since we only create an array with at-most the same number of elements)

    Ex : Original state [(1, 4)], Add(3, 5), New state: [(1, 5)]

            Parameters:
                    start (int): start of the new range to add
                    end   (int): end of the new range to add
    """
    updatedRanges = []
    newRange = [int(start),int(end)]

    #If our structure is empty, initialize it with new range
    if (len(self.ranges) == 0):
      self.ranges = [newRange]

    #Else if our new range is before all our ranges
    elif (end < self.ranges[0][0]):
      self.ranges = [newRange] + self.ranges

    #Else if our new range is after all our ranges
    elif (start > self.ranges[-1][1]):
      self.ranges = self.ranges + [newRange]

    #Else somewhere in between
    else :
      #Iterage through existing ranges and see where the new range fits == > (O(n))
      for i,curr in enumerate(self.ranges):
        #Case 1 : New range is before curr range --> We place our new range before the current range
        if (newRange[1] < curr[0]):
          updatedRanges.append([newRange[0],newRange[1]])
          self.ranges = updatedRanges + self.ranges[i:]
          return
        #Case 2 : New range is after curr range --> Keep current range in place, move to next iter
        elif (newRange[0] > curr[1]):
          updatedRanges.append(curr)
        #Case 3 : New range is overlapping with another range --> We merge them
        else :
          newRange = [min(newRange[0],curr[0]),max(newRange[1],curr[1])]
      
      #Add our new range and update our list of ranges
      updatedRanges.append(newRange)
      self.ranges = updatedRanges


  @ConvertToInt
  def Delete(self,start:int,end:int):
    """ 
    Deletes a range from the data structure. 
    If the provided [start,end] range overlaps with existing ranges, those ranges are deleted from the data structure
    Time Complexity : O(n) where n = number of ranges currently in the data structure
    Space complexity : O(n) where n = number of ranges currently in the data structure (since we only create an array with at-most the same number of elements)

    Ex : Original state [(1, 6)], Delete(4, 10), New state: [(1, 4)]: 

            Parameters:
                    start (int): start of the range to deleted
                    end   (int): end of the range to delete
    """

    updatedRanges = []
    deletedRange = [start,end]

    if len(self.ranges) == 0:
      return

    if(end < self.ranges[0][0]) or (start > self.ranges[-1][1]):
      return
    else:
      for curr in self.ranges:
        if deletedRange[0] < curr[0] and deletedRange[1] > curr[1]:
          pass
        elif (deletedRange[0] <= curr[0]) and (deletedRange[1] < curr[0]):
          updatedRanges.append(curr) #do nothing
        elif (deletedRange[0] <= curr[0]) and (deletedRange[1] < curr[1]):
          updatedRanges.append([deletedRange[1],curr[1]])
        elif (deletedRange[0] > curr[0]) and (deletedRange[0] > curr[1]):
          updatedRanges.append(curr)
        elif (deletedRange[0] > curr[0]) and (deletedRange[1] < curr[1]):
          updatedRanges.append([curr[0],deletedRange[0]])
          updatedRanges.append([deletedRange[1], curr[1]])
        else:
            updatedRanges.append([curr[0],deletedRange[0]])

      self.ranges = updatedRanges


  @ConvertToInt
  def Get(self,start:int,end:int):
    """ 
    Gets the ranges that intersect with the input range. 
    Time Complexity : O(n) where n = number of ranges currently in the data structure
    Space complexity : O(n) where n = number of ranges currently in the data structure (since we only create an array with at-most the same number of elements)

    Ex : State [(1, 3), (5, 6)]. Get(2, 9). Returns [(1, 3), (5, 6)]

            Parameters:
                    start (int): start of the range to get
                    end   (int): end of the range to get
    """

    selectedRanges = []
    for curr in self.ranges:
      if (start < curr[0] and end >= curr[1]):
        selectedRanges.append([curr[0],curr[1]])
      elif (end > curr[0] and end < curr[1]) or (start > curr[0] and start < curr[1]):
        selectedRanges.append([max(start,curr[0]),min(end,curr[1])])

    return selectedRanges

  @ConvertToInt
  def GetV2(self,start:int,end:int):
    """ 

    Gets the ranges that overlap with the input range. 
    Time Complexity : O(n) where n = number of ranges currently in the data structure
    Space complexity : O(n) where n = number of ranges currently in the data structure (since we only create an array with at-most the same number of elements)

    Ex : State [(1, 3), (5, 6)]. Get(2, 9). Returns [(2, 3), (5, 6)]

            Parameters:
                    start (int): start of the range to get
                    end   (int): end of the range to get
    """

    selectedRanges = []
    for curr in self.ranges:
      if (start < curr[0] and end >= curr[1]):
        selectedRanges.append([curr[0],curr[1]])
      elif (end > curr[0] and end < curr[1]) or (start > curr[0] and start < curr[1]):
        selectedRanges.append([curr[0],curr[1]])

    return selectedRanges
