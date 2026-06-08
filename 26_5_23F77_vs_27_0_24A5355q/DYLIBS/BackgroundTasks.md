## BackgroundTasks

> `/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks`

```diff

-2109.120.16.0.0
-  __TEXT.__text: 0xad94
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0xdf8
-  __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x6f9
-  __TEXT.__oslogstring: 0x7a9
-  __TEXT.__gcc_except_tab: 0xbc
+2463.0.0.502.1
+  __TEXT.__text: 0xb13c
+  __TEXT.__objc_methlist: 0xec0
+  __TEXT.__const: 0xf8
+  __TEXT.__cstring: 0x74e
+  __TEXT.__oslogstring: 0x95b
+  __TEXT.__gcc_except_tab: 0xb8
   __TEXT.__unwind_info: 0x360
-  __TEXT.__objc_classname: 0x20f
-  __TEXT.__objc_methname: 0x22d0
-  __TEXT.__objc_methtype: 0x4aa
-  __TEXT.__objc_stubs: 0x1940
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x248
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_nlclslist: 0x8
-  __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x870
+  __DATA_CONST.__objc_selrefs: 0x910
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x1b0
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x6a0
-  __AUTH_CONST.__objc_const: 0x17e0
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0xdc
-  __DATA.__data: 0x248
-  __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__bss: 0x40
+  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__objc_const: 0x1890
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0xe0
+  __DATA.__data: 0x2a8
+  __DATA.__bss: 0x40
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C954740-F7F9-3642-9B5D-643D1C40FEAD
-  Functions: 295
-  Symbols:   1171
-  CStrings:  618
+  UUID: E2CDB553-C589-3FF2-AB56-D9A175D82E3E
+  Functions: 315
+  Symbols:   1245
+  CStrings:  173
 
Symbols:
+ +[BGContinuedProcessingTaskContext backgroundedSubmissionContext]
+ +[BGTaskScheduler _bgErrorFromDASError:]
+ -[BGContinuedProcessingTask _pauseHandler]
+ -[BGContinuedProcessingTask _setPauseHandler:]
+ -[BGContinuedProcessingTask setTaskPaused]
+ -[BGContinuedProcessingTask setTaskPaused].cold.1
+ -[BGContinuedProcessingTask setTaskPaused].cold.2
+ -[BGContinuedProcessingTaskRequest _isBackgroundedSubmission]
+ -[BGTaskScheduler _callExpirationHandlersFor:shouldQueue:]
+ -[BGTaskScheduler _callSuspensionHandlersFor:]
+ -[BGTaskScheduler _expirationRequestsFrom:]
+ -[BGTaskScheduler _invokeExpirationHandlersForExpirationRequests:]
+ -[BGTaskScheduler _registerForTaskWithDynamicIdentifier:usingQueue:launchHandler:]
+ -[BGTaskScheduler _registerForTaskWithDynamicIdentifier:usingQueue:launchHandler:].cold.1
+ -[BGTaskScheduler _registerForTaskWithDynamicIdentifier:usingQueue:launchHandler:].cold.2
+ -[BGTaskScheduler _unsafe_registerForTaskWithIdentifier:usingQueue:launchHandler:bypassInfoPlistValidation:]
+ -[BGTaskScheduler _unsafe_registerForTaskWithIdentifier:usingQueue:launchHandler:bypassInfoPlistValidation:].cold.1
+ -[BGTaskScheduler _unsafe_submitTaskRequest:legacySubmission:completionHandler:]
+ -[BGTaskScheduler _unsafe_submitTaskRequest:legacySubmission:completionHandler:].cold.1
+ -[BGTaskScheduler scheduler:handleLifecycleEvents:]
+ -[BGTaskScheduler submitTaskRequest:completionHandler:]
+ -[_BGTaskIdentifierRegistry isPermissibleIdentifierForDynamicRegistration:]
+ -[_DASActivityExpirationEvent(BGTaskScheduler) asBGContinuedProcessingExpirationReason]
+ -[_DASActivityExpirationEvent(BGTaskScheduler) asBGTaskExpirationRequestForTask:]
+ -[_DASActivitySuspensionEvent(BGTaskScheduler) asBGContinuedProcessingExpirationReason]
+ -[_DASActivitySuspensionEvent(BGTaskScheduler) asBGTaskExpirationRequestForTask:]
+ GCC_except_table30
+ GCC_except_table50
+ _OBJC_CLASS_$__DASActivityExpirationEvent
+ _OBJC_CLASS_$__DASActivitySuspensionEvent
+ _OBJC_IVAR_$_BGContinuedProcessingTask.__pauseHandler
+ __OBJC_$_CATEGORY_INSTANCE_METHODS__DASActivityExpirationEvent_$_BGTaskScheduler
+ __OBJC_$_CATEGORY_INSTANCE_METHODS__DASActivitySuspensionEvent_$_BGTaskScheduler
+ __OBJC_$_CATEGORY__DASActivityExpirationEvent_$_BGTaskScheduler
+ __OBJC_$_CATEGORY__DASActivitySuspensionEvent_$_BGTaskScheduler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__BGTaskTranslatable
+ __OBJC_$_PROTOCOL_METHOD_TYPES__BGTaskTranslatable
+ __OBJC_CATEGORY_PROTOCOLS_$__DASActivityExpirationEvent_$_BGTaskScheduler
+ __OBJC_CATEGORY_PROTOCOLS_$__DASActivitySuspensionEvent_$_BGTaskScheduler
+ __OBJC_LABEL_PROTOCOL_$__BGTaskTranslatable
+ __OBJC_PROTOCOL_$__BGTaskTranslatable
+ ___41-[BGTaskScheduler _runTask:registration:]_block_invoke.101
+ ___41-[BGTaskScheduler _runTask:registration:]_block_invoke.105
+ ___41-[BGTaskScheduler _runTask:registration:]_block_invoke_2.106
+ ___41-[BGTaskScheduler _runTask:registration:]_block_invoke_3.107
+ ___42-[BGContinuedProcessingTask setTaskPaused]_block_invoke
+ ___43-[BGTaskScheduler submitTaskRequest:error:]_block_invoke
+ ___66-[BGTaskScheduler _invokeExpirationHandlersForExpirationRequests:]_block_invoke
+ ___80-[BGTaskScheduler _unsafe_submitTaskRequest:legacySubmission:completionHandler:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_literal_global.46
+ ___block_literal_global.59
+ ___block_literal_global.62
+ ___block_literal_global.95
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_bgErrorFromDASError:
+ _objc_msgSend$_callExpirationHandlersFor:shouldQueue:
+ _objc_msgSend$_callSuspensionHandlersFor:
+ _objc_msgSend$_completed
+ _objc_msgSend$_expirationRequestsFrom:
+ _objc_msgSend$_invokeExpirationHandlersForExpirationRequests:
+ _objc_msgSend$_isBackgroundedSubmission
+ _objc_msgSend$_pauseHandler
+ _objc_msgSend$_setCompleted:
+ _objc_msgSend$_setPauseHandler:
+ _objc_msgSend$_unsafe_registerForTaskWithIdentifier:usingQueue:launchHandler:bypassInfoPlistValidation:
+ _objc_msgSend$_unsafe_submitTaskRequest:legacySubmission:completionHandler:
+ _objc_msgSend$acknowledgeTaskPause:
+ _objc_msgSend$activity
+ _objc_msgSend$asBGContinuedProcessingExpirationReason
+ _objc_msgSend$asBGTaskExpirationRequestForTask:
+ _objc_msgSend$backgroundedSubmissionContext
+ _objc_msgSend$expiration
+ _objc_msgSend$expirationReasons
+ _objc_msgSend$isPermissibleIdentifierForDynamicRegistration:
+ _objc_msgSend$submitTaskRequest:completionHandler:
+ _objc_msgSend$suspension
+ _objc_msgSend$type
+ _objc_msgSend$unknownReasonsForActivities:
+ _objc_msgSend$userInfo
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x8
- -[BGTaskScheduler _callExpirationHandlersForActivities:shouldQueue:]
- -[BGTaskScheduler _unsafe_registerForTaskWithIdentifier:usingQueue:launchHandler:]
- -[BGTaskScheduler _unsafe_registerForTaskWithIdentifier:usingQueue:launchHandler:].cold.1
- -[BGTaskScheduler _unsafe_submitTaskRequest:error:]
- -[BGTaskScheduler _unsafe_submitTaskRequest:error:].cold.1
- -[BGTaskScheduler scheduler:willExpireActivities:]
- -[_BGTaskExpirationRequest setReason:]
- -[_DASActivity(BGTaskScheduler) bgTaskExpirationReason]
- GCC_except_table53
- _OUTLINED_FUNCTION_4
- __OBJC_$_CATEGORY_INSTANCE_METHODS__DASActivity_$_BGTaskScheduler
- __OBJC_$_CATEGORY__DASActivity_$_BGTaskScheduler
- ___41-[BGTaskScheduler _runTask:registration:]_block_invoke.137
- ___41-[BGTaskScheduler _runTask:registration:]_block_invoke_4
- ___41-[BGTaskScheduler _runTask:registration:]_block_invoke_5
- ___68-[BGTaskScheduler _callExpirationHandlersForActivities:shouldQueue:]_block_invoke
- ___block_literal_global.101
- ___block_literal_global.131
- ___block_literal_global.85
- ___block_literal_global.98
- _objc_msgSend$_callExpirationHandlersForActivities:shouldQueue:
- _objc_msgSend$_unsafe_createExpirationRequestsForActivities:
- _objc_msgSend$_unsafe_registerForTaskWithIdentifier:usingQueue:launchHandler:
- _objc_msgSend$_unsafe_submitTaskRequest:error:
- _objc_msgSend$bgTaskExpirationReason
- _objc_msgSend$lastDenialValue
CStrings:
+ "Acknowledging pause for simulated task: %@"
+ "Acknowledging pause for task %{public}@"
+ "AssociatedHost (host: %@)"
+ "BackgroundedSubmission"
+ "Calling expiration handlers for lifecycle events: %{public}@"
+ "Dynamic registration rejected; %@ is not a well-formed identifier for this application"
+ "Handling suspension for activities: %{public}@"
+ "No pause handler set for task %{public}@"
+ "Task %{public}@ already completed, ignoring pause acknowledgement"
+ "Will handle lifecycle events: %{public}@"
+ "_registerForTaskWithDynamicIdentifier: %{public}@"
+ "submitTaskRequest:completionHandler: %{public}@"
+ "v16@?0@\"NSError\"8"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<_DASActivityBackgroundTasksScheduler>\""
- "@\"BGContinuedProcessingTaskContext\""
- "@\"BGTask\""
- "@\"NSDate\""
- "@\"NSMapTable\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSProgress\""
- "@\"NSProgress\"16@0:8"
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"_BGTaskIdentifierRegistry\""
- "@\"_DASActivity\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24q32"
- "@48@0:8@16@24@32@40"
- "@48@0:8{?=[8I]}16"
- "@56@0:8q16{?=[8I]}24"
- "@?"
- "@?16@0:8"
- "@?28@0:8B16d20"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16^@24"
- "B40@0:8@16@24@?32"
- "BGAppRefreshTask"
- "BGAppRefreshTaskRequest"
- "BGContinuedProcessingTaskContext"
- "BGContinuedProcessingTaskRequest"
- "BGHealthResearchTask"
- "BGHealthResearchTaskRequest"
- "BGProcessingTask"
- "BGProcessingTaskRequest"
- "BGTask"
- "BGTaskRequest"
- "BGTaskScheduler"
- "Calling expiration handlers for activities: %{public}@"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSProgressReporting"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<_DASActivityBackgroundTasksScheduler>\",&,N,S_setScheduler:,V__scheduler"
- "T@\"BGContinuedProcessingTaskContext\",&,N,V_context"
- "T@\"BGTask\",R,V_task"
- "T@\"BGTaskRequest\",R,C"
- "T@\"BGTaskScheduler\",R"
- "T@\"NSDate\",C,V_earliestBeginDate"
- "T@\"NSMapTable\",&,N,S_setRunningTasksMap:,V__runningTasksMap"
- "T@\"NSMutableDictionary\",&,N,S_setRegistrations:,V__registrations"
- "T@\"NSMutableSet\",&,N,S_setQueuedExpiredLaunchActivities:,V__queuedExpiredLaunchActivities"
- "T@\"NSMutableSet\",&,N,S_setQueuedLaunchActivities:,V__queuedLaunchActivities"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,S_setHandlerQueue:,V__handlerQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_os_log>\",&,N,V_log"
- "T@\"NSProgress\",&,N,V_internalProgress"
- "T@\"NSProgress\",R"
- "T@\"NSProgress\",R,V_progress"
- "T@\"NSSet\",R,N,V_permittedContinuedProcessingBaseNotationIdentifiers"
- "T@\"NSSet\",R,N,V_permittedIdentifiers"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_applicationBundleIdentifier"
- "T@\"NSString\",C,N,V_iconBundleIdentifier"
- "T@\"NSString\",C,N,V_linkToBundleIdentifier"
- "T@\"NSString\",C,N,V_subtitle"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSString\",C,V_iconUTI"
- "T@\"NSString\",C,V_linkToBundleIdentifier"
- "T@\"NSString\",C,V_reason"
- "T@\"NSString\",C,V_subtitle"
- "T@\"NSString\",C,V_title"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_hostAppBundleIdentifier"
- "T@\"NSString\",R,C,V_identifier"
- "T@\"NSString\",V_protectionTypeOfRequiredData"
- "T@\"_BGTaskIdentifierRegistry\",&,N,S_setIdentifierRegistry:,V__identifierRegistry"
- "T@\"_DASActivity\",&,N,S_setActivity:,V__activity"
- "T@\"_DASActivity\",R,V_schedulerActivity"
- "T@?,C,N,S_setCompletionHandler:,V__completionHandler"
- "T@?,C,N,S_setDescriptionUpdateHandler:,V__descriptionUpdateHandler"
- "T@?,C,N,S_setProgressHandler:,V__progressHandler"
- "T@?,C,N,V_launchHandler"
- "T@?,C,V_expirationHandler"
- "T@?,C,V_expirationHandlerWithReason"
- "TB,N,S_setCompleted:,V__completed"
- "TB,R"
- "TB,V_requiresExternalPower"
- "TB,V_requiresNetworkConnectivity"
- "TQ,R"
- "Tq,N,V_requiredResources"
- "Tq,N,V_strategy"
- "Tq,R"
- "Tq,R,N"
- "Tq,R,N,V_topology"
- "Tq,V_reason"
- "T{?=[8I]},R,N,V_hostAppAuditToken"
- "T{os_unfair_lock_s=I},N,S_setLock:,V__lock"
- "Vv16@0:8"
- "Will expire activities: %{public}@"
- "^{_NSZone=}16@0:8"
- "_BGContinuedProcessingTask"
- "_BGContinuedProcessingTaskRequest"
- "_BGTaskExpirationRequest"
- "_BGTaskIdentifierRegistry"
- "_BGTaskSchedulerRegistration"
- "_DASActivityBackgroundTasksSchedulerDelegate"
- "__activity"
- "__completed"
- "__completionHandler"
- "__descriptionUpdateHandler"
- "__handlerQueue"
- "__identifierRegistry"
- "__lock"
- "__progressHandler"
- "__queuedExpiredLaunchActivities"
- "__queuedLaunchActivities"
- "__registrations"
- "__runningTasksMap"
- "__scheduler"
- "_activity"
- "_appAdoptsUISceneLifecycle"
- "_applicationBundleIdentifier"
- "_applicationDidFinishLaunching:"
- "_callExpirationHandlerWithReason:"
- "_callExpirationHandlersForActivities:shouldQueue:"
- "_callRegisteredHandlersForActivities:"
- "_completed"
- "_completionHandler"
- "_context"
- "_correspondingTaskClass"
- "_descriptionUpdateHandler"
- "_earliestBeginDate"
- "_expirationHandler"
- "_expirationHandlerWithReason"
- "_handleAppLaunch"
- "_handleSubmissionWithoutRegistrationForTaskRequest:error:"
- "_handlerQueue"
- "_hasExtensionEntitlement"
- "_hostAppAuditToken"
- "_hostAppBundleIdentifier"
- "_iconBundleIdentifier"
- "_iconUTI"
- "_identifier"
- "_identifierRegistry"
- "_init"
- "_initWithIdentifier:"
- "_initWithIdentifier:activity:"
- "_internalProgress"
- "_isNotApplication"
- "_isRunningInExtension"
- "_isRunningInNonExtensionOrApplication"
- "_isRunningTaskOfClass:"
- "_launchHandler"
- "_linkToBundleIdentifier"
- "_lock"
- "_log"
- "_permittedContinuedProcessingBaseNotationIdentifiers"
- "_permittedIdentifiers"
- "_progress"
- "_progressHandler"
- "_protectionTypeOfRequiredData"
- "_queue"
- "_queueForRegistration:"
- "_queuedExpiredLaunchActivities"
- "_queuedLaunchActivities"
- "_reason"
- "_registrations"
- "_requestFromActivity:"
- "_requiredResources"
- "_requiresExternalPower"
- "_requiresNetworkConnectivity"
- "_runTask:registration:"
- "_runningTasks"
- "_runningTasksMap"
- "_scheduler"
- "_schedulerActivity"
- "_setActivity:"
- "_setCompleted:"
- "_setCompletionHandler:"
- "_setDescriptionUpdateHandler:"
- "_setHandlerQueue:"
- "_setIdentifierRegistry:"
- "_setLock:"
- "_setProgressHandler:"
- "_setQueuedExpiredLaunchActivities:"
- "_setQueuedLaunchActivities:"
- "_setRegistrations:"
- "_setRunningTasksMap:"
- "_setScheduler:"
- "_setTaskCompletedWithSuccess:actionsIfNotAlreadyCompleted:"
- "_sharedSchedulerIfExists"
- "_simulateExpirationForTaskWithIdentifier:"
- "_simulateLaunchForTaskWithIdentifier:"
- "_strategy"
- "_subtitle"
- "_task"
- "_title"
- "_topology"
- "_unsafe_createExpirationRequestsForActivities:"
- "_unsafe_registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "_unsafe_registrationForIdentifier:"
- "_unsafe_setTaskCompletedWithSuccess:afterDelay:"
- "_unsafe_submitTaskRequest:error:"
- "_unsafe_taskForActivity:"
- "_updateSnapshotForBackgroundApplication:"
- "activityWithName:priority:duration:startingAfter:startingBefore:"
- "addObject:"
- "addObserver:forKeyPath:options:context:"
- "addObserver:selector:name:object:"
- "allocWithZone:"
- "applicationBundleIdentifier"
- "array"
- "arrayWithObject:"
- "arrayWithObjects:"
- "autorelease"
- "bgTaskExpirationReason"
- "bundleIdentifier"
- "cStringUsingEncoding:"
- "cancel"
- "cancelTaskRequestWithIdentifier:"
- "class"
- "clientProvidedIdentifier"
- "clientProvidedStartDate"
- "code"
- "completeTaskRequest:withSuccess:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "containsObject:"
- "containsString:"
- "context"
- "continuedProcessingDeviceCapabilities:"
- "continuedProcessingWrapper"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "currentProcess"
- "currentThread"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultCenter"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "distantFuture"
- "domain"
- "earliestBeginDate"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "executionContext"
- "expirationHandler"
- "expirationHandlerWithReason"
- "fileProtection"
- "firstObject"
- "fractionCompleted"
- "getBytes:length:"
- "getPendingTaskRequestsWithCompletionHandler:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasPrefix:"
- "hasSuffix:"
- "hash"
- "iconBundleIdentifier"
- "iconUTI"
- "identifier"
- "infoDictionary"
- "init"
- "initWithActivity:task:reason:"
- "initWithCoder:"
- "initWithContentsFromPlist"
- "initWithIdentifier:"
- "initWithIdentifier:iconBundleIdentifier:"
- "initWithIdentifier:iconBundleIdentifier:applicationBundleIdentifier:"
- "initWithIdentifier:iconBundleIdentifier:onBehalfOf:linkToBundleIdentifier:"
- "initWithIdentifier:queue:launchHandler:"
- "initWithIdentifier:title:subtitle:"
- "initWithIdentifier:title:subtitle:context:"
- "initWithIdentifier:title:subtitle:onBehalfOf:"
- "initWithPermittedIdentifiers:"
- "initWithTitle:subtitle:iconUTI:linkToBundleIdentifier:resources:"
- "initWithTitle:subtitle:resources:submissionStrategy:executionContext:hostAppAuditToken:"
- "initWithTopology:hostAppAuditToken:"
- "initWithTopology:hostAppBundleIdentifier:"
- "initialize"
- "internalProgress"
- "isApplication"
- "isEqual:"
- "isEqualToString:"
- "isIdentifierValidContinuedProcessingBaseNotation:"
- "isIdentifierValidContinuedProcessingComposedNotation:"
- "isIdentifierValidContinuedProcessingWildcardNotation:"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isPermissibleFullyComposedIdentifier:"
- "isProxy"
- "keyEnumerator"
- "lastDenialValue"
- "launchHandler"
- "launchReason"
- "length"
- "linkToBundleIdentifier"
- "load"
- "log"
- "mainBundle"
- "now"
- "null"
- "numberWithInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "permittedContinuedProcessingBaseNotationIdentifiers"
- "permittedIdentifiers"
- "postNotificationName:object:"
- "progress"
- "protectionType"
- "protectionTypeOfRequiredData"
- "protectionWithType:"
- "proxyContextForApp:"
- "proxyContextForAuditToken:"
- "q"
- "q16@0:8"
- "queue"
- "reason"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "registryWithContentsFromPlist"
- "relatedApplications"
- "release"
- "removeObjectForKey:"
- "removeObserver:"
- "requestWithActivity:task:reason:"
- "requiredResources"
- "requiresExternalPower"
- "requiresNetwork"
- "requiresNetworkConnectivity"
- "requiresPlugin"
- "resources"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scheduler:handleLaunchForActivities:"
- "scheduler:willExpireActivities:"
- "schedulerActivity"
- "self"
- "set"
- "setApplicationBundleIdentifier:"
- "setBackgroundTasksSchedulerDelegate:"
- "setClientProvidedIdentifier:"
- "setClientProvidedStartDate:"
- "setContext:"
- "setContinuedProcessingWrapper:"
- "setEarliestBeginDate:"
- "setExpirationHandler:"
- "setExpirationHandlerWithReason:"
- "setFileProtection:"
- "setGroupName:"
- "setIconBundleIdentifier:"
- "setIconUTI:"
- "setIdentifier:"
- "setInternalProgress:"
- "setLaunchHandler:"
- "setLaunchReason:"
- "setLinkToBundleIdentifier:"
- "setLog:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setProtectionTypeOfRequiredData:"
- "setQueue:"
- "setReason:"
- "setRelatedApplications:"
- "setRequiredResources:"
- "setRequiresExternalPower:"
- "setRequiresNetwork:"
- "setRequiresNetworkConnectivity:"
- "setRequiresPlugin:"
- "setStrategy:"
- "setSubtitle:"
- "setTaskCompletedWithSuccess:"
- "setTitle:"
- "setWithCapacity:"
- "sharedApplication"
- "sharedScheduler"
- "standardContext"
- "strategy"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "strongToWeakObjectsMapTable"
- "submissionStrategy"
- "submitTaskRequest:"
- "submitTaskRequest:error:"
- "subtitle"
- "superclass"
- "supportsSecureCoding"
- "task"
- "taskRequest"
- "title"
- "unionSet:"
- "updateOngoingTask:"
- "updateProgress:"
- "updateProgress:forOngoingTask:"
- "updateProgressPercentage:"
- "updateTitle:subtitle:"
- "updateTitle:withReason:"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v28@0:8B16@?20"
- "v32@0:8@\"<_DASActivityBackgroundTasksScheduler>\"16@\"NSSet\"24"
- "v32@0:8@16@24"
- "v32@0:8@16^@24"
- "v48@0:8@16@24@32^v40"
- "zone"
- "{?=\"val\"[8I]}"
- "{?=[8I]}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
