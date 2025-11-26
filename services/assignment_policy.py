from operator import itemgetter

class Assignment_policy:
    def __init__(self):
        pass



    @staticmethod
    def sort_by_distance(list_soldiers: list[dict]) -> list[dict]:
        list_by_distance = sorted(list_soldiers, key=itemgetter('distance_from_Base'), reverse=True)
        return list_by_distance

    
  