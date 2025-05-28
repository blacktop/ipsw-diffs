## mediasetupd

> `/usr/libexec/mediasetupd`

```diff

-207.30.3.0.0
-  __TEXT.__text: 0x318c4
-  __TEXT.__auth_stubs: 0x740
+207.40.20.0.0
+  __TEXT.__text: 0x315a4
+  __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x4b00
-  __TEXT.__objc_methlist: 0x1648
-  __TEXT.__cstring: 0x2372
-  __TEXT.__oslogstring: 0x5885
-  __TEXT.__objc_methname: 0x68f3
+  __TEXT.__objc_methlist: 0x1640
+  __TEXT.__cstring: 0x23e4
+  __TEXT.__oslogstring: 0x571f
+  __TEXT.__objc_methname: 0x6967
   __TEXT.__objc_classname: 0x33b
   __TEXT.__objc_methtype: 0x11d2
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x844
-  __TEXT.__unwind_info: 0xa9c
-  __DATA_CONST.__auth_got: 0x3b0
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0x2018
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x874
+  __TEXT.__unwind_info: 0xaa4
+  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x2038
   __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x370
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x4168
+  __DATA.__objc_const: 0x41a8
   __DATA.__objc_selrefs: 0x1700
-  __DATA.__objc_classrefs: 0x370
-  __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x150
+  __DATA.__objc_ivar: 0x154
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x4e0
   __DATA.__bss: 0xe0

   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CloudMediaServicesInterfaceKit.framework/CloudMediaServicesInterfaceKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1003
-  Symbols:   301
-  CStrings:  1940
+  Functions: 997
+  Symbols:   288
+  CStrings:  1939
 
Symbols:
+ _OBJC_CLASS_$_BGSystemTaskScheduler
- _OBJC_CLASS_$_MSDefaultServiceChangedEvent
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _kBackgroundActivityPublicDatabaseRefreshTaskIdentifier
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_state
- _xpc_activity_should_defer
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
CStrings:
+ "\x12!"
+ "-[MSDPublicDBManager _syncDataWithCloudKitWithCompletion:]"
+ "Failed to expire publicDB refresh task: %@"
+ "Scheduling background task for publicDB refreshes"
+ "T@\"NSString\",?,R,C"
+ "Unknown reason"
+ "_publicDBRefreshQueue"
+ "_syncDataWithCloudKitWithCompletion:"
+ "com.apple.mediasetup.publicdb-refresh-queue"
+ "com.apple.mediasetupd.publicDBRefresh"
+ "home:didUpdateSupportsResidentActionSetStateEvaluation:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "setExpirationHandler:"
+ "setTaskCompleted"
+ "setTaskExpiredWithRetryAfter:error:"
+ "sharedScheduler"
+ "v16@?0@\"BGRepeatingSystemTask\"8"
- "\x11!"
- "-[MSDPublicDBManager _syncDataWithCloudKitRefreshTask:completion:]"
- "Beginning scheduled background sync with public db"
- "Deferring activity: %@ deferred: %@"
- "Failed setting activity state to Defer"
- "Failed setting activity state to continue"
- "Failed setting activity state to done"
- "No"
- "Successfully updated default media service %{private}@"
- "Yes"
- "[Public] Error from Background Activity Scheduler, Requested task should be deferred"
- "[Public] Error from Background Activity Scheduler, XPC Activity state is not XPC_ACTIVITY_STATE_CONTINUE"
- "_getXPCActivityCriteria"
- "_syncDataWithCloudKitRefreshTask:completion:"
- "configuration"
- "initWithOldServiceID:newServiceID:"
- "sendDefaultServiceChangedEvent:"
- "setXPCActivity:"

```
