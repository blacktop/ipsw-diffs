## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks`

```diff

-1770.0.0.0.6
-  __TEXT.__text: 0x10130
+1781.0.0.0.5
+  __TEXT.__text: 0x108cc
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0xd5c
+  __TEXT.__objc_methlist: 0xd84
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x86c
-  __TEXT.__oslogstring: 0x196e
+  __TEXT.__cstring: 0x83e
+  __TEXT.__oslogstring: 0x1b16
   __TEXT.__gcc_except_tab: 0x474
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__unwind_info: 0x418
   __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methname: 0x307e
+  __TEXT.__objc_methname: 0x313d
   __TEXT.__objc_methtype: 0x3e9
-  __TEXT.__objc_stubs: 0x1dc0
-  __DATA_CONST.__got: 0x110
+  __TEXT.__objc_stubs: 0x1de0
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x948
+  __DATA_CONST.__objc_selrefs: 0x960
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x2098
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__cfstring: 0xac0
+  __AUTH_CONST.__objc_const: 0x20c8
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x188
+  __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x180
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/Versions/A/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 443
-  Symbols:   1088
-  CStrings:  105
+  Functions: 449
+  Symbols:   1099
+  CStrings:  104
 
Symbols:
+ -[BGSystemTask hasPropagatedExpiration]
+ -[BGSystemTask invokeExpirationHandlerWithReason:]
+ -[BGSystemTask invokeExpirationHandlerWithReason:].cold.1
+ -[BGSystemTask setHasPropagatedExpiration:]
+ -[BGSystemTaskScheduler pendingTaskRegistrationsMap]
+ -[BGSystemTaskScheduler setPendingTaskRegistrationsMap:]
+ GCC_except_table17
+ GCC_except_table21
+ GCC_except_table25
+ GCC_except_table29
+ OBJC_IVAR_$_BGSystemTask._hasPropagatedExpiration
+ OBJC_IVAR_$_BGSystemTaskScheduler._pendingTaskRegistrationsMap
+ __48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.88
+ __48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.88.cold.1
+ __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.104
+ __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.105
+ __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.94
+ __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.94.cold.1
+ __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.98
+ __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.98.cold.1
+ __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.99
+ __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.99.cold.1
+ __49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.84
+ __49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.84.cold.1
+ __49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.86
+ __49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.86.cold.1
+ __50-[BGSystemTaskScheduler installEventStreamHandler]_block_invoke.76
+ __54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.106
+ __63-[BGSystemTaskScheduler cancelTaskRequestWithIdentifier:error:]_block_invoke.87
+ __63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.cold.2
+ __71-[BGSystemTaskScheduler validateTaskIdentifier:resultProduction:error:]_block_invoke.115
+ __72-[BGSystemTaskScheduler validateTaskIdentifier:resultConsumption:error:]_block_invoke.119
+ __74-[BGSystemTaskScheduler resetResultsForIdentifier:byTaskIdentifier:error:]_block_invoke.120
+ ___37-[BGSystemTask setExpirationHandler:]_block_invoke
+ ___47-[BGSystemTask setExpirationHandlerWithReason:]_block_invoke
+ _kDASSystemContextGPWorkloadRunningState
+ _kDASSystemContextMCWorkloadRunningState
+ _kDASSystemContextNonDASCriticalWorkloadRunning
+ _objc_msgSend$invokeExpirationHandlerWithReason:
+ _objc_msgSend$pendingTaskRegistrationsMap
- -[BGSystemTaskScheduler expireTaskWithRegistration:withReason:].cold.2
- -[BGSystemTaskScheduler pendingTasksMap]
- -[BGSystemTaskScheduler setPendingTasksMap:]
- GCC_except_table16
- GCC_except_table20
- GCC_except_table24
- GCC_except_table28
- GCC_except_table36
- OBJC_IVAR_$_BGSystemTaskScheduler._pendingTasksMap
- __48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.86
- __48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.86.cold.1
- __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.102
- __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.103
- __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.92
- __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.92.cold.1
- __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.96
- __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.96.cold.1
- __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.97
- __49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.97.cold.1
- __49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.82
- __49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.82.cold.1
- __49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.84
- __49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.84.cold.1
- __50-[BGSystemTaskScheduler installEventStreamHandler]_block_invoke.74
- __54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.104
- __63-[BGSystemTaskScheduler cancelTaskRequestWithIdentifier:error:]_block_invoke.85
- __71-[BGSystemTaskScheduler validateTaskIdentifier:resultProduction:error:]_block_invoke.113
- __72-[BGSystemTaskScheduler validateTaskIdentifier:resultConsumption:error:]_block_invoke.117
- __74-[BGSystemTaskScheduler resetResultsForIdentifier:byTaskIdentifier:error:]_block_invoke.118
- _objc_msgSend$pendingTasksMap
CStrings:
- "_DASSystemContextNonDASCritialWorkloadRunning"

```
