## signpost_reporter

> `/usr/libexec/signpost_reporter`

```diff

-174.8.0.0.0
-  __TEXT.__text: 0xb534
+197.0.0.0.0
+  __TEXT.__text: 0xa988
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0x1740
+  __TEXT.__objc_stubs: 0x1780
   __TEXT.__objc_methlist: 0x62c
-  __TEXT.__const: 0xfa
-  __TEXT.__objc_methname: 0x1a23
-  __TEXT.__cstring: 0x1316
-  __TEXT.__objc_classname: 0x18a
+  __TEXT.__const: 0x10a
+  __TEXT.__objc_methname: 0x1a63
+  __TEXT.__cstring: 0x1216
+  __TEXT.__objc_classname: 0x17f
   __TEXT.__objc_methtype: 0x244
-  __TEXT.__oslogstring: 0xc4f
-  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__oslogstring: 0x99d
+  __TEXT.__gcc_except_tab: 0x34c
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_reflstr: 0x60
   __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2f8
-  __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x6a0
+  __TEXT.__unwind_info: 0x308
+  __DATA_CONST.__const: 0x6c0
   __DATA_CONST.__cfstring: 0x16c0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
+  __DATA_CONST.__auth_got: 0x478
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x10e8
-  __DATA.__objc_selrefs: 0x620
+  __DATA.__objc_selrefs: 0x638
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x510
   __DATA.__data: 0x1c8
-  __DATA.__bss: 0x150
+  __DATA.__bss: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 534E7DBD-EB69-3C36-BC07-A77C16AD0BED
-  Functions: 266
+  UUID: 89A83117-6A66-3EEC-938B-8E5EE6CC482D
+  Functions: 265
   Symbols:   205
-  CStrings:  777
+  CStrings:  761
 
Symbols:
+ _OBJC_CLASS_$_BGSystemTask
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_retain_x2
+ _swift_retain_x20
- _OBJC_CLASS_$_AnalyticsConfigurationObserver
- _XPC_ACTIVITY_CHECK_IN
- __dispatch_source_type_timer
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_source_set_timer
- _dispatch_time
- _os_transaction_create
- _os_variant_has_internal_diagnostics
- _swift_retain
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_state
- _xpc_activity_should_defer
CStrings:
+ "Asked to run in environment without `BGSystemTask`. Bailing..."
+ "Finishing up due to task being %{public}s"
+ "Registering for background task '%{public}@'\n"
+ "Reporting based on being a customer seed build."
+ "deferred"
+ "done"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "setExpirationHandler:"
+ "setFormatOptions:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "stringFromDate:"
+ "v16@?0@\"BGSystemTask\"8"
+ "visionOS"
- "%{public}s to mark activity as done due to %{public}s."
- "Able"
- "Checking in\n"
- "Deferral not requested, continuing."
- "Deferred signpost_reporter\n"
- "Not reporting based on not being tasked-on by CoreAnalytics ('%@' is false)"
- "Not reporting based on not being tasked-on by CoreAnalytics (Non-NSDictionary configuration object)"
- "Not reporting based on not being tasked-on by CoreAnalytics (Timeout waiting for config)"
- "Not reporting based on not being tasked-on by CoreAnalytics (nil configuration object)"
- "Not reporting based on not being tasked-on by CoreAnalytics (unexpected type string: '%@')"
- "Not reporting since is not tasked-on by CoreAnalytics (nil value for %@ key)"
- "Not reporting since not tasked-on by CoreAnalytics (Wrong value class for class for %@)"
- "Reporting based on being tasked-on by CoreAnalytics"
- "Reporting based on os_variant result"
- "TaskedOn"
- "Trying to stop in-flight reporting work."
- "Unable"
- "Unknown state %ld\n"
- "boolValue"
- "com.apple.performance.signpost_reporter_tasking"
- "com.apple.signpost"
- "com.apple.signpost.signpost_reporter_activity transaction"
- "completion"
- "deferral"
- "setConfigurationObserverDelegate:queue:"
- "signpost_reporter configuration observing queue"
- "signpost_reporter defer polling queue"
- "startObservingConfigurationType:"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "v24@?0@\"NSObject\"8@\"NSString\"16"

```
