## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x18fec
+  __TEXT.__text: 0x1904c
   __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_stubs: 0x3080
-  __TEXT.__objc_methlist: 0xfb8
-  __TEXT.__const: 0x62
-  __TEXT.__objc_methname: 0x2f44
+  __TEXT.__objc_stubs: 0x30a0
+  __TEXT.__objc_methlist: 0xfc8
+  __TEXT.__const: 0x6a
+  __TEXT.__objc_methname: 0x2f60
   __TEXT.__oslogstring: 0x2ce7
   __TEXT.__cstring: 0x11b6
   __TEXT.__objc_classname: 0x192

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x2768
-  __DATA.__objc_selrefs: 0xdf0
+  __DATA.__objc_selrefs: 0xdf8
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x300

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 447
-  Symbols:   1345
-  CStrings:  1088
+  Functions: 448
+  Symbols:   1347
+  CStrings:  1089
 
Symbols:
+ -[PKDTransaction _getInstanceUUIDFromRequest]
+ GCC_except_table15
+ GCC_except_table18
+ GCC_except_table34
+ GCC_except_table36
+ _objc_msgSend$_getInstanceUUIDFromRequest
- GCC_except_table14
- GCC_except_table17
- GCC_except_table33
- GCC_except_table35
Functions:
~ -[PKDTransaction initWithRequest:forClient:] : 632 -> 260
~ -[PKDTransaction dispatch] : 684 -> 880
+ -[PKDTransaction _getInstanceUUIDFromRequest]
CStrings:
+ "_getInstanceUUIDFromRequest"
```
