## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-740.53.1.0.0
-  __TEXT.__text: 0x36460
-  __TEXT.__objc_methlist: 0x3630
+740.57.1.0.0
+  __TEXT.__text: 0x36464
+  __TEXT.__objc_methlist: 0x3648
   __TEXT.__const: 0x158
   __TEXT.__oslogstring: 0x5720
   __TEXT.__cstring: 0x80eb
   __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__unwind_info: 0xbd0
+  __TEXT.__unwind_info: 0xbd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2130
+  __DATA_CONST.__objc_selrefs: 0x2138
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1409
-  Symbols:   3021
+  Functions: 1410
+  Symbols:   3023
   CStrings:  1091
 
Symbols:
+ +[RPPipViewController deviceOrientationForInterfaceOrientation:fallback:]
+ __OBJC_$_CLASS_METHODS_RPPipViewController
Functions:
~ ___48-[RPControlCenterClient setUpFrontBoardServices]_block_invoke.85 : 120 -> 108
+ +[RPPipViewController deviceOrientationForInterfaceOrientation:fallback:]
```
