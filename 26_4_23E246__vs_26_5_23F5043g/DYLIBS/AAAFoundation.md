## AAAFoundation

> `/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation`

```diff

-100.475.5.0.0
-  __TEXT.__text: 0xfc98
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_methlist: 0x1774
-  __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0xa14
-  __TEXT.__cstring: 0xe57
-  __TEXT.__gcc_except_tab: 0x22c
+100.575.2.0.0
+  __TEXT.__text: 0x12dd0
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0x1b1c
+  __TEXT.__const: 0xd0
+  __TEXT.__oslogstring: 0xd6e
+  __TEXT.__cstring: 0xfb9
+  __TEXT.__gcc_except_tab: 0x2ac
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0x5f8
-  __TEXT.__objc_classname: 0x304
-  __TEXT.__objc_methname: 0x378f
-  __TEXT.__objc_methtype: 0x7d2
-  __TEXT.__objc_stubs: 0x2740
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x928
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__unwind_info: 0x718
+  __TEXT.__objc_classname: 0x369
+  __TEXT.__objc_methname: 0x3f59
+  __TEXT.__objc_methtype: 0x95f
+  __TEXT.__objc_stubs: 0x2de0
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0xa70
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xff8
+  __DATA_CONST.__objc_selrefs: 0x1260
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x440
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0x3658
+  __AUTH_CONST.__cfstring: 0x1080
+  __AUTH_CONST.__objc_const: 0x3e88
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x17c
-  __DATA.__data: 0x3c8
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x1a4
+  __DATA.__data: 0x428
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50200859-80CA-356F-8343-99131FDF913C
-  Functions: 571
-  Symbols:   2292
-  CStrings:  1188
+  - /usr/lib/libsqlite3.dylib
+  UUID: 69E49BCA-4BC1-3C60-927F-1D1DC732FE0E
+  Functions: 683
+  Symbols:   2683
+  CStrings:  1360
 
Symbols:
+ +[AAFSQLiteHelper dataFromColumn:inStatement:]
+ +[AAFSQLiteHelper doubleFromColumn:inStatement:]
+ +[AAFSQLiteHelper integerFromColumn:inStatement:]
+ +[AAFSQLiteHelper numberOfRowsForTable:withExecutor:]
+ +[AAFSQLiteHelper stringFromColumn:inStatement:]
+ +[AAFSQLiteHelper tableInfoForTable:withExecutor:]
+ +[AAFSQLiteQuery queryWithString:]
+ +[AAFStoreUtils hash:]
+ +[AAFStoreUtils hash:].cold.1
+ -[AAFSQLiteExecutor .cxx_destruct]
+ -[AAFSQLiteExecutor _assertQueueIfNeeded]
+ -[AAFSQLiteExecutor _bindParametersForQuery:statement:]
+ -[AAFSQLiteExecutor _configureOpenedDatabase]
+ -[AAFSQLiteExecutor _configureOpenedDatabase].cold.1
+ -[AAFSQLiteExecutor _currentDataBaseError]
+ -[AAFSQLiteExecutor _executeQuery:]
+ -[AAFSQLiteExecutor _executeQuery:].cold.1
+ -[AAFSQLiteExecutor _executeQuery:].cold.2
+ -[AAFSQLiteExecutor _finalizeStatement:error:]
+ -[AAFSQLiteExecutor _finalizeStatement:error:].cold.1
+ -[AAFSQLiteExecutor _handleDatabaseFailureError:]
+ -[AAFSQLiteExecutor _handleDatabaseFailureError:].cold.1
+ -[AAFSQLiteExecutor _handleDatabaseFailureError:].cold.2
+ -[AAFSQLiteExecutor _performDatabaseOperationAndWait:]
+ -[AAFSQLiteExecutor _prepareStatementForQuery:error:]
+ -[AAFSQLiteExecutor _printStatement:]
+ -[AAFSQLiteExecutor _printStatement:].cold.1
+ -[AAFSQLiteExecutor _stepThroughRowsWithQuery:statement:]
+ -[AAFSQLiteExecutor _unsafe_closeDatabase]
+ -[AAFSQLiteExecutor _unsafe_closeDatabase].cold.1
+ -[AAFSQLiteExecutor _unsafe_closeDatabase].cold.2
+ -[AAFSQLiteExecutor _unsafe_createDataBase]
+ -[AAFSQLiteExecutor _unsafe_createDataBase].cold.1
+ -[AAFSQLiteExecutor _unsafe_createDataBase].cold.2
+ -[AAFSQLiteExecutor _unsafe_createDataBase].cold.3
+ -[AAFSQLiteExecutor _unsafe_createDataBase].cold.4
+ -[AAFSQLiteExecutor _unsafe_createDataBase].cold.5
+ -[AAFSQLiteExecutor _unsafe_openDatabase:]
+ -[AAFSQLiteExecutor _unsafe_wipeDatabase:]
+ -[AAFSQLiteExecutor _unsafe_wipeDatabase:].cold.1
+ -[AAFSQLiteExecutor _unsafe_wipeDatabase:].cold.2
+ -[AAFSQLiteExecutor closeDatabase]
+ -[AAFSQLiteExecutor commitTransaction]
+ -[AAFSQLiteExecutor databasePath]
+ -[AAFSQLiteExecutor database]
+ -[AAFSQLiteExecutor dealloc]
+ -[AAFSQLiteExecutor initWithDatabasePath:migrationController:]
+ -[AAFSQLiteExecutor migrator]
+ -[AAFSQLiteExecutor openDatabase:]
+ -[AAFSQLiteExecutor openTransaction]
+ -[AAFSQLiteExecutor performBlock:]
+ -[AAFSQLiteExecutor performBlockAndWait:]
+ -[AAFSQLiteExecutor performInsertQuery:]
+ -[AAFSQLiteExecutor performInsertQuery:error:]
+ -[AAFSQLiteExecutor performQuery:]
+ -[AAFSQLiteExecutor performQuery:error:]
+ -[AAFSQLiteExecutor performQuery:rowHandler:]
+ -[AAFSQLiteExecutor performTransactionBlockAndWait:]
+ -[AAFSQLiteExecutor rollbackTransaction]
+ -[AAFSQLiteExecutor setMigrator:]
+ -[AAFSQLiteExecutor setShouldAutomaticallyMigrate:]
+ -[AAFSQLiteExecutor shouldAutomaticallyMigrate]
+ -[AAFSQLiteExecutor wipeDatabase:]
+ -[AAFSQLiteExecutor wipeDatabase:].cold.1
+ -[AAFSQLiteQuery .cxx_destruct]
+ -[AAFSQLiteQuery _bindStatement:withParameter:atPosition:]
+ -[AAFSQLiteQuery _bindStatement:withParameter:atPosition:].cold.1
+ -[AAFSQLiteQuery bindHandler]
+ -[AAFSQLiteQuery bindParameter:error:]
+ -[AAFSQLiteQuery bindParameters:error:]
+ -[AAFSQLiteQuery bindingFailure]
+ -[AAFSQLiteQuery queryString]
+ -[AAFSQLiteQuery rowHandler]
+ -[AAFSQLiteQuery setBindHandler:]
+ -[AAFSQLiteQuery setBindingFailure:]
+ -[AAFSQLiteQuery setQueryString:]
+ -[AAFSQLiteQuery setRowHandler:]
+ -[AAFStoreMigrator .cxx_destruct]
+ -[AAFStoreMigrator _schemaVersion]
+ -[AAFStoreMigrator _schemaVersion].cold.1
+ -[AAFStoreMigrator currentSchemaVersion]
+ -[AAFStoreMigrator currentSchemaVersion].cold.1
+ -[AAFStoreMigrator executor]
+ -[AAFStoreMigrator initWithExecutor:]
+ -[AAFStoreMigrator migrateSchemaFromVersion:]
+ -[AAFStoreMigrator migrateSchemaFromVersion:].cold.1
+ -[AAFStoreMigrator migrateSchemaIfNecessary]
+ -[AAFStoreMigrator setExecutor:]
+ -[AAFStoreMigrator storeName]
+ -[AAFStoreMigrator storeName].cold.1
+ GCC_except_table26
+ GCC_except_table33
+ _AAFSQLErrorDomain
+ _NSLocalizedFailureErrorKey
+ _OBJC_CLASS_$_AAFSQLiteExecutor
+ _OBJC_CLASS_$_AAFSQLiteHelper
+ _OBJC_CLASS_$_AAFSQLiteQuery
+ _OBJC_CLASS_$_AAFStoreMigrator
+ _OBJC_CLASS_$_AAFStoreUtils
+ _OBJC_CLASS_$_NSDecimalNumber
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_IVAR_$_AAFSQLiteExecutor._database
+ _OBJC_IVAR_$_AAFSQLiteExecutor._databasePath
+ _OBJC_IVAR_$_AAFSQLiteExecutor._databaseQueue
+ _OBJC_IVAR_$_AAFSQLiteExecutor._migrator
+ _OBJC_IVAR_$_AAFSQLiteExecutor._shouldAutomaticallyMigrate
+ _OBJC_IVAR_$_AAFSQLiteQuery._bindHandler
+ _OBJC_IVAR_$_AAFSQLiteQuery._bindingFailure
+ _OBJC_IVAR_$_AAFSQLiteQuery._queryString
+ _OBJC_IVAR_$_AAFSQLiteQuery._rowHandler
+ _OBJC_IVAR_$_AAFStoreMigrator._executor
+ _OBJC_METACLASS_$_AAFSQLiteExecutor
+ _OBJC_METACLASS_$_AAFSQLiteHelper
+ _OBJC_METACLASS_$_AAFSQLiteQuery
+ _OBJC_METACLASS_$_AAFStoreMigrator
+ _OBJC_METACLASS_$_AAFStoreUtils
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_AAFSQLiteHelper
+ __OBJC_$_CLASS_METHODS_AAFSQLiteQuery
+ __OBJC_$_CLASS_METHODS_AAFStoreUtils
+ __OBJC_$_INSTANCE_METHODS_AAFSQLiteExecutor
+ __OBJC_$_INSTANCE_METHODS_AAFSQLiteQuery
+ __OBJC_$_INSTANCE_METHODS_AAFStoreMigrator
+ __OBJC_$_INSTANCE_VARIABLES_AAFSQLiteExecutor
+ __OBJC_$_INSTANCE_VARIABLES_AAFSQLiteQuery
+ __OBJC_$_INSTANCE_VARIABLES_AAFStoreMigrator
+ __OBJC_$_PROP_LIST_AAFSQLiteExecutor
+ __OBJC_$_PROP_LIST_AAFSQLiteQuery
+ __OBJC_$_PROP_LIST_AAFStoreMigrator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAFSQLiteMigration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAFSQLiteMigration
+ __OBJC_$_PROTOCOL_REFS_AAFSQLiteMigration
+ __OBJC_CLASS_PROTOCOLS_$_AAFStoreMigrator
+ __OBJC_CLASS_RO_$_AAFSQLiteExecutor
+ __OBJC_CLASS_RO_$_AAFSQLiteHelper
+ __OBJC_CLASS_RO_$_AAFSQLiteQuery
+ __OBJC_CLASS_RO_$_AAFStoreMigrator
+ __OBJC_CLASS_RO_$_AAFStoreUtils
+ __OBJC_LABEL_PROTOCOL_$_AAFSQLiteMigration
+ __OBJC_METACLASS_RO_$_AAFSQLiteExecutor
+ __OBJC_METACLASS_RO_$_AAFSQLiteHelper
+ __OBJC_METACLASS_RO_$_AAFSQLiteQuery
+ __OBJC_METACLASS_RO_$_AAFStoreMigrator
+ __OBJC_METACLASS_RO_$_AAFStoreUtils
+ __OBJC_PROTOCOL_$_AAFSQLiteMigration
+ ___34-[AAFSQLiteExecutor closeDatabase]_block_invoke
+ ___34-[AAFSQLiteExecutor openDatabase:]_block_invoke
+ ___34-[AAFSQLiteExecutor performBlock:]_block_invoke
+ ___34-[AAFSQLiteExecutor wipeDatabase:]_block_invoke
+ ___34-[AAFStoreMigrator _schemaVersion]_block_invoke
+ ___38-[AAFSQLiteQuery bindParameter:error:]_block_invoke
+ ___38-[AAFSQLiteQuery bindParameter:error:]_block_invoke.cold.1
+ ___38-[AAFSQLiteQuery bindParameter:error:]_block_invoke.cold.2
+ ___39-[AAFSQLiteQuery bindParameters:error:]_block_invoke
+ ___39-[AAFSQLiteQuery bindParameters:error:]_block_invoke.2
+ ___39-[AAFSQLiteQuery bindParameters:error:]_block_invoke.2.cold.1
+ ___39-[AAFSQLiteQuery bindParameters:error:]_block_invoke.cold.1
+ ___41-[AAFSQLiteExecutor performBlockAndWait:]_block_invoke
+ ___44-[AAFStoreMigrator migrateSchemaIfNecessary]_block_invoke
+ ___45-[AAFSQLiteExecutor performQuery:rowHandler:]_block_invoke
+ ___50+[AAFSQLiteHelper tableInfoForTable:withExecutor:]_block_invoke
+ ___53+[AAFSQLiteHelper numberOfRowsForTable:withExecutor:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e27_v24?0^{sqlite3_stmt=}8^B16ls32l8
+ ___block_descriptor_40_e8_32r_e23_v16?0^{sqlite3_stmt=}8lr32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e23_v16?0^{sqlite3_stmt=}8ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40w_e23_v16?0^{sqlite3_stmt=}8lw40l8s32l8
+ ___block_descriptor_56_e8_32s_e15_v32?08Q16^B24ls32l8
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_assertQueueIfNeeded
+ _objc_msgSend$_bindParametersForQuery:statement:
+ _objc_msgSend$_bindStatement:withParameter:atPosition:
+ _objc_msgSend$_configureOpenedDatabase
+ _objc_msgSend$_currentDataBaseError
+ _objc_msgSend$_executeQuery:
+ _objc_msgSend$_finalizeStatement:error:
+ _objc_msgSend$_handleDatabaseFailureError:
+ _objc_msgSend$_performDatabaseOperationAndWait:
+ _objc_msgSend$_prepareStatementForQuery:error:
+ _objc_msgSend$_printStatement:
+ _objc_msgSend$_schemaVersion
+ _objc_msgSend$_stepThroughRowsWithQuery:statement:
+ _objc_msgSend$_unsafe_closeDatabase
+ _objc_msgSend$_unsafe_createDataBase
+ _objc_msgSend$_unsafe_openDatabase:
+ _objc_msgSend$_unsafe_wipeDatabase:
+ _objc_msgSend$bindHandler
+ _objc_msgSend$bindingFailure
+ _objc_msgSend$commitTransaction
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$currentSchemaVersion
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionary
+ _objc_msgSend$doubleValue
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$integerValue
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$longLongValue
+ _objc_msgSend$migrateSchemaFromVersion:
+ _objc_msgSend$migrateSchemaIfNecessary
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$openTransaction
+ _objc_msgSend$performBlockAndWait:
+ _objc_msgSend$performInsertQuery:error:
+ _objc_msgSend$performQuery:error:
+ _objc_msgSend$performQuery:rowHandler:
+ _objc_msgSend$performTransactionBlockAndWait:
+ _objc_msgSend$queryString
+ _objc_msgSend$queryWithString:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$rollbackTransaction
+ _objc_msgSend$rowHandler
+ _objc_msgSend$setBindingFailure:
+ _objc_msgSend$setExecutor:
+ _objc_msgSend$setQueryString:
+ _objc_msgSend$setRowHandler:
+ _objc_msgSend$storeName
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringFromColumn:inStatement:
+ _os_transaction_create
+ _sqlite3_bind_blob64
+ _sqlite3_bind_double
+ _sqlite3_bind_int64
+ _sqlite3_bind_null
+ _sqlite3_bind_text
+ _sqlite3_changes
+ _sqlite3_close
+ _sqlite3_column_blob
+ _sqlite3_column_bytes
+ _sqlite3_column_double
+ _sqlite3_column_int64
+ _sqlite3_column_text
+ _sqlite3_errcode
+ _sqlite3_errmsg
+ _sqlite3_exec
+ _sqlite3_expanded_sql
+ _sqlite3_finalize
+ _sqlite3_free
+ _sqlite3_last_insert_rowid
+ _sqlite3_open_v2
+ _sqlite3_prepare_v2
+ _sqlite3_step
CStrings:
+ "%02x"
+ "%@: Failed to open file at path %@"
+ "<undefined>"
+ "@\"<AAFSQLiteMigration>\""
+ "@\"AAFSQLiteExecutor\""
+ "@32@0:8q16^{sqlite3_stmt=}24"
+ "AAFSQLErrorCode"
+ "AAFSQLiteExecutor"
+ "AAFSQLiteHelper"
+ "AAFSQLiteMigration"
+ "AAFSQLiteQuery"
+ "AAFSQLiteQuery deallocated, not binding parameters"
+ "AAFStoreMigrator"
+ "AAFStoreUtils"
+ "Attempting to open database at path: %@"
+ "Attempting to wipe database at path: %@"
+ "B24@0:8^@16"
+ "B32@0:8@16@?24"
+ "B32@0:8@16^{sqlite3_stmt=}24"
+ "B32@0:8^{sqlite3_stmt=}16^@24"
+ "B36@0:8^{sqlite3_stmt=}16@24i32"
+ "BEGIN EXCLUSIVE TRANSACTION"
+ "COMMIT TRANSACTION"
+ "Cannot convert %@ to a non-nil string"
+ "Closed database with result: %d"
+ "Closing database at path: %@"
+ "Creating path for database..."
+ "Current %@ database version: %i"
+ "Current schema version undefined!"
+ "Current store name undefined!"
+ "Database %@ wiped..."
+ "Database corruption detected: %@"
+ "Database error detected: %@"
+ "Database opened at path: %@"
+ "Error binding sql statement with parameter: %@"
+ "Executing query: %@"
+ "Executing query: %s"
+ "Failed to create database. Error: %@"
+ "Failed to wipe database with error: %@"
+ "Migration logic not present (from: %i)"
+ "PRAGMA table_info('%@')"
+ "Parameter type not handled, failing binding statement."
+ "ROLLBACK TRANSACTION"
+ "Rows changed: %d"
+ "SELECT COUNT(*) FROM %@"
+ "SELECT db_version FROM version;"
+ "SQL Exec %@ failed with error %s."
+ "T@\"<AAFSQLiteMigration>\",&,N,V_migrator"
+ "T@\"AAFSQLiteExecutor\",W,N,V_executor"
+ "T@\"NSString\",C,N,V_queryString"
+ "T@\"NSString\",R,N"
+ "T@?,C,N,V_bindHandler"
+ "T@?,C,N,V_rowHandler"
+ "TB,N,V_bindingFailure"
+ "T^{sqlite3=},R,N"
+ "Wanted to migrate database, but migrator is nil!"
+ "^{sqlite3=}"
+ "^{sqlite3=}16@0:8"
+ "^{sqlite3_stmt=}32@0:8@16^@24"
+ "_assertQueueIfNeeded"
+ "_bindHandler"
+ "_bindParametersForQuery:statement:"
+ "_bindStatement:withParameter:atPosition:"
+ "_bindingFailure"
+ "_configureOpenedDatabase"
+ "_currentDataBaseError"
+ "_database"
+ "_databasePath"
+ "_databaseQueue"
+ "_executeQuery:"
+ "_executor"
+ "_finalizeStatement:error:"
+ "_handleDatabaseFailureError:"
+ "_migrator"
+ "_performDatabaseOperationAndWait:"
+ "_prepareStatementForQuery:error:"
+ "_printStatement:"
+ "_queryString"
+ "_rowHandler"
+ "_schemaVersion"
+ "_shouldAutomaticallyMigrate"
+ "_stepThroughRowsWithQuery:statement:"
+ "_unsafe_closeDatabase"
+ "_unsafe_createDataBase"
+ "_unsafe_openDatabase:"
+ "_unsafe_wipeDatabase:"
+ "bindHandler"
+ "bindParameter:error:"
+ "bindParameters:error:"
+ "bindingFailure"
+ "closeDatabase"
+ "com.apple.aaafoundation.sqlite"
+ "com.apple.aaafoundation.storage"
+ "com.apple.aaafoundation.storage.%@"
+ "commitTransaction"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "currentSchemaVersion"
+ "dataFromColumn:inStatement:"
+ "database"
+ "databasePath"
+ "defaultManager"
+ "dictionary"
+ "doubleFromColumn:inStatement:"
+ "doubleValue"
+ "executor"
+ "fileExistsAtPath:"
+ "hash:"
+ "i16@0:8"
+ "i24@0:8@16"
+ "i32@0:8@16@24"
+ "initWithBytes:length:"
+ "initWithDatabasePath:migrationController:"
+ "initWithExecutor:"
+ "integerFromColumn:inStatement:"
+ "integerValue"
+ "lastPathComponent"
+ "localizedDescription"
+ "longLongValue"
+ "migrateSchemaFromVersion:"
+ "migrateSchemaIfNecessary"
+ "migrator"
+ "numberOfRowsForTable:withExecutor:"
+ "numberWithInt:"
+ "numberWithLongLong:"
+ "openDatabase:"
+ "openTransaction"
+ "performBlock:"
+ "performBlockAndWait:"
+ "performInsertQuery:"
+ "performInsertQuery:error:"
+ "performQuery:"
+ "performQuery:error:"
+ "performQuery:rowHandler:"
+ "performTransactionBlockAndWait:"
+ "pragma foreign_keys=on"
+ "q32@0:8@16^@24"
+ "queryString"
+ "queryWithString:"
+ "removeItemAtPath:error:"
+ "rollbackTransaction"
+ "rowHandler"
+ "setBindHandler:"
+ "setBindingFailure:"
+ "setExecutor:"
+ "setMigrator:"
+ "setQueryString:"
+ "setRowHandler:"
+ "setShouldAutomaticallyMigrate:"
+ "shouldAutomaticallyMigrate"
+ "storeName"
+ "stringByDeletingLastPathComponent"
+ "stringFromColumn:inStatement:"
+ "tableInfoForTable:withExecutor:"
+ "v16@?0^{sqlite3_stmt=}8"
+ "v24@0:8@\"AAFSQLiteExecutor\"16"
+ "v24@0:8^@16"
+ "v24@0:8^{sqlite3_stmt=}16"
+ "v24@?0^{sqlite3_stmt=}8^B16"
+ "v32@0:8@16^{sqlite3_stmt=}24"
+ "wipeDatabase:"

```
