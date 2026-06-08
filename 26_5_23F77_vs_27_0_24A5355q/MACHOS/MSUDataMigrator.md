## MSUDataMigrator

> `/System/Library/DataClassMigrators/MSUDataMigrator.migrator/MSUDataMigrator`

```diff

-2422.120.23.0.9
-  __TEXT.__text: 0x14cc
-  __TEXT.__auth_stubs: 0x310
+2717.0.0.0.0
+  __TEXT.__text: 0x147c
+  __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x20
   __TEXT.__cstring: 0x9bf

   __TEXT.__objc_methname: 0x226
   __TEXT.__objc_methtype: 0x10
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x190
-  __DATA_CONST.__got: 0x38
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x38
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 07147592-C971-3434-B512-CBE3723E62FD
+  UUID: E2FE936B-1570-3647-B719-22F5AE2E1299
   Functions: 14
-  Symbols:   181
+  Symbols:   179
   CStrings:  100
 
Symbols:
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUDataMigrator.build/Objects-normal/arm64e/MSUDataMigrator.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUDataMigrator.build/Objects-normal/arm64e/MSUEarlyBootTask.o
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Sources/MobileSoftwareUpdate/MSUDataMigrator/
+ /Library/Caches/com.apple.xbs/045C4C30-0D13-4374-A00F-72B96D453890/TemporaryDirectory.CZdRsJ/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x8
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUDataMigrator.build/Objects-normal/arm64e/MSUDataMigrator.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUDataMigrator.build/Objects-normal/arm64e/MSUEarlyBootTask.o
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Sources/MobileSoftwareUpdate/MSUDataMigrator/
- /Library/Caches/com.apple.xbs/08FFD531-AC3D-4FAF-AAF4-8D7AACAC0B9A/TemporaryDirectory.jLzTaf/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
- _objc_release_x25
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x25
- _objc_retain_x26
Functions:
~ _debugv : 160 -> 156
~ _logString : 304 -> 292
~ _delete_folder_contents : 864 -> 848
~ _moveFolderContentsIfItExists : 656 -> 652
~ -[MSUDataMigrator performMigration] : 1616 -> 1572

```
