## 00LaunchServicesMigrator

> `/System/Library/DataClassMigrators/00LaunchServicesMigrator.migrator/00LaunchServicesMigrator`

```diff

-1299.2.3.2.0
+1300.5.18.0.0
   __TEXT.__text: 0x748
   __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x2e0

   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0xe8
-  __DATA.__objc_classrefs: 0x20
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

```
