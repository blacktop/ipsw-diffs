## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.60.9.0.0
-  __TEXT.__text: 0x3141c0
+4257.80.5.0.2
+  __TEXT.__text: 0x3141d8
   __TEXT.__auth_stubs: 0x1b40
   __TEXT.__objc_methlist: 0x1a44c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7dc32
+  __TEXT.__cstring: 0x7dc38
   __TEXT.__oslogstring: 0x3c3ae
-  __TEXT.__gcc_except_tab: 0x1a648
+  __TEXT.__gcc_except_tab: 0x1a634
   __TEXT.__ustring: 0x88
   __TEXT.__unwind_info: 0xa070
   __TEXT.__objc_classname: 0x2b47
-  __TEXT.__objc_methname: 0x44a4e
+  __TEXT.__objc_methname: 0x44a54
   __TEXT.__objc_methtype: 0x90b4
   __TEXT.__objc_stubs: 0x2f520
   __DATA_CONST.__got: 0x1718

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E43E32E5-93DE-3EC2-94D7-A9E76FCB00E5
+  UUID: 87D3674C-EDF3-3CFB-96D7-3A407D28E23C
   Functions: 13649
   Symbols:   44440
   CStrings:  27821
Symbols:
+ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:error:]
+ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:error:].cold.1
+ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:error:].cold.2
+ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:error:].cold.3
+ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:error:].cold.4
+ ___block_literal_global.509
+ _objc_msgSend$_shouldReingestAfterUploadErrorWithItem:record:error:
- -[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:].cold.11
- -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:]
- -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:].cold.1
- -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:].cold.2
- -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:].cold.3
- ___block_literal_global.510
- _objc_msgSend$_shouldReingestAfterUploadErrorWithItem:record:
Functions:
~ -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:] -> -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:error:] : 1544 -> 1680
~ -[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:] : 3468 -> 3356
~ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.1 -> -[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:error:].cold.4 : 176 -> 104
~ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.2 -> -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.1 : 168 -> 176
~ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.3 -> -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.2 : 140 -> 168
~ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.4 -> -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.3 : 104 -> 140
~ -[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:].cold.2 -> -[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:].cold.1 : 112 -> 104
~ -[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:].cold.3 -> -[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:].cold.2 : 104 -> 112
CStrings:
+ "-[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:error:]"
+ "_shouldReingestAfterUploadErrorWithItem:record:error:"
- "-[BRCFSUploader _shouldReingestAfterUploadErrorWithItem:record:]"
- "_shouldReingestAfterUploadErrorWithItem:record:"

```
