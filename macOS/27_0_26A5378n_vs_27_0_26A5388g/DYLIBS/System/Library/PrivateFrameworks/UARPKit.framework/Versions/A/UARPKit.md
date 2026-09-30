## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1587.0.21.0.0
-  __TEXT.__text: 0x15974
-  __TEXT.__objc_methlist: 0x14d8
+1587.0.27.0.0
+  __TEXT.__text: 0x15a30
+  __TEXT.__objc_methlist: 0x14f8
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x1dea
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__oslogstring: 0x8a3
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__unwind_info: 0x450
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd78
+  __DATA_CONST.__objc_selrefs: 0xd88
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x1e88
+  __AUTH_CONST.__objc_const: 0x1e90
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x18c

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 537
-  Symbols:   1026
+  Functions: 539
+  Symbols:   1029
   CStrings:  249
 
Symbols:
+ -[UARPDeviceManager startPruning]
+ GCC_except_table130
+ GCC_except_table133
+ ___33-[UARPDeviceManager startPruning]_block_invoke
+ _objc_msgSend$endpointControllerStartPruning
- GCC_except_table128
- GCC_except_table131
```
