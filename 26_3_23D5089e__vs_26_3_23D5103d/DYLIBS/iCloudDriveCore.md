## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.80.5.0.2
-  __TEXT.__text: 0x3141d8
+4257.80.8.0.0
+  __TEXT.__text: 0x314384
   __TEXT.__auth_stubs: 0x1b40
   __TEXT.__objc_methlist: 0x1a44c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7dc38
+  __TEXT.__cstring: 0x7dc6b
   __TEXT.__oslogstring: 0x3c3ae
   __TEXT.__gcc_except_tab: 0x1a634
   __TEXT.__ustring: 0x88

   __DATA_CONST.__objc_selrefs: 0xe7e0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x940
-  __DATA_CONST.__objc_arraydata: 0xe60
+  __DATA_CONST.__objc_arraydata: 0xe78
   __AUTH_CONST.__auth_got: 0xdb0
   __AUTH_CONST.__const: 0x2c00
-  __AUTH_CONST.__cfstring: 0x22c60
+  __AUTH_CONST.__cfstring: 0x22cc0
   __AUTH_CONST.__objc_const: 0x3d560
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x228

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 87D3674C-EDF3-3CFB-96D7-3A407D28E23C
+  UUID: 6B137B6B-3E69-3371-B2DA-1FCA8375C36B
   Functions: 13649
   Symbols:   44440
-  CStrings:  27821
+  CStrings:  27827
 
Symbols:
+ ___26-[BRCAccountSession close]_block_invoke.305
+ ___27-[BRCClientZone _startSync]_block_invoke.193
+ ___27-[BRCClientZone _startSync]_block_invoke.197
+ ___27-[BRCClientZone _startSync]_block_invoke.197.cold.1
+ ___27-[BRCClientZone _startSync]_block_invoke.197.cold.2
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.328
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.328.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.244
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246.cold.2
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246.cold.3
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.246.cold.4
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.337
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.337.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.340
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.362
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.362.cold.1
+ ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.306
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.352
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.353
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.354
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.359
+ ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.131
+ ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.132
+ ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.133
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.437
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.437.cold.1
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.437.cold.2
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.438
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.433
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.433.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.435
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.436
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.375
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.376
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.256
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.256.cold.1
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.256.cold.2
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.261
+ ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.392
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.439
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.440
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.447
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.448
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.456
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.456.cold.1
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.368
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.368.cold.1
+ ___90-[BRCClientZone fetchDirectoryContentsIfNecessary:isUserWaiting:rescheduleApplyScheduler:]_block_invoke.334
+ ___block_literal_global.251
+ ___block_literal_global.273
+ ___block_literal_global.308
+ ___block_literal_global.315
+ ___block_literal_global.327
+ ___block_literal_global.339
+ ___block_literal_global.373
+ ___block_literal_global.953
- ___26-[BRCAccountSession close]_block_invoke.299
- ___27-[BRCClientZone _startSync]_block_invoke.190
- ___27-[BRCClientZone _startSync]_block_invoke.194
- ___27-[BRCClientZone _startSync]_block_invoke.194.cold.1
- ___27-[BRCClientZone _startSync]_block_invoke.194.cold.2
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.322
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.322.cold.1
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.241
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.243
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.243.cold.1
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.243.cold.2
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.243.cold.3
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.243.cold.4
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.251
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.251.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.331
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.331.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.334
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.356
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.356.cold.1
- ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.303
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.349
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.350
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.351
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.356
- ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.128
- ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.129
- ___51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.130
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.434
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.434.cold.1
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.434.cold.2
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.435
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.430
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.430.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.432
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.433
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.369
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.370
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.253
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.253.cold.1
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.253.cold.2
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.255
- ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.386
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.436
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.437
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.444
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.445
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.453
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.453.cold.1
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.362
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.362.cold.1
- ___90-[BRCClientZone fetchDirectoryContentsIfNecessary:isUserWaiting:rescheduleApplyScheduler:]_block_invoke.331
- ___block_literal_global.270
- ___block_literal_global.301
- ___block_literal_global.305
- ___block_literal_global.309
- ___block_literal_global.321
- ___block_literal_global.333
- ___block_literal_global.367
- ___block_literal_global.947
Functions:
~ -[BRCClientZone handleZoneLevelErrorIfNeeded:forItemCreation:] : 1152 -> 1412
~ -[BRCAccountSession captureDBCorruptionInfoWithDescription:error:] : 764 -> 932
CStrings:
+ "DB Reset: %@"
+ "Zone Error Reset: %@"
+ "parent not found"

```
