## ToolRenderer

> `/System/Library/PrivateFrameworks/ToolRenderer.framework/ToolRenderer`

```diff

-  __TEXT.__text: 0x81264
-  __TEXT.__const: 0x57b2
-  __TEXT.__swift5_typeref: 0x140c
+  __TEXT.__text: 0x82fcc
+  __TEXT.__const: 0x57c2
+  __TEXT.__swift5_typeref: 0x1406
   __TEXT.__swift5_capture: 0x9b0
-  __TEXT.__cstring: 0x500b
-  __TEXT.__swift5_reflstr: 0x16a7
+  __TEXT.__cstring: 0x54db
+  __TEXT.__swift5_reflstr: 0x16d7
   __TEXT.__swift5_assocty: 0x438
-  __TEXT.__constg_swiftt: 0x1160
-  __TEXT.__swift5_fieldmd: 0x1cac
+  __TEXT.__constg_swiftt: 0x1144
+  __TEXT.__swift5_fieldmd: 0x1cc0
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_proto: 0x570
-  __TEXT.__swift5_types: 0x1dc
-  __TEXT.__swift_as_entry: 0x2a4
-  __TEXT.__swift_as_ret: 0x1b8
+  __TEXT.__swift5_proto: 0x560
+  __TEXT.__swift5_types: 0x1d8
+  __TEXT.__swift_as_entry: 0x298
+  __TEXT.__swift_as_ret: 0x1b4
   __TEXT.__swift_as_cont: 0x4d0
   __TEXT.__oslogstring: 0x157
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x2290
-  __TEXT.__eh_frame: 0x5e98
+  __TEXT.__unwind_info: 0x2258
+  __TEXT.__eh_frame: 0x5d60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5a0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x69f0
-  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__const: 0x6998
+  __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0xf8
-  __AUTH_CONST.__auth_got: 0xcf8
+  __AUTH_CONST.__auth_got: 0xd08
   __AUTH.__data: 0x5b8
-  __DATA.__data: 0xd80
+  __DATA.__data: 0xd60
   __DATA.__bss: 0x5e10
   __DATA.__common: 0x8
-  __DATA_DIRTY.__data: 0x118
+  __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3522
-  Symbols:   3185
-  CStrings:  505
+  Functions: 3529
+  Symbols:   3224
+  CStrings:  512
 
Sections:
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__data : content changed
Symbols:
+ _OUTLINED_FUNCTION_317
+ ___swift_memcpy144_8
+ _get_enum_tag_for_layout_string 12ToolRenderer20ArgumentDefaultValueO
+ _swift_retain_n
+ _type_layout_string 12ToolRenderer20ArgumentDefaultValueO
- ___swift_memcpy136_8
- _symbolic _____ 7ToolKit14TypeIdentifierO09PrimitivecD0O0A8RendererE22PersonPythonDefinitionV
CStrings:
+ "\n\nclass Measurement:\n    \"\"\"A measurement of a quantity in a specific unit.\"\"\"\n\n    def __init__(self, "
+ "\":\n        \"\"\"This measurement converted to a different unit. Use this to normalize units before comparing or doing arithmetic with measurements.\n        Args:\n            "
+ "# ContentCollection[T] is `List[T]` renamed to surface Shortcuts' content-collection semantics. Treat it as a flat, 1-indexed collection that stands in for a single T wherever the runtime can.\n#\n# - Tools take ContentCollection[T] as input and return it as output. Mapping tools (e.g. com_apple_shortcuts_adjust_date) apply the same operation to every element and return a same-sized collection.\n# - Wherever a parameter accepts T, ContentCollection[T] is accepted in its place — the runtime resolves the collection-vs-single mismatch automatically.\n# - Property access auto-maps: e.g. `events.title` on ContentCollection[CalendarEvent] yields ContentCollection[str].\n# - Collections are flat — no ContentCollection[ContentCollection[T]].\n#\n# Subscript with get_item_from_list ONLY when:\n# - You're confident the collection has multiple items AND the next step needs exactly one of them, or\n# - You want to deterministically discard all items except one, without asking the user to choose.\n#\n# In every other case, pass the ContentCollection through directly.\nContentCollection = List"
+ ": The unit to convert the measurement to.\n        \"\"\""
+ "ContentCollection["
+ "format"
+ "is.workflow.actions.ride.requestride"
- "\n\nclass Measurement:\n    \"\"\"A measurement of a quantity in a specific unit.\"\"\"\n    \n    def __init__(self, "
- ":\n    display_name: Optional[str]\n    name_components: Optional[PersonNameComponents]\n    handle: Optional[PersonHandle]\n    label: Optional[PersonLabel]\n    relationship: Optional[PersonRelationship]"

```
