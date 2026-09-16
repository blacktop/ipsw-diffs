## Diagnostic-7004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1307.2.4.0.0
-  __TEXT.__text: 0x374
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x180
+1307.40.46.0.0
+  __TEXT.__text: 0x268
+  __TEXT.__auth_stubs: 0xe0
+  __TEXT.__objc_stubs: 0x100
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__const: 0x50
   __TEXT.__oslogstring: 0xb
-  __TEXT.__cstring: 0x6c
+  __TEXT.__cstring: 0x4c
   __TEXT.__objc_classname: 0x4c
-  __TEXT.__objc_methname: 0x294
+  __TEXT.__objc_methname: 0x26a
   __TEXT.__objc_methtype: 0x100
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x78
+  __DATA_CONST.__got: 0x18
   __DATA.__objc_const: 0x2d8
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_selrefs: 0x118
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7
-  Symbols:   40
-  CStrings:  73
+  Symbols:   33
+  CStrings:  68
 
Symbols:
- _MGGetBoolAnswer
- _OBJC_CLASS_$_CRPearlController
- _OBJC_CLASS_$_NSNumber
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_retain_x8
Functions:
~ sub_100000e24 : 544 -> 276
CStrings:
- "InDiagnosticsMode"
- "InternalBuild"
- "code"
- "numberWithInteger:"
- "powerCycleSensor:"
```
