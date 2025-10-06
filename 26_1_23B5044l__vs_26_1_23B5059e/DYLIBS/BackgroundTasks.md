## BackgroundTasks

> `/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks`

```diff

-2109.40.8.0.0
-  __TEXT.__text: 0x937c
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0xbc0
+2109.40.11.502.1
+  __TEXT.__text: 0x9bb4
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_methlist: 0xcb8
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x65c
-  __TEXT.__oslogstring: 0x7e8
+  __TEXT.__cstring: 0x6c5
+  __TEXT.__oslogstring: 0x7a9
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__unwind_info: 0x2c0
-  __TEXT.__objc_classname: 0x1bd
-  __TEXT.__objc_methname: 0x1dea
-  __TEXT.__objc_methtype: 0x38f
-  __TEXT.__objc_stubs: 0x15a0
+  __TEXT.__unwind_info: 0x2f0
+  __TEXT.__objc_classname: 0x1d4
+  __TEXT.__objc_methname: 0x2070
+  __TEXT.__objc_methtype: 0x40c
+  __TEXT.__objc_stubs: 0x1720
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x248
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_nlclslist: 0x8
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x760
-  __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x238
+  __DATA_CONST.__objc_selrefs: 0x7c8
+  __DATA_CONST.__objc_superrefs: 0x80
+  __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x13e8
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xb4
+  __AUTH_CONST.__cfstring: 0x500
+  __AUTH_CONST.__objc_const: 0x15c0
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x188
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 800E77CF-F3A9-34D9-B89D-7EBFDF1A5117
-  Functions: 248
-  Symbols:   1001
-  CStrings:  517
+  UUID: EBCAFB54-85AD-3159-BB1F-9127BF17E5AF
+  Functions: 267
+  Symbols:   1069
+  CStrings:  549
 
Symbols:
+ +[_BGTaskExpirationRequest requestWithActivity:task:reason:]
+ -[BGContinuedProcessingTask _callExpirationHandlerWithReason:]
+ -[BGContinuedProcessingTask expirationHandlerWithReason]
+ -[BGContinuedProcessingTask expirationHandler]
+ -[BGContinuedProcessingTask setExpirationHandler:]
+ -[BGContinuedProcessingTask setExpirationHandler:].cold.1
+ -[BGContinuedProcessingTask setExpirationHandlerWithReason:]
+ -[BGContinuedProcessingTask setExpirationHandlerWithReason:].cold.1
+ -[BGTask _callExpirationHandlerWithReason:]
+ -[BGTask _callExpirationHandlerWithReason:].cold.1
+ -[BGTaskScheduler _unsafe_createExpirationRequestsForActivities:]
+ -[BGTaskScheduler _unsafe_taskForActivity:]
+ -[_BGContinuedProcessingTaskRequest initWithIdentifier:iconBundleIdentifier:onBehalfOf:linkToBundleIdentifier:]
+ -[_BGContinuedProcessingTaskRequest linkToBundleIdentifier]
+ -[_BGContinuedProcessingTaskRequest setLinkToBundleIdentifier:]
+ -[_BGTaskExpirationRequest .cxx_destruct]
+ -[_BGTaskExpirationRequest copyWithZone:]
+ -[_BGTaskExpirationRequest description]
+ -[_BGTaskExpirationRequest initWithActivity:task:reason:]
+ -[_BGTaskExpirationRequest reason]
+ -[_BGTaskExpirationRequest schedulerActivity]
+ -[_BGTaskExpirationRequest setReason:]
+ -[_BGTaskExpirationRequest task]
+ -[_DASActivity(BGTaskScheduler) bgTaskExpirationReason]
+ GCC_except_table24
+ GCC_except_table49
+ GCC_except_table53
+ OBJC_IVAR_$_BGTask.__lock
+ _OBJC_CLASS_$__BGTaskExpirationRequest
+ _OBJC_IVAR_$_BGContinuedProcessingTask._expirationHandlerWithReason
+ _OBJC_IVAR_$__BGContinuedProcessingTaskRequest._linkToBundleIdentifier
+ _OBJC_IVAR_$__BGTaskExpirationRequest._reason
+ _OBJC_IVAR_$__BGTaskExpirationRequest._schedulerActivity
+ _OBJC_IVAR_$__BGTaskExpirationRequest._task
+ _OBJC_METACLASS_$__BGTaskExpirationRequest
+ __OBJC_$_CATEGORY_INSTANCE_METHODS__DASActivity_$_BGTaskScheduler
+ __OBJC_$_CATEGORY__DASActivity_$_BGTaskScheduler
+ __OBJC_$_CLASS_METHODS__BGTaskExpirationRequest
+ __OBJC_$_INSTANCE_METHODS__BGTaskExpirationRequest
+ __OBJC_$_INSTANCE_VARIABLES__BGTaskExpirationRequest
+ __OBJC_$_PROP_LIST__BGTaskExpirationRequest
+ __OBJC_CLASS_PROTOCOLS_$__BGTaskExpirationRequest
+ __OBJC_CLASS_RO_$__BGTaskExpirationRequest
+ __OBJC_METACLASS_RO_$__BGTaskExpirationRequest
+ ___41-[BGTaskScheduler _runTask:registration:]_block_invoke.137
+ ___block_literal_global.101
+ ___block_literal_global.131
+ ___block_literal_global.85
+ ___block_literal_global.98
+ _objc_msgSend$_callExpirationHandlerWithReason:
+ _objc_msgSend$_unsafe_createExpirationRequestsForActivities:
+ _objc_msgSend$_unsafe_taskForActivity:
+ _objc_msgSend$bgTaskExpirationReason
+ _objc_msgSend$expirationHandlerWithReason
+ _objc_msgSend$initWithActivity:task:reason:
+ _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:linkToBundleIdentifier:resources:
+ _objc_msgSend$lastDenialValue
+ _objc_msgSend$linkToBundleIdentifier
+ _objc_msgSend$requestWithActivity:task:reason:
+ _objc_msgSend$schedulerActivity
+ _objc_msgSend$setExpirationHandlerWithReason:
+ _objc_msgSend$setLinkToBundleIdentifier:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$task
+ _os_unfair_recursive_lock_lock_with_options
+ _os_unfair_recursive_lock_unlock
- -[BGTask _callExpirationHandler]
- -[BGTask _callExpirationHandler].cold.1
- -[BGTask _lock]
- -[BGTask _setLock:]
- -[BGTaskScheduler _callExpirationHandlersForActivities:shouldQueue:].cold.1
- GCC_except_table26
- GCC_except_table43
- GCC_except_table51
- _OBJC_IVAR_$_BGTask.__lock
- ___41-[BGTaskScheduler _runTask:registration:]_block_invoke.100
- ___block_literal_global.47
- ___block_literal_global.60
- ___block_literal_global.63
- ___block_literal_global.94
- _objc_msgSend$_callExpirationHandler
- _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:resources:
- _objc_msgSend$removeObject:
CStrings:
+ "%"
+ "<_BGTaskExpirationRequest: %@, reason: %ld task: %@"
+ "@\"BGTask\""
+ "@40@0:8@16@24q32"
+ "BGTask.m"
+ "Only a single expiration handler may be set"
+ "T@\"BGTask\",R,V_task"
+ "T@\"NSString\",C,N,V_linkToBundleIdentifier"
+ "T@\"_DASActivity\",R,V_schedulerActivity"
+ "T@?,C,V_expirationHandlerWithReason"
+ "Tq,V_reason"
+ "_BGTaskExpirationRequest"
+ "_callExpirationHandlerWithReason:"
+ "_expirationHandlerWithReason"
+ "_linkToBundleIdentifier"
+ "_schedulerActivity"
+ "_task"
+ "_unsafe_createExpirationRequestsForActivities:"
+ "_unsafe_taskForActivity:"
+ "bgTaskExpirationReason"
+ "expirationHandlerWithReason"
+ "initWithActivity:task:reason:"
+ "initWithIdentifier:iconBundleIdentifier:onBehalfOf:linkToBundleIdentifier:"
+ "initWithTitle:subtitle:iconBundleIdentifier:linkToBundleIdentifier:resources:"
+ "lastDenialValue"
+ "linkToBundleIdentifier"
+ "requestWithActivity:task:reason:"
+ "schedulerActivity"
+ "setExpirationHandlerWithReason:"
+ "setLinkToBundleIdentifier:"
+ "setWithCapacity:"
+ "task"
+ "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
- "Unknown activities expired, completing immediately: %{public}@"
- "_callExpirationHandler"
- "initWithTitle:subtitle:iconBundleIdentifier:resources:"
- "removeObject:"

```
