import time


def polling(exception, retry: int = 10, timeout: float = 0.1):
    """
    Wraps method and try to returns value from it. If exception will be raised
    function will be called repeatedly retry times.
    Parameters:
        - exception: exception type
        - retry: number of times function will be called
        - timeout: timeout for `time.sleep` function
    """
    def sleep(func):
        def wrapper(instance, *args, **kwargs):
            retries = retry
            while bool(retries):
                try:
                    result = func(instance)
                    return result
                except exception:
                    time.sleep(timeout)
                    retries -= 1
            raise
        return wrapper
    return sleep
