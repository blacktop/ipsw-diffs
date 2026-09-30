## DADaemonSupport

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport`

```diff

-2691.2.2.0.0
-  __TEXT.__text: 0x37f9c
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x2574
-  __TEXT.__const: 0x112
-  __TEXT.__gcc_except_tab: 0x844
-  __TEXT.__oslogstring: 0x6463
-  __TEXT.__cstring: 0x13bb
-  __TEXT.__unwind_info: 0xb38
-  __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x6f5
-  __TEXT.__objc_methname: 0x7e2a
-  __TEXT.__objc_methtype: 0x1203
-  __TEXT.__objc_stubs: 0x6be0
-  __DATA_CONST.__got: 0xb40
-  __DATA_CONST.__const: 0x8a8
+2691.4.5.0.0
+  __TEXT.__text: 0x3b360
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x25c4
+  __TEXT.__const: 0x132
+  __TEXT.__gcc_except_tab: 0x7ec
+  __TEXT.__oslogstring: 0x65b0
+  __TEXT.__cstring: 0x140b
+  __TEXT.__unwind_info: 0xca0
+  __TEXT.__objc_classname: 0x6fa
+  __TEXT.__objc_methname: 0x8088
+  __TEXT.__objc_methtype: 0x1221
+  __TEXT.__objc_stubs: 0x6ec0
+  __DATA_CONST.__got: 0xb50
+  __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fb0
+  __DATA_CONST.__objc_selrefs: 0x2058
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0x5b20
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__objc_const: 0x5b70
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x290
+  __DATA.__objc_ivar: 0x298
   __DATA.__data: 0x8a8
   __DATA.__bss: 0x74
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x7e
   __DATA_DIRTY.__common: 0x14
   - /AppleInternal/Library/Frameworks/CalDAVServerSimulator.framework/CalDAVServerSimulator
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CalDAV.framework/CalDAV
   - /System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 81BB86AD-D0E5-3C7B-B363-251468664FA8
-  Functions: 941
-  Symbols:   4033
-  CStrings:  2135
+  UUID: 88019924-AF9B-3EB2-8A82-2BFC1A370797
+  Functions: 954
+  Symbols:   4084
+  CStrings:  2170
 
Symbols:
+ -[DARefreshManager _cancelPushRefresh]
+ -[DARefreshManager _nextPushRegistrationRefreshDeadline]
+ -[DARefreshManager _reschedulePushRefresh]
+ -[DARefreshManager _schedulePushRefreshWithDeadline:]
+ -[DARefreshManager handlePushRefreshTask:]
+ -[DARefreshManager wrapperPushRegistrationFinished:]
+ -[DARefreshWrapper pushRefreshInterval]
+ -[DARefreshWrapper setWrapperDelegate:]
+ -[DARefreshWrapper wrapperDelegate]
+ GCC_except_table22
+ GCC_except_table43
+ GCC_except_table44
+ _BGSystemTaskSchedulerErrorDomain
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_IVAR_$_DARefreshManager._pushRefreshSchedulingStateLock
+ _OBJC_IVAR_$_DARefreshManager._scheduledPushRefreshTime
+ _OBJC_IVAR_$_DARefreshWrapper._wrapperDelegate
+ _OUTLINED_FUNCTION_2
+ ___33+[DARefreshManager sharedManager]_block_invoke_2
+ ___42-[DARefreshManager handlePushRefreshTask:]_block_invoke
+ ___51-[DARefreshWrapper startFetchActivityWithInterval:]_block_invoke.23
+ ___52-[DARefreshManager wrapperPushRegistrationFinished:]_block_invoke
+ ___56-[DARefreshManager startDailyRefreshActivityForWrapper:]_block_invoke.68
+ ___block_descriptor_32_e34_v16?0"BGNonRepeatingSystemTask"8l
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.5
+ ___block_literal_global.58
+ _objc_msgSend$_cancelPushRefresh
+ _objc_msgSend$_nextPushRegistrationRefreshDeadline
+ _objc_msgSend$_reschedulePushRefresh
+ _objc_msgSend$_schedulePushRefreshWithDeadline:
+ _objc_msgSend$cancelTaskRequestWithIdentifier:error:
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$handlePushRefreshTask:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$isBeforeDate:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$pushRefreshInterval
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$scheduleAfter
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setRequiresNetworkConnectivity:
+ _objc_msgSend$setScheduleAfter:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTrySchedulingBefore:
+ _objc_msgSend$setWrapperDelegate:
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$trySchedulingBefore
+ _objc_msgSend$wrapperPushRegistrationFinished:
- -[DARefreshManager setTokenRegistrationTimer:]
- -[DARefreshManager tokenRegistrationTimer]
- GCC_except_table34
- GCC_except_table35
- _OBJC_CLASS_$_NSThread
- _OBJC_IVAR_$_DARefreshManager._tokenRegistrationTimer
- ___51-[DARefreshWrapper startFetchActivityWithInterval:]_block_invoke.21
- ___56-[DARefreshManager startDailyRefreshActivityForWrapper:]_block_invoke.61
- ___63-[DARefreshWrapper tokenRegistrationRequest:finishedWithError:]_block_invoke
- ___87-[DATokenRegistrationRequest URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke
- _arc4random
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$isMainThread
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "@\"<DARefreshWrapperDelegate>\""
+ "B32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "Canceled push refresh task"
+ "Checking APS registration"
+ "Failed to cancel push refresh task with error: %@"
+ "Failed to schedule push refresh task for %@ with error: %@"
+ "Next push refresh date already scheduled: %@"
+ "Next push refresh date needs to be updated from: %@ to %@"
+ "No existing push refresh task to cancel"
+ "Push registration refresh task fired"
+ "Scheduling push registration refresh to happen after %f seconds and before %f seconds from now"
+ "Successfully scheduled push registration refresh for %@"
+ "T@\"<DARefreshWrapperDelegate>\",W,N,V_wrapperDelegate"
+ "Td,R,N"
+ "_cancelPushRefresh"
+ "_nextPushRegistrationRefreshDeadline"
+ "_pushRefreshSchedulingStateLock"
+ "_reschedulePushRefresh"
+ "_schedulePushRefreshWithDeadline:"
+ "_scheduledPushRefreshTime"
+ "_wrapperDelegate"
+ "cancelTaskRequestWithIdentifier:error:"
+ "com.apple.dataaccess.dataaccessd.PushRefresh"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "handlePushRefreshTask:"
+ "initWithIdentifier:"
+ "isBeforeDate:"
+ "pushRefreshInterval"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "scheduleAfter"
+ "setPriority:"
+ "setRequiresNetworkConnectivity:"
+ "setScheduleAfter:"
+ "setTaskCompleted"
+ "setTrySchedulingBefore:"
+ "setWrapperDelegate:"
+ "sharedScheduler"
+ "submitTaskRequest:error:"
+ "trySchedulingBefore"
+ "v16@?0@\"BGNonRepeatingSystemTask\"8"
+ "wrapperDelegate"
+ "wrapperPushRegistrationFinished:"
- "3"
- "APS token timer set outside main thread. Timer needs to be run on main thread. Push notification may be missed."
- "B32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
- "T@\"NSTimer\",&,N,V_tokenRegistrationTimer"
- "Timer fired. Re-registering everything with APS"
- "_tokenRegistrationTimer"
- "isMainThread"
- "setTokenRegistrationTimer:"
- "tokenRegistrationTimer"

```
