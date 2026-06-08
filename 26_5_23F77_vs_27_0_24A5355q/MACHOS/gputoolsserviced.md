## gputoolsserviced

> `/usr/libexec/gputoolsserviced`

```diff

-314.14.0.0.0
-  __TEXT.__text: 0x29278
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0x4bc0
-  __TEXT.__objc_methlist: 0x2ccc
-  __TEXT.__const: 0x4a8
-  __TEXT.__cstring: 0x2736
-  __TEXT.__objc_classname: 0x726
-  __TEXT.__objc_methname: 0x6bc4
-  __TEXT.__objc_methtype: 0x1156
-  __TEXT.__oslogstring: 0xfcc
-  __TEXT.__unwind_info: 0x868
-  __DATA_CONST.__auth_got: 0x690
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xac0
-  __DATA_CONST.__cfstring: 0x2800
-  __DATA_CONST.__objc_classlist: 0x228
-  __DATA_CONST.__objc_protolist: 0xe8
+2027.0.28.0.0
+  __TEXT.__text: 0x33108
+  __TEXT.__auth_stubs: 0xf30
+  __TEXT.__objc_stubs: 0x55c0
+  __TEXT.__objc_methlist: 0x35fc
+  __TEXT.__const: 0x4d0
+  __TEXT.__oslogstring: 0x18ec
+  __TEXT.__cstring: 0x4689
+  __TEXT.__objc_methname: 0x775a
+  __TEXT.__objc_classname: 0x84d
+  __TEXT.__objc_methtype: 0x1404
+  __TEXT.__unwind_info: 0xa20
+  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__cfstring: 0x33c0
+  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_classrefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5ee0
-  __DATA.__objc_selrefs: 0x1ac0
-  __DATA.__objc_ivar: 0x3b8
-  __DATA.__objc_data: 0x1590
-  __DATA.__data: 0xd30
-  __DATA.__bss: 0x2c
+  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__got: 0x268
+  __DATA.__objc_const: 0x6e90
+  __DATA.__objc_selrefs: 0x1db8
+  __DATA.__objc_ivar: 0x440
+  __DATA.__objc_data: 0x19a0
+  __DATA.__data: 0xff8
+  __DATA.__bss: 0xc8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D538729C-EF14-3670-9328-24885F443A8B
-  Functions: 974
-  Symbols:   295
-  CStrings:  2269
+  - /usr/lib/libsqlite3.dylib
+  UUID: D4FC6F61-E4B0-36AC-A651-BF319A206525
+  Functions: 1171
+  Symbols:   329
+  CStrings:  2757
 
Symbols:
+ _NSProtocolFromString
+ __set_user_dir_suffix
+ _confstr
+ _mach_memory_entry_ownership
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _protocol_conformsToProtocol
+ _pthread_mutexattr_destroy
+ _pthread_mutexattr_init
+ _pthread_mutexattr_settype
+ _rename
+ _sqlite3_bind_int64
+ _sqlite3_bind_text
+ _sqlite3_close
+ _sqlite3_column_int
+ _sqlite3_column_int64
+ _sqlite3_column_text
+ _sqlite3_errmsg
+ _sqlite3_errstr
+ _sqlite3_exec
+ _sqlite3_extended_errcode
+ _sqlite3_extended_result_codes
+ _sqlite3_finalize
+ _sqlite3_free
+ _sqlite3_open
+ _sqlite3_prepare_v2
+ _sqlite3_reset
+ _sqlite3_step
+ _strerror
+ _xpc_copy
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "  baseDir:          %@"
+ "  resolvedURL:      %@"
+ "  standardizedBase: %@"
+ "%@: Observer deregistered (total: %lu)"
+ "%@: Observer registered (total: %lu)"
+ "%llu"
+ "%s: %s"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_thread_mutex.c:50"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capabilities/runtime/GTCapabilitiesRuntime.m:313"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capabilities/serialization/GTCapabilitiesSerialization.m:338"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capabilities/serialization/GTCapabilitiesSerialization.m:45"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capabilities/serialization/GTCapabilitiesSerialization.m:610"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capabilities/serialization/GTCapabilitiesSerialization.m:639"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capabilities/serialization/GTCapabilitiesSerialization.m:74"
+ "@\"<GTStashServiceObserver>\""
+ "@\"<GTStashServicePrivate>\""
+ "@\"GTStashDatabase\""
+ "@\"GTStashFileStore\""
+ "@\"GTStashItem\""
+ "@\"GTStashSession\"32@0:8@\"GTStashSessionDescriptor\"16^@24"
+ "@\"GTStashStorageBackend\""
+ "@\"NSArray\"24@0:8^@16"
+ "@\"NSArray\"32@0:8Q16^@24"
+ "@\"NSSet\"16@0:8"
+ "@\"NSURL\"32@0:8@\"GTStashItem\"16^@24"
+ "@24@0:8^@16"
+ "@32@0:8Q16Q24"
+ "@32@0:8Q16^@24"
+ "@40@0:8@16@24^@32"
+ "Assertion failed: %s"
+ "B32@0:8@\"GTStashItem\"16^@24"
+ "B32@0:8Q16Q24"
+ "B40@0:8@\"GTStashItem\"16@\"NSString\"24^@32"
+ "B40@0:8@16@24^@32"
+ "B40@0:8@16Q24^@32"
+ "B40@0:8Q16Q24^@32"
+ "B48@0:8Q16Q24@32^@40"
+ "BEGIN TRANSACTION"
+ "COMMIT"
+ "CREATE TABLE IF NOT EXISTS sessions (  session_id INTEGER PRIMARY KEY,  created_at INTEGER NOT NULL);CREATE TABLE IF NOT EXISTS items (  session_id INTEGER NOT NULL,  item_id INTEGER NOT NULL,  relative_path TEXT NOT NULL,  added_at INTEGER NOT NULL,  retain_count INTEGER DEFAULT 0,  PRIMARY KEY (session_id, item_id),  FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE);CREATE INDEX IF NOT EXISTS idx_items_session_retain_count ON items(session_id, retain_count);"
+ "DELETE FROM items WHERE session_id = ? AND item_id = ?"
+ "Descriptor cannot be nil"
+ "Dump"
+ "ErrorReport"
+ "Failed to begin transaction for removeItems"
+ "Failed to commit removeItems transaction"
+ "Failed to create schema"
+ "Failed to enable foreign keys"
+ "Failed to execute addItem statement"
+ "Failed to execute createSession statement"
+ "Failed to execute releaseItem statement"
+ "Failed to execute removeItem statement"
+ "Failed to execute removeItems statement"
+ "Failed to execute retainItem statement"
+ "Failed to initialize Stash service: %@"
+ "Failed to open database"
+ "Failed to prepare addItem statement"
+ "Failed to prepare allItemPathsInSession statement"
+ "Failed to prepare allRelativePathsInSession statement"
+ "Failed to prepare allSessionIDs statement"
+ "Failed to prepare countNonRetainedItemsInSession statement"
+ "Failed to prepare createSession statement"
+ "Failed to prepare itemExists statement"
+ "Failed to prepare listAllItems statement"
+ "Failed to prepare listItemsInSession statement"
+ "Failed to prepare maximumSessionId statement"
+ "Failed to prepare oldestNonRetainedItemInSession statement"
+ "Failed to prepare relativePathForItem statement"
+ "Failed to prepare releaseItem statement"
+ "Failed to prepare removeItem statement"
+ "Failed to prepare removeItems statement"
+ "Failed to prepare retainItem statement"
+ "GTSecureCoding"
+ "GTStashDatabase"
+ "GTStashEvent"
+ "GTStashFileStore"
+ "GTStashItem"
+ "GTStashObserverRegistration"
+ "GTStashReplyStream"
+ "GTStashService"
+ "GTStashServiceImpl"
+ "GTStashServiceObserver"
+ "GTStashServiceObserverXPCDispatcher"
+ "GTStashServicePrivate"
+ "GTStashServiceXPCDispatcher"
+ "GTStashServiceXPCProxy"
+ "GTStashSession"
+ "GTStashSessionDescriptor"
+ "GTStashSessionInternal"
+ "GTStashStorageBackend"
+ "INSERT INTO items (session_id, item_id, relative_path, added_at, retain_count) VALUES (?, ?, ?, ?, 0)"
+ "INSERT INTO sessions (session_id, created_at) VALUES (?, ?)"
+ "Item cannot be nil"
+ "Item not found"
+ "Malformed message: unknown selector"
+ "MarketingName"
+ "MemWatch"
+ "Object serialization failed: %@"
+ "PRAGMA foreign_keys = ON;"
+ "Path '%@' must resolve to somewhere within the session directory '%@'"
+ "Path cannot be nil"
+ "Q24@0:8@\"<GTStashServiceObserver>\"16"
+ "Q24@0:8Q16"
+ "Q24@0:8^@16"
+ "Q32@0:8@\"<GTStashServiceObserver>\"16Q24"
+ "Q32@0:8@16Q24"
+ "Q40@0:8Q16Q24^@32"
+ "ROLLBACK"
+ "Remote protocol %@ does not conform to %@"
+ "SELECT 1 FROM items WHERE session_id = ? AND item_id = ?"
+ "SELECT COUNT(*) FROM items WHERE session_id = ? AND retain_count = 0"
+ "SELECT DISTINCT session_id FROM sessions"
+ "SELECT MAX(session_id) FROM sessions"
+ "SELECT item_id, relative_path FROM items WHERE session_id = ?"
+ "SELECT relative_path FROM items WHERE session_id = ?"
+ "SELECT relative_path FROM items WHERE session_id = ? AND item_id = ?"
+ "SELECT session_id, item_id FROM items"
+ "SELECT session_id, item_id FROM items WHERE session_id = ?"
+ "SELECT session_id, item_id FROM items WHERE session_id = ? AND retain_count = 0 ORDER BY ROWID ASC LIMIT 1"
+ "ServiceProvider"
+ "Stash crash recovery complete: %lu orphaned files deleted, %lu invalid DB records removed, %lu empty directories removed"
+ "Stash crash recovery starting..."
+ "Stash database: %s (SQLite code %d, extended: %d - %s)"
+ "Stash database: Failed to create base directory: %@"
+ "Stash database: addItem called with nil relativePath"
+ "Stash file store: Invalid relative path (escapes base directory): %@"
+ "Stash recovery: Deleting orphaned file: session=%llu path=%@"
+ "Stash recovery: Deleting orphaned session directory: %@"
+ "Stash recovery: Failed to batch remove invalid DB records for session=%llu: %@"
+ "Stash recovery: Failed to delete orphaned file session=%llu path=%@: %@"
+ "Stash recovery: Failed to delete orphaned session directory %@: %@"
+ "Stash recovery: Failed to remove empty session directory %@: %@"
+ "Stash recovery: Found invalid DB record (file missing): session=%llu item=%llu path=%@"
+ "Stash: Added item %llu (%@) to session %llu"
+ "Stash: Database error detected, deleting and recreating"
+ "Stash: Failed to recreate staging directory: %@"
+ "Stash: Failed to remove base directory during recovery: %@"
+ "Stash: Failed to remove item on disk after deleting from db %@"
+ "Stash: Item %llu doesn't exist in session %llu"
+ "Stash: Observer deregistered (total: %lu)"
+ "Stash: Observer registered (total: %lu)"
+ "Stash: Released item %llu in session %llu (retain count: %lu)"
+ "Stash: Removed item %llu from session %llu"
+ "Stash: Rename failed, check for staging and items directories on different filesystems!"
+ "Stash: Retained item %llu in session %llu (retain count: %lu)"
+ "Stash: Unknown sessionId %llu"
+ "Stash: addItem called with nil item"
+ "Stash: addItem called with nil path"
+ "Stash: registerObserver called with nil observer"
+ "Stash: releaseItem called with nil item"
+ "Stash: retainItem called with nil item"
+ "Stash: startSession called with nil descriptor"
+ "Stash: urlForItem called with nil item"
+ "T@\"<GTStashServiceObserver>\",&,N,V_observer"
+ "T@\"GTStashDatabase\",R,N,V_database"
+ "T@\"GTStashFileStore\",R,N,V_fileStore"
+ "T@\"GTStashItem\",&,V_item"
+ "T@\"NSString\",C,N,V_MarketingName"
+ "T@\"NSURL\",&,N,V_sessionDirectory"
+ "T@\"NSURL\",&,V_sessionDirectory"
+ "TI,N,V_memWatchMode"
+ "TQ,N,V_countMetalFXHistory"
+ "TQ,N,V_sessionId"
+ "TQ,N,V_windowSize"
+ "TQ,V_itemId"
+ "TQ,V_sessionId"
+ "TQ,V_windowSize"
+ "Tq,V_eventType"
+ "UPDATE items SET retain_count = MAX(retain_count - 1, 0) WHERE session_id = ? AND item_id = ? RETURNING retain_count"
+ "UPDATE items SET retain_count = retain_count + 1 WHERE session_id = ? AND item_id = ? RETURNING retain_count"
+ "URLByAppendingPathComponent:"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLByStandardizingPath"
+ "Unarchiver failure for %s: %@"
+ "Unknown error"
+ "^{sqlite3=}"
+ "_GTItemList"
+ "_GTStashDescriptor"
+ "_GTStashEvent"
+ "_GTStashItem"
+ "_GTStashObserverId"
+ "_GTStashSession"
+ "_GTStashSessionId"
+ "_MarketingName"
+ "_baseDirectory"
+ "_countMetalFXHistory"
+ "_database"
+ "_databasePath"
+ "_db"
+ "_deleteItem:fromSession:"
+ "_deleteItemAndNotify:fromSession:"
+ "_enforceWindowSizeForSession:"
+ "_eventType"
+ "_fileStore"
+ "_gtXPCConnection"
+ "_item"
+ "_itemId"
+ "_itemsRoot"
+ "_memWatchMode"
+ "_nextSessionId"
+ "_notifyObservers:"
+ "_queue"
+ "_sandboxExtension"
+ "_serviceImpl"
+ "_sessionDirectory"
+ "_sessionId"
+ "_stagingRoot"
+ "_storage"
+ "_url"
+ "_windowSize"
+ "addItem:path:error:"
+ "addItem:toSession:relativePath:error:"
+ "addItem_path_error_:replyConnection:"
+ "allItemPathsInSession:"
+ "allItemSessionDirectories"
+ "allRelativePathsInItemsDirectory:"
+ "allRelativePathsInSession:"
+ "allSessionIds"
+ "cleanupStagingDirectories:"
+ "clearStash:"
+ "clearStash_:replyConnection:"
+ "com.apple.gputools.GPUToolsDebugService"
+ "com.apple.gputools.GPUToolsMLReplayService"
+ "com.apple.gputools.stash"
+ "com.apple.gputoolsserviced"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "countMetalFXHistory"
+ "countNonRetainedItemsInSession:"
+ "createSchemaWithError:"
+ "createSessionWithError:"
+ "createStagingDirectoryForSession:error:"
+ "database"
+ "dealloc"
+ "deleteAllDataWithError:"
+ "eventType"
+ "failed to initialize temporary directory: %{darwin.errno}d"
+ "fileStore"
+ "initWithBaseDirectory:error:"
+ "initWithConnection:serviceInfo:"
+ "initWithName:"
+ "initWithService:properties:queue:"
+ "item"
+ "itemExists:inSession:"
+ "itemId"
+ "items"
+ "itemsDirectoryForSession:"
+ "launchDebugService:error:"
+ "launchDebugService_error_:replyConnection:"
+ "launchMLReplayService:error:"
+ "launchMLReplayService_error_:replyConnection:"
+ "listAllItems"
+ "listItemsInSession:"
+ "listItemsWithError:"
+ "listItemsWithError_:replyConnection:"
+ "listItemsWithSessionId:error:"
+ "listItemsWithSessionId_error_:replyConnection:"
+ "longLongValue"
+ "marketingName"
+ "maximumSessionId"
+ "memWatchMode"
+ "moveItemFromStaging:inSession:error:"
+ "notifyItem serialization failed: %@"
+ "notifyItem:"
+ "notifyItem_:replyConnection:"
+ "observer"
+ "oldestNonRetainedItemInSession:"
+ "performCrashRecovery"
+ "registerObserver:forSessionId:"
+ "registerObserver_forSessionId_:replyConnection:"
+ "relativePath cannot be nil"
+ "relativePathForItem:inSession:"
+ "releaseItem:error:"
+ "releaseItem:inSession:error:"
+ "releaseItem_error_:replyConnection:"
+ "removeItem:fromSession:error:"
+ "removeItems:fromSession:error:"
+ "retainItem:error:"
+ "retainItem:inSession:error:"
+ "retainItem_error_:replyConnection:"
+ "service"
+ "serviceInfo"
+ "sessionDirectory"
+ "sessionId"
+ "set"
+ "setByAddingObjectsFromArray:"
+ "setCountMetalFXHistory:"
+ "setEventType:"
+ "setItem:"
+ "setItemId:"
+ "setMarketingName:"
+ "setMemWatchMode:"
+ "setObserver:"
+ "setSessionDirectory:"
+ "setSessionId:"
+ "setWindowSize:"
+ "setWithObject:"
+ "shouldDeleteAndRecreateForError:"
+ "staging"
+ "stagingDirectoryForSession:"
+ "startSessionWithDescriptor:error:"
+ "startSessionWithDescriptor_error_:replyConnection:"
+ "stash"
+ "stash.db"
+ "stopSessionWithSessionId:error:"
+ "stopSessionWithSessionId_error_:replyConnection:"
+ "timeIntervalSince1970"
+ "toPublicSession"
+ "unarchiverClasses"
+ "urlForItem:error:"
+ "urlForItem_error_:replyConnection:"
+ "v24@0:8@\"GTStashEvent\"16"
+ "v32@0:8Q16Q24"
+ "validateAndResolveRelativePath:inBaseDirectory:error:"
+ "warning: failed to create memory entry error 0x%x (%s)\n"
+ "warning: failed to map memory error 0x%x (%s)\n"
+ "warning: failed to mark memory(GRAPHICS) error 0x%x (%s)"
+ "warning: failed to mark memory(GRAPHICS) error 0x%x (%s)\n"
+ "windowSize"
- "GTDeviceCapabilitiesXPCProxy"
- "unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:"

```
