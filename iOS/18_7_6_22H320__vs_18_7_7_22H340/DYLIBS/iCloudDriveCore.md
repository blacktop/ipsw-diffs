## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3437.140.4.0.0
-  __TEXT.__text: 0x2f1cb0
+3437.140.4.700.1
+  __TEXT.__text: 0x2f1dd4
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x1909c
+  __TEXT.__objc_methlist: 0x19094
   __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0x7a45d
-  __TEXT.__oslogstring: 0x3aec5
+  __TEXT.__cstring: 0x7a454
+  __TEXT.__oslogstring: 0x3ae8d
   __TEXT.__gcc_except_tab: 0x19ab0
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x99a0
-  __TEXT.__objc_classname: 0x269f
-  __TEXT.__objc_methname: 0x411f9
+  __TEXT.__unwind_info: 0x99b8
+  __TEXT.__objc_classname: 0x2698
+  __TEXT.__objc_methname: 0x411ec
   __TEXT.__objc_methtype: 0x882e
-  __TEXT.__objc_stubs: 0x2cae0
-  __DATA_CONST.__got: 0x16f8
+  __TEXT.__objc_stubs: 0x2cb20
+  __DATA_CONST.__got: 0x1708
   __DATA_CONST.__const: 0x8e38
   __DATA_CONST.__objc_classlist: 0x988
-  __DATA_CONST.__objc_catlist: 0xe0
+  __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdca8
+  __DATA_CONST.__objc_selrefs: 0xdca0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x880
   __DATA_CONST.__objc_arraydata: 0xe40
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__const: 0x2958
   __AUTH_CONST.__cfstring: 0x22040
-  __AUTH_CONST.__objc_const: 0x3b2b8
+  __AUTH_CONST.__objc_const: 0x3b278
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F97DC4C9-4E7D-3785-8717-A34D3E1205E2
-  Functions: 13123
+  UUID: 851B7430-0F48-3CE7-BDCD-BFC35AF23D6E
+  Functions: 13122
   Symbols:   42906
-  CStrings:  26903
+  CStrings:  26900
 
Symbols:
+ -[BRCClientZone _getPrivateClientZone]
+ -[BRCClientZone postContainerStatusChangeNotificationForKey:value:]
+ -[BRCClientZone postContainerStatusChangeNotificationForKey:value:].cold.1
+ GCC_except_table191
+ GCC_except_table210
+ GCC_except_table240
+ GCC_except_table246
+ GCC_except_table260
+ GCC_except_table269
+ GCC_except_table278
+ GCC_except_table356
+ GCC_except_table382
+ GCC_except_table413
+ _BRContainerDidChangeStatusDistributedNotification
+ _BRContainerIDKey
+ ___27-[BRCClientZone _startSync]_block_invoke.169
+ ___27-[BRCClientZone _startSync]_block_invoke.173
+ ___27-[BRCClientZone _startSync]_block_invoke.173.cold.1
+ ___27-[BRCClientZone _startSync]_block_invoke.173.cold.2
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.220
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.222
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.222.cold.1
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.222.cold.2
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.222.cold.3
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.222.cold.4
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.230
+ ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.230.cold.1
+ ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.217
+ ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.282
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.330
+ ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.335
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.413.cold.1
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.413.cold.2
+ ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.414
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.409
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.409.cold.1
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.411
+ ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.412
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.232
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.232.cold.1
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.232.cold.2
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.234
+ ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.237
+ ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.416
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.424
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.432
+ ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.432.cold.1
+ ___90-[BRCClientZone fetchDirectoryContentsIfNecessary:isUserWaiting:rescheduleApplyScheduler:]_block_invoke.311
+ ___block_literal_global.227
+ ___block_literal_global.284
+ _objc_msgSend$_getPrivateClientZone
+ _objc_msgSend$postContainerStatusChangeNotificationForKey:value:
+ _objc_msgSend$setZoneRowID:
- -[BRContainer(Daemon) currentStatus]
- -[BRContainer(Daemon) currentStatus].cold.1
- -[BRContainer(Daemon) lastServerUpdate]
- -[BRContainer(Daemon) lastServerUpdate].cold.1
- GCC_except_table128
- GCC_except_table137
- GCC_except_table189
- GCC_except_table192
- GCC_except_table208
- GCC_except_table238
- GCC_except_table250
- GCC_except_table259
- GCC_except_table263
- GCC_except_table276
- GCC_except_table313
- GCC_except_table319
- GCC_except_table353
- GCC_except_table379
- GCC_except_table408
- GCC_except_table410
- __OBJC_$_CATEGORY_BRContainer_$_Daemon
- __OBJC_$_CATEGORY_INSTANCE_METHODS_BRContainer_$_Daemon
- ___27-[BRCClientZone _startSync]_block_invoke.168
- ___27-[BRCClientZone _startSync]_block_invoke.172
- ___27-[BRCClientZone _startSync]_block_invoke.172.cold.1
- ___27-[BRCClientZone _startSync]_block_invoke.172.cold.2
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.219
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.221
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.221.cold.1
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.221.cold.2
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.221.cold.3
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.221.cold.4
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.229
- ___39-[BRCClientZone notifyClient:whenIdle:]_block_invoke.229.cold.1
- ___39-[BRCServerZone collectTombstoneRanks:]_block_invoke.218
- ___47-[BRCClientZone _crossZoneMoveDocumentsToZone:]_block_invoke.281
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.327
- ___49-[BRCClientZone fetchRecentAndFavoriteDocuments:]_block_invoke.334
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.412
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.412.cold.1
- ___57-[BRCClientZone performBlock:whenItemWithIDIsDownloaded:]_block_invoke.412.cold.2
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.408
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.408.cold.1
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke.410
- ___59-[BRCClientZone performBlock:whenItemWithRecordIDIsOnDisk:]_block_invoke_2.411
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.231
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.231.cold.1
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.231.cold.2
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.233
- ___61-[BRCClientZone syncDownOperation:didFinishWithError:status:]_block_invoke.236
- ___68-[BRCClientZone performBlock:whenSyncDownCompletesLookingForItemID:]_block_invoke.414
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.422
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.431
- ___71-[BRCClientZone performBlock:whenLocatingCompletesForItemWithRecordID:]_block_invoke.431.cold.1
- ___90-[BRCClientZone fetchDirectoryContentsIfNecessary:isUserWaiting:rescheduleApplyScheduler:]_block_invoke.310
- ___block_literal_global.226
- ___block_literal_global.248
- ___block_literal_global.283
- _objc_msgSend$postContainerStatusChangeNotificationWithID:key:value:
CStrings:
+ "-[BRCClientZone postContainerStatusChangeNotificationForKey:value:]"
+ "[CRIT] Assertion failed: key != nil && value != nil%@"
+ "[DEBUG] broadcasting to framework clients zone %@ change %@=%@%@"
+ "_getPrivateClientZone"
+ "postContainerStatusChangeNotificationForKey:value:"
- "-[BRContainer(Daemon) currentStatus]"
- "-[BRContainer(Daemon) lastServerUpdate]"
- "Daemon"
- "[CRIT] UNREACHABLE: -[BRContainer currentStatus] shouldn't be called by the daemon.%@"
- "[CRIT] UNREACHABLE: -[BRContainer lastServerUpdate] shouldn't be called by the daemon.%@"
- "currentStatus"
- "lastServerUpdate"
- "postContainerStatusChangeNotificationWithID:key:value:"

```
