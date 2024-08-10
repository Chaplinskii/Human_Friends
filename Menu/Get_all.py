from Controller.Controller import Controller
class Get_all:
    @classmethod
    def get_all(cls):
        try:
            for i in Controller.get_all():
                print(i)
            print(f'Total records : {len(Controller.get_all())}')
        except Exception as e:
            print(f'Error: {e}')
            return True
        return True