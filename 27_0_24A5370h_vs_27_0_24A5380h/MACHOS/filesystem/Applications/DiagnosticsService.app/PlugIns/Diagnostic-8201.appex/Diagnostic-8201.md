## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

-  __TEXT.__text: 0x223d0
+  __TEXT.__text: 0x223e0
   __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0xa80
   __TEXT.__init_offsets: 0x4
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
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
~ sub_100017f48 -> sub_100017f54 : 108 -> 112

```
