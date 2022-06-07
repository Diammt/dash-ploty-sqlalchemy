from sqlalchemy_serializer import SerializerMixin


class BaseModel(SerializerMixin):

    @classmethod
    def schema(cls):
        no_nullbale_columns = [column for column in cls.__table__.columns if not column.nullable and column.key != "id"]
        nullable_columns = [column for column in cls.__table__.columns if column.nullable]
        schema = {
            "type": "object"
        }
        properties = {}
        for column in no_nullbale_columns + nullable_columns:
            properties.update({
                column.key: {
                    "type": "string"
                }
            })
        required = []
        for column in no_nullbale_columns:
            required.append(column.key)
        schema.update({
            "properties": properties,
            "required": required
        })
        return schema

    
