from django.core import exceptions as django_exceptions
from django.db import models as django_models

from common.models.fields import base


class PositiveIntegerEnumField(django_models.fields.PositiveIntegerField):
    MIN_VALUE = 0
    MAX_VALUE = 4294967295
    description = 'An integral enum field.'

    def __init__(self, *args, **kwargs):
        self.enum_type = kwargs.pop('enum_type', None)

        if self.enum_type:
            if not self._can_store_enum(self.enum_type):
                raise ValueError(
                    'Field type {field_type} out of range of {min_value}-{max_value}'.format(
                        field_type=self.__class__.__name__,
                        min_value=self.MIN_VALUE,
                        max_value=self.MAX_VALUE,
                    )
                )

        super(PositiveIntegerEnumField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super(PositiveIntegerEnumField, self).contribute_to_class(cls, name, **kwargs)
        setattr(cls, self.name, base.AssignmentSetter(self))

    @classmethod
    def _can_store_enum(cls, enum_type):
        enum_max_value = max(i.value for i in enum_type)
        enum_min_value = min(i.value for i in enum_type)
        if cls.MAX_VALUE < enum_max_value:
            return False
        elif cls.MIN_VALUE > enum_min_value:
            return False
        return True

    def to_python(self, value):
        if value is None:
            return None

        try:
            return self.enum_type(value)
        except ValueError:
            raise django_exceptions.ValidationError(
                'Value {0} cannot be deserialized to {1}.'.format(value, self.enum_type.__name__),
            )

    def get_prep_value(self, value):
        if value is None:
            return None

        if not isinstance(value, self.enum_type):
            raise django_exceptions.ValidationError(
                'Value {0} is not an instance of type {1}.'.format(value, self.enum_type.__name__),
            )

        return value.value

    def get_default(self):
        if self.has_default():
            if self.default is None:
                return None
            if callable(self.default):
                default = self.default()
            else:
                default = self.default

            try:
                default = self.enum_type(default)
            except ValueError:
                raise django_exceptions.ValidationError(
                    'Default value {0} is not an instance or valid value of type {1}'.format(
                        default, self.enum_type.__name__
                    ),
                )
            return default

        return super(PositiveIntegerEnumField, self).get_default()

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class PositiveSmallIntegerEnumField(PositiveIntegerEnumField):
    MIN_VALUE = 0
    MAX_VALUE = 65535

    def get_internal_type(self):
        return 'PositiveSmallIntegerField'
