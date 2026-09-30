## mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0xb30c
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x1e60
-  __TEXT.__objc_methlist: 0xaa4
+800.14.111.0.0
+  __TEXT.__text: 0xb5d0
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0x20e0
+  __TEXT.__objc_methlist: 0xaec
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__objc_methname: 0x2fb2
-  __TEXT.__oslogstring: 0xf28
-  __TEXT.__cstring: 0x556
+  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__objc_methname: 0x319f
+  __TEXT.__oslogstring: 0xe67
+  __TEXT.__cstring: 0x51d
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methtype: 0xf30
-  __TEXT.__unwind_info: 0x250
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x410
+  __TEXT.__objc_methtype: 0xf28
+  __TEXT.__unwind_info: 0x260
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__cfstring: 0x460
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA.__objc_const: 0xb80
-  __DATA.__objc_selrefs: 0xba0
+  __DATA.__objc_selrefs: 0xc40
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x3c0

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
-  - /System/Library/PrivateFrameworks/BackgroundTaskAgent.framework/BackgroundTaskAgent
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MediaStream.framework/MediaStream

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7662D8A1-70A6-394A-A9AB-F5DBBE4009EB
-  Functions: 171
-  Symbols:   284
-  CStrings:  689
+  UUID: 94891DD1-B427-3060-9674-B0E8C4048441
+  Functions: 178
+  Symbols:   265
+  CStrings:  705
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
- _BackgroundTaskAgentAddJob
- _BackgroundTaskAgentCopyJob
- _BackgroundTaskAgentInit
- _BackgroundTaskAgentRemoveJob
- _kBackgroundTaskAgentAllowedDuringRoaming
- _kBackgroundTaskAgentCellularAllowed
- _kBackgroundTaskAgentJobExpired
- _kBackgroundTaskAgentJobStatus
- _kBackgroundTaskAgentJobWindowEndTime
- _kBackgroundTaskAgentJobWindowStartTime
- _kBackgroundTaskAgentNetworkRequired
- _kBackgroundTaskAgentPowerPluggedinTime
- _kBackgroundTaskAgentRequiredBatteryLevel
- _objc_retain_x25
- _strcmp
- _xpc_dictionary_create
- _xpc_dictionary_get_bool
- _xpc_dictionary_get_double
- _xpc_dictionary_get_int64
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_double
CStrings:
+ "@32@0:8@16@24"
+ "BGST request failed: %@"
+ "Deregistering task %s"
+ "_scheduleNextBTAJobNextActivityDate:serviceName:"
+ "addAccessControlEntries:toAlbumWithGUID:personID:info:completionBlock:"
+ "deregisterPluggedInTask"
+ "deregisterTaskWithIdentifier:"
+ "deregisterWakeupTask"
+ "handlePluggedInTask:"
+ "handleWakeupTask:"
+ "initWithIdentifier:"
+ "now"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "schedulePluggedInTask"
+ "scheduleWakeupTaskAfter:"
+ "setRandomInitialDelay:"
+ "setRequiresExternalPower:"
+ "setRequiresInexpensiveNetworkConnectivity:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresUnconstrainedNetworkConnectivity:"
+ "setResourceIntensive:"
+ "setScheduleAfter:"
+ "setTaskCompleted"
+ "setTrySchedulingBefore:"
+ "sharedScheduler"
+ "stringWithUTF8String:"
+ "submitTaskRequest:error:"
+ "taskRequestForIdentifier:"
+ "v16@?0@\"BGSystemTask\"8"
- "...ignoring."
- "@\"NSObject<OS_xpc_object>\"16@?0@\"NSDate\"8"
- "@48@0:8@16r*24@32@?40"
- "Background task agent could not schedule the next Shared Photo Stream task."
- "Background task agent sent Shared Photo Stream event status: %llu..."
- "Got notification for job %s"
- "No more scheduled jobs for %{public}@. Unscheduling."
- "_scheduleNextBTAJobNextActivityDate:jobName:serviceName:createJobBlock:"
- "addAccessControlEntries:toAlbumWithGUID:personID:info:"
- "compare:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "timeIntervalSinceReferenceDate"
- "v24@?0r*8@\"NSObject<OS_xpc_object>\"16"

```
