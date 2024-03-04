#Function: This program determines if a student will be admitted or rejected.

## housekeeping ##
# get inputs #
testScore = input("Student Test Score: ")
classRank = input("Student Class Rank: ")

# convert inputs #
testScore = int(testScore)
classRank = int(classRank)


## Detail ##
# Test using admission requirements and print Accept or Reject
if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")