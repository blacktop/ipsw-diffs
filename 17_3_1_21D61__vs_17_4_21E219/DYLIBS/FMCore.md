## FMCore

> `/System/Library/PrivateFrameworks/FMCore.framework/FMCore`

```diff

-210.0.0.0.0
-  __TEXT.__text: 0x15124
+214.0.0.0.0
+  __TEXT.__text: 0x156cc
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x1a20
+  __TEXT.__objc_methlist: 0x1a2c
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x398
   __TEXT.__cstring: 0xf3e
-  __TEXT.__oslogstring: 0x12e6
+  __TEXT.__oslogstring: 0x13ba
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__unwind_info: 0x70c
   __TEXT.__objc_classname: 0x308
-  __TEXT.__objc_methname: 0x504f
+  __TEXT.__objc_methname: 0x508f
   __TEXT.__objc_methtype: 0x12b9
-  __TEXT.__objc_stubs: 0x3de0
-  __DATA_CONST.__got: 0x228
+  __TEXT.__objc_stubs: 0x3e00
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x758
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3218
-  __DATA_CONST.__objc_selrefs: 0x13d8
+  __DATA_CONST.__objc_selrefs: 0x13e0
+  __DATA_CONST.__objc_classrefs: 0x210
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__cfstring: 0x12c0
   __AUTH_CONST.__objc_const: 0xc90

   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_classrefs: 0x210
-  __DATA.__objc_superrefs: 0xb8
   __DATA.__objc_ivar: 0x1b8
   __DATA.__data: 0x2d0
   __DATA.__bss: 0x158

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 710
-  Symbols:   2781
-  CStrings:  1418
+  Functions: 712
+  Symbols:   2788
+  CStrings:  1425
 
Symbols:
+ -[FMKeychainManager _migrateToValueDataIfNeeded:account:service:]
+ -[FMKeychainManager dataForAccount:service:].cold.1
+ _kSecReturnData
+ _kSecValueData
+ _objc_msgSend$_migrateToValueDataIfNeeded:account:service:
CStrings:
+ "Migration of keychain item result: %ld, a: %@, s: %@"
+ "No migration of keychain item required. a: %@, s: %@."
+ "T@\"NSString\",?,R,C"
+ "_migrateToValueDataIfNeeded:account:service:"
+ "dataForAccount a: %@, s: %@ error: %@"
+ "dataForAccount a: %@, s: %@."
+ "dataForAccount is empty a: %@, s: %@!"

```
