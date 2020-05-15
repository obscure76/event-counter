import time
from unittest import TestCase, main
from eventcounter.eventcounter import EventCounter


class TestEventCounter(TestCase):
    def test_increment(self):
        event_counter = EventCounter()
        event_counter._set_events([])
        event_counter.increment()
        events = event_counter._get_events()
        assert len(events) == 1

    def test_get_count(self):
        event_counter = EventCounter()
        event_counter._set_events([])
        assert event_counter.get_count() == 0
        event_counter.increment()
        assert event_counter.get_count(duration=30) == 1
        event_counter.increment()
        assert event_counter.get_count(duration=30) == 2

    def test_delete_events_past_threshold(self):
        event_counter = EventCounter()
        event_counter._set_events([])
        event_counter.increment()
        assert event_counter.get_count(duration=30) == 1
        event_counter.set_window(5)
        time.sleep(6)
        assert event_counter.get_count(duration=30) == 0

    def test_bin_search(self):
        event_counter = EventCounter()
        event_counter._set_events([1, 5, 10])
        assert event_counter._bin_search(5) == 1
        assert event_counter._bin_search(7) == 2
        assert event_counter._bin_search(11) == 3
        assert event_counter._bin_search(-1) == 0


if __name__ == '__main__':
    main()
