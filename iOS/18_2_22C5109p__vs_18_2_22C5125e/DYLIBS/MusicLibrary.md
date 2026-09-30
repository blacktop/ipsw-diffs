## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.300.14.0.0
-  __TEXT.__text: 0x27aefc
-  __TEXT.__auth_stubs: 0x1fa0
-  __TEXT.__objc_methlist: 0xd81c
+4024.300.23.0.0
+  __TEXT.__text: 0x27b5ac
+  __TEXT.__auth_stubs: 0x1fb0
+  __TEXT.__objc_methlist: 0xd844
   __TEXT.__const: 0x26080
-  __TEXT.__gcc_except_tab: 0x13898
-  __TEXT.__cstring: 0x66727
-  __TEXT.__oslogstring: 0x1a168
+  __TEXT.__gcc_except_tab: 0x13804
+  __TEXT.__cstring: 0x6681f
+  __TEXT.__oslogstring: 0x1a2c2
   __TEXT.__ustring: 0x210
   __TEXT.__dlopen_cstrs: 0x193
-  __TEXT.__unwind_info: 0x7188
+  __TEXT.__unwind_info: 0x7180
   __TEXT.__eh_frame: 0x1ca0
   __TEXT.__objc_classname: 0x1919
-  __TEXT.__objc_methname: 0x1df24
-  __TEXT.__objc_methtype: 0x5276
-  __TEXT.__objc_stubs: 0x14740
+  __TEXT.__objc_methname: 0x1e043
+  __TEXT.__objc_methtype: 0x5285
+  __TEXT.__objc_stubs: 0x147e0
   __DATA_CONST.__got: 0xb18
-  __DATA_CONST.__const: 0x90d0
+  __DATA_CONST.__const: 0x9100
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a18
+  __DATA_CONST.__objc_selrefs: 0x6a40
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0x1098
-  __AUTH_CONST.__auth_got: 0xfe8
+  __AUTH_CONST.__auth_got: 0xff0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x12560
-  __AUTH_CONST.__cfstring: 0x24d80
+  __AUTH_CONST.__cfstring: 0x24e20
   __AUTH_CONST.__objc_const: 0x15830
   __AUTH_CONST.__objc_arrayobj: 0x20b8
-  __AUTH_CONST.__objc_intobj: 0x1b60
+  __AUTH_CONST.__objc_intobj: 0x1b30
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xe6c
   __DATA.__data: 0x1960
-  __DATA.__bss: 0xb20
+  __DATA.__bss: 0xb10
   __DATA.__common: 0xa58
   __DATA_DIRTY.__objc_data: 0x4470
   __DATA_DIRTY.__data: 0x198

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8075
-  Symbols:   9800
-  CStrings:  12389
+  Functions: 8079
+  Symbols:   9806
+  CStrings:  12404
 
Symbols:
+ _MLDatabaseOperationAttributeSpotlightIndexAppEntityAssociatorKey
+ _MSVCopySystemBuildVersion
CStrings:
+ "<MusicLibrary: %!p(MISSING)> path=%!@(MISSING) _sharedLibraryDatabasePath=%!@(MISSING) computedSharedLibraryDatabasePath=%!@(MISSING) _connectionPool=%!p(MISSING) _autoUpdatingSharedLibrary=%!d(MISSING), _isHomeSharingLibrary=%!d(MISSING)"
+ "Connection pool %!{(MISSING)public}@ isClosed=%!{(MISSING)BOOL}u, readerSubPoolHasBusyConnections=%!{(MISSING)BOOL}u, writerSubPoolHasBusyConnections=%!{(MISSING)BOOL}u."
+ "Counts in item table(s) are inconsistent: item(%!l(MISSING)li), item_extra(%!l(MISSING)li), item_stats(%!l(MISSING)li), item_store(%!l(MISSING)li), item_video(%!l(MISSING)li) "
+ "ML3DatabaseKeyMaintenanceTaskOperationSanitizeClientBuildVersion"
+ "MLDatabaseOperationAttributeSpotlightIndexAppEntityAssociatorKey"
+ "MusicAppEntitiesDonatedToSpotlight"
+ "Must have a resource mananger or valid file path to create the library"
+ "SELECT COUNT() FROM item_stats"
+ "SELECT COUNT() FROM item_store"
+ "SELECT COUNT() FROM item_video"
+ "Sanity check recoverable condition for inconsistent counts: item(%!l(MISSING)li), item_extra(%!l(MISSING)li), item_stats(%!l(MISSING)li), item_store(%!l(MISSING)li), item_video(%!l(MISSING)li) "
+ "Sanity check recoverable condition: %!l(MISSING)li rows in item and %!l(MISSING)li rows in lyrics"
+ "Sanity check recoverable condition: Sort map is inconsistent"
+ "Sanity check recoverable condition: Sort map was missing the following names %!{(MISSING)public}@"
+ "Sanity check: Deleted garbage tracks %!{(MISSING)public}@"
+ "Sanity check: Incrementing revision for removed tracks: %!{(MISSING)public}@"
+ "Sanity check: flagging cloud library for full refresh after next update"
+ "Sanity check: flagging purchase history for next update to include all tokens"
+ "Sanity check: resetting sync anchors"
+ "Sort map nextOrder %!l(MISSING)li, nameOrder %!l(MISSING)li"
+ "Sort map nextSection %!l(MISSING)li, nameSection %!l(MISSING)li"
+ "TB,N,GisAutoUpdatingSharedLibrary,V_autoUpdatingSharedLibrary"
+ "[MaintenanceTasksOperation] Clearing sanitizeClientBuildVersion as it's invalid"
+ "[MaintenanceTasksOperation] Item tables are not in sync - will perform a client initiated reset lastClientInitiatedResetClientBuildVersion=%!{(MISSING)public}@, currentDeviceBuildVersion=%!{(MISSING)public}@"
+ "_autoUpdatingSharedLibrary"
+ "_onGlobalQueue_shareableMusicLibraryWithResourcesManager:libraryFilePath:"
+ "associateAppEntityForEntityOfType:persistentID:library:properties:withSearchableItemWithAttributeSet:"
+ "autoUpdatingSharedLibrary"
+ "hasBusyConnections"
+ "isAutoUpdatingSharedLibrary"
+ "sanitizeDatabaseContentsUsingConnection:removeOrphanedAssets:"
+ "sanitizeSortMapContentsUsingConnection:didSortMapEntries:"
+ "setAutoUpdatingSharedLibrary:"
+ "v32@0:8@16^B24"
+ "validateItemTablesEntriesUsingConnection:"
- "<MusicLibrary: %!p(MISSING)> path=%!@(MISSING) _sharedLibraryDatabasePath=%!@(MISSING) computedSharedLibraryDatabasePath=%!@(MISSING) _connectionPool=%!p(MISSING) _usingSharedLibraryPath=%!d(MISSING), _isHomeSharingLibrary=%!d(MISSING)"
- "Cannot create library with no resource mananger and invalid autoUpdatingLibraryPath"
- "Connection pool %!{(MISSING)public}@ isClosed=%!{(MISSING)BOOL}u, readerSubPoolClosed=%!{(MISSING)BOOL}u, readerSubPoolClosed=%!{(MISSING)BOOL}u."
- "TB,N,GisUsingSharedLibraryPath,V_usingSharedLibraryPath"
- "[Migration] Sanity check recoverable condition: %!l(MISSING)li items in item and %!l(MISSING)li items in item_extra"
- "[Migration] Sanity check recoverable condition: %!l(MISSING)li rows in item and %!l(MISSING)li rows in lyrics"
- "[Migration] Sanity check recoverable condition: Sort map is inconsistent"
- "[Migration] Sanity check recoverable condition: Sort map was missing the following names %!{(MISSING)public}@"
- "[Migration] Sanity check: Deleted garbage tracks %!{(MISSING)public}@"
- "[Migration] Sanity check: Incrementing revision for removed tracks: %!{(MISSING)public}@"
- "[Migration] Sanity check: flagging cloud library for full refresh after next update"
- "[Migration] Sanity check: flagging purchase history for next update to include all tokens"
- "[Migration] Sanity check: resetting sync anchors"
- "[Migration] Sort map nextOrder %!l(MISSING)li, nameOrder %!l(MISSING)li"
- "[Migration] Sort map nextSection %!l(MISSING)li, nameSection %!l(MISSING)li"
- "_onGlobalQueue_shareableMusicLibraryWithResourcesManager:autoUpdatingSharedLibraryPath:"
- "_usingSharedLibraryPath"
- "isUsingSharedLibraryPath"
- "setUsingSharedLibraryPath:"
- "usingSharedLibraryPath"

```
