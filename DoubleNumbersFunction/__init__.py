import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    data = req.get_json()
    numbers = data.get("numbers", [])
    result = [x * 2 for x in numbers]
    return func.HttpResponse(json.dumps({"result": result}), mimetype="application/json")
