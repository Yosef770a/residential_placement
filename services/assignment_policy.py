from operator import itemgetter

class Assignment_policy:
    def __init__(self):
        pass



    @staticmethod
    def Sort_by_distance(list_soldiers: list[dict]) -> list[dict]:
        list_by_distance = sorted(list_soldiers, key=itemgetter('distance_from_Base'), reverse=True)
        return list_by_distance

    
    


# listi =[{'id': '8525125', 'first_name': 'רון', 'last_name': 'בכר', 'gender': 'זכר', 'citi': 'אילת', 'distance_from_Base': '10'},
#          {'id': '8841961', 'first_name': 'אלון', 'last_name': 'בכר', 'gender': 'זכר', 'citi': 'אילת', 'distance_from_Base': '1'}, {'id': '8494659', 'first_name': 'אלון', 'last_name': 'פרץ', 'gender': 'זכר', 'citi': 'אשדוד', 'distance_from_Base': '15'}, {'id': '8176687', 'first_name': 'תמר', 'last_name': 'בכר', 'gender': 'נקבה', 'citi': 'אשדוד', 'distance_from_Base': '28'}, {'id': '8317185', 'first_name': 'דנה', 'last_name': 'בכר', 'gender': 'נקבה', 'citi': 'באר שבע', 'distance_from_Base': '15'}, {'id': '8398221', 'first_name': 'יולי', 'last_name': 'כהן', 'gender': 'נקבה', 'citi': 'רעננה', 'distance_from_Base': '45'}]
        

# for i in listi:
#     print(i)

# listt = Assignment_policy.Sort_by_distance(listi)

# for i in listt:
#     print(i)

