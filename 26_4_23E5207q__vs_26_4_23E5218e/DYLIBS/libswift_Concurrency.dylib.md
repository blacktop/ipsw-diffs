## libswift_Concurrency.dylib

> `/usr/lib/swift/libswift_Concurrency.dylib`

```diff

-6.3.0.119.3
-  __TEXT.__text: 0x749bc
-  __TEXT.__auth_stubs: 0xfa0
+6.3.0.122.5
+  __TEXT.__text: 0x74ec4
+  __TEXT.__auth_stubs: 0xfe0
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x317a
   __TEXT.__cstring: 0x24a6
-  __TEXT.__oslogstring: 0x494
+  __TEXT.__oslogstring: 0x4ec
   __TEXT.__swift5_typeref: 0xc1d
   __TEXT.__swift5_capture: 0x240
   __TEXT.__swift5_reflstr: 0x2dc

   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH_CONST.__const: 0x2e40
   __AUTH_CONST.__objc_const: 0x810
   __AUTH.__data: 0xad0
   __DATA.__data: 0x108
   __DATA.__bss: 0x4460
-  __DATA.__common: 0x90
+  __DATA.__common: 0x88
   __DATA_DIRTY.__data: 0x4a0
   __DATA_DIRTY.__bss: 0x1a90
   __DATA_DIRTY.__common: 0x68

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/system/libdispatch.dylib
-  UUID: 826A8BF6-C657-3B20-B2EF-24D5CF02E297
-  Functions: 3110
-  Symbols:   8654
-  CStrings:  234
+  UUID: 67F0D859-6938-3CF8-A389-33FC15775C1A
+  Functions: 3111
+  Symbols:   8668
+  CStrings:  236
 
Symbols:
+ __ZN12_GLOBAL__N_116DefaultActorImpl23scheduleActorProcessJobEN5swift11JobPriorityENS1_15TaskExecutorRefE
+ __ZN5swift23swift_executor_escalateENS_17SerialExecutorRefEPNS_9AsyncTaskENS_11JobPriorityE.cold.1
+ __ZN5swift23swift_executor_escalateENS_17SerialExecutorRefEPNS_9AsyncTaskENS_11JobPriorityE.cold.2
+ __ZN5swift23swift_executor_escalateENS_17SerialExecutorRefEPNS_9AsyncTaskENS_11JobPriorityE.cold.3
+ __ZN5swift9AsyncTask14PrivateStorage8completeEPS0_
+ _dispatch_lock_override_end
+ _dispatch_lock_override_start_with_debounce
+ _dispatch_thread_get_current_override_qos_floor
+ _dispatch_thread_override_self
+ _swift_defaultActor_enqueue.cold.2
- __ZN5swift9AsyncTask20OpaquePrivateStorage8completeEPS0_
Functions:
~ __ZN5swift9AsyncTask26flagAsAndEnqueueOnExecutorENS_17SerialExecutorRefE : 376 -> 384
~ __ZN5swift15addStatusRecordEPNS_9AsyncTaskEPNS_16TaskStatusRecordERNS_16ActiveTaskStatusEN7__swift9__runtime4llvm12function_refIFbS4_S5_EEE : 328 -> 348
~ __ZN7__swift9__runtime4llvm12function_refIFbN5swift16ActiveTaskStatusERS4_EE11callback_fnIZNS3_9AsyncTask26flagAsAndEnqueueOnExecutorENS3_17SerialExecutorRefEEUlS4_S5_E0_EEblS4_S5_ : 28 -> 36
~ _swift_defaultActor_enqueue : 1188 -> 1392
+ __ZN12_GLOBAL__N_116DefaultActorImpl23scheduleActorProcessJobEN5swift11JobPriorityENS1_15TaskExecutorRefE
~ __ZN5swift18removeStatusRecordEPNS_9AsyncTaskEPNS_16TaskStatusRecordERNS_16ActiveTaskStatusEN7__swift9__runtime4llvm12function_refIFvS4_S5_EEE : 308 -> 320
~ __ZN5swift9AsyncTask13flagAsRunningEv : 444 -> 572
~ __ZN7__swift9__runtime4llvm12function_refIFvN5swift16ActiveTaskStatusERS4_EE11callback_fnIZNS3_9AsyncTask13flagAsRunningEvEUlS4_S5_E_EEvlS4_S5_ : 24 -> 136
~ __ZL23completeTaskWithClosurePN5swift12AsyncContextEPNS_10SwiftErrorE : 288 -> 128
~ __ZN12_GLOBAL__N_116DefaultActorImpl7tryLockEb : 484 -> 596
+ __ZN5swift9AsyncTask14PrivateStorage8completeEPS0_
~ __ZN12_GLOBAL__N_116DefaultActorImpl6unlockEb : 1000 -> 1044
~ __ZN12_GLOBAL__N_119ProcessOutOfLineJob7processEPN5swift3JobE : 1336 -> 1344
~ __ZL20withStatusRecordLockPN5swift9AsyncTaskENS_16ActiveTaskStatusEN7__swift9__runtime4llvm12function_refIFvS2_EEENS6_IFvS2_RS2_EEE : 516 -> 568
~ __ZN5swift9AsyncTask10waitFutureEPS0_PNS_12AsyncContextEPU14swiftasynccallFvU19swift_async_contextS3_ES3_PNS_11OpaqueValueE : 764 -> 780
~ __ZL23swift_task_escalateImplPN5swift9AsyncTaskENS_11JobPriorityE : 564 -> 600
~ __ZN7__swift9__runtime4llvm12function_refIFbN5swift16ActiveTaskStatusERS4_EE11callback_fnIZNS3_9AsyncTask15flagAsSuspendedEPNS3_26TaskDependencyStatusRecordEEUlS4_S5_E_EEblS4_S5_ : 60 -> 68
~ __ZL21swift_task_cancelImplPN5swift9AsyncTaskE : 252 -> 260
~ __ZN7__swift9__runtime4llvm12function_refIFvN5swift16ActiveTaskStatusERS4_EE11callback_fnIZNS3_9AsyncTask26flagAsAndEnqueueOnExecutorENS3_17SerialExecutorRefEEUlS4_S5_E_EEvlS4_S5_ : 20 -> 24
~ __ZL27swift_continuation_initImplPN5swift24ContinuationAsyncContextENS_22AsyncContinuationFlagsE : 688 -> 704
~ __ZL28swift_continuation_awaitImplPN5swift24ContinuationAsyncContextE : 604 -> 624
~ __ZN7__swift9__runtime4llvm12function_refIFvN5swift16ActiveTaskStatusERS4_EE11callback_fnIZNS3_23removeStatusRecordWhereEPNS3_9AsyncTaskES5_NS2_IFbS4_PNS3_16TaskStatusRecordEEEES7_E3$_1EEvlS4_S5_ : 56 -> 52
~ __ZN7__swift9__runtime4llvm12function_refIFbN5swift16ActiveTaskStatusERS4_EE11callback_fnIZL41swift_task_pushTaskExecutorPreferenceImplNS3_15TaskExecutorRefEE3$_0EEblS4_S5_ : 20 -> 24
~ __ZN7__swift9__runtime4llvm12function_refIFbN5swift16ActiveTaskStatusERS4_EE11callback_fnIZNS3_9AsyncTask33pushInitialTaskExecutorPreferenceENS3_15TaskExecutorRefEbE3$_0EEblS4_S5_ : 20 -> 24
~ __ZN7__swift9__runtime4llvm12function_refIFvN5swift16ActiveTaskStatusERS4_EE11callback_fnIZL40swift_task_popTaskExecutorPreferenceImplPNS3_34TaskExecutorPreferenceStatusRecordEE3$_1EEvlS4_S5_ : 32 -> 36
~ _swift_defaultActor_deallocate : 408 -> 412
~ __ZL12completeTaskPN5swift12AsyncContextEPNS_10SwiftErrorE : 288 -> 128
~ __ZN7__swift9__runtime4llvm12function_refIFvN5swift16ActiveTaskStatusERS4_EE11callback_fnIZNS3_18removeStatusRecordEPNS3_9AsyncTaskEPNS3_16TaskStatusRecordES5_S7_E3$_1EEvlS4_S5_ : 56 -> 52
~ __ZN5swift23swift_executor_escalateENS_17SerialExecutorRefEPNS_9AsyncTaskENS_11JobPriorityE : 556 -> 1472
~ __ZL38swift_taskGroup_wait_next_throwingImplPN5swift11OpaqueValueEPNS_12AsyncContextEPNS_9TaskGroupEPU14swiftasynccallFvU19swift_async_contextS3_U13swift_contextPvES3_ : 1268 -> 1284
~ __ZL27swift_taskGroup_waitAllImplPN5swift11OpaqueValueEPNS_12AsyncContextEPNS_9TaskGroupEPNS_10SwiftErrorEPU14swiftasynccallFvU19swift_async_contextS3_U13swift_contextPvES3_ : 1188 -> 1208
~ _swift_task_suspend : 240 -> 48
~ __ZL22swift_task_suspendImplv : 172 -> 188
~ __ZL22swift_task_suspendSlowRNSt3__16atomicImEEmPU9swiftcallFPN5swift9AsyncTaskEvE : 248 -> 104
~ __ZL18completeInlineTaskPN5swift12AsyncContextE : 288 -> 128
- __ZN5swift9AsyncTask20OpaquePrivateStorage8completeEPS0_
~ __ZN7__swift9__runtime4llvm12function_refIFvN5swift16ActiveTaskStatusERS4_EE11callback_fnIZNS3_15addStatusRecordEPNS3_9AsyncTaskEPNS3_16TaskStatusRecordES5_NS2_IFbS4_S5_EEEE3$_1EEvlS4_S5_ : 112 -> 108
~ __ZN5swift9AsyncTask26flagAsAndEnqueueOnExecutorENS_17SerialExecutorRefE.cold.1 : 144 -> 168
CStrings:
+ " enableTelemetry=YES actor=%p oldPriority=%zu newPriority=%zu"
+ "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "scheduled_actor_inversion"
- "/AppleInternal/Library/BuildRoots/4~CILGugD0WImLMQYmQMvVQZWHZ86o509UwWTYQAc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CILGugD0WImLMQYmQMvVQZWHZ86o509UwWTYQAc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"

```
