from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BootstrapRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class BootstrapResponse(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class FileInput(_message.Message):
    __slots__ = ["path"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["prompt"]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    def __init__(self, prompt: _Optional[str] = ...) -> None: ...

class ReadyRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadyResponse(_message.Message):
    __slots__ = ["ready"]
    READY_FIELD_NUMBER: _ClassVar[int]
    ready: bool
    def __init__(self, ready: bool = ...) -> None: ...
