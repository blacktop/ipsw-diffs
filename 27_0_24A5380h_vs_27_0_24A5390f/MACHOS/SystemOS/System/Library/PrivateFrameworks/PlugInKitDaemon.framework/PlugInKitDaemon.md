## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-511.0.0.0.0
-  __TEXT.__text: 0x177ec
+512.0.0.0.0
+  __TEXT.__text: 0x17848
   __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_stubs: 0x3180
-  __TEXT.__objc_methlist: 0xfe8
+  __TEXT.__objc_stubs: 0x31a0
+  __TEXT.__objc_methlist: 0xff8
   __TEXT.__const: 0x62
-  __TEXT.__objc_methname: 0x3062
+  __TEXT.__objc_methname: 0x307e
   __TEXT.__oslogstring: 0x2c24
   __TEXT.__cstring: 0x138c
   __TEXT.__objc_classname: 0x171

   __DATA_CONST.__got: 0x480
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2798
-  __DATA.__objc_selrefs: 0xe28
+  __DATA.__objc_selrefs: 0xe30
   __DATA.__objc_ivar: 0x11c
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x300

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 436
-  Symbols:   1366
-  CStrings:  1104
+  Functions: 437
+  Symbols:   1368
+  CStrings:  1105
 
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
~ -[PKDTransaction initWithRequest:forClient:] : 568 -> 256
~ -[PKDTransaction dispatch] : 668 -> 812
+ -[PKDTransaction marshalPaths:]
CStrings:
+ "_getInstanceUUIDFromRequest"
```
