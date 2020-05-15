import time
import sys
import logging


"""
EventCounter class primarily supports two public methods:
1) increment()
2) get_count()
"""
class EventCounter(object):
    WINDOW_SECONDS = 300  # time window in secs for which we track events
    EVENTS = list()  # A list where we store events
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    def __init__(self):
        pass

    # testing purposes
    def _set_events(self, events):
        self.EVENTS = events

    # testing purposes
    def _get_events(self):
        return self.EVENTS

    '''
    set window duration to given seconds.
    '''
    def set_window(self, seconds):
        self.WINDOW_SECONDS = seconds

    '''
    _delete_events_past_threshold deletes all the events from out storage
    which are older than 300 seconds.
    '''
    def _delete_events_past_threshold(self):
        now = time.time()
        pre_window_time_point = int(now - self.WINDOW_SECONDS)
        index = self._bin_search(pre_window_time_point)
        if index > 0:
            logging.debug("Deleting events past threshold duration:%s seconds", self.WINDOW_SECONDS)
            self.EVENTS = self.EVENTS[index:]

    '''
    increment appends the event in the time series using current time point. 
    '''
    def increment(self):
        self.EVENTS.append(int(time.time()))

    '''
    _bin_search searches the index for a data point in the stored time series
    such that the time value at the data point is just before given time point
    '''
    def _bin_search(self, time_point):
        logging.debug("Finding time_point %s in the time series", time_point)
        l, r = 0, len(self.EVENTS)
        while l < r:
            m = int((l + r) / 2)
            try:
                if time_point > self.EVENTS[m]:
                    l = m + 1
                else:
                    r = m
            except Exception:
                logging.exception(l, r, m)
                break
        return l

    '''
    get_count returns the number of events that were recorded in
    the last duration seconds. The default value is 60 seconds. It
    first locates the time point among the time series we stored from 
    which duration starts.  No matter how big the duration value is, 
    since we track only last 300 seconds of data, we return count for
    maximum duration of 300 seconds.
    '''
    def get_count(self, duration=60):
        logging.debug("Getting count for duration: %s in the time series", duration)
        self._delete_events_past_threshold()
        time_point = int(time.time() - duration)
        index = self._bin_search(time_point)
        return max(len(self.EVENTS) - index, 0)
