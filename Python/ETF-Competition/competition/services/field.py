from competition import Field


class FieldService:
    @staticmethod
    def read(field_id):
        return Field.query.filter_by(id=field_id).first()

    @staticmethod
    def read_all():
        return Field.query.all()

    @staticmethod
    def field_to_select_options():
        fields = FieldService.read_all()
        return [(f.id, f.name) for f in fields]
