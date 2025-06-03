## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

```diff

-1439.0.4.0.2
-  __TEXT.__text: 0x5a2c
+1439.40.24.0.0
+  __TEXT.__text: 0x5b28
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x80c
+  __TEXT.__objc_methlist: 0x7e4
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x579
-  __TEXT.__oslogstring: 0x7a1
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__objc_classname: 0xee
-  __TEXT.__objc_methname: 0x1aac
-  __TEXT.__objc_methtype: 0x23e
+  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__cstring: 0x550
+  __TEXT.__oslogstring: 0x7ec
+  __TEXT.__unwind_info: 0x184
+  __TEXT.__objc_classname: 0xec
+  __TEXT.__objc_methname: 0x1ab4
+  __TEXT.__objc_methtype: 0x242
   __TEXT.__objc_stubs: 0x11c0
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__const: 0x218
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf20
-  __DATA_CONST.__objc_selrefs: 0x550
+  __DATA_CONST.__objc_const: 0xef0
+  __DATA_CONST.__objc_selrefs: 0x548
   __AUTH_CONST.__objc_const: 0x318
-  __AUTH_CONST.__cfstring: 0x7e0
+  __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__auth_got: 0x290
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_classrefs: 0x60
   __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0x108
+  __DATA.__objc_ivar: 0x104
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 213D4E05-0211-3A85-A68C-61CB2DF86B92
-  Functions: 213
-  Symbols:   826
-  CStrings:  523
+  UUID: 189DC29C-09C8-31FC-ABB0-87F88E54FD8F
+  Functions: 209
+  Symbols:   818
+  CStrings:  521
 
Symbols:
+ -[BGSystemTask expirationAckHandler]
+ -[BGSystemTask expiring]
+ -[BGSystemTask setExpirationAckHandler:]
+ -[BGSystemTask setExpiring:]
+ -[BGSystemTask setTaskExpiredWithRetryAfter:error:]
+ -[BGSystemTaskScheduler expireTaskWithRegistration:]
+ -[BGSystemTaskScheduler expireTaskWithRegistration:].cold.1
+ -[BGSystemTaskScheduler expireTaskWithRegistration:].cold.2
+ -[BGSystemTaskScheduler internalQueue]
+ -[BGSystemTaskScheduler setInternalQueue:]
+ GCC_except_table15
+ GCC_except_table21
+ GCC_except_table26
+ GCC_except_table3
+ GCC_except_table33
+ _OBJC_IVAR_$_BGSystemTask._expirationAckHandler
+ _OBJC_IVAR_$_BGSystemTask._expiring
+ _OBJC_IVAR_$_BGSystemTaskScheduler._internalQueue
+ ___32-[BGSystemTask setTaskCompleted]_block_invoke
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.62
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.63
+ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.56
+ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.56.cold.1
+ ___51-[BGSystemTask setTaskExpiredWithRetryAfter:error:]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e8_v12?0B8ls32l8s40l8s48l8r72l8s56l8s64l8r80l8
+ _objc_msgSend$completionHandler
+ _objc_msgSend$expireTaskWithRegistration:
+ _objc_msgSend$expiring
+ _objc_msgSend$internalQueue
+ _objc_msgSend$setExpirationAckHandler:
+ _objc_msgSend$setExpiring:
+ _objc_release_x28
+ _objc_retain_x25
+ _objc_retain_x26
- -[BGSystemTask lock]
- -[BGSystemTask setLock:]
- -[BGSystemTask setSuspending:]
- -[BGSystemTask suspendTaskForDuration:]
- -[BGSystemTask suspending]
- -[BGSystemTaskScheduler cleanupTaskObject:]
- -[BGSystemTaskScheduler queue]
- -[BGSystemTaskScheduler setQueue:]
- -[BGSystemTaskScheduler suspendTaskWithRegistration:]
- -[BGSystemTaskScheduler suspendTaskWithRegistration:].cold.1
- -[BGSystemTaskScheduler suspendTaskWithRegistration:].cold.2
- -[BGSystemTaskSchedulerRegistration expirationQueue]
- -[BGSystemTaskSchedulerRegistration setExpirationQueue:]
- GCC_except_table17
- GCC_except_table25
- GCC_except_table30
- GCC_except_table36
- GCC_except_table40
- _OBJC_IVAR_$_BGSystemTask._lock
- _OBJC_IVAR_$_BGSystemTask._suspending
- _OBJC_IVAR_$_BGSystemTaskScheduler._queue
- _OBJC_IVAR_$_BGSystemTaskSchedulerRegistration._expirationQueue
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.70
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke_2
- ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.64
- ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.64.cold.1
- ___53-[BGSystemTaskScheduler suspendTaskWithRegistration:]_block_invoke
- ___53-[BGSystemTaskScheduler suspendTaskWithRegistration:]_block_invoke.71
- ___53-[BGSystemTaskScheduler suspendTaskWithRegistration:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8w56l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e8_v12?0B8ls32l8s40l8s48l8r64l8s56l8r72l8
- _objc_msgSend$cleanupTaskObject:
- _objc_msgSend$expirationQueue
- _objc_msgSend$queue
- _objc_msgSend$setSuspending:
- _objc_msgSend$suspendTaskWithRegistration:
- _objc_msgSend$suspending
- _objc_retain_x9
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
CStrings:
+ "\x05"
+ "Acking task %{public}@ expired"
+ "B32@0:8d16^@24"
+ "Not expiring, task %{public}@ already finished"
+ "Received request to expire %@"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQueue"
+ "T@?,C,N,V_expirationAckHandler"
+ "TB,N,V_expiring"
+ "Unable to expire %{public}@ since it wasn't found running"
+ "_expirationAckHandler"
+ "_expiring"
+ "_internalQueue"
+ "com.apple.bg.system.task.internal.queue"
+ "expirationAckHandler"
+ "expireTaskWithRegistration:"
+ "expiring"
+ "internalQueue"
+ "setExpirationAckHandler:"
+ "setExpiring:"
+ "setInternalQueue:"
+ "setTaskExpiredWithRetryAfter:error:"
- "\x06"
- "\x14"
- "B24@0:8d16"
- "Received suspend request for %@"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_expirationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "TB,N,V_suspending"
- "Unable to suspend %{public}@ since it wasn't found running"
- "_expirationQueue"
- "_queue"
- "_suspending"
- "cleanupTaskObject:"
- "com.apple.BGSystemTaskScheduler.expirationQ.(%@)"
- "com.apple.bg.system.task.client"
- "expirationQueue"
- "queue"
- "setExpirationQueue:"
- "setQueue:"
- "setSuspending:"
- "suspendTaskForDuration:"
- "suspendTaskWithRegistration:"
- "suspending"

```
