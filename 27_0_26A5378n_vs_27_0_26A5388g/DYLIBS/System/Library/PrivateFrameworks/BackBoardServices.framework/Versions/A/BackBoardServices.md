## BackBoardServices

> `/System/Library/PrivateFrameworks/BackBoardServices.framework/Versions/A/BackBoardServices`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__DATA.__data`

```diff

-868.0.0.0.0
-  __TEXT.__text: 0x5fe9c
-  __TEXT.__objc_methlist: 0x6124
+873.200.0.0.0
+  __TEXT.__text: 0x5fef0
+  __TEXT.__objc_methlist: 0x613c
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x320
-  __TEXT.__cstring: 0x83ae
+  __TEXT.__cstring: 0x83ce
   __TEXT.__oslogstring: 0x139a
   __TEXT.__ustring: 0x14
   __TEXT.__dlopen_cstrs: 0x96

   __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2078
+  __DATA_CONST.__objc_selrefs: 0x2088
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x590
   __AUTH_CONST.__const: 0x1a00
-  __AUTH_CONST.__cfstring: 0x7a20
-  __AUTH_CONST.__objc_const: 0xcb60
+  __AUTH_CONST.__cfstring: 0x7a40
+  __AUTH_CONST.__objc_const: 0xcb70
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x418
-  __AUTH.__objc_data: 0x1720
+  __AUTH.__objc_data: 0x14f0
   __DATA.__objc_ivar: 0x690
   __DATA.__data: 0xba0
-  __DATA.__bss: 0x428
-  __DATA_DIRTY.__objc_data: 0x1130
-  __DATA_DIRTY.__bss: 0x168
+  __DATA.__bss: 0x3f8
+  __DATA_DIRTY.__objc_data: 0x1360
+  __DATA_DIRTY.__bss: 0x198
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2291
-  Symbols:   4994
-  CStrings:  1386
+  Functions: 2293
+  Symbols:   4998
+  CStrings:  1387
 
Symbols:
+ -[BKSHIDTouchRoutingPolicy setAvoidCancelingContinuingClients:]
+ -[BKSHIDTouchRoutingPolicy shouldAvoidCancelingContinuingClients]
+ GCC_except_table1903
+ GCC_except_table1904
+ GCC_except_table2150
+ GCC_except_table2159
+ GCC_except_table2220
+ _objc_msgSend$setAvoidCancelingContinuingClients:
+ _objc_msgSend$shouldAvoidCancelingContinuingClients
- GCC_except_table1901
- GCC_except_table1902
- GCC_except_table2148
- GCC_except_table2157
- GCC_except_table2218
Functions:
~ -[BKSHIDTouchRoutingPolicy initWithCoder:] : 1036 -> 1064
~ -[BKSHIDTouchRoutingPolicy encodeWithCoder:] : 260 -> 288
+ -[BKSHIDTouchRoutingPolicy setAvoidCancelingContinuingClients:]
+ -[BKSHIDTouchRoutingPolicy setRestrictHitTestToTheseTargets:]
CStrings:
+ "avoidCancelingContinuingClients"
+ "backboardd-attr-cache-21000327"
- "backboardd-attr-cache-21000325"
```
