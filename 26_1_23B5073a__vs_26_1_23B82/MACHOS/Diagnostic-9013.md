## Diagnostic-9013

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9013.appex/Diagnostic-9013`

```diff

 921.40.62.0.0
-  __TEXT.__text: 0x1740
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x3a0
+  __TEXT.__text: 0x1ad4
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x460
   __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x1a8
-  __TEXT.__oslogstring: 0x186
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x1dd
+  __TEXT.__oslogstring: 0x22f
   __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0x4c6
+  __TEXT.__objc_methname: 0x4d6
   __TEXT.__objc_methtype: 0x184
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0xf8
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x48
-  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x428
-  __DATA.__objc_selrefs: 0x1f0
+  __DATA.__objc_selrefs: 0x1f8
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BF424F26-CAFE-3CFC-863A-61380BA499D0
-  Functions: 29
-  Symbols:   61
-  CStrings:  159
+  UUID: 910B6373-1068-397F-BC0A-7B8CD8E9D05E
+  Functions: 30
+  Symbols:   63
+  CStrings:  169
 
Symbols:
+ _objc_release_x27
+ _objc_release_x28
Functions:
~ sub_100001268 : 260 -> 1020
+ sub_100002298
- sub_100001fac
+ sub_1000024d4
CStrings:
+ "Failed to probe gasgauge status, error: %@"
+ "Gasgauge already locked, exiting..."
+ "Gasgauge locking not required, exiting..."
+ "Locking gasgauge..."
+ "currentGasgaugeLockStatus"
+ "doGgLock: %d, doGgReset: %d"
+ "numberWithBool:"
+ "previousGasgaugeLockStatus"

```
