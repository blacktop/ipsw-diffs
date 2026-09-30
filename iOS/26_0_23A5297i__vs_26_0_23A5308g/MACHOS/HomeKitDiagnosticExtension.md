## HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

```diff

-1345.1.0.1.1
-  __TEXT.__text: 0x1be3c
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0x38e0
+1349.1.2.0.0
+  __TEXT.__text: 0x1c414
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_stubs: 0x3a40
   __TEXT.__objc_methlist: 0x1f54
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x57c
-  __TEXT.__cstring: 0x179a
+  __TEXT.__gcc_except_tab: 0x6b0
+  __TEXT.__cstring: 0x1a93
   __TEXT.__oslogstring: 0x14f4
-  __TEXT.__objc_methname: 0x3dab
+  __TEXT.__objc_methname: 0x3ecf
   __TEXT.__objc_classname: 0x882
   __TEXT.__objc_methtype: 0x629
-  __TEXT.__unwind_info: 0x760
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x3b0
+  __TEXT.__unwind_info: 0x758
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0x950
-  __DATA_CONST.__cfstring: 0x2040
+  __DATA_CONST.__cfstring: 0x2200
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x44d0
-  __DATA.__objc_selrefs: 0x1268
+  __DATA.__objc_selrefs: 0x12c0
   __DATA.__objc_ivar: 0x11c
   __DATA.__objc_data: 0x13b0
   __DATA.__data: 0x4e0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMemoryResourceException.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B20CABBD-3B52-3DAF-9630-A0E326E37942
-  Functions: 627
-  Symbols:   263
-  CStrings:  1567
+  UUID: C30B701D-09EC-34DF-AD61-A7D7CB830B95
+  Functions: 628
+  Symbols:   286
+  CStrings:  1614
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _NSPersistentHistoryTrackingKey
+ _NSReadOnlyPersistentStoreOption
+ _NSSQLiteStoreType
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSManagedObjectContext
+ _OBJC_CLASS_$_NSManagedObjectModel
+ _OBJC_CLASS_$_NSPersistentStoreCoordinator
+ ___assert_rtn
+ _compression_stream_destroy
+ _compression_stream_init
+ _compression_stream_process
+ _objc_exception_rethrow
+ _objc_terminate
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _printf
+ _sqlite3_close
+ _sqlite3_column_blob
+ _sqlite3_column_bytes
+ _sqlite3_column_type
+ _sqlite3_errmsg
+ _sqlite3_exec_b
+ _sqlite3_open
CStrings:
+ "%s\n"
+ "/Library/Managed Preferences/mobile/com.apple.homed.plist"
+ "Error Adding Store - %s at path %s \n"
+ "Error Decoding Model - %s \n"
+ "Error Fetching History - %s for store %s \n"
+ "HMKTDumpHistory.m"
+ "SELECT Z_CONTENT FROM Z_MODELCACHE"
+ "SQLITE_BLOB == sqlite3_column_type(stmt, 0)"
+ "Transaction (%lld): %@:%@:%@ at %@"
+ "Unable to open persistence store : %@ / %@\n"
+ "WakeOnLanV2Enabled"
+ "_allowDecodingCyclesInSecureMode"
+ "addPersistentStoreWithType:configuration:URL:options:error:"
+ "appendBytes:length:"
+ "cStringUsingEncoding:"
+ "compressed cached model has zero size(?!) \n"
+ "compressedModel == nil"
+ "compressedModelData_block_invoke"
+ "data"
+ "decompressed cached model is %llu bytes \n"
+ "error"
+ "failed to decompress cached model: %d \n"
+ "failed to exec `SELECT Z_CONTENT FROM Z_MODELCACHE`: %s \n"
+ "failed to initialize compression decoder: %d"
+ "failed to open \"%s\": %s \n"
+ "found cached model with compressed size: %llu \n"
+ "i16@?0^{sqlite3_stmt=}8"
+ "initForReadingFromData:error:"
+ "initWithConcurrencyType:"
+ "initWithManagedObjectModel:"
+ "nil model found after decompression: %@ / %@\n"
+ "root"
+ "setDecodingFailurePolicy:"
+ "setPersistentStoreCoordinator:"
+ "setRequiresSecureCoding:"
+ "setWithObject:"
+ "store does not contain a cached model \n"
+ "yyyy-MM-dd HH:mm:ss.SSSZ"
- "Failed to fetch persistent history: %@\n"
- "Transaction (%lld): %@:%@:%@ at %@\n"
- "setFetchBatchSize:"
- "setFetchLimit:"
- "yyyy-MM-dd HH:mm:ss.SSSZZZ"

```
