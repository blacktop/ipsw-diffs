## CoreData

> `/System/Library/Frameworks/CoreData.framework/CoreData`

```diff

-1509.1.0.0.0
-  __TEXT.__text: 0x2b4880
-  __TEXT.__auth_stubs: 0x25b0
+1510.0.0.0.0
+  __TEXT.__text: 0x2b4fe8
+  __TEXT.__auth_stubs: 0x25f0
   __TEXT.__objc_methlist: 0xf928
   __TEXT.__const: 0x13f8
-  __TEXT.__cstring: 0x36675
+  __TEXT.__cstring: 0x36761
   __TEXT.__swift5_typeref: 0x4ce
   __TEXT.__swift5_capture: 0x25c
   __TEXT.__constg_swiftt: 0x414

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x171e4
-  __TEXT.__oslogstring: 0x3214b
-  __TEXT.__unwind_info: 0x6650
+  __TEXT.__gcc_except_tab: 0x1729c
+  __TEXT.__oslogstring: 0x3235d
+  __TEXT.__unwind_info: 0x6660
   __TEXT.__eh_frame: 0x808
   __TEXT.__objc_classname: 0x33ea
-  __TEXT.__objc_methname: 0x1b03f
+  __TEXT.__objc_methname: 0x1b05c
   __TEXT.__objc_methtype: 0x461f
   __TEXT.__objc_stubs: 0x127a0
   __DATA_CONST.__got: 0x900
-  __DATA_CONST.__const: 0x45d0
+  __DATA_CONST.__const: 0x45b0
   __DATA_CONST.__objc_classlist: 0xe20
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x110

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb48
   __DATA_CONST.__objc_arraydata: 0x70f8
-  __AUTH_CONST.__auth_got: 0x12e8
+  __AUTH_CONST.__auth_got: 0x1308
   __AUTH_CONST.__const: 0x1800
-  __AUTH_CONST.__cfstring: 0x1e040
-  __AUTH_CONST.__objc_const: 0x23d70
+  __AUTH_CONST.__cfstring: 0x1e060
+  __AUTH_CONST.__objc_const: 0x23d90
   __AUTH_CONST.__objc_dictobj: 0x20d0
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_arrayobj: 0x7980
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2e90
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0x171c
+  __DATA.__objc_ivar: 0x1720
   __DATA.__data: 0x1029
   __DATA.__bss: 0xb49
   __DATA.__common: 0x5d0

   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3EA3A7AA-04D5-3088-980B-082BA7C7445F
-  Functions: 8144
-  Symbols:   26128
-  CStrings:  17295
+  UUID: CEBC1599-60F1-3A11-84D7-2BCC75E40E46
+  Functions: 8146
+  Symbols:   26130
+  CStrings:  17305
 
Symbols:
+ -[NSSQLiteConnection _walCheckpointWithMode:]
+ GCC_except_table126
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table178
+ GCC_except_table184
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table204
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table227
+ GCC_except_table229
+ GCC_except_table35
+ GCC_except_table68
+ GCC_except_table80
+ GCC_except_table88
+ _.str.1064
+ _.str.341
+ _.str.342
+ _.str.552
+ _.str.73
+ _OBJC_IVAR_$_NSSQLCore._checkpointSerializationLock
+ __NSSQLiteConnectionWalHook
+ __PFClassFromString
+ ___64-[NSSQLiteConnection writeCorrelationMasterReordersFromTracker:]_block_invoke.383
+ ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.483
+ ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.490
+ ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.542
+ ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.544
+ ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.401
+ ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.408
+ ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.417
+ ___block_literal_global.125
+ ___block_literal_global.138
+ ___block_literal_global.140
+ ___block_literal_global.344
+ ___block_literal_global.410
+ ___block_literal_global.61
+ ___block_literal_global.735
+ ___block_literal_global.75
+ _clock_gettime_nsec_np
+ _os_unfair_lock_trylock
+ _qos_class_self
+ _sqlite3_wal_hook
- -[NSSQLiteConnection _walCheckpoint]
- GCC_except_table124
- GCC_except_table129
- GCC_except_table136
- GCC_except_table148
- GCC_except_table154
- GCC_except_table166
- GCC_except_table167
- GCC_except_table170
- GCC_except_table175
- GCC_except_table177
- GCC_except_table185
- GCC_except_table187
- GCC_except_table190
- GCC_except_table193
- GCC_except_table196
- GCC_except_table202
- GCC_except_table205
- GCC_except_table208
- GCC_except_table210
- GCC_except_table212
- GCC_except_table226
- GCC_except_table228
- GCC_except_table87
- GCC_except_table96
- _.str.1061
- _.str.338
- _.str.339
- _.str.551
- _.str.71
- ___64-[NSSQLiteConnection writeCorrelationMasterReordersFromTracker:]_block_invoke.381
- ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.482
- ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.489
- ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.541
- ___65-[NSPersistentStoreCoordinator executeRequest:withContext:error:]_block_invoke.543
- ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.400
- ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.407
- ___91-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]_block_invoke.416
- ___block_literal_global.122
- ___block_literal_global.129
- ___block_literal_global.137
- ___block_literal_global.341
- ___block_literal_global.409
- ___block_literal_global.58
- ___block_literal_global.72
- ___block_literal_global.734
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CoreData
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CoreData
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CoreData
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CoreData
CStrings:
+ "CoreData: error: Deprecated option '%@' is no longer supported and the symbol will be removed in a future release. Please adopt %@ instead.\n"
+ "CoreData: error: WAL checkpoint: Checkpoint took %llu ms. Requested QoS: %d. Log size: %d checkpointed: %d\n"
+ "CoreData: error: sqlite3_db_config for SQLITE_DBCONFIG_ENABLE_ATTACH_CREATE failed: %d\n"
+ "CoreData: error: sqlite3_db_config for SQLITE_DBCONFIG_ENABLE_COMMENTS failed: %d\n"
+ "CoreData: warning: WAL checkpoint: Checkpoint took %llu ms. Requested QoS: %d. Log size: %d checkpointed: %d\n"
+ "WAL checkpoint: Checkpoint took %llu ms. Requested QoS: %d. Log size: %d checkpointed: %d"
+ "_checkpointSerializationLock"
+ "sqlite3_db_config for SQLITE_DBCONFIG_ENABLE_ATTACH_CREATE failed: %d"
+ "sqlite3_db_config for SQLITE_DBCONFIG_ENABLE_COMMENTS failed: %d"

```
