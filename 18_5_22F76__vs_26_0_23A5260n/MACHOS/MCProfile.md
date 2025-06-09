## MCProfile

> `/System/Library/DataClassMigrators/MCProfile.migrator/MCProfile`

```diff

-2400.5.2.0.0
-  __TEXT.__text: 0xf0c
+2420.1.1.0.0
+  __TEXT.__text: 0xf24
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_stubs: 0x560
   __TEXT.__objc_methlist: 0xa4
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x366
+  __TEXT.__cstring: 0x385
   __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methname: 0x521
   __TEXT.__objc_methtype: 0x2b

   __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B17C940E-DD73-303E-9BF1-6A79C9CDCC97
+  UUID: 77703AE9-582E-35AE-964B-B7C760FC621F
   Functions: 16
   Symbols:   61
-  CStrings:  96
+  CStrings:  98
 
Symbols:
+ _MCPostSetupAutoInstallProfilePathNF
- _MCPostSetupAutoInstallProfilePath
Functions:
~ sub_ad4 : 984 -> 1008
CStrings:
+ "MCProfileMigrator: context: %@"

```
