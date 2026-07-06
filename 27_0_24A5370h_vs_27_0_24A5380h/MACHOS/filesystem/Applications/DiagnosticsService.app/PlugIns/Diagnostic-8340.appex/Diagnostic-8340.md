## Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

-  __TEXT.__text: 0x308c
+  __TEXT.__text: 0x309c
   __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_stubs: 0x5c0
   __TEXT.__objc_methlist: 0x2fc

   __TEXT.__objc_classname: 0x4e
   __TEXT.__objc_methname: 0x8c7
   __TEXT.__objc_methtype: 0x147
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x10
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ _initializeIOServiceConnectionWithNameAndType
- _initializeIOServiceConnectionWithName
Functions:
~ _initializeIOServiceConnectionWithName -> _initializeIOServiceConnectionWithNameAndType : 184 -> 196
~ sub_1000034ac -> sub_1000034b8 : 108 -> 112

```
