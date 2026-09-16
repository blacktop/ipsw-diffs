## Diagnostic-9008

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1307.2.4.0.0
-  __TEXT.__text: 0xb874
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x1f20
+1307.40.46.0.0
+  __TEXT.__text: 0xb834
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0x1ec0
   __TEXT.__objc_methlist: 0x8d8
   __TEXT.__const: 0x47a
   __TEXT.__gcc_except_tab: 0x160
   __TEXT.__oslogstring: 0x947
-  __TEXT.__cstring: 0x89d
+  __TEXT.__cstring: 0x87d
   __TEXT.__objc_methname: 0x2335
   __TEXT.__objc_classname: 0x17f
   __TEXT.__objc_methtype: 0x991

   __TEXT.__unwind_info: 0x448
   __TEXT.__eh_frame: 0x74
   __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__cfstring: 0x7e0
+  __DATA_CONST.__cfstring: 0x7a0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__auth_got: 0x430
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0xdf0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 301
-  Symbols:   194
-  CStrings:  663
+  Symbols:   193
+  CStrings:  661
 
Symbols:
- _MGGetBoolAnswer
Functions:
~ sub_100005ed8 : 340 -> 276
CStrings:
- "InDiagnosticsMode"
- "InternalBuild"
```
