## MessagesDataMigrator

> `/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0xd70
+1450.700.11.2.3
+  __TEXT.__text: 0xd94
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__cstring: 0x80
-  __TEXT.__oslogstring: 0x2e2
+  __TEXT.__oslogstring: 0x2d5
   __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methname: 0x1c2
   __TEXT.__objc_methtype: 0x39
   __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 598D65B9-B314-377F-8817-61425490109F
+  UUID: D050F930-3CC1-36A7-98C3-EC8C085E9494
   Functions: 11
-  Symbols:   70
+  Symbols:   71
   CStrings:  39
 
Symbols:
+ _IMCKMOCAccountsMatch
Functions:
~ sub_239856598 -> sub_23a97f598 : 1272 -> 1308
CStrings:
+ "We are upgrade installing (accountsMatch: %{BOOL}d)"
- "We are upgrade installing, so no need to update the MOC defaults"

```
