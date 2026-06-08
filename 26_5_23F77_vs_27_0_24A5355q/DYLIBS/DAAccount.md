## DAAccount

> `/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0xe4
-  __TEXT.__auth_stubs: 0x50
+2703.0.0.0.0
+  __TEXT.__text: 0xe0
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0x4
   __TEXT.__cstring: 0xc
   __TEXT.__oslogstring: 0x3e
   __TEXT.__unwind_info: 0x60
-  __TEXT.__objc_classname: 0x12
-  __TEXT.__objc_methname: 0x98
-  __TEXT.__objc_methtype: 0x18
-  __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x10
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x30
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00A843DA-2A59-31BF-834E-72196FC97C65
+  UUID: FB375DEA-0ED5-3DFD-93AE-87360990EB52
   Functions: 4
   Symbols:   30
-  CStrings:  15
+  CStrings:  3
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[DAAccountMigrator performMigration] : 196 -> 192
CStrings:
- "@16@0:8"
- "B16@0:8"
- "DAAccountMigrator"
- "dataClassName"
- "didMigrateBackupFromDifferentDevice"
- "didRestoreFromBackup"
- "didUpgrade"
- "estimatedDuration"
- "f16@0:8"
- "migrationProgress"
- "performMigration"
- "upgradeAccounts:"

```
