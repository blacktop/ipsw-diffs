## UnblockService

> `/System/Library/PrivateFrameworks/UnblockService.framework/UnblockService`

```diff

-10.0.0.0.0
-  __TEXT.__text: 0xba48
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x3b8
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0xd8
-  __TEXT.__cstring: 0x4b0
-  __TEXT.__oslogstring: 0x1908
-  __TEXT.__unwind_info: 0x1d8
+12.0.0.0.0
+  __TEXT.__text: 0xbe54
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x3c8
+  __TEXT.__const: 0xd0
+  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__cstring: 0x4b1
+  __TEXT.__oslogstring: 0x1948
+  __TEXT.__unwind_info: 0x1e8
   __TEXT.__objc_classname: 0xbd
-  __TEXT.__objc_methname: 0x152d
-  __TEXT.__objc_methtype: 0x2b2
+  __TEXT.__objc_methname: 0x159b
+  __TEXT.__objc_methtype: 0x2aa
   __TEXT.__objc_stubs: 0x1740
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x620
+  __DATA_CONST.__objc_selrefs: 0x628
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x318
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x380
-  __AUTH_CONST.__objc_const: 0x8f8
+  __AUTH_CONST.__objc_const: 0x908
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_ivar: 0x80

   - /System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A5A56BB-0621-3F85-A625-7A919D9CE426
-  Functions: 160
-  Symbols:   755
-  CStrings:  459
+  UUID: 67611CB7-30EB-32D1-B598-4141BF4CCA79
+  Functions: 157
+  Symbols:   768
+  CStrings:  461
 
Symbols:
+ -[UBUnblockReactiveRecovery dependencyChainForNode:processInfos:options:]
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:]
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:].cold.1
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:].cold.2
+ -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:].cold.3
+ -[UBUnblockReactiveRecovery processThreadInfosForDeadlock:processInfos:options:]
+ -[UBUnblockReactiveRecovery taskIs3PApp:options:]
+ -[UBUnblockReactiveRecovery taskIs3PApp:options:].cold.1
+ -[UBUnblockReactiveRecovery taskIs3PAppDict]
+ -[UBUnblockService(XPCHandling) handleIncomingMessage:].cold.3
+ GCC_except_table66
+ GCC_except_table67
+ ___117-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:]_block_invoke
+ ___117-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:]_block_invoke.195
+ ___49-[UBUnblockReactiveRecovery taskIs3PApp:options:]_block_invoke
+ ___block_descriptor_44_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_52_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s_e31_"UBProcessInfo"16?0"SATask"8ls32l8s40l8
+ ___block_literal_global.279
+ ___block_literal_global.282
+ ___kCFBooleanFalse
+ __dispatch_source_type_proc
+ __xpc_error_key_description
+ _dispatch_activate
+ _dispatch_get_global_queue
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$dependencyChainForNode:processInfos:options:
+ _objc_msgSend$fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:
+ _objc_msgSend$initWithPid:name:is3P:
+ _objc_msgSend$processThreadInfosForDeadlock:processInfos:options:
+ _objc_msgSend$setServiceProcessIs3P:
+ _objc_msgSend$taskIs3PApp:options:
+ _objc_msgSend$unarchivedArrayOfObjectsOfClass:fromData:error:
+ _objc_sync_enter
+ _objc_sync_exit
- -[UBUnblockReactiveRecovery dependencyChainForNode:processInfos:]
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:]
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:].cold.1
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:].cold.2
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:].cold.3
- -[UBUnblockReactiveRecovery processThreadInfosForDeadlock:processInfos:]
- -[UBUnblockReactiveRecovery taskIs3PApp:]
- -[UBUnblockReactiveRecovery taskIs3PApp:].cold.1
- -[UBUnblockReactiveRecovery taskIs3PApp:].cold.2
- -[UBUnblockReactiveRecovery taskIs3PApp:].cold.3
- _OBJC_CLASS_$_NSUUID
- _OUTLINED_FUNCTION_13
- ___109-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:]_block_invoke
- ___109-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:]_block_invoke.195
- ___55-[UBUnblockService(XPCHandling) openListenerConnection]_block_invoke.cold.2
- ___block_descriptor_40_e8_32s_e31_"UBProcessInfo"16?0"SATask"8ls32l8
- ___block_literal_global.277
- ___block_literal_global.280
- _objc_msgSend$dependencyChainForNode:processInfos:
- _objc_msgSend$fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:
- _objc_msgSend$initWithPid:name:
- _objc_msgSend$processThreadInfosForDeadlock:processInfos:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$taskIs3PApp:
- _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
CStrings:
+ "Candidate task %{public}@ [%d] is not eligible for termination"
+ "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Checking for threads blocked by thread exhaustion in last dependency %{public}@ [%d]."
+ "T@\"NSMutableDictionary\",R,V_taskIs3PAppDict"
+ "Thread Exhaustion in %@, blocking %lu tasks"
+ "Unblock service for [%d] received an error %s"
+ "Unblock service listener received an error %s"
+ "Unexpected request type received: %d."
+ "dependencyChainForNode:processInfos:options:"
+ "fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:options:"
+ "initWithPid:name:is3P:"
+ "processThreadInfosForDeadlock:processInfos:options:"
+ "setServiceProcessIs3P:"
+ "taskIs3PApp:options:"
+ "taskIs3PAppDict"
+ "unarchivedArrayOfObjectsOfClass:fromData:error:"
+ "v56@0:8@16@24@32@40Q48"
- "B24@0:8@16"
- "Candidate task %{public}@ [%d] is not eligble for termination"
- "Service <%{public}@ [%d] tid[%llx] time-elapsed[%fs]>: Checking for threads blocked by thread exhausion in last dependency %{public}@ [%d]."
- "Thread Exhausion in %@, blocking %lu tasks"
- "Unblock service received an error"
- "Unexpected request type received."
- "dependencyChainForNode:processInfos:"
- "fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:threadExhaustions:"
- "initWithPid:name:"
- "processThreadInfosForDeadlock:processInfos:"
- "setWithObjects:"
- "taskIs3PApp:"
- "unarchivedObjectOfClasses:fromData:error:"
- "v48@0:8@16@24@32@40"

```
