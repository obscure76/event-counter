# Eventcounter
A small lib to process events.

EventCounter stores the events as a time series data for the last 300s.
It exposes two APIs:
1) increment()
2) get_count()


#Usage:


`event_counter = EventCounter()`

`event_counter.increment()`

`count = event_counter.get_count(duration=30)`


#Unit tests:
`coverage run -m pytest`
