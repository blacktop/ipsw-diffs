## medialibraryd

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd`

```diff

-4024.300.23.0.0
-  __TEXT.__text: 0x17ea4
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_stubs: 0x3120
-  __TEXT.__objc_methlist: 0xc34
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x1aa3
-  __TEXT.__oslogstring: 0x2852
-  __TEXT.__objc_methname: 0x44d5
+4024.500.21.0.0
+  __TEXT.__text: 0x18684
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__objc_stubs: 0x3300
+  __TEXT.__objc_methlist: 0x143c
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x17a3
+  __TEXT.__oslogstring: 0x2aeb
+  __TEXT.__objc_methname: 0x4689
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x106
   __TEXT.__swift5_reflstr: 0x15

   __TEXT.__swift5_types: 0x4
   __TEXT.__objc_classname: 0x3c9
   __TEXT.__objc_methtype: 0xe69
-  __TEXT.__gcc_except_tab: 0x6f4
-  __TEXT.__unwind_info: 0x6d8
-  __DATA_CONST.__auth_got: 0x5d8
-  __DATA_CONST.__got: 0x438
+  __TEXT.__gcc_except_tab: 0x6f8
+  __TEXT.__unwind_info: 0x6e8
+  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__got: 0x418
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xed0
-  __DATA_CONST.__cfstring: 0x1220
+  __DATA_CONST.__const: 0xf68
+  __DATA_CONST.__cfstring: 0x1240
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x3270
-  __DATA.__objc_selrefs: 0xf30
-  __DATA.__objc_ivar: 0x138
+  __DATA_CONST.__objc_dictobj: 0xc8
+  __DATA.__objc_const: 0x23c0
+  __DATA.__objc_selrefs: 0x1208
+  __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x580
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x38

   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/MusicKit.framework/MusicKit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MediaLibraryCore.framework/MediaLibraryCore

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 466
-  Symbols:   363
-  CStrings:  1267
+  Functions: 477
+  Symbols:   353
+  CStrings:  1284
 
Symbols:
+ _ML3IsProcessRunning
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _dispatch_activate
+ _objc_retain_x10
+ _xpc_transaction_exit_clean
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
- __swift_FORCE_LOAD_$_swiftFileProvider
- _xpc_activity_register
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
CStrings:
+ "\x05\x1f\x03"
+ "%{public}@ Failed to cancel existing task. err=%{public}@"
+ "%{public}@ Failed to set up maintenance task handler"
+ "%{public}@ Failed to submit new task. err=%{public}@"
+ "%{public}@ Have existing task scheduled - no need to register a new one"
+ "%{public}@ Performing maintenance task"
+ "%{public}@ Registering new background task"
+ "%{public}@ Setting up maintenance task"
+ "*** Received termination signal. Canceling operations and preparing for shutdown..."
+ "Handling SIGTERM event"
+ "Handling SIGUSR1 event"
+ "Setting up signal handlers"
+ "[Maintenance] Synchronous maintenance activity triggered."
+ "[Maintenance] Synchronous maintenance operation complete. Performing artwork reconciliation."
+ "_debugSignalDispatchSource"
+ "_handleTerminationSignal"
+ "_performMaintenanceOnDatabaseAtPath:"
+ "_setupSignalHandlers"
+ "_tearDownSignalHandlers"
+ "_terminateSignalDispatchSource"
+ "cancelActiveTransactionForClient:"
+ "cancelDatabaseOperationsForClient:completion:"
+ "cancelTaskRequestWithIdentifier:error:"
+ "com.apple.CascadeSets.DonateNow"
+ "com.apple.datamigrator"
+ "initWithIdentifier:"
+ "interval"
+ "performMaintenanceTasksForDatabaseAtPath:"
+ "priority"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "requiresUserInactivity"
+ "setInterval:"
+ "setPriority:"
+ "setRequiresUserInactivity:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "submitTaskRequest:error:"
+ "taskRequestForIdentifier:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v32@?0@8Q16^B24"
+ "waitUntilFinished"
- "\x05\x1f\x01"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Spotlight indexing isn't supported on this platform"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "_platformSupportsSiriIndexing"
- "_platformSupportsSpotlightIndexing"
- "_setupSignalHandler"
- "_tearDownSignalHandler"
- "cancelActiveTransationAndDatabaseOperationsForClient:"
- "com.apple.siri.koa.donate"
- "invalid Collection: less than 'count' elements in collection"

```
