from masonite.controllers import Controller
from masonite.request import Request
from masonite.views import View
from masonite.response import Response
from masonite.facades import Dump



from app.models.Event import Event


class EventController(Controller):
    def get_events(self):
       
        return Event.all()

    def index(self, view: View):
        # Dump.dd(Event.all())
        return view.render("events.index")

    def create(self, view: View, request: Request):
        date = request.input('date')
        # Dump.dd(date)
        return view.render("events.create", {'date': date})

    def edit(self, view: View, request: Request):
        event = Event.find(request.param('event_id'))
        # Dump.dd(event.serialize())
        return view.render('events.edit', {'event': event})

    def store(self, request: Request, response: Response):
        # Dump.dd(request.all())
        Event.create(request.all())
        return response.redirect('/events')

    def update(self, request: Request, response: Response):
        event = Event.find(request.input('event_id'))
        event.update(request.only('title', 'start', 'end'))
        return response.redirect('/events')
