import azure.functions as func
import json
import time

def main(req: func.HttpRequest) -> func.HttpResponse:
    start_time = time.time()

    data = req.get_json()
    numbers = data.get("numbers", [])
    result = [x * 2 for x in numbers]

    execution_time = time.time() - start_time
    response_data = {
        "result": result,
        "executionTime": execution_time
    }

    return func.HttpResponse(json.dumps(response_data), mimetype="application/json")
