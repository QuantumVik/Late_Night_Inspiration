from fastapi import APIRouter,Depends
from Late_Night_Inspiration.app.db.models.ideas import Idea , Clarification, UpdateIdea
from Late_Night_Inspiration.app.services.idea_service import IdeaService


router = APIRouter()
@router.get('/home')
def helo():
    return {'helo meri jaan'}


@router.post('/add_idea')
def add_idea(idea:Idea,serivce: IdeaService = Depends()):
    return serivce.add_idea(idea)

@router.get('/get-all')
def get_all_idea(service:IdeaService=Depends()):
    return service.get_ideas()

@router.put(f'/clarification/{id}')
def add_clarification(id:int,data:Clarification,service : IdeaService=Depends()):
    return service.add_clarification(id,data)

@router.patch(f'/update/{id}/update_cont_clari')
def update_idea(id:int,data:UpdateIdea ,service:IdeaService=Depends()):
    return service.update_idea(id,data)

@router.delete(f'/delete/{id}')
def delete_idea(id:int,service:IdeaService=Depends()):
    return  service.delete_idea(id)

