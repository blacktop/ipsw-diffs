## APFoundation

> `/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation`

```diff

-485.0.0.0.0
-  __TEXT.__text: 0xc4bb8
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x24d0
-  __TEXT.__const: 0x4a10
-  __TEXT.__cstring: 0x2369
-  __TEXT.__oslogstring: 0x3583
-  __TEXT.__gcc_except_tab: 0x52c
+500.2.0.0.0
+  __TEXT.__text: 0xc7b58
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_methlist: 0x2920
+  __TEXT.__const: 0x4a20
+  __TEXT.__cstring: 0x25f9
+  __TEXT.__oslogstring: 0x34e6
+  __TEXT.__gcc_except_tab: 0x554
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x23
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x948
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x58a
-  __TEXT.__objc_methname: 0x5bf0
-  __TEXT.__objc_methtype: 0x10f9
-  __TEXT.__objc_stubs: 0x4ce0
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0xb10
-  __DATA_CONST.__objc_classlist: 0x150
+  __TEXT.__objc_classname: 0x64b
+  __TEXT.__objc_methname: 0x681a
+  __TEXT.__objc_methtype: 0x1297
+  __TEXT.__objc_stubs: 0x5720
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0xbb0
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4038
-  __DATA_CONST.__objc_selrefs: 0x1828
-  __AUTH_CONST.__cfstring: 0x22e0
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_const: 0x4848
+  __DATA_CONST.__objc_selrefs: 0x1b20
+  __AUTH_CONST.__cfstring: 0x26a0
+  __AUTH_CONST.__objc_const: 0x2d0
+  __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__const: 0x52f0
-  __AUTH_CONST.__auth_got: 0x650
-  __AUTH.__objc_data: 0x0
+  __AUTH_CONST.__auth_got: 0x690
+  __AUTH.__objc_data: 0x230
   __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x290
-  __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x258
-  __DATA.__data: 0x940
-  __DATA.__bss: 0x10
+  __DATA.__objc_classrefs: 0x2e0
+  __DATA.__objc_superrefs: 0x100
+  __DATA.__objc_ivar: 0x2a8
+  __DATA.__data: 0xa60
+  __DATA.__bss: 0x30
   __DATA.__common: 0xa4
-  __DATA_DIRTY.__const: 0x240
-  __DATA_DIRTY.__objc_const: 0x1528
-  __DATA_DIRTY.__objc_data: 0xd80
+  __DATA_DIRTY.__const: 0x2a0
+  __DATA_DIRTY.__objc_const: 0x1498
+  __DATA_DIRTY.__objc_data: 0xd30
   __DATA_DIRTY.__data: 0x118
-  __DATA_DIRTY.__bss: 0x2e0
+  __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 98790F2A-B0F5-3249-A13D-E49A705EDAAE
-  Functions: 893
-  Symbols:   475
-  CStrings:  2301
+  UUID: 0BB256B0-C9C0-384A-801C-BCB723FE9E7C
+  Functions: 987
+  Symbols:   500
+  CStrings:  2532
 
Symbols:
+ _APDatabaseError
+ _AP_XPC_ACTIVITY_SCHEDULED_TIME
+ _NSURLNameKey
+ _OBJC_CLASS_$_APDatabaseCursor
+ _OBJC_CLASS_$_APDatabaseFileUtilities
+ _OBJC_CLASS_$_APDatabaseMigration
+ _OBJC_CLASS_$_APDatabasePath
+ _OBJC_CLASS_$_APDatabaseTable
+ _OBJC_CLASS_$_APDeviceLockedTask
+ _OBJC_CLASS_$_APTestingRig
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_METACLASS_$_APDatabaseCursor
+ _OBJC_METACLASS_$_APDatabaseFileUtilities
+ _OBJC_METACLASS_$_APDatabaseMigration
+ _OBJC_METACLASS_$_APDatabasePath
+ _OBJC_METACLASS_$_APDatabaseTable
+ _OBJC_METACLASS_$_APDeviceLockedTask
+ _OBJC_METACLASS_$_APTestingRig
+ _XPC_ACTIVITY_DISK_INTENSIVE
+ _clock_gettime_nsec_np
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_storeWeak
+ _sqlite3_bind_int64
+ _sqlite3_busy_timeout
+ _sqlite3_column_int64
+ _sqlite3_extended_result_codes
+ _xpc_dictionary_set_double
- _OBJC_CLASS_$_APDBVersion
- _OBJC_METACLASS_$_APDBVersion
CStrings:
+ "\x03\x13"
+ "!"
+ "\""
+ "%@"
+ ": %.3f"
+ "<redacted>"
+ "@\"<APDatabaseTableProtocol>\""
+ "@\"<APDatabaseTableProtocol>\"16@0:8"
+ "@\"APDatabaseManager\""
+ "@\"APDatabaseManager\"16@0:8"
+ "@\"APDatabasePath\""
+ "@\"APDeviceLockedTask\""
+ "@\"APInMemoryTTLCache\""
+ "@\"APLocationInfo\"16@0:8"
+ "@24@0:8#16"
+ "@32@0:8^{sqlite3_stmt=}16@24"
+ "@48@0:8@16@24@32@40"
+ "APDatabase"
+ "APDatabaseCursor"
+ "APDatabaseFileUtilities"
+ "APDatabaseMigration"
+ "APDatabasePath"
+ "APDatabaseRowProtocol"
+ "APDatabaseTable"
+ "APDatabaseTableProtocol"
+ "APDeviceLockedTask"
+ "APLocationManaging"
+ "APPurgeableCacheObjectP"
+ "APScheduledTime"
+ "APTestingRig"
+ "Current Location: (%{private}@)."
+ "Database"
+ "DatabaseMigrationScritps"
+ "ECObservability"
+ "Error, Database:%@, Version:%ld, Type:%d, Error code: %d"
+ "Error, Unkown database Name: %@"
+ "Error: Path 'rowClass' to be implemented for each subclass."
+ "ErrorCode"
+ "ErrorType"
+ "FPDI server request type %ld: %.3f"
+ "FPDIAttrDestroy"
+ "FPDIAttrSetContextStashingPolicy"
+ "FPDIAttrSetPrivacyLevel"
+ "FPDICreate"
+ "FPDIDataDestroy"
+ "FPDIDestroy"
+ "FPDIDestroyAllContexts"
+ "FPDIInit"
+ "FPDIInitAttribute"
+ "FPDISetup"
+ "FPDISign"
+ "Failed to create Database subdirectories for %@, error: %@, userInfo: %@"
+ "JSONObjectWithData:options:error:"
+ "Message was not registered"
+ "Name"
+ "PRAGMA auto_vacuum = INCREMENTAL"
+ "PRAGMA freelist_count"
+ "PRAGMA incremental_vacuum"
+ "PRAGMA journal_mode = WAL"
+ "PRAGMA locking_mode = EXCLUSIVE"
+ "PRAGMA locking_mode = NORMAL"
+ "PRAGMA page_count"
+ "PRAGMA synchronous = NORMAL"
+ "PRAGMA user_version"
+ "PRAGMA user_version = %ld"
+ "Queries"
+ "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
+ "T@\"<APDatabaseTableProtocol>\",R,W,N"
+ "T@\"APDatabaseManager\",R,W,N"
+ "T@\"APDatabasePath\",R,N,V_databasePath"
+ "T@\"APDeviceLockedTask\",&,N,V_deviceLockedTask"
+ "T@\"APInMemoryTTLCache\",&,N,V_tableCache"
+ "T@\"APUnfairLock\",&,N,V_theLock"
+ "T@\"NSArray\",R,N,V_sortedScriptsURLs"
+ "T@\"NSDictionary\",&,N,V_columns"
+ "T@\"NSDictionary\",&,N,V_readOnlyColumnsDic"
+ "T@\"NSMutableDictionary\",&,N,V_handlers"
+ "T@\"NSMutableDictionary\",R,N,V_registryByPurpose"
+ "T@\"NSMutableDictionary\",R,N,V_registryToAllPurpose"
+ "T@\"NSMutableDictionary\",R,N,V_registryToExternalPurpose"
+ "T@\"NSMutableDictionary\",R,N,V_registryToInternalPurpose"
+ "T@\"NSString\",&,N,V_dbName"
+ "T@\"NSString\",R"
+ "T@\"NSString\",R,N,V_databaseName"
+ "T@?,R,N,V_taskHandler"
+ "TB,N,V_isDiskIntensive"
+ "TQ,N,V_createdMonotonicClockTimestamp"
+ "T^{sqlite3_stmt=},N,V_statement"
+ "Td,N,V_scheduledTime"
+ "Ti,N,V_lastStepResult"
+ "Tq,N,V_currentVersion"
+ "Version"
+ "[%{private}@]: Database connection closed sucessfully."
+ "[%{private}@]: Database connection opened sucessfully."
+ "[%{private}@]: Database has %f free pages."
+ "[%{private}@]: Database manager is nil when trying to delete row."
+ "[%{private}@]: Database manager is nil when trying to save row."
+ "[%{private}@]: Database manager is nil when trying to select all."
+ "[%{private}@]: Database vacuuming complete."
+ "[%{private}@]: Database vacuuming started."
+ "[%{private}@]: Error: Could not create dictionary from data: %{public}@."
+ "[%{private}@]: Error: Could not get contents of directory: %{public}@."
+ "[%{private}@]: Error: No data found at path: %{private}@."
+ "[%{private}@]: Error: No migration files found."
+ "[%{private}@]: Error: No migration queries found at path: %{private}@."
+ "[%{private}@]: Failed to Move Corrupted File, error: %{public}@, userInfo: %{public}@"
+ "[%{private}@]: Failed to Remove Database: %{public}@ %{public}@"
+ "[%{private}@]: Open database called when connection is already open."
+ "[%{private}@]: RowId is nil when trying to update row."
+ "[%{private}@]: Start Database migration from v%{public}ld to v%ld."
+ "^{sqlite3_stmt=}"
+ "^{sqlite3_stmt=}16@0:8"
+ "^{sqlite3_stmt=}24@0:8@16"
+ "_buildSortedURLs"
+ "_clearCachedPaths"
+ "_closuresForRegisteredForNonSpecificPurposeInternal:"
+ "_createdMonotonicClockTimestamp"
+ "_databaseBundleDirectory"
+ "_databaseName"
+ "_databasePath"
+ "_dbName"
+ "_deviceLockedTask"
+ "_executePragmaSelectQuery:"
+ "_getQueriesForFileAtURL:"
+ "_getVersionFromFileAtURL:"
+ "_handlers"
+ "_isConnectionOpen"
+ "_isDiskIntensive"
+ "_lastStepResult"
+ "_manager"
+ "_moveCorruptedFileAtPath:"
+ "_openDBConnectionCanRepeat:databasePath:"
+ "_prepareStatementForQuery:"
+ "_registerHandlerInRegistry:closure:"
+ "_registryByPurpose"
+ "_registryToAllPurpose"
+ "_registryToExternalPurpose"
+ "_registryToInternalPurpose"
+ "_scheduledTime"
+ "_setInstanceClass:"
+ "_setUserVersion:"
+ "_sortedScriptsURLs"
+ "_statement"
+ "_table"
+ "_tableCache"
+ "_tableExists"
+ "_taskHandler"
+ "_theLock"
+ "_updateVersionForPath:"
+ "_userVersion"
+ "addObjectsFromArray:"
+ "allMetrics"
+ "bundleWithIdentifier:"
+ "checkinWithCriteria:"
+ "closeDatabaseConnection"
+ "columns"
+ "com.apple.ap.APFoundation"
+ "com.apple.ap.database.corruptedfile.queue"
+ "com.apple.ap.db-table-cache.queue"
+ "compare:"
+ "createdMonotonicClockTimestamp"
+ "dataWithContentsOfURL:"
+ "databaseDirectory"
+ "databaseFilePath"
+ "databaseName"
+ "databasePath"
+ "dbName"
+ "decodeInt64ForKey:"
+ "deviceLockedTask"
+ "deviceUnlockedSinceBoot"
+ "executeSelectQuery:forTable:withParameters:"
+ "executeSelectQuery:forTable:withParameters:groupedByColumn:"
+ "fileURLWithPath:"
+ "getCursorForQuery:parameters:"
+ "getMigrationQueriesFromVersion:"
+ "getTableForClass:"
+ "handlers"
+ "incrementalVacuumIfNeeded"
+ "initAsNewObjectWithTable:"
+ "initWithDatabaseManager:"
+ "initWithDatabaseName:"
+ "initWithDatabasePath:"
+ "initWithHandler:"
+ "initWithLong:"
+ "initWithStatement:lock:"
+ "initWithTable:"
+ "instanceClass"
+ "invokeHandlerForMessage:payload:completionHandler:"
+ "isDiskIntensive"
+ "isPromotedContentDaemon"
+ "lastPathComponent"
+ "lastStepResult"
+ "lastVersion"
+ "lockForPath"
+ "longValue"
+ "mainDatabase"
+ "manager"
+ "migrationScriptsPath"
+ "monotonic_timestamp"
+ "moveItemAtPath:toPath:error:"
+ "openConnectionIfFileExistsToDatabaseWithName:"
+ "openDatabaseConnectionWithName:"
+ "pathForName:"
+ "pathForResource:ofType:"
+ "pathToNameDictionary"
+ "propertyListWithData:options:format:error:"
+ "q24@0:8@?16"
+ "q24@0:8@?<v@?@\"<APMetricProtocol>\">16"
+ "q24@?0@\"NSURL\"8@\"NSURL\"16"
+ "q32@0:8@16@?24"
+ "readOnlyColumnsDic"
+ "registerHandlerForAllPurposesAndAllMetricsWithClosure:"
+ "registerHandlerForExternalPurposesAndAllMetricsWithClosure:"
+ "registerHandlerForInternalPurposesAndAllMetricsWithClosure:"
+ "registryByPurpose"
+ "registryToAllPurpose"
+ "registryToExternalPurpose"
+ "registryToInternalPurpose"
+ "removeDatabaseAtPath:"
+ "rowClass"
+ "scheduledTime"
+ "setColumns:"
+ "setCreatedMonotonicClockTimestamp:"
+ "setCurrentVersion:"
+ "setDbName:"
+ "setDeviceLockedTask:"
+ "setHandlers:"
+ "setIsDiskIntensive:"
+ "setLastStepResult:"
+ "setMainDatabase:"
+ "setReadOnlyColumnsDic:"
+ "setScheduledTime:"
+ "setStatement:"
+ "setTableCache:"
+ "setTheLock:"
+ "setUpDatabaseWithPath:"
+ "setUpMainDatabase"
+ "setWithArray:"
+ "sortedArrayUsingComparator:"
+ "sortedScriptsURLs"
+ "sql3"
+ "statement"
+ "stringByAppendingFormat:"
+ "stringByAppendingPathExtension:"
+ "stringByDeletingPathExtension"
+ "subscribeForDictMessage:handler:"
+ "subscribeForMessage:handler:"
+ "table"
+ "tableCache"
+ "tableName"
+ "taskHandler"
+ "theLock"
+ "translateCriteria"
+ "unionSet:"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8^{sqlite3_stmt=}16"
+ "v24@?0@\"NSString\"8@?<v@?@\"NSString\">16"
+ "v40@0:8@16@24@?32"
- "\x11"
- "@40@0:8@16#24@32"
- "@48@0:8@16#24@32@40"
- "APDBVersion"
- "APDataObject"
- "APDatabase.sql3"
- "APDatabaseSettings.rebuildDatabase"
- "CREATE TABLE IF NOT EXISTS APDBVersion (version INTEGER NOT NULL)"
- "Failed to create Database subdirectory."
- "Failed to open Database connection."
- "INSERT INTO APDBVersion (version) VALUES (?)"
- "PCD - Database setup failed on lock state notification."
- "SELECT rowid, * FROM APDBVersion WHERE rowId = ?"
- "SELECT version FROM APDBVersion WHERE rowId = ?"
- "T@\"NSMutableDictionary\",R,N,V_registryByRoute"
- "T@\"NSNumber\",&,D,N"
- "TB,N,V_staticActivity"
- "UPDATE APDBVersion SET version = ? WHERE rowid = ?"
- "[%{private}@]: Checking in on XPC activity %{public}@"
- "[%{private}@]: Database connetion is nil, no access to filesystem skipping setup."
- "[%{private}@]: Error %d executing query: %{private}s"
- "[%{private}@]: Error Database called when connection is not ready"
- "[%{private}@]: Error on Execute Query Statement. SQLError %{public}d"
- "[%{private}@]: Error on Execute Query Statement. SQLError %{public}d. SQL '%{private}@'"
- "[%{private}@]: Error on Execute Query Statement. SQLError %{public}d. SQL '%{sensitive}@'"
- "[%{private}@]: Error on Prepare Insert Statement. SQLError %{public}d"
- "[%{private}@]: Error on Prepare Insert Statement. SQLError %{public}d. SQL '%{sensitive}@'"
- "[%{private}@]: Error on Prepare execute Statement. SQLError %{public}d. SQL '%{private}@'"
- "[%{private}@]: Error on prepare select statement. SQLError %{public}d"
- "[%{private}@]: Error tyring to open DB, SQLITE Error %{public}d"
- "[%{private}@]: Error while commit transaction for DB migration."
- "[%{private}@]: Error while commit transaction."
- "[%{private}@]: Error while opening transaction for DB migration."
- "[%{private}@]: Error while opening transaction."
- "[%{private}@]: Failed to Delete Database: %{public}@ %{public}@"
- "[%{private}@]: Failed to create Database subdirectory: %{public}@ %{public}@"
- "[%{private}@]: RowId is nill when trying to update row."
- "[%{private}@]: Start Database migration from v%{public}ld to v%{public}ld."
- "_closeConnectionAndDeleteDBWithName:"
- "_deviceUnlockedSinceBoot"
- "_openDBConnectionCanRepeat:dataBaseName:"
- "_registryByRoute"
- "_staticActivity"
- "_updateToVersion1"
- "_updateVersion"
- "_updateVersionToCurrent"
- "all"
- "databaseManager"
- "executeSelectQuery:forClass:withParameters:"
- "executeSelectQuery:forClass:withParameters:groupedByColumn:"
- "initAsNewObject"
- "initWithVersion:"
- "registryByRoute"
- "setDatabaseManager:"
- "setStaticActivity:"
- "setUp"
- "staticActivity"
- "version"

```
