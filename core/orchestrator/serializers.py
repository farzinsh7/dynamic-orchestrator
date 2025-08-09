from rest_framework import serializers

FIELD_TYPE_MAP = {
    "string": serializers.CharField,
    "integer": serializers.IntegerField,
    "boolean": serializers.BooleanField,
    "float": serializers.FloatField,
}


def build_dynamic_serializer(schema):
    fields = {}
    for field_name, rules in schema.items():
        field_cls = FIELD_TYPE_MAP[rules["type"]]
        kwargs = {k: v for k, v in rules.items() if k != "type"}
        fields[field_name] = field_cls(**kwargs)

    # Dynamically create the serializer class with the fields
    return type("DynamicSerializer", (serializers.Serializer,), fields)