## ToolRenderer

> `/System/Library/PrivateFrameworks/ToolRenderer.framework/Versions/A/ToolRenderer`

```diff

-5037.0.17.0.0
-  __TEXT.__text: 0x811a0
-  __TEXT.__const: 0x5b42
-  __TEXT.__swift5_typeref: 0x1480
-  __TEXT.__swift5_capture: 0x9e8
-  __TEXT.__cstring: 0x576b
-  __TEXT.__swift5_reflstr: 0x1787
-  __TEXT.__swift5_assocty: 0x468
-  __TEXT.__constg_swiftt: 0x11c8
-  __TEXT.__swift5_fieldmd: 0x1dcc
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_proto: 0x580
-  __TEXT.__swift5_types: 0x1e8
-  __TEXT.__swift_as_entry: 0x298
-  __TEXT.__swift_as_ret: 0x1bc
-  __TEXT.__swift_as_cont: 0x4e0
+5110.0.8.0.0
+  __TEXT.__text: 0x83524
+  __TEXT.__const: 0x5fa2
+  __TEXT.__swift5_typeref: 0x14fa
+  __TEXT.__swift5_capture: 0xa28
+  __TEXT.__cstring: 0x581b
+  __TEXT.__swift5_reflstr: 0x1807
+  __TEXT.__swift5_assocty: 0x498
+  __TEXT.__constg_swiftt: 0x12e4
+  __TEXT.__swift5_fieldmd: 0x1f24
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_proto: 0x5d8
+  __TEXT.__swift5_types: 0x204
+  __TEXT.__swift_as_entry: 0x2e8
+  __TEXT.__swift_as_ret: 0x1e8
+  __TEXT.__swift_as_cont: 0x510
+  __TEXT.__swift5_protos: 0x34
   __TEXT.__oslogstring: 0x197
-  __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__unwind_info: 0x28b8
-  __TEXT.__eh_frame: 0x5f40
+  __TEXT.__unwind_info: 0x29d0
+  __TEXT.__eh_frame: 0x6178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5a0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x6d18
+  __AUTH_CONST.__const: 0x7380
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x118
-  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH_CONST.__auth_got: 0xbf0
   __AUTH.__data: 0x5c0
-  __DATA.__data: 0xe20
+  __DATA.__data: 0xe68
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__common: 0x30

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3655
-  Symbols:   1263
-  CStrings:  510
+  Functions: 3783
+  Symbols:   1277
+  CStrings:  513
 
Symbols:
+ _WFWorkflowTypeShowInSearch
+ __swift_exist.box.addr_destructor.74Tm
+ _associated conformance So18WFWorkflowTypeNameaSHSCSQ
+ _associated conformance So18WFWorkflowTypeNameas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So18WFWorkflowTypeNameas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _symbolic $s12ToolRenderer20RunSurfaceEnablementP
+ _symbolic _____ 12ToolRenderer15WatchEnablementV
+ _symbolic _____ 12ToolRenderer20ShareSheetEnablementV
+ _symbolic _____ 12ToolRenderer22QuickActionsEnablementV
+ _symbolic _____ 12ToolRenderer22ShowInSearchEnablementV
+ _symbolic _____ 12ToolRenderer23WhatsOnScreenEnablementV
+ _symbolic _____ 12ToolRenderer31EnablementClassPythonDefinitionV
+ _symbolic _____ So18WFWorkflowTypeNamea
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 12ToolRenderer20RunSurfaceEnablementP
+ _type_layout_string 12ToolRenderer15WatchEnablementV
+ _type_layout_string 12ToolRenderer31EnablementClassPythonDefinitionV
- _WFWorkflowTypeMenuBar
- _WFWorkflowTypeSleep
CStrings:
+ "\": ...\n@staticmethod\ndef "
+ "Referable = TypeVar(\"Referable\")\n\nclass CatalogRef(Generic[Referable]):\n    \"\"\"\n    A reference to a value in the parameter catalog.\n    \"\"\"\n\ndef ref(tag: int, /) -> CatalogRef:\n    \"\"\"\n    A reference to an entry in the parameter catalog.\n    Only tags returned from tool calls are valid.\n    Tag must be formatted as a 4 digit hex number, e.g. 0xABCD\n    \"\"\"\n    ...\n\nclass Resolved(CatalogRef[Referable]):\n    \"\"\"\n    An entity which must be retrieved from the user's device.\n    Identify it by searching for the entity by name, then pass the returned catalog reference (ref(0x…)).\n    \"\"\"\n\nclass Picked(CatalogRef[Referable]):\n    \"\"\"\n    A value that must be chosen by the user.\n    Use the pick tool with a descriptive question to ask the user to select this value.\n    \"\"\"\n\nclass Comparable:\n    \"\"\"\n    A type whose values can be searched by name.\n    Name searches return catalog references for values of this type.\n    \"\"\""
+ "Whether the shortcut runs on the "
+ "from typing import Any, Callable, Optional, Union, List, Dict, Literal, TypeVar, Generic, Protocol"
+ "input_from_search"
+ "input_from_search: bool = False"
+ "input_from_search=True"
+ "on the specified run surfaces"
- "INPUT_FROM_SEARCH"
- "Referable = TypeVar(\"Referable\")\n\nclass CatalogRef(Generic[Referable]):\n    \"\"\"\n    A reference to a value in the parameter catalog.\n    \"\"\"\n\ndef ref(tag: int, /) -> CatalogRef:\n    \"\"\"\n    Represents a catalog entry returned by find_entities or pick.\n    Only tags returned from these tools are valid.\n    Tag must be formatted as a 4 digit hex number, e.g. 0xABCD\n    \"\"\"\n    ...\n\nclass Resolved(CatalogRef[Referable]):\n    \"\"\"\n    An entity which must be retrieved from the user's device.\n    Retrieve entites using the find_entities tool.\n    \"\"\"\n\nclass Picked(CatalogRef[Referable]):\n    \"\"\"\n    A value that must be chosen by the user.\n    Use the pick tool with a descriptive question to ask the user to select this value.\n    \"\"\"\n\nclass Comparable:\n    \"\"\"\n    A type whose values can be searched by name.\n    Use the find_entities tool to resolve values of this type.\n    \"\"\""
- "The surface on which to show this shortcut."
- "from typing import Any, Callable, Optional, Union, List, Dict, Literal, TypeVar, Generic"
- "on the specified run surface"
```
