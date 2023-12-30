from ninja import Router
from ninja_extra import NinjaExtraAPI
from django.shortcuts import redirect

api = NinjaExtraAPI()
router = Router()


@router.post('/example_root')
def example_root(request):
    return {'status': 200}


@router.get('/example_redirect/{inventory_id}')
def example_redirect(request, inventory_id: int):
    return redirect(f'/uri/{inventory_id}')
