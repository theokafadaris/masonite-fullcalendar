from masonite.routes import Route

ROUTES = [Route.get("/", "WelcomeController@show"),
          Route.get("/events", "EventController@index"),
          Route.get("/events/get_events", "EventController@get_events"),
          Route.get("/events/create", "EventController@create"),
          Route.post("/events", "EventController@store"),
          Route.get("/events/edit/@event_id", "EventController@edit"),
          Route.post("/events/update", "EventController@update"),
    
]
