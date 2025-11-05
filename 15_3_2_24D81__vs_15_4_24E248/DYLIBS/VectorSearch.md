## VectorSearch

> `/System/Library/PrivateFrameworks/VectorSearch.framework/Versions/A/VectorSearch`

```diff

-33.0.0.0.0
-  __TEXT.__text: 0x62214
-  __TEXT.__auth_stubs: 0x1930
-  __TEXT.__objc_methlist: 0x83c
-  __TEXT.__const: 0x1e58
-  __TEXT.__cstring: 0x4433
-  __TEXT.__constg_swiftt: 0xec0
-  __TEXT.__swift5_typeref: 0xebc
-  __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xae5
-  __TEXT.__swift5_fieldmd: 0xc78
-  __TEXT.__swift5_types: 0xe0
-  __TEXT.__swift5_capture: 0x4e8
+38.1.0.0.0
+  __TEXT.__text: 0x68eec
+  __TEXT.__auth_stubs: 0x19d0
+  __TEXT.__objc_methlist: 0x8d4
+  __TEXT.__const: 0x1f40
+  __TEXT.__cstring: 0x43f5
+  __TEXT.__constg_swiftt: 0xf4c
+  __TEXT.__swift5_typeref: 0x100e
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_reflstr: 0xbe5
+  __TEXT.__swift5_fieldmd: 0xd10
+  __TEXT.__swift5_types: 0xec
+  __TEXT.__swift5_capture: 0x694
+  __TEXT.__oslogstring: 0xfc4
   __TEXT.__swift5_proto: 0x184
-  __TEXT.__oslogstring: 0xb84
-  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0x1518
-  __TEXT.__eh_frame: 0x35b8
+  __TEXT.__swift5_mpenum: 0x3c
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0x1720
+  __TEXT.__eh_frame: 0x42a8
   __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methname: 0x16dd
-  __TEXT.__objc_methtype: 0x4c0
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __TEXT.__objc_methname: 0x196c
+  __TEXT.__objc_methtype: 0x4d6
+  __TEXT.__objc_stubs: 0x8e0
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c8
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xca0
-  __AUTH_CONST.__const: 0x1d68
-  __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x19e0
+  __AUTH_CONST.__auth_got: 0xcf0
+  __AUTH_CONST.__const: 0x22f8
+  __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__objc_const: 0x1a58
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xb38
-  __AUTH.__data: 0xdc0
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0xb00
-  __DATA.__bss: 0x2980
-  __DATA.__common: 0x70
+  __AUTH.__objc_data: 0xbf0
+  __AUTH.__data: 0xe90
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0xb58
+  __DATA.__bss: 0x2a00
+  __DATA.__common: 0x68
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 72A8B04E-7B0A-3A39-8776-19A9BBDF8D04
-  Functions: 1687
-  Symbols:   215
-  CStrings:  626
+  UUID: 1583978B-4D2A-3EA1-86D2-C7B717446088
+  Functions: 1777
+  Symbols:   226
+  CStrings:  666
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSProgress
+ _VSKErrorDomainName
+ __Block_copy
+ __Block_release
+ _ceilf
+ _sqlite3_close
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
- _sqlite3_close_v2
- _swift_conformsToProtocol2
CStrings:
+ "    ALTER TABLE "
+ "    INNER JOIN attributes ON "
+ " (\n        asset_id TEXT,\n        vector_id INTEGER\n        "
+ " (asset_id, vector_id "
+ " as f0\n    INNER JOIN observations f1 ON f0.asset_id = f1.observationid"
+ " sets of attributes to be set. Found "
+ "%f: Updating vector database index"
+ "%s does not exist. Returning from rebuildFTSIndex."
+ "(attributes_fts."
+ ")\n    SELECT f0.asset_id, f1.id "
+ ")\nON CONFLICT(asset_id, vector_id) DO UPDATE SET "
+ ",\n        PRIMARY KEY (asset_id, vector_id)\n    ) STRICT"
+ ", and sqlite error message: "
+ ", error message from DB: "
+ ". Extended error code: "
+ "@56@0:8@16@24@32@40@48"
+ "An error explaining that the base tokenizer could not be found."
+ "An error explaining that the tokenizer instance could not be created"
+ "An error explaining that the unicode61wrapper tokenizer could not be created."
+ "Async rebuild called"
+ "Cannot filter on attributes when no filterable attributes are defined."
+ "Could not create error message"
+ "Could not create tokenizer instance. SQLite Code: "
+ "Could not create unicode61wrapper Tokenizer. Error: "
+ "Could not create unicode61wrapper. SQLite code: "
+ "Could not find base tokenizer. SQLite Code: "
+ "Explicitly cancelling rebuild."
+ "FTS is disabled. Returning from rebuildFTSIndex."
+ "Failed to close database connection with error code: %d"
+ "Failed to close database connection with error code: %d. Error message: %s. Dangling pointer."
+ "Failed to reset statement"
+ "Failed to take RunningBoard assertion: %@"
+ "INNER JOIN attributes ON "
+ "INNER JOIN attributes_fts ON "
+ "Invalid or corrupted DB file "
+ "No error message"
+ "Rebuild not cancelled. Running for %f seconds. Checking again in %llu seconds"
+ "SELECT COUNT(DISTINCT(attributes.asset_id)) FROM attributes"
+ "SELECT id FROM observations WHERE observationid = ?"
+ "SQLExpressionEvaluator"
+ "SQLExpressionEvaluator: Failed to reset statement with error code: %d"
+ "SQLExpressionEvaluator: deinitializer"
+ "T@\"NSArray\",C,N,V_perVectorAttribute"
+ "Unicode61Tokenizer: Could not create unicode61 tokenizer. Error: %d."
+ "Unicode61Tokenizer: Could not find unicode61 tokenizer. Error: %d"
+ "Unicode61Tokenizer: Internal failure during xCreateTokenizer: %d."
+ "Unicode61TokenizerWrapper already added to database connection."
+ "Unicode61Tokenizers: Created successfully."
+ "Unrecoverable error due to invliad or corrupted DB: "
+ "VectorDatabase"
+ "VectorDatabaseConfig:migrate no-op for %s migration"
+ "VectorDatabaseConfig:migrate no-op for .perVectorAttribute migration"
+ "VectorSearch/SQLObjects.swift"
+ "_TtC12VectorSearch18SQLDatabasePointer"
+ "_TtC12VectorSearch20SQLPreparedStatement"
+ "_TtC12VectorSearch38Unicode61WrapperTokenizerDataReference"
+ "_perVectorAttribute"
+ "addChild:withPendingUnitCount:"
+ "arrayWithCapacity:"
+ "count"
+ "count called with filter"
+ "countWithAttributeFilters:error:"
+ "countWithError:error:"
+ "databaseFilePath"
+ "databasePointer"
+ "initWithDomain:code:userInfo:"
+ "initWithIdentifier:vectors:attributes:perVectorAttribute:payload:"
+ "initWithIdentifier:vectors:perVectorAttribute:payload:"
+ "initWithStringIdentifier:vectors:perVectorAttribute:payload:"
+ "objectAtIndexedSubscript:"
+ "perVectorAttribute"
+ "progressWithTotalUnitCount:"
+ "rawPointer"
+ "rebuild(progress:): Increase progress.totalUnitCount to 1"
+ "rebuildWithProgress:checkCancellationIntervalInMilliseconds:shouldCancel:completionHandler:"
+ "setCompletedUnitCount:"
+ "setObject:atIndexedSubscript:"
+ "setPerVectorAttribute:"
+ "setTotalUnitCount:"
+ "timerTask cancelled"
+ "tokenizerDataPointer"
+ "totalUnitCount"
+ "unicode61"
+ "unicode61WrapperCreate: Begin"
+ "unicode61WrapperCreate: Finish"
+ "unicode61WrapperCreate: Malformed pCtx"
+ "unicode61WrapperDelete: Begin"
+ "unicode61WrapperDelete: End"
+ "unicode61WrapperTokenizerDataReference"
+ "v48@0:8@\"NSProgress\"16Q24@?<B@?>32@?<v@?@\"NSError\">40"
+ "v48@0:8@16Q24@?32@?40"
- "    ALTER TABLE attributes_temp RENAME TO attributes"
- "    DROP TABLE attributes"
- "    DROP TABLE attributes_fts"
- "    INNER JOIN attributes ON attributes.asset_id = "
- " and extended error code: "
- " and extendedErrorCode: "
- " with error code: "
- "\". Delta count did not any statistics."
- ")\nON CONFLICT(asset_id) DO UPDATE SET "
- ", and extended error code: "
- ", with error code: "
- ". Error message "
- ". Error message: "
- "Add previous indices"
- "Can't construct Array with count < 0"
- "Constructing new index table"
- "Create intermediate tables and indices"
- "Determining new partitions"
- "Failed to close database connection with error code: %d. Error message: %s"
- "Failed to get prepared statement for expression "
- "Failed to get prepared statement for expression DELETE FROM observations WHERE observationid = ?"
- "Failed to get prepared statement for expression begin immediate"
- "Failed to get prepared statement for expression rollback"
- "Insufficient space allocated to copy string contents"
- "Internal error in fts5_tokenizer.xCreate: "
- "Internal error in xFindTokenizer: "
- "Internal error: nil tokenizer"
- "Internal failure during xTokenizer: "
- "SELECT fts5(?)"
- "SQLExpressionEvaluator: Failed to reset statement with error code: %d. Error message: %s"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Switching from old to new index table"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_TtC12VectorSearchP33_F6F6291BE4184B60FBC77E314B7DB2C923FTS5RegisteredTokenizer"
- "_TtC12VectorSearchP33_F6F6291BE4184B60FBC77E314B7DB2C924FTS5TokenizerConstructor"
- "constructor"
- "db"
- "dbPath"
- "invalid Collection: less than 'count' elements in collection"
- "nil fts5_tokenizer.xCreate"
- "tokenizerPointer"
- "xTokenizer"

```
