from ninja import NinjaAPI
from backend.utils import weather as wea

api = NinjaAPI()


@api.get("/test")
def hello(request):
    return "connected test"


@api.get("/wea")
def weather(request):
    data = wea.wea_data()
    return data
