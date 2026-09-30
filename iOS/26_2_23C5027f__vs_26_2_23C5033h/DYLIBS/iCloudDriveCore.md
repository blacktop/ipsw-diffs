## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.60.1.0.0
-  __TEXT.__text: 0x313a24
+4257.60.5.0.1
+  __TEXT.__text: 0x31433c
   __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0x1a42c
+  __TEXT.__objc_methlist: 0x1a44c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7d9de
-  __TEXT.__oslogstring: 0x3c34c
-  __TEXT.__gcc_except_tab: 0x1a68c
+  __TEXT.__cstring: 0x7dbe4
+  __TEXT.__oslogstring: 0x3c40f
+  __TEXT.__gcc_except_tab: 0x1a6a0
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0xa068
+  __TEXT.__unwind_info: 0xa078
   __TEXT.__objc_classname: 0x2b47
-  __TEXT.__objc_methname: 0x449db
+  __TEXT.__objc_methname: 0x44a7e
   __TEXT.__objc_methtype: 0x90b4
-  __TEXT.__objc_stubs: 0x2f480
+  __TEXT.__objc_stubs: 0x2f500
   __DATA_CONST.__got: 0x1718
   __DATA_CONST.__const: 0x9640
   __DATA_CONST.__objc_classlist: 0xa80
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe7c0
+  __DATA_CONST.__objc_selrefs: 0xe7e0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x940
   __DATA_CONST.__objc_arraydata: 0xe60
   __AUTH_CONST.__auth_got: 0xdb0
   __AUTH_CONST.__const: 0x2c00
-  __AUTH_CONST.__cfstring: 0x22b80
+  __AUTH_CONST.__cfstring: 0x22c60
   __AUTH_CONST.__objc_const: 0x3d590
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x228

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 76ACCBFD-B175-3BE9-B48A-3C6B84FF4B84
-  Functions: 13643
-  Symbols:   44425
-  CStrings:  27800
+  UUID: BE3D4695-F892-3B4F-9F5E-4883958C9709
+  Functions: 13650
+  Symbols:   44445
+  CStrings:  27823
 
Symbols:
+ -[BRCFSImporter _ttrImportingPackageAsRegularFileWithTemplateItem:]
+ -[BRCFSUploader _finishedUploadingItem:record:jobID:stageID:syncContext:hasPerformedServerSideAssetCopy:error:].cold.11
+ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:]
+ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.1
+ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.2
+ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.3
+ -[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:].cold.4
+ ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.277
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.151
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.151.cold.1
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.151.cold.2
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.158
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.163
+ ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.163.cold.1
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.230
+ ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.231
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.100
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.100.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.100.cold.2
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.93
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.93.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.95
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.95.cold.1
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.96
+ ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.96.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.111
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.111.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.111.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.112
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.112.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.112.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.113
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.113.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.113.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.114
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.114.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.114.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.115
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.115.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.115.cold.2
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.116
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.116.cold.1
+ ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.118
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.307
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.313
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.313.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.314
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.311
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.311.cold.1
+ ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.315
+ ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.247
+ ___block_literal_global.261
+ ___block_literal_global.510
+ _objc_msgSend$_isUploadingPackageAsRegularFileForItem:record:error:
+ _objc_msgSend$_ttrImportingPackageAsRegularFileWithTemplateItem:
+ _objc_msgSend$brc_errorImportObjectTypeMismatch
+ _objc_msgSend$brc_errorNotRegularFile
- GCC_except_table138
- ___51-[BRCFSUploader _scheduleQuotaFetchForDefaultOwner]_block_invoke.259
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.136
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.136.cold.1
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.136.cold.2
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.143
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.148
- ___63-[BRCFSImporter _cleanItemBatchAfterMigrationToFPFSIfNecessary]_block_invoke.148.cold.1
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke.212
- ___65-[BRCFSUploader _performServerSideAssetCopyForItem:transferSize:]_block_invoke_2.213
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.78
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.78.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.80
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.80.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.81
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.81.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.85
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.85.cold.1
- ___66-[BRCFSImporter _markNextChildBatchDead:persistedState:batchSize:]_block_invoke.85.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.100.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.101
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.101.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.103
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.96
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.96.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.96.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.97
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.97.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.97.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.98
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.98.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.98.cold.2
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99.cold.1
- ___84-[BRCFSImporter _propagateFieldsToNextChildBatch:persistedState:minRowID:batchSize:]_block_invoke.99.cold.2
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.289
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.295
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.295.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.296
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.293
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.293.cold.1
- ___94-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke_2.297
- ___98-[BRCFSUploader _transferStreamOfSyncContext:didBecomeReadyWithMaxRecordsCount:sizeHint:priority:]_block_invoke.229
- ___block_literal_global.243
- ___block_literal_global.490
CStrings:
+ "-[BRCFSUploader _isUploadingPackageAsRegularFileForItem:record:error:]"
+ "Detected an attempt to import a package as a regular file"
+ "Detected an attempt to upload a package as a regular file"
+ "ICLOUD_DRIVE_EDIT_ON_RO_SHARE"
+ "We are trying to import %@ as a regular file when it is actually a package."
+ "We are trying to upload %@ as a regular file when it is actually a package.\n%@"
+ "[CRIT] UNREACHABLE: Items have the same creation identifier but are of different kinds %@ vs %@%@"
+ "[DEBUG] Attempting to upload a package as a regular file%@"
+ "[DEBUG] File at path is directory: [%s]%@"
+ "[DEBUG] No item exists at the URL's path: %@%@"
+ "[DEBUG] failed to get the fileContent asset%@"
+ "[Upload Error] Detected an attempt to import a package as a regular file"
+ "[Upload Error] Detected an attempt to upload a package as a regular file"
+ "_isUploadingPackageAsRegularFileForItem:record:error:"
+ "_ttrImportingPackageAsRegularFileWithTemplateItem:"
+ "brc_errorImportObjectTypeMismatch"
+ "brc_errorNotRegularFile"
- "[CRIT] UNREACHABLE: Items have the same creation identifier but are of differnt kinds %@ vs %@%@"

```
