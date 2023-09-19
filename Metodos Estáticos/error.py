class Error:

    @staticmethod
    def error_500():
        print('internal server error')
    
    @staticmethod
    def error_404():
        print('not found')

Error.error_500()
Error.error_404()