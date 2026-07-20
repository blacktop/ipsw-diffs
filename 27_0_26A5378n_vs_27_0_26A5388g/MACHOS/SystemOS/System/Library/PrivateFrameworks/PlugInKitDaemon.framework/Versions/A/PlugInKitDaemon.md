## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/Versions/A/PlugInKitDaemon`

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
-  __TEXT.__text: 0x1b9c8
+512.0.0.0.0
+  __TEXT.__text: 0x1ba24
   __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_stubs: 0x3340
-  __TEXT.__objc_methlist: 0xff8
+  __TEXT.__objc_stubs: 0x3360
+  __TEXT.__objc_methlist: 0x1008
   __TEXT.__const: 0x62
-  __TEXT.__objc_methname: 0x318e
+  __TEXT.__objc_methname: 0x31aa
   __TEXT.__oslogstring: 0x32e9
   __TEXT.__cstring: 0x1314
   __TEXT.__objc_classname: 0x171

   __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2768
-  __DATA.__objc_selrefs: 0xe90
+  __DATA.__objc_selrefs: 0xe98
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x300

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 494
-  Symbols:   1400
-  CStrings:  1164
+  Functions: 495
+  Symbols:   1402
+  CStrings:  1165
 
Symbols:
+ -[PKDTransaction _getInstanceUUIDFromRequest]
+ GCC_except_table20
+ GCC_except_table27
+ GCC_except_table48
+ GCC_except_table50
+ _objc_msgSend$_getInstanceUUIDFromRequest
- GCC_except_table19
- GCC_except_table26
- GCC_except_table47
- GCC_except_table49
CStrings:
+ "_getInstanceUUIDFromRequest"
```
