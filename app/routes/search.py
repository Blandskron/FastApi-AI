from fastapi import APIRouter, HTTPException
from app.services.elastic import search_in_elasticsearch
from app.services.ai import reformulate_query
from app.models.search import SearchQuery

router = APIRouter()

@router.post("/ai-search/")
async def ai_search(payload: SearchQuery):
    question = payload.question
    size = payload.size
    try:
        reformulated_query = reformulate_query(question)
        results = search_in_elasticsearch(reformulated_query, size)
        return {
            "original_question": question,
            "reformulated_query": reformulated_query,
            "results": results,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
