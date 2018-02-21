import time
from functools import wraps

_total_time_call_stack = [0]

def _log(message):
    print('[BetterTimeTracker] {function_name} {total_time:.3f} {partial_time:.3f}'.format(**message))


def better_time_tracker(log_fun=_log):
    def _better_time_tracker(fn):
        @wraps(fn)
        def wrapped_fn(*args, **kwargs):
            global _total_time_call_stack
            _total_time_call_stack.append(0)

            start_time = time.time()

            try:
                result = fn(*args, **kwargs)
            finally:
                elapsed_time = time.time() - start_time
                inner_total_time = _total_time_call_stack.pop()
                partial_time = elapsed_time - inner_total_time

                _total_time_call_stack[-1] += elapsed_time

                # log the result
                log_fun({
                    'function_name': fn.__name__,
                    'total_time': elapsed_time,
                    'partial_time': partial_time,
                })

            return result

        return wrapped_fn
    return _better_time_tracker
