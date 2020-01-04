import time


def sleep_seconds(request):
    sleep_seconds_arg = request.args.get('sleep_seconds', default=0, type=float)
    time.sleep(sleep_seconds_arg)
    return sleep_seconds_arg


def override_status_code(request):
    status_code_arg = request.args.get('status_code', default=200, type=int)
    return status_code_arg