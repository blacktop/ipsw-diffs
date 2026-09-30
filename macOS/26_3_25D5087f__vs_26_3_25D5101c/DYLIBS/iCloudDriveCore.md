## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/iCloudDriveCore`

```diff

-4257.80.5.0.2
-  __TEXT.__text: 0x36ca60
+4257.80.8.0.0
+  __TEXT.__text: 0x36cc4c
   __TEXT.__auth_stubs: 0x1a00
   __TEXT.__objc_methlist: 0x1a5c4
   __TEXT.__const: 0x4f8
-  __TEXT.__cstring: 0x7e373
+  __TEXT.__cstring: 0x7e3a6
   __TEXT.__oslogstring: 0x3d323
   __TEXT.__gcc_except_tab: 0x1ac24
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0xa248
+  __TEXT.__unwind_info: 0xa258
   __TEXT.__objc_classname: 0x2b21
   __TEXT.__objc_methname: 0x45005
   __TEXT.__objc_methtype: 0x91f1

   __DATA_CONST.__objc_selrefs: 0xe940
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x938
-  __DATA_CONST.__objc_arraydata: 0xf80
+  __DATA_CONST.__objc_arraydata: 0xf98
   __AUTH_CONST.__auth_got: 0xd10
   __AUTH_CONST.__const: 0xb4c0
-  __AUTH_CONST.__cfstring: 0x231c0
+  __AUTH_CONST.__cfstring: 0x23220
   __AUTH_CONST.__objc_const: 0x3d3f8
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x2b8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1A6A7F66-11C5-3ED9-B954-D012AF18F4DF
+  UUID: 766B929A-7750-37C8-9F6D-128E227DA476
   Functions: 13921
   Symbols:   30215
-  CStrings:  28040
+  CStrings:  28046
 
Symbols:
+ __26-[BRCAccountSession close]_block_invoke.385
+ __27-[BRCClientZone _startSync]_block_invoke.199
+ __27-[BRCClientZone _startSync]_block_invoke.203
+ __27-[BRCClientZone _startSync]_block_invoke.203.cold.1
+ __27-[BRCClientZone _startSync]_block_invoke.203.cold.2
+ __37-[BRCAccountSession destroyLocalData]_block_invoke.420
+ __37-[BRCAccountSession destroyLocalData]_block_invoke.420.cold.1
+ __39-[BRCClientZone addSyncDownDependency:]_block_invoke.194
+ __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.253
+ __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.257
+ __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.257.cold.1
+ __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.257.cold.2
+ __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.257.cold.3
+ __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.257.cold.4
+ __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.265
+ __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.265.cold.1
+ __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.424
+ __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.424.cold.1
+ __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.424.cold.2
+ __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.424.cold.3
+ __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.424.cold.4
+ __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.431
+ __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.431.cold.1
+ __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.434
+ __45-[BRCAccountSession destroySharedClientZone:]_block_invoke.463
+ __45-[BRCAccountSession destroySharedClientZone:]_block_invoke.463.cold.1
+ __47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.325
+ __49-[BRCAccountSession _cloudDocsAppsListDidChange:]_block_invoke.491
+ __49-[BRCAccountSession _cloudDocsAppsListDidChange:]_block_invoke.493
+ __49-[BRCAccountSession _cloudDocsAppsListDidChange:]_block_invoke_2.494
+ __49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.377
+ __49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.378
+ __49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.379
+ __49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.384
+ __51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.133
+ __51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.134
+ __51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.135
+ __57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.473
+ __57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.473.cold.1
+ __57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.473.cold.2
+ __57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.474
+ __58-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:]_block_invoke.474
+ __59-[BRCClientZone _dumpItemsToContext:includeAllItems:error:]_block_invoke.571
+ __59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.461
+ __59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.461.cold.1
+ __59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.465
+ __59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.466
+ __60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.481
+ __60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.482
+ __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.269
+ __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.269.cold.1
+ __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.269.cold.2
+ __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.273
+ __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.277
+ __66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.510
+ __68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.475
+ __68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.480
+ __70-[BRCClientZone dumpActivityToContext:includeExpensiveActivity:error:]_block_invoke.620
+ __70-[BRCClientZone dumpActivityToContext:includeExpensiveActivity:error:]_block_invoke.627
+ __70-[BRCClientZone dumpActivityToContext:includeExpensiveActivity:error:]_block_invoke.634
+ __71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.487
+ __71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.489
+ __71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.501
+ __71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.501.cold.1
+ __84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.469
+ __84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.469.cold.1
+ __90-[BRCClientZone fetchDirectoryContentsIfNecessary:isUserWaiting:rescheduleApplyScheduler:]_block_invoke.355
+ __block_literal_global.1077
+ __block_literal_global.262
+ __block_literal_global.292
+ __block_literal_global.327
+ __block_literal_global.387
+ __block_literal_global.395
+ __block_literal_global.419
+ __block_literal_global.433
+ __block_literal_global.479
- __26-[BRCAccountSession close]_block_invoke.379
- __27-[BRCClientZone _startSync]_block_invoke.196
- __27-[BRCClientZone _startSync]_block_invoke.200
- __27-[BRCClientZone _startSync]_block_invoke.200.cold.1
- __27-[BRCClientZone _startSync]_block_invoke.200.cold.2
- __37-[BRCAccountSession destroyLocalData]_block_invoke.414
- __37-[BRCAccountSession destroyLocalData]_block_invoke.414.cold.1
- __39-[BRCClientZone addSyncDownDependency:]_block_invoke.191
- __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.250
- __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254
- __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254.cold.1
- __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254.cold.2
- __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254.cold.3
- __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.254.cold.4
- __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.262
- __39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.262.cold.1
- __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.418
- __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.418.cold.1
- __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.418.cold.2
- __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.418.cold.3
- __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.418.cold.4
- __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.425
- __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.425.cold.1
- __45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.428
- __45-[BRCAccountSession destroySharedClientZone:]_block_invoke.457
- __45-[BRCAccountSession destroySharedClientZone:]_block_invoke.457.cold.1
- __47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.322
- __49-[BRCAccountSession _cloudDocsAppsListDidChange:]_block_invoke.485
- __49-[BRCAccountSession _cloudDocsAppsListDidChange:]_block_invoke.487
- __49-[BRCAccountSession _cloudDocsAppsListDidChange:]_block_invoke_2.488
- __49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.374
- __49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.375
- __49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.376
- __49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.381
- __51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.130
- __51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.131
- __51-[BRCClientZone handleSaltingErrorIfNeeded:record:]_block_invoke.132
- __57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.470
- __57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.470.cold.1
- __57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.470.cold.2
- __57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.471
- __58-[BRCAccountSession getOrCreateSharedZones:shareAcceptOp:]_block_invoke.468
- __59-[BRCClientZone _dumpItemsToContext:includeAllItems:error:]_block_invoke.568
- __59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.458
- __59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.458.cold.1
- __59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.462
- __59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.463
- __60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.475
- __60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.476
- __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.266
- __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.266.cold.1
- __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.266.cold.2
- __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.270
- __61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.274
- __66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.504
- __68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.472
- __68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.477
- __70-[BRCClientZone dumpActivityToContext:includeExpensiveActivity:error:]_block_invoke.617
- __70-[BRCClientZone dumpActivityToContext:includeExpensiveActivity:error:]_block_invoke.624
- __70-[BRCClientZone dumpActivityToContext:includeExpensiveActivity:error:]_block_invoke.631
- __71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.484
- __71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.486
- __71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.498
- __71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.498.cold.1
- __84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.463
- __84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.463.cold.1
- __90-[BRCClientZone fetchDirectoryContentsIfNecessary:isUserWaiting:rescheduleApplyScheduler:]_block_invoke.352
- __block_literal_global.1071
- __block_literal_global.259
- __block_literal_global.289
- __block_literal_global.381
- __block_literal_global.427
- __block_literal_global.473
Functions:
~ -[BRCClientZone handleZoneLevelErrorIfNeeded:forItemCreation:] : 1284 -> 1592
~ -[BRCAccountSession captureDBCorruptionInfoWithDescription:error:] : 872 -> 1056
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/account/BRCAccountSession.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/account/BRCAccountsManager.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/backup/BRCBackupSession.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/containers/BRCClientZone.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/containers/BRCServerZone.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/daemon/BRCDaemon.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCClientDatabaseFacade.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCClientState.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseManager.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseSchema.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCServerPersistedState.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/foundation/BRCFairScheduler.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/foundation/BRCPQLConnection.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/items/BRCItemID.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/notifs/BRCAccountHandler.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
+ "/AppleInternal/Library/BuildRoots/4~CE80ugA6mVMqAm8vFPOl0pCNDhAxS0NXlXZx_Wo/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/sync/transfers/BRCTransferStream.m"
+ "DB Reset: %@"
+ "Zone Error Reset: %@"
+ "parent not found"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/account/BRCAccountSession.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/account/BRCAccountsManager.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/backup/BRCBackupSession.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/containers/BRCClientZone.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/containers/BRCServerZone.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/daemon/BRCDaemon.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCClientDatabaseFacade.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCClientState.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseManager.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseSchema.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/database/BRCServerPersistedState.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/foundation/BRCFairScheduler.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/foundation/BRCPQLConnection.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/items/BRCItemID.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/notifs/BRCAccountHandler.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
- "/AppleInternal/Library/BuildRoots/4~CDzeugDssyxAUdH8t32XbRdN1Wi-lRnV-xsDotM/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/core/shared/sync/transfers/BRCTransferStream.m"

```
