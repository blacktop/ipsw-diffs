## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory`

```diff

-  __TEXT.__text: 0x1bcbc4
-  __TEXT.__objc_methlist: 0x38b4
-  __TEXT.__const: 0x1e670
-  __TEXT.__cstring: 0x4236
-  __TEXT.__oslogstring: 0x6049
-  __TEXT.__gcc_except_tab: 0x7c8
+  __TEXT.__text: 0x1bd1a0
+  __TEXT.__objc_methlist: 0x39e4
+  __TEXT.__const: 0x1e6b0
+  __TEXT.__cstring: 0x4266
+  __TEXT.__oslogstring: 0x63d9
+  __TEXT.__gcc_except_tab: 0x7dc
   __TEXT.__dlopen_cstrs: 0xe3
-  __TEXT.__swift5_typeref: 0x5257
-  __TEXT.__swift5_reflstr: 0x700e
-  __TEXT.__swift5_assocty: 0x1be0
-  __TEXT.__swift5_fieldmd: 0x59b4
   __TEXT.__constg_swiftt: 0x114cc
+  __TEXT.__swift5_typeref: 0x524b
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_protos: 0x28
+  __TEXT.__swift5_reflstr: 0x700e
+  __TEXT.__swift5_fieldmd: 0x59b4
+  __TEXT.__swift5_assocty: 0x1be0
   __TEXT.__swift5_proto: 0xe0c
   __TEXT.__swift5_types: 0x440
+  __TEXT.__swift5_protos: 0x28
   __TEXT.__swift_as_entry: 0xdc
   __TEXT.__swift_as_ret: 0xc8
   __TEXT.__swift_as_cont: 0x104
   __TEXT.__swift5_capture: 0x3e0
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6568
-  __TEXT.__eh_frame: 0x7930
+  __TEXT.__unwind_info: 0x6580
+  __TEXT.__eh_frame: 0x78f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x970
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__const: 0x990
+  __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2540
+  __DATA_CONST.__objc_selrefs: 0x25b0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__got: 0x9e0
+  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__got: 0x9e8
   __AUTH_CONST.__const: 0x5c48
-  __AUTH_CONST.__cfstring: 0x3740
-  __AUTH_CONST.__objc_const: 0x14648
+  __AUTH_CONST.__cfstring: 0x3760
+  __AUTH_CONST.__objc_const: 0x14af8
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x11c8
-  __AUTH.__objc_data: 0x1bb0
-  __AUTH.__data: 0x14e18
-  __DATA.__objc_ivar: 0x2b4
-  __DATA.__data: 0x4540
-  __DATA.__bss: 0x1ccb0
-  __DATA.__common: 0xc8
-  __DATA_DIRTY.__objc_data: 0xf00
-  __DATA_DIRTY.__data: 0x508
-  __DATA_DIRTY.__bss: 0x1ce0
-  __DATA_DIRTY.__common: 0x50
+  __AUTH_CONST.__auth_got: 0x11c0
+  __AUTH.__objc_data: 0x1b88
+  __AUTH.__data: 0x1228
+  __DATA.__objc_ivar: 0x2c0
+  __DATA.__data: 0x3e28
+  __DATA.__bss: 0x1cc20
+  __DATA.__common: 0xc0
+  __DATA_DIRTY.__objc_data: 0xf78
+  __DATA_DIRTY.__data: 0x14868
+  __DATA_DIRTY.__bss: 0x1d70
+  __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12341
-  Symbols:   6359
-  CStrings:  1503
+  Functions: 12376
+  Symbols:   6426
+  CStrings:  1521
 
Sections:
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
Symbols:
+ +[CHPersistentStoreDescription persistentStoreDescriptionWithURL:processHandle:error:]
+ +[DBManager persistentStoreOptionsWithURL:isEncrypted:error:]
+ -[CHDefaultDatabaseOperations .cxx_destruct]
+ -[CHDefaultDatabaseOperations addStoreAtURL:isEncrypted:]
+ -[CHDefaultDatabaseOperations createManagedObjectContext]
+ -[CHDefaultDatabaseOperations databaseVersionAtURL:]
+ -[CHDefaultDatabaseOperations dbManager]
+ -[CHDefaultDatabaseOperations destroyStoreAtURL:modelURL:]
+ -[CHDefaultDatabaseOperations initWithDBManager:]
+ -[CHDefaultDatabaseOperations migrateStoreAtURL:destinationModelProvider:isEncrypted:]
+ -[CHDefaultDatabaseOperations moveStoreFromURL:toURL:modelURL:]
+ -[CHDefaultDatabaseOperations storeInitializationStatusAtURL:modelURL:]
+ -[CallDBManagerClient _createDatabaseIsPermanent:afterSyncHelperDidSucceed:]
+ -[CallDBManagerClient _createDatabaseIsPermanent:atLocation:shouldRetry:shouldSetChangeReason:]
+ -[CallDBManagerClient _didValidateDatabaseIsPermanent:atLocation:]
+ -[CallDBManagerClient helperConnectionFactory]
+ -[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:]
+ -[CallDBManagerClient setHelperConnectionFactory:]
+ -[CallDBManagerServer databaseOperations]
+ -[CallDBManagerServer initWithDeviceObserver:databaseOperations:metaInfoProvider:]
+ CHCallStatusToINInteractionDirection
+ CHRecentCallMediaTypeToINCallCapability
+ GCC_except_table11
+ GCC_except_table25
+ OBJC_IVAR_$_CHDefaultDatabaseOperations._dbManager
+ OBJC_IVAR_$_CallDBManagerClient._helperConnectionFactory
+ OBJC_IVAR_$_CallDBManagerServer._databaseOperations
+ _OBJC_CLASS_$_CHDefaultDatabaseOperations
+ _OBJC_CLASS_$_NSError
+ _OBJC_METACLASS_$_CHDefaultDatabaseOperations
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_INSTANCE_METHODS_CHDefaultDatabaseOperations
+ __OBJC_$_INSTANCE_VARIABLES_CHDefaultDatabaseOperations
+ __OBJC_$_PROP_LIST_CHDefaultDatabaseOperations
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CHDatabaseOperations
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CHDatabaseOperations
+ __OBJC_$_PROTOCOL_REFS_CHDatabaseOperations
+ __OBJC_CLASS_PROTOCOLS_$_CHDefaultDatabaseOperations
+ __OBJC_CLASS_RO_$_CHDefaultDatabaseOperations
+ __OBJC_LABEL_PROTOCOL_$_CHDatabaseOperations
+ __OBJC_METACLASS_RO_$_CHDefaultDatabaseOperations
+ __OBJC_PROTOCOL_$_CHDatabaseOperations
+ ___111-[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:]_block_invoke
+ ___111-[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:]_block_invoke_2
+ ___block_descriptor_32_e22_"NSXPCConnection"8?0l
+ _objc_msgSend$_createDatabaseIsPermanent:afterSyncHelperDidSucceed:
+ _objc_msgSend$_createDatabaseIsPermanent:atLocation:shouldRetry:shouldSetChangeReason:
+ _objc_msgSend$_didValidateDatabaseIsPermanent:atLocation:
+ _objc_msgSend$addStoreAtURL:isEncrypted:
+ _objc_msgSend$databaseOperations
+ _objc_msgSend$databaseVersionAtURL:
+ _objc_msgSend$destroyStoreAtURL:modelURL:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$helperConnectionFactory
+ _objc_msgSend$initWithDeviceObserver:databaseOperations:metaInfoProvider:
+ _objc_msgSend$initWithProcessHandle:metaInfoProvider:databaseLocationProvider:helperConnectionFactory:
+ _objc_msgSend$migrateStoreAtURL:destinationModelProvider:isEncrypted:
+ _objc_msgSend$moveStoreFromURL:toURL:modelURL:
+ _objc_msgSend$persistentStoreDescriptionWithURL:processHandle:error:
+ _objc_msgSend$persistentStoreOptionsWithURL:isEncrypted:error:
+ _objc_msgSend$storeInitializationStatusAtURL:modelURL:
- +[CHPersistentStoreDescription persistentStoreDescriptionWithURL:]
- +[DBManager persistentStoreOptionsWithURL:isEncrypted:]
- -[CallDBManagerClient _createDatabaseIsPermanent:]
- -[CallDBManagerServer initWithDeviceObserver:metaInfoProvider:]
- GCC_except_table21
- ___45-[CallDBManagerClient initWithProcessHandle:]_block_invoke
- ___87-[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:]_block_invoke
- _objc_msgSend$_createDatabaseIsPermanent:
- _objc_msgSend$initWithDeviceObserver:metaInfoProvider:
- _objc_msgSend$persistentStoreDescriptionWithURL:
- _objc_msgSend$persistentStoreOptionsWithURL:isEncrypted:
- _swift_runtimeSupportsNoncopyableTypes
- get_type_metadata 15Synchronization5MutexVy11CallHistory17ContainerProviderC5State33_83E8AB6B1A11CF80BE371E18A1212E57LLOG noncopyable
- get_type_metadata 15Synchronization5MutexVy11CallHistory17ContainerProviderCG noncopyable
CStrings:
+ "145.100.7"
+ "145.100.7~143"
+ "@\"NSXPCConnection\"8@?0"
+ "Built persistent store description with URL %{public}@"
+ "Call History access requires data store access entitlement %@ or %@."
+ "Call History access requires data vault entitlement %@"
+ "Data store (permanent:%{public}i) metadata valid but database validation failed with code %{public}@"
+ "Database (permanent:%{public}i) file doesn't exist"
+ "Database (permanent:%{public}i) validation failed"
+ "Failed to get persistent store options for destination data store, with error %{public}@"
+ "Failed to get persistent store options for source data store: %{public}@, with error %{public}@"
+ "Failed to get persistent store options to add data store, with error %{public}@"
+ "Failed to send transactions to XPC service: %{public}@"
+ "File at path %{public}@ has version %{public}li, not %{public}li"
+ "File at path %{public}@ is not readable"
+ "Initializing permanent data store"
+ "Initializing temporary data store"
+ "No model provided for DB destroy operation; creating a new NSPersistentStoreCoordinator"
+ "No model provided for DB move; creating a new NSPersistentStoreCoordinator"
+ "Not attempting to create helper connection because we're missing the %@ and %@ entitlements (one is required)"
+ "Not initializing permanent data store"
+ "Not initializing temporary data store"
+ "Poking sync helper for data store (permanent:%{public}i)"
+ "Will not poke sync helper for data store (permanent:%{public}i); client lacks sufficient access"
+ "com.apple.private.CallHistory"
- "143.100.11.1.1"
- "143.100.11.1.1~5"
- "Call History access requires boolean entitlement %@ or %@. This will be a hard error in the future."
- "Database (permanent:%{public}i) file doesn't exist; poking sync helper. Error code: %{public}@"
- "Database (permanent:%{public}i) metadata valid but data store check failed with code: %{public}@; poking sync helper"
- "Database (permanent:%{public}i) validation failed, poking sync helper"
- "Failed to send transactions to XPC service"
- "File at path: %{public}@ is not readable"

```
