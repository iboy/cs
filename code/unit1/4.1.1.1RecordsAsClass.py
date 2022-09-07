# Python does not have a built in record data type so we have to use a class and OOP and recreate a class and objects with attributes that define the fields used in our record.

class ExamRecord(object):
  def __init__(self, name, examscore, examgrade, resit, meangcsescore):
    self.name = name
    self.examscore = examscore
    self.resit = resit
    self.meangcsescore = meangcsescore 

# create an instance - or a record
myResultRecord = ExamRecord("Ian", 97, 9, False, 8)

print(myResultRecord.name)
print(myResultRecord.examscore)
# etc
print(type(myResultRecord))

# Create another record
anotherResultRecord = ExamRecord("Hannah", 98, 9, False, 9)
# Add records to a list called records
records = [myResultRecord, anotherResultRecord]
print(records[0].name)
print(records[1].name)