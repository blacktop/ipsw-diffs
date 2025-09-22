## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1188.0.11.0.0
-  __TEXT.__text: 0x646ec
+1188.40.8.0.1
+  __TEXT.__text: 0x6432c
   __TEXT.__auth_stubs: 0x1950
   __TEXT.__objc_methlist: 0x1e0c
   __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0xd78a
-  __TEXT.__oslogstring: 0x38d6
-  __TEXT.__gcc_except_tab: 0x2d8c
+  __TEXT.__cstring: 0xd68d
+  __TEXT.__oslogstring: 0x382c
+  __TEXT.__gcc_except_tab: 0x2d1c
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__unwind_info: 0x16d0
   __TEXT.__objc_classname: 0x30c
-  __TEXT.__objc_methname: 0x4fb5
+  __TEXT.__objc_methname: 0x4f9a
   __TEXT.__objc_methtype: 0x1595
-  __TEXT.__objc_stubs: 0x40a0
+  __TEXT.__objc_stubs: 0x4080
   __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__const: 0x28c8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1530
+  __DATA_CONST.__objc_selrefs: 0x1528
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x4130
   __AUTH_CONST.__auth_got: 0xcb8
   __AUTH_CONST.__const: 0x940
-  __AUTH_CONST.__cfstring: 0x180e0
+  __AUTH_CONST.__cfstring: 0x18080
   __AUTH_CONST.__objc_const: 0x3510
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0xc0

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 732286B4-E2E1-374E-8AA4-FC7016901477
-  Functions: 1898
-  Symbols:   5879
-  CStrings:  7944
+  UUID: C48577F0-53C4-3723-B5EC-7033AF30DA69
+  Functions: 1897
+  Symbols:   5876
+  CStrings:  7935
 
Symbols:
+ _____PCSDeleteGuitarfishTokenRecord_block_invoke.26
- ___PCSCopyHSMData.cold.2
- _____PCSDeleteGuitarfishTokenRecord_block_invoke.33
- _objc_msgSend$passwordVersionForAccount:
Functions:
~ ___PCSCopyHSMData : 908 -> 700
~ _PCSGuitarfishCreateSetupParameters : 3100 -> 3048
~ _PCSGuitarfishRepairIdentities : 10380 -> 10132
~ _PCSGuitarfishValidateIdentities : 6656 -> 6340
~ ___PCSCopyHSMData.cold.1 : 136 -> 220
- ___PCSCopyHSMData.cold.2
CStrings:
- "No kPCSSetupPasswordGeneration provided, unable to attempt HSM p_password recovery"
- "Not attempting recovery because input (%@) password generation does not match the record (%@) password generation"
- "expected password version %@ and got %@ from the record"
- "passwordVersionForAccount:"

```
