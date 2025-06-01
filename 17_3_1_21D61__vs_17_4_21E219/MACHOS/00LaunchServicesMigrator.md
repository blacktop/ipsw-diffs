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

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC1D0FEE-5EC0-372D-B13A-B85E9CF7F364
+  UUID: D0FCF90A-7292-36F4-931C-46FD476F7607
   Functions: 9
   Symbols:   32
   CStrings:  49

```
