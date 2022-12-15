from Ranges import Ranges

##  Testing ADD method ##
def test_add_case_1():
  rg = Ranges(1,2)
  rg.Add(3,5)
  assert (rg.ranges == [[1,2],[3,5]])

def test_add_case_2():
  rg = Ranges(1,6)
  rg.Add(3,5)
  assert (rg.ranges == [[1,6]])

def test_add_case_3():
  rg = Ranges(1,4)
  rg.Add(3,5)
  assert (rg.ranges == [[1,5]])

def test_add_case_4():
  rg = Ranges(1,4)
  rg.Add(7,9)
  assert (rg.ranges == [[1,4],[7,9]])

def test_add_case_5():
  rg = Ranges()
  rg.Add(7,9)
  assert (rg.ranges == [[7,9]])

def test_add_case_6():
  rg = Ranges(1,5)
  rg.Add(7,9)
  assert (rg.ranges == [[1,5],[7,9]])
  rg.Add(3,8)
  assert (rg.ranges == [[1,9]])

def test_delete_case_7():
  rg = Ranges()
  rg.Add(1,10)
  rg.Add(100,500)
  assert(rg.ranges == [[1,10],[100,500]])
  rg.Add(0,99999)
  print(rg.ranges)
  assert(rg.ranges == [[0,99999]])

##  Testing DELETE method ##
def test_delete_case_1():
  rg = Ranges(1,6)
  rg.Delete(-3,-1)
  assert (rg.ranges == [[1,6]])

def test_delete_case_2():
  rg = Ranges(1,6)
  rg.Delete(0,3)
  assert (rg.ranges == [[3,6]])

def test_delete_case_3():
  rg = Ranges(1,6)
  rg.Delete(3,5)
  assert (rg.ranges == [[1,3],[5,6]])
  rg.Delete(0,2)
  assert (rg.ranges == [[2,3],[5,6]])

def test_delete_case_4():
  rg = Ranges()
  rg.Delete(0,3)
  assert (rg.ranges == [])

def test_delete_case_5():
  rg = Ranges()
  rg.Add(1,10)
  rg.Add(100,500)
  assert(rg.ranges == [[1,10],[100,500]])
  rg.Delete(0,99999)
  print(rg.ranges)
  assert(rg.ranges == [])


##  Testing GET method ##
def test_get_case_1():
  rg = Ranges(1,3)
  rg.Add(5,7)
  assert (rg.Get(4,5) == [])

def test_get_case_2():
  rg = Ranges(1,3)
  rg.Add(5,6)
  assert (rg.Get(4,6) == [[5,6]])

def test_get_case_3():
  rg = Ranges(1,3)
  rg.Add(5,6)
  assert (rg.Get(2,9) == [[2,3],[5,6]])

def test_get_case_4():
  rg = Ranges(2,3)
  rg.Add(5,6)
  assert (rg.Get(0,1) == [])

def test_get_case_5():
  rg = Ranges(2,3)
  rg.Add(5,6)
  assert (rg.Get(0,10) == [[2,3],[5,6]])


##  Testing GETV2 method ##
def test_getV2_case_1():
  rg = Ranges(1,3)
  rg.Add(5,7)
  assert (rg.GetV2(4,5) == [])

def test_getV2_case_2():
  rg = Ranges(1,3)
  rg.Add(5,6)
  assert (rg.GetV2(4,6) == [[5,6]])

def test_getV2_case_3():
  rg = Ranges(1,3)
  rg.Add(5,6)
  assert (rg.GetV2(2,9) == [[1,3],[5,6]])

def test_getV2_case_4():
  rg = Ranges(2,3)
  rg.Add(5,6)
  assert (rg.GetV2(0,1) == [])

def test_getV2_case_5():
  rg = Ranges(2,3)
  rg.Add(5,6)
  assert (rg.GetV2(0,10) == [[2,3],[5,6]])