from fastapi import FastAPI,File, UploadFile
import uvicorn
from datetime import datetime
from services.process_list_soldiers import Process_list_soldiers
from services.assignment_policy import Assignment_policy
from db.db import DatabaseManager
import sqlite3


db = DatabaseManager()
db.create_tables()

residential_buildings = [{
    "name": "Dorm A",
    "number_of_rooms": 10,
    "number_of_places_room": 8
},
{
    "name": "Dorm b",
    "number_of_rooms": 10,
    "number_of_places_room": 8
}]

app = FastAPI()
@app.get("/")
def get_root():
    return {"ts": datetime.now()}

@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
    if not "csv" in file.content_type:
        return {"msg": f"content_type: `{file.content_type}` not allowed!"}
    text = file.file.read().decode()
    list_soldiers = Process_list_soldiers.csv_to_dict_list(text)
    list_soldiers_translate = Process_list_soldiers.translate_Hebrew_keys(list_soldiers)
    sorted_list_soldiers = Assignment_policy.sort_by_distance(list_soldiers_translate[1])
    soldiers_inlay = Process_list_soldiers.placement_residential_buildings(sorted_list_soldiers, residential_buildings)
    list_summary = Process_list_soldiers.list_summary(soldiers_inlay)
    with sqlite3.connect("Inlay_system.db") as conn:
        db.add_soldiers_to_table(conn, "deploying_soldiers", soldiers_inlay)
    # db.add_soldiers_to_table(soldiers_inlay)
    return {
        "total_number_of_soldiers_received": len(list_soldiers),
        "total_number_of_soldiers_deployed": len(list_summary[0]),
        "total_number_of_soldiers_on_the_waiting_list": len(list_summary[1]),
        "list_of_soldiers_deployed": list_summary[0],
        "list_of_soldiers_on_the_waiting_list":  list_summary[1]
    }


if __name__ == "__main__":
    uvicorn.run(app)

