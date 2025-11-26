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
                        "distance_from_Base" :int(i["מרחק מהבסיס"])
                        }
                translated_list.append(soldier)
            return True, translated_list
        except Exception as e:
            return False, f"Error: The field {format(e)} Not in the correct format"


    @staticmethod
    def get_total_spaces(residential_buildings:list[dict]) -> int:
        total_places = []
        for building in residential_buildings:
            places_building = building["number_of_rooms"] * building["number_of_places_room"]
            total_places.append(places_building)
        return sum(total_places)


    @staticmethod
    def placement_residential_buildings(soldiers: list[dict], residential_buildings:list[dict]) -> list[dict]:
        total_places = Process_list_soldiers.get_total_spaces(residential_buildings)

        soldiers_before_inlay = []
        for soldier in soldiers:
            soldier_copy = dict(soldier)
            soldiers_before_inlay.append(soldier_copy)

        inlay_list = []
        if total_places > len(inlay_list):
            for building in residential_buildings:
                for room in range(building["number_of_rooms"]):
                    for place in range(building["number_of_places_room"]):
                        if soldiers_before_inlay:
                            if total_places > len(inlay_list):
                                soldier_inlay = soldiers_before_inlay.pop(0)
                                soldier_inlay["assignment_status"] = "שובץ"
                                soldier_inlay["residential_building"] = building["name"]
                                soldier_inlay["room"] = room+1
                                inlay_list.append(soldier_inlay)
                            else:
                                for soldier in soldiers_before_inlay:
                                    soldier_inlay = soldiers_before_inlay.pop(0)
                                    soldier_inlay["assignment_status"] = "לא שובץ"
                                    inlay_list.append(soldier_inlay)
        return inlay_list

    @staticmethod
    def list_summary(inlay_list:list[dict]) -> int:
        total_embedded = []
        total_pending = []
        for solider in inlay_list:
            if solider["assignment_status"] == "שובץ":
                total_embedded.append(solider)
            else:
                total_pending.append(solider)
        return total_embedded, total_pending



                    




         
