## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-921.60.3.0.1
-  __TEXT.__text: 0x5207c
+921.60.4.0.1
+  __TEXT.__text: 0x520b4
   __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_methlist: 0x4c64
   __TEXT.__const: 0x360

   __TEXT.__objc_methname: 0x9b14
   __TEXT.__objc_methtype: 0x13eb
   __TEXT.__objc_stubs: 0x53c0
-  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__got: 0x3e0
   __DATA_CONST.__const: 0xc40
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8D36BE3-C77A-36A7-98DB-2537E5B36A7D
+  UUID: 26D64AD6-382B-3649-AEF5-31E837D70276
   Functions: 1715
-  Symbols:   5083
+  Symbols:   5084
   CStrings:  3672
 
Symbols:
+ _kSecUseDataProtectionKeychain
Functions:
~ +[NPUtilities saveDataToKeychain:withIdentifier:accountName:] : 536 -> 564
~ +[NPUtilities saveKeyToKeychain:withIdentifier:] : 340 -> 368

```
