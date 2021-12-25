students = [
         {
             "name": "RadoRado",
             "status": "not_finalized"
         },
         {
             "name": "Ivo",
             "status": "finalized"
         },
         {
             "name": "Genadi",
             "status": "finalized"
         }
     ]
key = "status"
def status_count(students, key):
    dict = {"status":"finalized", "status":"not_finalized"}
    if key in students:
        return dict[1]
   
print(status_count(students, key))
