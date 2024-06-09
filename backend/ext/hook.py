# 作   者：林枭熠
# 开发时间:2024/6/8 下午2:03
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject


class HookSerializer:
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = {}
        fields = self._readable_fields

        for field in fields:
            if hasattr(self, 'nb_%s' % field.field_name):
                value = getattr(self, 'nb_%s' % field.field_name)(instance)
                ret[field.field_name] = value
            else:
                try:
                    attribute = field.get_attribute(instance)
                except SkipField:
                    continue
                check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
                if check_for_none is None:
                    ret[field.field_name] = None
                else:
                    ret[field.field_name] = field.to_representation(attribute)
        return ret
