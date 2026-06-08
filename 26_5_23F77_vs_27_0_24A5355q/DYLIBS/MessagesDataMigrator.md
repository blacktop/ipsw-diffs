## MessagesDataMigrator

> `/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0xd70
-  __TEXT.__auth_stubs: 0x1a0
+1481.100.29.2.9
+  __TEXT.__text: 0xd00
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0xc0
   __TEXT.__cstring: 0x80
-  __TEXT.__oslogstring: 0x2e2
+  __TEXT.__oslogstring: 0x2d5
   __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0x15
-  __TEXT.__objc_methname: 0x1c2
-  __TEXT.__objc_methtype: 0x39
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x120
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 598D65B9-B314-377F-8817-61425490109F
+  UUID: 5724D915-BBA9-3C4D-B33D-E74EAC8F801E
   Functions: 11
-  Symbols:   70
-  CStrings:  39
+  Symbols:   69
+  CStrings:  16
 
Symbols:
+ _IMCKMOCAccountsMatch
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ sub_239855d2c -> sub_23c47dd2c : 356 -> 324
~ sub_2398562fc -> sub_23c47e2dc : 668 -> 600
~ sub_239856598 -> sub_23c47e534 : 1272 -> 1260
CStrings:
+ "We are upgrade installing (accountsMatch: %{BOOL}d)"
- "@16@0:8"
- "B16@0:8"
- "We are upgrade installing, so no need to update the MOC defaults"
- "__im_setiCloudBackupAttribute:onDirectoryAndChildrenAtPath:error:"
- "_cloudKitEnabled"
- "_didRestoreFromDeviceToDevice"
- "_printCriticalDefaultsWithMessage:"
- "clearMOCDefaultsForRestoreFromBackupIfNeeded"
- "dataClassName"
- "defaultManager"
- "didMigrateBackupFromDifferentDevice"
- "didRestoreFromBackup"
- "didRestoreFromCloudBackup"
- "didUpgrade"
- "estimatedDuration"
- "f16@0:8"
- "performMigration"
- "saveDeviceState:isMigrating:"
- "setiCloudBackupsAndRestoresEnabledForSMSDirectory"
- "userDataDisposition"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8B16B20"

```
