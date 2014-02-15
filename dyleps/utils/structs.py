from collections import namedtuple


def named_validable_tuple(name, fields):
    def validate(self):
        for field, cls in fields:
            field = getattr(self, field)
            assert isinstance(field, cls)
            if hasattr(field, "validate"):
                field.validate()
    return type(
        name,
        (
            namedtuple(
                name,
                [field for field, _ in fields]
            ),
        ),
        {
            "validate": validate
        }
    )



