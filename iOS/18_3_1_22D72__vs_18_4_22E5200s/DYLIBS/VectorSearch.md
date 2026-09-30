## VectorSearch

> `/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch`

```diff

-33.0.0.0.0
-  __TEXT.__text: 0x61830
-  __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x83c
-  __TEXT.__const: 0x1e58
-  __TEXT.__cstring: 0x4433
-  __TEXT.__constg_swiftt: 0xec0
-  __TEXT.__swift5_typeref: 0xebc
+37.0.0.0.0
+  __TEXT.__text: 0x62344
+  __TEXT.__auth_stubs: 0x1bd0
+  __TEXT.__objc_methlist: 0x8d4
+  __TEXT.__const: 0x2708
+  __TEXT.__cstring: 0x42e5
+  __TEXT.__constg_swiftt: 0xf90
+  __TEXT.__swift5_typeref: 0x1020
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xae5
-  __TEXT.__swift5_fieldmd: 0xc78
-  __TEXT.__swift5_types: 0xe0
-  __TEXT.__swift5_capture: 0x4e8
+  __TEXT.__swift5_reflstr: 0xb55
+  __TEXT.__swift5_fieldmd: 0xcec
+  __TEXT.__swift5_types: 0xe8
+  __TEXT.__swift5_capture: 0x588
+  __TEXT.__oslogstring: 0xd44
   __TEXT.__swift5_proto: 0x184
-  __TEXT.__oslogstring: 0xb84
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0x1508
-  __TEXT.__eh_frame: 0x35b8
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0x1560
+  __TEXT.__eh_frame: 0x3f20
   __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methname: 0x16dd
-  __TEXT.__objc_methtype: 0x4c0
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __TEXT.__objc_methname: 0x196c
+  __TEXT.__objc_methtype: 0x4d6
+  __TEXT.__objc_stubs: 0x8e0
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c8
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xd68
-  __AUTH_CONST.__auth_ptr: 0x480
-  __AUTH_CONST.__const: 0x1d68
-  __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x19e0
+  __AUTH_CONST.__auth_got: 0xdf0
+  __AUTH_CONST.__auth_ptr: 0x458
+  __AUTH_CONST.__const: 0x20b8
+  __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__objc_const: 0x1b30
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x340
-  __AUTH.__data: 0x248
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x550
-  __DATA.__bss: 0x1680
-  __DATA_DIRTY.__objc_data: 0x7f8
-  __DATA_DIRTY.__data: 0x1128
-  __DATA_DIRTY.__bss: 0x1300
-  __DATA_DIRTY.__common: 0x70
+  __AUTH.__objc_data: 0x2c8
+  __AUTH.__data: 0x188
+  __DATA.__objc_ivar: 0x64
+  __DATA.__data: 0x368
+  __DATA.__bss: 0x1480
+  __DATA_DIRTY.__objc_data: 0x928
+  __DATA_DIRTY.__data: 0x15c8
+  __DATA_DIRTY.__bss: 0x1500
+  __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1687
-  Symbols:   239
-  CStrings:  629
+  Functions: 1650
+  Symbols:   258
+  CStrings:  653
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSProgress
+ _VSKErrorDomainName
+ __Block_copy
+ __Block_release
+ _ceilf
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
- _swift_initStructMetadata
CStrings:
+ "\x05"
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
+ ", error message from DB: "
+ "@56@0:8@16@24@32@40@48"
+ "Async rebuild called"
+ "Cannot filter on attributes when no filterable attributes are defined."
+ "Could not create error message"
+ "Explicitly cancelling rebuild."
+ "FTS is disabled. Returning from rebuildFTSIndex."
+ "Failed to close database connection with error code: %d"
+ "Failed to reset statement"
+ "INNER JOIN attributes ON "
+ "INNER JOIN attributes_fts ON "
+ "Internal error in xFindTokenizer"
+ "Invalid or corrupted DB file "
+ "No error message"
+ "Rebuild not cancelled. Running for %f seconds. Checking again in %llu seconds"
+ "SELECT COUNT(DISTINCT(attributes.asset_id)) FROM attributes"
+ "SELECT id FROM observations WHERE observationid = ?"
+ "SQLExpressionEvaluator: Failed to reset statement with error code: %d"
+ "T@\"NSArray\",C,N,V_perVectorAttribute"
+ "Unrecoverable error due to invliad or corrupted DB: "
+ "VectorDatabase"
+ "VectorDatabaseConfig:migrate no-op for %s migration"
+ "VectorDatabaseConfig:migrate no-op for .perVectorAttribute migration"
+ "VectorSearch/SQLObjects.swift"
+ "_TtC12VectorSearch18SQLDatabasePointer"
+ "_TtC12VectorSearch20SQLPreparedStatement"
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
+ "totalUnitCount"
+ "v48@0:8@\"NSProgress\"16Q24@?<B@?>32@?<v@?@\"NSError\">40"
+ "v48@0:8@16Q24@?32@?40"
- "\x04"
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
- "Failed to get prepared statement for expression "
- "Failed to get prepared statement for expression DELETE FROM observations WHERE observationid = ?"
- "Failed to get prepared statement for expression begin immediate"
- "Failed to get prepared statement for expression rollback"
- "Insufficient space allocated to copy string contents"
- "Internal error in xFindTokenizer: "
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
- "dbPath"
- "invalid Collection: less than 'count' elements in collection"

```
