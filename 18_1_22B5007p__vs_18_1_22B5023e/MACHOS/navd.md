## navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

-2859.30.7.3.5
-  __TEXT.__text: 0x56e84
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_stubs: 0x8c80
-  __TEXT.__objc_methlist: 0x2c4c
+2864.31.7.31.2
+  __TEXT.__text: 0x57330
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_stubs: 0x8f20
+  __TEXT.__objc_methlist: 0x2c64
   __TEXT.__const: 0x270
-  __TEXT.__objc_methname: 0x9aa0
-  __TEXT.__cstring: 0x683e
-  __TEXT.__oslogstring: 0x5fff
+  __TEXT.__objc_methname: 0x9cdc
+  __TEXT.__cstring: 0x685d
+  __TEXT.__oslogstring: 0x60c4
   __TEXT.__objc_classname: 0xc81
   __TEXT.__objc_methtype: 0x236b
   __TEXT.__gcc_except_tab: 0x6254
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__unwind_info: 0x18c8
-  __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0x7c0
+  __DATA_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__got: 0x778
   __DATA_CONST.__const: 0x3a30
-  __DATA_CONST.__cfstring: 0x3720
+  __DATA_CONST.__cfstring: 0x37a0
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x190

   __DATA_CONST.__objc_doubleobj: 0x200
   __DATA_CONST.__objc_floatobj: 0x30
   __DATA.__objc_const: 0x87e8
-  __DATA.__objc_selrefs: 0x2740
+  __DATA.__objc_selrefs: 0x27e8
   __DATA.__objc_ivar: 0x50c
   __DATA.__objc_data: 0x16d0
   __DATA.__data: 0x1860

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1376
-  Symbols:   455
-  CStrings:  3382
+  Functions: 1377
+  Symbols:   440
+  CStrings:  3409
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_NETWORK_DOWNLOAD_SIZE
- _XPC_ACTIVITY_NETWORK_UPLOAD_SIZE
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_INEXPENSIVE_NETWORK_CONNECTIVITY
- _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
- _XPC_ACTIVITY_SHOULD_WAKE_DEVICE
- _xpc_activity_register
- _xpc_activity_unregister
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
CStrings:
+ "Failed to submit background system task with error: %!@(MISSING)"
+ "Failed to submit task with error: %!@(MISSING)"
+ "Registering Location Background Task triggered (timer: (%!f(MISSING)), graceperiod: (%!f(MISSING)), delay: (%!f(MISSING))"
+ "Unable to cancel the location use task request."
+ "Unable to cancel the stale location use task request."
+ "Unknown"
+ "cancelTaskRequestWithIdentifier:error:"
+ "deregisterBackgroundTasks"
+ "deregisterTaskWithIdentifier:"
+ "hardwareIdentifier"
+ "initWithIdentifier:"
+ "registerBackgroundTasks"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "setClientCapabilitiesHardwareIdentifier:"
+ "setDefaultTraitsHardwareIdentifier:"
+ "setNetworkDownloadSize:"
+ "setNetworkUploadSize:"
+ "setPriority:"
+ "setRequiresExternalPower:"
+ "setRequiresInexpensiveNetworkConnectivity:"
+ "setRequiresNetworkConnectivity:"
+ "setScheduleAfter:"
+ "setShouldWakeDevice:"
+ "setTaskCompleted"
+ "setTrySchedulingBefore:"
+ "sharedScheduler"
+ "submitTaskRequest:error:"
+ "v16@?0@\"BGSystemTask\"8"
- "Registering Location XPC activity triggered (timer: (%!f(MISSING)), graceperiod: (%!f(MISSING)), delay: (%!f(MISSING))"

```
