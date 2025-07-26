from pymongo import MongoClient

def load_case_summaries():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["courtlistener_db"]
    collection = db["cases"]

    documents = []
    for case in collection.find({}, {
        "case_title": 1,
        "opinion_text": 1,
        "court_name": 1,
        "docket_number": 1,
        "judges": 1,
        "opinion_author": 1,
        "citations": 1
    }):
        if case.get("opinion_text"):
            metadata = {
                "title": case.get("case_title", ""),
                "court": case.get("court_name", ""),
                "docket_number": case.get("docket_number", ""),
                "judges": case.get("judges", ""),
                "opinion_author": case.get("opinion_author", ""),
                "citations": case.get("citations", "")
            }
            documents.append({
                "text": case["opinion_text"],
                "metadata":metadata
            })
    return documents