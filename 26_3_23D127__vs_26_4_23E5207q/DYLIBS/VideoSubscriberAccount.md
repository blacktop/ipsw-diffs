## VideoSubscriberAccount

> `/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount`

```diff

-593.30.1.0.0
-  __TEXT.__text: 0xd621c
-  __TEXT.__auth_stubs: 0x1480
+593.40.5.0.0
+  __TEXT.__text: 0xf1720
+  __TEXT.__auth_stubs: 0x1410
   __TEXT.__objc_methlist: 0x88cc
-  __TEXT.__const: 0x110e0
-  __TEXT.__cstring: 0x9e96
-  __TEXT.__oslogstring: 0x5caa
-  __TEXT.__gcc_except_tab: 0x1650
+  __TEXT.__const: 0x11230
+  __TEXT.__cstring: 0x9c7a
+  __TEXT.__oslogstring: 0x610a
+  __TEXT.__gcc_except_tab: 0x1664
   __TEXT.__ustring: 0x178
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__swift5_typeref: 0x480
+  __TEXT.__swift5_typeref: 0x48c
   __TEXT.__swift5_reflstr: 0x4dd
   __TEXT.__swift5_assocty: 0x1f8
   __TEXT.__constg_swiftt: 0x444

   __TEXT.__swift5_types: 0x7c
   __TEXT.__swift_as_entry: 0xb0
   __TEXT.__swift_as_ret: 0xb4
-  __TEXT.__swift5_capture: 0x1a4
+  __TEXT.__swift5_capture: 0x190
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2b70
-  __TEXT.__eh_frame: 0xe40
-  __TEXT.__objc_classname: 0x1364
-  __TEXT.__objc_methname: 0x122f9
-  __TEXT.__objc_methtype: 0x1eb9
-  __TEXT.__objc_stubs: 0xbc80
-  __DATA_CONST.__got: 0x9d8
-  __DATA_CONST.__const: 0x26e8
+  __TEXT.__unwind_info: 0x3000
+  __TEXT.__eh_frame: 0xdf0
+  __TEXT.__objc_classname: 0x1416
+  __TEXT.__objc_methname: 0x1236c
+  __TEXT.__objc_methtype: 0x2034
+  __TEXT.__objc_stubs: 0xbfa0
+  __DATA_CONST.__got: 0x9c0
+  __DATA_CONST.__const: 0x26e0
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4030
+  __DATA_CONST.__objc_selrefs: 0x4060
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0xa50
-  __AUTH_CONST.__const: 0x7df8
-  __AUTH_CONST.__cfstring: 0x82a0
+  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__const: 0x83f0
+  __AUTH_CONST.__cfstring: 0x82c0
   __AUTH_CONST.__objc_const: 0x165e8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x340
   __AUTH.__data: 0x180
   __DATA.__objc_ivar: 0x910
-  __DATA.__data: 0x1348
+  __DATA.__data: 0x15d8
   __DATA.__bss: 0x1e60
-  __DATA.__common: 0xa38
+  __DATA.__common: 0xab8
   __DATA_DIRTY.__objc_data: 0x3250
   __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E72B113E-607C-3A02-9F06-490D775D8008
-  Functions: 4403
-  Symbols:   12178
-  CStrings:  6364
+  UUID: 5574B00B-9830-3296-A564-91533DB2CCF5
+  Functions: 4394
+  Symbols:   12358
+  CStrings:  6393
 
Symbols:
+ -[VSUserAccountPersistentContainer configureDescriptonInMemory:].cold.1
+ -[VSUserAccountPersistentContainer configureDescriptonInMemory:].cold.2
+ -[VSUserAccountPersistentContainer configureDescriptonInMemory:].cold.3
+ -[VSUserAccountPersistentContainer configureDescriptonInMemory:].cold.4
+ -[VSUserAccountPersistentContainer configureDescriptonInMemory:].cold.5
+ -[VSUserAccountPersistentContainer configureDescriptonInMemory:].cold.6
+ -[VSUserAccountPersistentContainer initInMemory:].cold.1
+ -[VSUserAccountPersistentContainer initInMemory:].cold.2
+ -[VSUserAccountPersistentContainer initInMemory:].cold.3
+ -[VSUserAccountPersistentContainer initInMemory:].cold.4
+ -[VSUserAccountPersistentContainer initInMemory:].cold.5
+ -[VSUserAccountPersistentContainer initInMemory:].cold.6
+ -[VSUserAccountPersistentContainer initInMemory:].cold.7
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _mmap
+ _munmap
+ _objc_msgSend$ams_sharedAccountStoreForMediaType:
+ _objc_msgSend$ams_storefront
+ _objc_msgSend$authorization
+ _objc_msgSend$bundlePath
+ _objc_msgSend$configurations
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$deleteAutoSignInTokenWithCompletionHandler:
+ _objc_msgSend$enqueueEvents:
+ _objc_msgSend$entities
+ _objc_msgSend$firstAccountWithCompletionHandler:
+ _objc_msgSend$flush
+ _objc_msgSend$flushMetrics
+ _objc_msgSend$initWithBundleID:
+ _objc_msgSend$initWithContainerID:bag:
+ _objc_msgSend$initWithUnderlyingDictionary:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$queryAutoSignInTokenWithCompletionHandler:
+ _objc_msgSend$requestAutoSignInAuthorizationWithCompletionHandler:
+ _objc_msgSend$setCheckDiagnosticsAndUsageSetting:
+ _objc_msgSend$setEventType:
+ _objc_msgSend$setTopic:
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$updateAutoSignInToken:updateContext:completionHandler:
+ _objc_msgSend$userAgentForProcessInfo:
+ _objectdestroy.25Tm
+ _sched_yield
+ _swift_bridgeObjectRelease_n
+ _symbolic _____Sg_ABt 10Foundation3URLV
+ _sysconf
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_VideoSubscriberAccount
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x11
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
- _objectdestroy.24Tm
- _objectdestroy.3Tm
CStrings:
+ "Bundle contains %lu resources"
+ "Container name: %@ managedObjectModel available: %@"
+ "Core Data model loaded but contains no entities!"
+ "Core Data model path found: %@"
+ "Created fallback description for empty array, new count: %lu"
+ "Created fallback description, new count: %lu"
+ "Failed to create any persistent store description after fallback attempts"
+ "Failed to initialize NSPersistentContainer with name:%@"
+ "Failed to load Core Data model from framework bundle!"
+ "Initial persistentStoreDescriptions count: %lu"
+ "Loaded managedObjectModel with %lu entities"
+ "Model entity count: %lu configuration count: %lu"
+ "NSPersistentContainer superclass failed to create store descriptions!"
+ "Still no valid description after fallback creation attempts!"
+ "Successfully initialized NSPersistentContainer with name:%@"
+ "This indicates the superclass initialization didn't complete properly."
+ "Using persistent store description successfully"
+ "VSUserAccountPersistentContainer configureDescriptonInMemory - inMemory:%@ count:%lu"
+ "VSUserAccountPersistentContainer init - modelName:%@ frameworkBundle available:%@"
+ "VSUserAccountPersistentContainer init on main thread: %@"
+ "bundlePath"
+ "configurations"
+ "contentsOfDirectoryAtPath:error:"
+ "entities"
+ "mom"
+ "momd"
+ "numberWithInt:"
+ "pathForResource:ofType:"
+ "persistentStoreDescriptions is empty!"
+ "persistentStoreDescriptions is nil!"
- "The [[self persistentStoreDescriptions] firstObject] parameter must not be nil."
- "The model parameter must not be nil."

```
