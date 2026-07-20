## BacklightServices

> `/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-6.0.36.0.0
-  __TEXT.__text: 0x29af0
-  __TEXT.__objc_methlist: 0x381c
+6.0.38.0.0
+  __TEXT.__text: 0x29af4
+  __TEXT.__objc_methlist: 0x3824
   __TEXT.__const: 0x138
   __TEXT.__oslogstring: 0x2987
   __TEXT.__cstring: 0x1b86
   __TEXT.__ustring: 0xfe
   __TEXT.__gcc_except_tab: 0xcb4
-  __TEXT.__unwind_info: 0x1058
+  __TEXT.__unwind_info: 0x1060
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1678
+  __DATA_CONST.__objc_selrefs: 0x1680
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__got: 0x400

   __AUTH.__objc_data: 0x16d0
   __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0xc68
-  __DATA.__bss: 0xd9
+  __DATA.__bss: 0xe1
   __DATA_DIRTY.__objc_data: 0xaa0
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1335
-  Symbols:   3255
+  Functions: 1336
+  Symbols:   3257
   CStrings:  525
 
Symbols:
+ +[BLSLowPowerRenderingAttribute requestLowPowerRenderingForFBSScene:]
+ _objc_msgSend$requestLowPowerRenderingForFBSScene:
Functions:
+ +[BLSLowPowerRenderingAttribute lowPowerRenderingForFBSScene:]
```
