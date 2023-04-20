class GracefulExit(SystemExit):
    pass


def shutdown():
    raise GracefulExit()
