## MSUDataMigrator

> `/System/Library/DataClassMigrators/MSUDataMigrator.migrator/MSUDataMigrator`

```diff

-2422.80.9.0.2
-  __TEXT.__text: 0x1484
-  __TEXT.__auth_stubs: 0x2f0
+2422.100.179.0.3
+  __TEXT.__text: 0x14cc
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x20
   __TEXT.__cstring: 0x9bf

   __TEXT.__objc_methname: 0x226
   __TEXT.__objc_methtype: 0x10
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C27CD9B8-818B-3623-B7E9-4CBC6AA01AF4
+  UUID: 4E130E60-7A5C-3E79-A876-2B2B4ED93D1A
   Functions: 14
-  Symbols:   179
+  Symbols:   181
   CStrings:  100
 
Symbols:
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUDataMigrator.build/Objects-normal/arm64e/MSUDataMigrator.o
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUDataMigrator.build/Objects-normal/arm64e/MSUEarlyBootTask.o
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Sources/MobileSoftwareUpdate/MSUDataMigrator/
+ /Library/Caches/com.apple.xbs/7402B4CC-18BB-4CD4-BF13-EC385A655759/TemporaryDirectory.psCVfe/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
+ _objc_release_x25
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x25
+ _objc_retain_x26
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUDataMigrator.build/Objects-normal/arm64e/MSUDataMigrator.o
- /Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUDataMigrator.build/Objects-normal/arm64e/MSUEarlyBootTask.o
- /Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUDataMigrator/
- /Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x8
Functions:
~ _debugv : 156 -> 160
~ _logString : 292 -> 304
~ _delete_folder_contents : 844 -> 864
~ _moveFolderContentsIfItExists : 652 -> 656
~ -[MSUDataMigrator performMigration] : 1584 -> 1616

```
