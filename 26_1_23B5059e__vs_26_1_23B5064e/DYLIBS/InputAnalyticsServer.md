## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x461fc
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x39c4
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x3689
-  __TEXT.__oslogstring: 0x4d83
-  __TEXT.__gcc_except_tab: 0x694
+111.1.0.0.0
+  __TEXT.__text: 0x4ba0c
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_methlist: 0x3e9c
+  __TEXT.__const: 0x300
+  __TEXT.__cstring: 0x3b49
+  __TEXT.__oslogstring: 0x54b3
+  __TEXT.__gcc_except_tab: 0x6b8
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_capture: 0x98
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xcc0
+  __TEXT.__unwind_info: 0xdb8
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0x834
-  __TEXT.__objc_methname: 0x8aee
-  __TEXT.__objc_methtype: 0xc16
-  __TEXT.__objc_stubs: 0x6c00
-  __DATA_CONST.__got: 0xed8
-  __DATA_CONST.__const: 0xe58
-  __DATA_CONST.__objc_classlist: 0x238
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__objc_classname: 0x937
+  __TEXT.__objc_methname: 0x91c9
+  __TEXT.__objc_methtype: 0xd73
+  __TEXT.__objc_stubs: 0x72a0
+  __DATA_CONST.__got: 0xf08
+  __DATA_CONST.__const: 0xe98
+  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1df0
+  __DATA_CONST.__objc_selrefs: 0x1fc8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0xd38
-  __AUTH_CONST.__cfstring: 0x3b20
-  __AUTH_CONST.__objc_const: 0x6740
+  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_arraydata: 0x110
+  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__const: 0xd78
+  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__objc_const: 0x6f48
   __AUTH_CONST.__objc_intobj: 0xcf0
-  __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x6a8
+  __AUTH_CONST.__objc_arrayobj: 0x150
+  __AUTH.__objc_data: 0x978
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x4b4
-  __DATA.__data: 0x3b0
-  __DATA.__bss: 0xe0
+  __DATA.__objc_ivar: 0x4e8
+  __DATA.__data: 0x410
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xfc8
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x368

   - /System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 18A8956F-ECB7-348F-802F-83454C26EA81
-  Functions: 1614
-  Symbols:   596
-  CStrings:  3011
+  UUID: F1D49C07-B4D1-3A8D-9BFE-B8C66372A013
+  Functions: 1721
+  Symbols:   623
+  CStrings:  3232
 
Symbols:
+ _NSInternalInconsistencyException
+ _NSStringFromSelector
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSTimeZone
+ ___NSArray0__struct
+ _objc_autorelease
+ _sqlite3_bind_double
+ _sqlite3_bind_int64
+ _sqlite3_bind_null
+ _sqlite3_bind_text
+ _sqlite3_close_v2
+ _sqlite3_column_count
+ _sqlite3_column_double
+ _sqlite3_column_int64
+ _sqlite3_column_name
+ _sqlite3_column_text
+ _sqlite3_column_type
+ _sqlite3_config
+ _sqlite3_errmsg
+ _sqlite3_exec
+ _sqlite3_finalize
+ _sqlite3_free
+ _sqlite3_open_v2
+ _sqlite3_prepare_v2
+ _sqlite3_step
CStrings:
+ " AND "
+ "%@ %@"
+ "%@ %@ NOT NULL"
+ "%@ = ?"
+ "%@.db"
+ "(null)"
+ "*"
+ ", "
+ "/var/mobile/Library/com.apple.inputanalyticsd"
+ "<%@: %p> columns=%@"
+ "<%@: %p> name=%@ dataType=%@ type=%@ retention=%@"
+ "@\"IASDataStoreSchema\""
+ "@\"IASDataStoreSchema\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSObject\"40@0:8@\"IASDataStoreKey\"16@\"NSString\"24@\"NSDate\"32"
+ "@48@0:8@16Q24Q32Q40"
+ "@56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSDateFormatter\"32@\"IASDataStoreSchema\"40@\"<IASDataStoreMigratorProtocol>\"48"
+ "@56@0:8@16@24@32@40@48"
+ "B24@0:8@\"<IASDataStoreTableProtocol>\"16"
+ "B24@0:8@\"NSDate\"16"
+ "B32@0:8Q16Q24"
+ "B40@0:8@\"IASDataStoreKey\"16@\"NSString\"24@\"NSDate\"32"
+ "B48@0:8@\"IASDataStoreKey\"16@\"NSObject\"24@\"NSString\"32@\"NSDate\"40"
+ "BOOL"
+ "CREATE TABLE IF NOT EXISTS %@ (%@);"
+ "DELETE FROM %@ WHERE date < ?"
+ "Daily"
+ "Durable"
+ "Error initializing datastore of type %@"
+ "Error initializing system table"
+ "Error migrating datastore of type %@"
+ "Error migrating system table"
+ "Error performing cleanup on datastore of type %@"
+ "Error: Cannot perform UPSERT for increment on table with no primary key columns"
+ "Error: Cannot perform UPSERT on table with no primary key columns"
+ "Error: Column %{private}@ is not a valid or compatible value column for table %{private}@"
+ "Error: Column %{private}@ is not a valid or incrementable value column for table %{private}@"
+ "Error: The provided key has no columns compatible with table %{private}@. Cannot perform increment."
+ "Error: The provided key has no columns compatible with table %{private}@. Cannot perform query."
+ "Error: The provided key has no columns compatible with table %{private}@. Cannot perform update."
+ "Error: no where clauses found for query."
+ "Failed to create SQL for table creation since no column definitions were found."
+ "Failed to create directory %{private}@ with error %{private}@"
+ "Failed to create table with error %{private}s"
+ "Failed to initialize key: Column name '%{private}@' does not exist in the schema for key class '%{private}@'."
+ "Failed to initialize key: Invalid value type '%{private}@' for column '%{private}@'."
+ "Failed to open database with error %{private}s"
+ "Failed to prepare cleanup statement: %{private}s"
+ "Failed to prepare getAllRows statement: %{private}s"
+ "Failed to prepare increment statement %{private}s"
+ "Failed to prepare statement %{private}s"
+ "Failed to prepare upsert statement %{private}s"
+ "IASAnalyticsDataStoreSystemTable"
+ "IASDataStoreColumnDataTypeHelper"
+ "IASDataStoreColumnTypeHelper"
+ "IASDataStoreKey"
+ "IASDataStoreMigratorProtocol"
+ "IASDataStoreRetentionPeriodHelper"
+ "IASDataStoreSchema"
+ "IASDataStoreSchemaColumn"
+ "IASDataStoreSystemTable"
+ "IASDataStoreTable.m"
+ "IASMockDataStoreTable.m"
+ "IASSystemTableKey"
+ "IASSystemTableMigrator"
+ "IASSystemTableSchema"
+ "INSERT INTO %@ (%@) VALUES (%@) ON CONFLICT(%@) DO UPDATE SET %@ = %@ + 1"
+ "INSERT INTO %@ (%@) VALUES (%@) ON CONFLICT(%@) DO UPDATE SET %@ = excluded.%@"
+ "INTEGER"
+ "Invalid argument(s) provided to getValueForKey — database: %p, key: %{private}@, columnName: %{private}@"
+ "Invalid argument(s) provided to incrementKey — database: %p, key: %{private}@, columnName: %{private}@"
+ "Invalid argument(s) provided to updateKey — database: %p, key: %{private}@, columnName: %{private}@"
+ "Key"
+ "Monthly"
+ "PRIMARY KEY (%@)"
+ "Query returned multiple rows for a key that should be unique."
+ "REAL"
+ "SELECT %@ FROM %@"
+ "SELECT %@ FROM %@ WHERE %@"
+ "T@\"IASDataStoreSchema\",&,N"
+ "T@\"IASDataStoreSchema\",&,N,Vschema"
+ "T@\"IASDataStoreSchema\",R,N,V_schema"
+ "T@\"NSArray\",&,N,V_dataStoreClasses"
+ "T@\"NSArray\",R,N,V_columns"
+ "T@\"NSMutableArray\",&,N,V_dataStores"
+ "T@\"NSMutableDictionary\",&,N,V_columnValues"
+ "T@\"NSNumber\",C,N"
+ "T@\"NSString\",C,N,VdatabasePath"
+ "T@\"NSString\",R,N,V_name"
+ "TEXT"
+ "TQ,R,N,V_columnDataType"
+ "TQ,R,N,V_columnType"
+ "TQ,R,N,V_retentionPeriod"
+ "T^{sqlite3=},N,Vdatabase"
+ "Type mismatch: Attempted to bind object of type '%@' to a column expecting REAL."
+ "Type mismatch: Attempted to bind object of type '%@' to a column expecting TEXT."
+ "Type mismatch: Attempted to bind object of type '%@' to a column expecting an INTEGER or BOOL."
+ "Type mismatch: Attempted to update mock table with object of type '%@' for a column expecting a different type."
+ "UNKNOWN"
+ "UTC"
+ "UTF8String"
+ "Unknown"
+ "Unknown column data type provided to _bindValue: %lu"
+ "Value"
+ "You must override %@ in a subclass of %@"
+ "^{sqlite3=}"
+ "^{sqlite3=}16@0:8"
+ "_bindValue:toStatement:atIndex:withColumnDataType:"
+ "_cleanupWithCutoffDate:"
+ "_columnDataType"
+ "_columnType"
+ "_columnValues"
+ "_columns"
+ "_createTableSQL"
+ "_dataStoreClasses"
+ "_dataStores"
+ "_getDatabaseDirectory"
+ "_getQueryStringForKey:withDate:"
+ "_initializeDatabase"
+ "_retentionPeriod"
+ "_schema"
+ "allValues"
+ "arrayByAddingObjectsFromArray:"
+ "cleanupWithCutoffDate:"
+ "columnDataType"
+ "columnType"
+ "columnType == %d"
+ "columnTypesDictionaryForTableRetention:"
+ "columnValues"
+ "columns"
+ "columnsCompatibleWithTableRetention:"
+ "configureSqlite3"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dataStoreClasses"
+ "dataStores"
+ "database"
+ "databasePath"
+ "date = ?"
+ "date TEXT NOT NULL"
+ "dealloc"
+ "defaultManager"
+ "doubleValue"
+ "exceptionWithName:reason:userInfo:"
+ "filteredArrayUsingPredicate:"
+ "getAllRows"
+ "getInfrastructureVersionForTable:"
+ "getValueForKey:forColumnName:withDate:"
+ "getVersionForTable:"
+ "incrementKey:forColumnName:withDate:"
+ "infrastructureVersion"
+ "initWithColumnValues:"
+ "initWithColumns:"
+ "initWithName:columnDataType:columnType:retentionPeriod:"
+ "initWithName:withTableVersion:withDateFormatter:withSchema:withMigrator:"
+ "initWithName:withTableVersion:withSchema:withMigrator:"
+ "initWithTableName:"
+ "initWithTables:andSystemTable:"
+ "isColumnRetentionPeriod:compatibleWithTableRetentionPeriod:"
+ "keyColumnsCompatibleWithTableRetention:"
+ "longLongValue"
+ "numberWithDouble:"
+ "numberWithLongLong:"
+ "orderedColumnNamesForTableRetention:"
+ "predicateWithFormat:"
+ "removeObjectsForKeys:"
+ "retentionPeriod"
+ "schema"
+ "set"
+ "setColumnValues:"
+ "setDataStoreClasses:"
+ "setDataStores:"
+ "setDatabase:"
+ "setDatabasePath:"
+ "setInfrastructureVersionForTable:"
+ "setMonth:"
+ "setSchema:"
+ "setTimeZone:"
+ "setVersionForTable:"
+ "sharedInstance"
+ "sqliteStringFromColumnDataType:"
+ "stringByAppendingPathComponent:"
+ "stringFromColumnDataType:"
+ "stringFromColumnType:"
+ "stringFromRetentionPeriod:"
+ "stringWithUTF8String:"
+ "tableName"
+ "timeZoneWithAbbreviation:"
+ "updateKey:withValue:forColumnName:withDate:"
+ "v24@0:8@\"IASDataStoreSchema\"16"
+ "v24@0:8@\"NSNumber\"16"
+ "v24@0:8^{sqlite3=}16"
+ "v44@0:8@16^{sqlite3_stmt=}24i32Q36"
+ "valueColumnsCompatibleWithTableRetention:"
+ "valueForColumn:"
- "<IAS_KV_DELIM>"
- "<IAS_KV_SEP>"
- "@\"NSObject\"40@0:8@\"NSString\"16@\"IASDataStoreMetadata\"24@\"NSDate\"32"
- "@40@0:8@\"NSString\"16@\"NSNumber\"24@\"<IASDataStoreMigratorProtocol>\"32"
- "B40@0:8@\"NSString\"16@\"IASDataStoreMetadata\"24@\"NSDate\"32"
- "B48@0:8@\"NSString\"16@\"NSObject\"24@\"IASDataStoreMetadata\"32@\"NSDate\"40"
- "IASDataStoreMetadata"
- "T@\"NSMutableDictionary\",&,N,V_metadataDictionary"
- "T@\"NSNumber\",R,C,N"
- "T@\"NSNumber\",R,C,N,VtableVersion"
- "_getQueryStringForKey:withMetadata:withDate:"
- "_metadataDictionary"
- "containsString:"
- "deserialize:"
- "getValueForKey:withMetadata:withDate:"
- "incrementKey:withMetadata:withDate:"
- "initWithName:withTableVersion:withDateFormatter:withMigrator:"
- "initWithName:withTableVersion:withMigrator:"
- "initWithTables:AndSystemTable:"
- "metadataDictionary"
- "serialize"
- "setMetadataDictionary:"
- "updateKey:withValue:withMetadata:withDate:"

```
