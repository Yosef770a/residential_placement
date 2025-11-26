from io import StringIO
import csv

class Process_list_soldiers:
    def __init__(self):
        pass

    @staticmethod
    def csv_to_dict_list(text: str) -> list[dict]:
        f = StringIO(text)
        reader = csv.DictReader(f)

        list = []
        for row in reader:
            cleaned = {key: (value if value is not None else "") for key, value in row.items()}
            list.append(cleaned)
        return list
    
    @staticmethod
    def translate_Hebrew_keys(dict_list: list[dict]):
        translated_list = []
        try:
            for i in dict_list:
                soldier = {"id": i["מספר אישי"],
                        "first_name" :i["שם פרטי"],
                        "last_name" :i["שם משפחה"],
                        "gender" :i["מין"],
                        "citi" :i["עיר מגורים"],
                        "distance_from_Base" :i["מרחק מהבסיס"]
                        }
                translated_list.append(soldier)
            return True, translated_list
        except Exception as e:
            return False, f"Error: The field {format(e)} Not in the correct format"

        

            

    
# מספר אישי	שם פרטי	שם משפחה	מין	עיר מגורים	מרחק מהבסיס

#         id INTEGER PRIMARY KEY,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         gender INTEGER,
#         citi TEXT NOT NULL,                    
#         distance_from_Base INTEGER,
#         assignment_status TEXT,
#         residential_building TEXT,
#         room INTEGER

tcsv = """מספר אישי,שם פרטי,שם משפחה,מין,עיר מגורים,מרחק מהבסיס
8525125,רון,בכר,זכר,אילת,10
8841961,אלון,בכר,זכר,אילת,1
8494659,אלון,פרץ,זכר,אשדוד,15
8176687,תמר,בכר,נקבה,אשדוד,28
8317185,דנה,בכר,נקבה,באר שבע,15
8398221,יולי,כהן,נקבה,רעננה,45
"""

rowss = Process_list_soldiers.csv_to_dict_list(tcsv)
# print("rowss", rowss)
print(Process_list_soldiers.translate_Hebrew_keys(rowss))

