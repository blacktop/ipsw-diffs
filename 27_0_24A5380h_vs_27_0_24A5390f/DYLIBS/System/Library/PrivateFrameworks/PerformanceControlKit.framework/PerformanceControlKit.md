## PerformanceControlKit

> `/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1794.0.7.0.2
-  __TEXT.__text: 0x12b64
-  __TEXT.__objc_methlist: 0x624
-  __TEXT.__cstring: 0xa3a
-  __TEXT.__gcc_except_tab: 0x1738
-  __TEXT.__const: 0xed0
-  __TEXT.__unwind_info: 0x780
+1794.0.24.0.0
+  __TEXT.__text: 0x12dd8
+  __TEXT.__objc_methlist: 0x654
+  __TEXT.__cstring: 0xa88
+  __TEXT.__gcc_except_tab: 0x1788
+  __TEXT.__const: 0xef0
+  __TEXT.__unwind_info: 0x798
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x370
+  __DATA_CONST.__objc_selrefs: 0x380
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x5d0
-  __AUTH_CONST.__cfstring: 0xc00
-  __AUTH_CONST.__objc_const: 0xe20
+  __AUTH_CONST.__cfstring: 0xc40
+  __AUTH_CONST.__objc_const: 0xe30
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x230

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 312
-  Symbols:   872
-  CStrings:  124
+  Functions: 314
+  Symbols:   876
+  CStrings:  126
 
Symbols:
+ -[CLPCUserClient getDeviceOrientationMode:]
+ -[CLPCUserClient setDeviceOrientationMode:error:]
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table32
- GCC_except_table30
CStrings:
+ "Failed to get Device Orientation Mode."
+ "Failed to set Device Orientation Mode."
```
