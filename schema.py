from pydantic import BaseModel

# Shema object is too complex to describe
# See https://www.asyncapi.com/docs/specifications/2.0.0#schemaObject
# So, using the type provided by pydantic `schema` method
Schema = type(BaseModel.schema())
