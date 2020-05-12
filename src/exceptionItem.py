class ExceptionItem(Exception):

    def __init__(self, *args):
        if args:
            self.msg = args[0]
        else:
            self.msg = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'ExceptionItem, {0} '.format(self.msg)
        else:
            return 'ExceptionItem has been raised'
