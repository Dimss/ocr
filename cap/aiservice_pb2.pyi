from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileInput(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class PredictRequest(_message.Message):
    __slots__ = ["file_input", "prompt_input"]
    FILE_INPUT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_INPUT_FIELD_NUMBER: _ClassVar[int]
    file_input: FileInput
    prompt_input: PromptInput
    def __init__(self, prompt_input: _Optional[_Union[PromptInput, _Mapping]] = ..., file_input: _Optional[_Union[FileInput, _Mapping]] = ...) -> None: ...

class PredictResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class PromptInput(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...
