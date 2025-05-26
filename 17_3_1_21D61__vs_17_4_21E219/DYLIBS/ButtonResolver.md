## ButtonResolver

> `/System/Library/PrivateFrameworks/ButtonResolver.framework/ButtonResolver`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x9a78
+37.100.1.0.0
+  __TEXT.__text: 0x9e58
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x75c
-  __TEXT.__cstring: 0xbc4
+  __TEXT.__objc_methlist: 0x764
+  __TEXT.__cstring: 0xc07
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__oslogstring: 0x320
-  __TEXT.__unwind_info: 0x224
+  __TEXT.__oslogstring: 0x33e
+  __TEXT.__unwind_info: 0x234
   __TEXT.__objc_classname: 0x7b
-  __TEXT.__objc_methname: 0xcff
+  __TEXT.__objc_methname: 0xd15
   __TEXT.__objc_methtype: 0x2d5
-  __TEXT.__objc_stubs: 0xec0
+  __TEXT.__objc_stubs: 0xee0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x990
-  __DATA_CONST.__objc_selrefs: 0x3f8
+  __DATA_CONST.__objc_selrefs: 0x400
+  __DATA_CONST.__objc_classrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x4f0
   __AUTH_CONST.__cfstring: 0xbe0
   __AUTH_CONST.__objc_const: 0x3f0

   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x1d0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0xa0
-  __DATA.__objc_superrefs: 0x40
   __DATA.__objc_ivar: 0xd4
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 219
-  Symbols:   823
-  CStrings:  413
+  Functions: 227
+  Symbols:   840
+  CStrings:  416
 
Symbols:
+ -[BRInterfaceLegacy serviceRemovedHandler:]
+ -[BRInterfaceLegacy serviceRemovedHandler:].cold.1
+ -[BRInterfaceLegacy serviceRemovedHandler:].cold.2
+ GCC_except_table11
+ _objc_msgSend$serviceRemovedHandler:
- GCC_except_table9
CStrings:
+ "%s Legacy service removed: %p"
+ "serviceRemovedHandler:"
+ "void serviceRemovedCallback(void *, void *, IOHIDServiceClientRef)"

```
