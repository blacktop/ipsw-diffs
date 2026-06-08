## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

```diff

-1513.120.7.0.0
-  __TEXT.__text: 0x80c8
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x614
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2bac
-  __TEXT.__gcc_except_tab: 0x240
-  __TEXT.__objc_methname: 0x1e81
-  __TEXT.__objc_classname: 0xad
+1655.0.0.0.0
+  __TEXT.__text: 0x7d4c
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0x16c0
+  __TEXT.__objc_methlist: 0x62c
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x2c64
+  __TEXT.__gcc_except_tab: 0x1b8
+  __TEXT.__objc_methname: 0x1ec0
+  __TEXT.__objc_classname: 0xa6
   __TEXT.__objc_methtype: 0x3cf
   __TEXT.__oslogstring: 0x142
-  __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__const: 0x328
-  __DATA_CONST.__cfstring: 0x1600
+  __DATA_CONST.__cfstring: 0x1640
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0x1a0
   __DATA.__objc_const: 0x880
-  __DATA.__objc_selrefs: 0x740
+  __DATA.__objc_selrefs: 0x750
   __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 19D000E8-2E78-3E24-8671-A2890655108F
-  Functions: 127
-  Symbols:   176
-  CStrings:  716
+  UUID: 6C00DD12-FC16-310F-A1C7-23810E9D5420
+  Functions: 129
+  Symbols:   180
+  CStrings:  722
 
Symbols:
+ _OBJC_CLASS_$_MIUserManagement
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OBJC_CLASS_$_MIGlobalConfiguration
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ "MISystemAppMigrator: Detected migration after RRTS: skipping SAD app install and migration"
+ "MISystemAppMigrator: Failed to look up primary persona: %@"
+ "MISystemAppMigrator: Migrator State--didUpgrade: %@, didRestoreFromBackup: %@, didRestoreFromCloudBackup: %@, didMigrateBackupFromDifferentDevice: %@, userDataDisposition: 0x%x"
+ "_discoverItemsToInstall"
+ "_processItemsToInstall"
+ "primaryPersonaUniqueStringWithError:"
- "MISystemAppMigrator: Migrator State--didUpgrade: %@, didRestoreFromBackup: %@, didRestoreFromCloudBackup: %@, didMigrateBackupFromDifferentDevice: %@"
- "primaryPersonaString"

```
