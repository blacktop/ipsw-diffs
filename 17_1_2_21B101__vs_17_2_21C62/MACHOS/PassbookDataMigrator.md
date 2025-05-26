## PassbookDataMigrator

> `/System/Library/DataClassMigrators/PassbookDataMigrator.migrator/PassbookDataMigrator`

```diff

-1552.2.4.3.0
-  __TEXT.__text: 0x158
+1552.3.6.4.0
+  __TEXT.__text: 0x160
   __TEXT.__auth_stubs: 0x60
-  __TEXT.__objc_stubs: 0xc0
+  __TEXT.__objc_stubs: 0x60
   __TEXT.__objc_methlist: 0x20
   __TEXT.__cstring: 0x10
   __TEXT.__oslogstring: 0xc4
   __TEXT.__objc_classname: 0x15
-  __TEXT.__objc_methname: 0x9b
+  __TEXT.__objc_methname: 0x68
   __TEXT.__objc_methtype: 0x10
   __TEXT.__unwind_info: 0x50
   __DATA_CONST.__auth_got: 0x38

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x40
+  __DATA.__objc_selrefs: 0x28
   __DATA.__objc_classrefs: 0x8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   Functions: 2
   Symbols:   17
-  CStrings:  15
+  CStrings:  12
 
Symbols:
+ _objc_release_x20
- _objc_release_x19
CStrings:
+ "migrateDataWithDidRestoreFromBackup:"
+ "userDataDisposition"
- "didMigrateBackupFromDifferentDevice"
- "didRestoreFromBackup"
- "didRestoreFromCloudBackup"
- "didUpgrade"
- "migrateData"

```
