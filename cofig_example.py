USER_ID = "workspace_owner's_id"

TOKEN = "token_v2_cookies"

HTTP_REQUEST = {
    "URL": "https://www.notion.so/api/v3/queryCollection",
    "HEADERS":
        {
            "Content-Type": "application/json"
        },
    "BODY":
        {
            "collectionId": "your_collection_id",
            "collectionViewId": "your_collection_view_id",
            "loader": 
            {
                "type": "table",
                "limit": 50,
                "searchQuery": "",
                "userTimeZone": "Asia/Seoul",
                "loadContentCover": True
            },
            "aggregations": [
                {
                "property": "title",
                "aggregator": "count"
                }
            ]
        }
}