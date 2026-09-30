## BackgroundTasks

> `/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks`

```diff

-1856.120.12.0.0
-  __TEXT.__text: 0x7a48
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0xa40
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x57a
-  __TEXT.__oslogstring: 0x5ae
-  __TEXT.__unwind_info: 0x278
-  __TEXT.__objc_classname: 0x18a
-  __TEXT.__objc_methname: 0x17a1
-  __TEXT.__objc_methtype: 0x2fa
-  __TEXT.__objc_stubs: 0x11c0
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x228
-  __DATA_CONST.__objc_classlist: 0x70
+2109.0.44.502.1
+  __TEXT.__text: 0x8e30
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0xba0
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0x5d2
+  __TEXT.__oslogstring: 0x7e8
+  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__objc_classname: 0x1ba
+  __TEXT.__objc_methname: 0x1cd2
+  __TEXT.__objc_methtype: 0x37b
+  __TEXT.__objc_stubs: 0x14c0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_nlclslist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x620
-  __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x220
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0x10e0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x90
-  __DATA.__data: 0x120
-  __DATA.__bss: 0x9
+  __DATA_CONST.__objc_selrefs: 0x730
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x480
+  __AUTH_CONST.__objc_const: 0x13b8
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0xb0
+  __DATA.__data: 0x188
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1BCE7080-45AA-3F2E-9494-8C2C6C166DB4
-  Functions: 207
-  Symbols:   849
-  CStrings:  422
+  UUID: 7B40B4B6-3F1C-3574-B4E7-AC83DD7368E6
+  Functions: 242
+  Symbols:   981
+  CStrings:  506
 
Symbols:
+ +[BGTaskRequest _requestFromActivity:].cold.1
+ +[BGTaskRequest initialize]
+ +[BGTaskScheduler supportedResources]
+ +[BGTaskScheduler supportedResources].cold.1
+ +[_BGTaskIdentifierRegistry registryWithContentsFromPlist]
+ -[BGContinuedProcessingTask _descriptionUpdateHandler]
+ -[BGContinuedProcessingTask _setDescriptionUpdateHandler:]
+ -[BGContinuedProcessingTask log]
+ -[BGContinuedProcessingTask observeValueForKeyPath:ofObject:change:context:]
+ -[BGContinuedProcessingTask progress]
+ -[BGContinuedProcessingTask setLog:]
+ -[BGContinuedProcessingTask setSubtitle:]
+ -[BGContinuedProcessingTask subtitle]
+ -[BGContinuedProcessingTask updateTitle:subtitle:]
+ -[BGContinuedProcessingTaskRequest initWithIdentifier:title:subtitle:]
+ -[BGContinuedProcessingTaskRequest requiredResources]
+ -[BGContinuedProcessingTaskRequest setRequiredResources:]
+ -[BGContinuedProcessingTaskRequest setStrategy:]
+ -[BGContinuedProcessingTaskRequest setSubtitle:]
+ -[BGContinuedProcessingTaskRequest strategy]
+ -[BGContinuedProcessingTaskRequest subtitle]
+ -[BGTask taskRequest]
+ -[BGTaskScheduler _handleSubmissionWithoutRegistrationForTaskRequest:error:]
+ -[BGTaskScheduler _handleSubmissionWithoutRegistrationForTaskRequest:error:].cold.1
+ -[BGTaskScheduler _identifierRegistry]
+ -[BGTaskScheduler _setIdentifierRegistry:]
+ -[BGTaskScheduler _unsafe_registerForTaskWithIdentifier:usingQueue:launchHandler:].cold.1
+ -[BGTaskScheduler _unsafe_submitTaskRequest:error:].cold.1
+ -[_BGContinuedProcessingTaskRequest _activity].cold.1
+ -[_BGTaskIdentifierRegistry .cxx_destruct]
+ -[_BGTaskIdentifierRegistry copyWithZone:]
+ -[_BGTaskIdentifierRegistry initWithContentsFromPlist]
+ -[_BGTaskIdentifierRegistry initWithPermittedIdentifiers:]
+ -[_BGTaskIdentifierRegistry isIdentifierValidContinuedProcessingBaseNotation:]
+ -[_BGTaskIdentifierRegistry isIdentifierValidContinuedProcessingComposedNotation:]
+ -[_BGTaskIdentifierRegistry isIdentifierValidContinuedProcessingWildcardNotation:]
+ -[_BGTaskIdentifierRegistry isPermissibleFullyComposedIdentifier:]
+ -[_BGTaskIdentifierRegistry permittedContinuedProcessingBaseNotationIdentifiers]
+ -[_BGTaskIdentifierRegistry permittedIdentifiers]
+ GCC_except_table26
+ GCC_except_table43
+ GCC_except_table51
+ _BGContinuedProcessingTaskProgressObserverContext
+ _NSStringFromSelector
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSProgress
+ _OBJC_CLASS_$__BGTaskIdentifierRegistry
+ _OBJC_CLASS_$__DASContinuedProcessingWrapper
+ _OBJC_IVAR_$_BGContinuedProcessingTask.__descriptionUpdateHandler
+ _OBJC_IVAR_$_BGContinuedProcessingTask._log
+ _OBJC_IVAR_$_BGContinuedProcessingTask._progress
+ _OBJC_IVAR_$_BGContinuedProcessingTask._subtitle
+ _OBJC_IVAR_$_BGContinuedProcessingTaskRequest._requiredResources
+ _OBJC_IVAR_$_BGContinuedProcessingTaskRequest._strategy
+ _OBJC_IVAR_$_BGContinuedProcessingTaskRequest._subtitle
+ _OBJC_IVAR_$_BGTaskScheduler.__identifierRegistry
+ _OBJC_IVAR_$__BGTaskIdentifierRegistry._log
+ _OBJC_IVAR_$__BGTaskIdentifierRegistry._permittedContinuedProcessingBaseNotationIdentifiers
+ _OBJC_IVAR_$__BGTaskIdentifierRegistry._permittedIdentifiers
+ _OBJC_METACLASS_$__BGTaskIdentifierRegistry
+ _OUTLINED_FUNCTION_1
+ __DASDefaultContinuedProcessingGroupName
+ __OBJC_$_CLASS_METHODS__BGTaskIdentifierRegistry
+ __OBJC_$_INSTANCE_METHODS__BGTaskIdentifierRegistry
+ __OBJC_$_INSTANCE_VARIABLES__BGTaskIdentifierRegistry
+ __OBJC_$_PROP_LIST_NSProgressReporting
+ __OBJC_$_PROP_LIST__BGTaskIdentifierRegistry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSProgressReporting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSProgressReporting
+ __OBJC_$_PROTOCOL_REFS_NSProgressReporting
+ __OBJC_CLASS_PROTOCOLS_$_BGContinuedProcessingTask
+ __OBJC_CLASS_PROTOCOLS_$__BGTaskIdentifierRegistry
+ __OBJC_CLASS_RO_$__BGTaskIdentifierRegistry
+ __OBJC_LABEL_PROTOCOL_$_NSProgressReporting
+ __OBJC_METACLASS_RO_$__BGTaskIdentifierRegistry
+ __OBJC_PROTOCOL_$_NSProgressReporting
+ ___37+[BGTaskScheduler supportedResources]_block_invoke
+ ___37+[BGTaskScheduler supportedResources]_block_invoke_2
+ ___41-[BGTaskScheduler _runTask:registration:]_block_invoke.100
+ ___41-[BGTaskScheduler _runTask:registration:]_block_invoke_5
+ ___block_descriptor_32_e8_v16?0q8l
+ ___block_literal_global.47
+ ___block_literal_global.60
+ ___block_literal_global.63
+ ___block_literal_global.94
+ __log
+ _objc_msgSend$_handleSubmissionWithoutRegistrationForTaskRequest:error:
+ _objc_msgSend$_identifierRegistry
+ _objc_msgSend$_setIdentifierRegistry:
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$completeTaskRequest:withSuccess:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$containsString:
+ _objc_msgSend$continuedProcessingDeviceCapabilities:
+ _objc_msgSend$continuedProcessingWrapper
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithContentsFromPlist
+ _objc_msgSend$initWithIdentifier:title:subtitle:
+ _objc_msgSend$initWithPermittedIdentifiers:
+ _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:resources:
+ _objc_msgSend$initWithTitle:subtitle:resources:submissionStrategy:
+ _objc_msgSend$isIdentifierValidContinuedProcessingComposedNotation:
+ _objc_msgSend$isIdentifierValidContinuedProcessingWildcardNotation:
+ _objc_msgSend$isPermissibleFullyComposedIdentifier:
+ _objc_msgSend$length
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$permittedContinuedProcessingBaseNotationIdentifiers
+ _objc_msgSend$permittedIdentifiers
+ _objc_msgSend$registryWithContentsFromPlist
+ _objc_msgSend$requiredResources
+ _objc_msgSend$setContinuedProcessingWrapper:
+ _objc_msgSend$setGroupName:
+ _objc_msgSend$setSubtitle:
+ _objc_msgSend$strategy
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$subtitle
+ _objc_msgSend$supportedResources
+ _objc_sync_enter
+ _objc_sync_exit
+ _supportedResources.onceToken
+ _supportedResources.resources
- -[BGContinuedProcessingTask reason]
- -[BGContinuedProcessingTask setReason:]
- -[BGContinuedProcessingTask updateProgress:]
- -[BGContinuedProcessingTaskRequest initWithIdentifier:]
- -[BGContinuedProcessingTaskRequest reason]
- -[BGContinuedProcessingTaskRequest setReason:]
- -[BGTaskScheduler _permittedIdentifiers]
- -[BGTaskScheduler _setPermittedIdentifiers:]
- GCC_except_table25
- GCC_except_table39
- _OBJC_CLASS_$_NSSet
- _OBJC_IVAR_$_BGContinuedProcessingTask._reason
- _OBJC_IVAR_$_BGContinuedProcessingTaskRequest._reason
- _OBJC_IVAR_$_BGTaskScheduler.__permittedIdentifiers
- ___41-[BGTaskScheduler _runTask:registration:]_block_invoke.91
- ___block_literal_global.50
- ___block_literal_global.85
- _objc_msgSend$_permittedIdentifiers
- _objc_msgSend$_setPermittedIdentifiers:
- _objc_msgSend$activityWithName:priority:duration:startingAfter:startingBefore:userInfo:
- _objc_msgSend$clientProvidedIconBundleIdentifier
- _objc_msgSend$clientProvidedReason
- _objc_msgSend$clientProvidedTitle
- _objc_msgSend$completeTaskRequest:
- _objc_msgSend$setClientProvidedReason:
- _objc_msgSend$setClientProvidedTitle:
- _objc_msgSend$setWithArray:
CStrings:
+ "%{public}@ Received KVO update for unknown context: (key-path: %@, context: %@)"
+ "%{public}@ is not advertised in the application's Info.plist"
+ "%{public}@ requested an unsupported set of resources: %{public}@"
+ ","
+ "."
+ ".*"
+ "<BGContinuedProcessingTask: %@ (%@)>"
+ "<BGContinuedProcessingTaskRequest: %@, (title: %@, subtitle: %@, resources: %@, submissionStrategy: %@)>"
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSProgress\"16@0:8"
+ "@\"_BGTaskIdentifierRegistry\""
+ "Attempt to create a _DASActivity from a BGTaskRequest missing a title (%@) or subtitle (%@)! Failing submission"
+ "Default"
+ "Fail"
+ "Failed to map launch reason to appropriate task type: %@"
+ "GPU"
+ "Identifier is too long, must be less than 128 characters: %@"
+ "Invalid identifier form for Continued Processing Task: %@"
+ "NSProgressReporting"
+ "Queue"
+ "Registration rejected; %@ is not advertised in the application's Info.plist"
+ "T@\"BGTaskRequest\",R,C"
+ "T@\"NSObject<OS_os_log>\",&,N,V_log"
+ "T@\"NSProgress\",R"
+ "T@\"NSProgress\",R,V_progress"
+ "T@\"NSSet\",R,N,V_permittedContinuedProcessingBaseNotationIdentifiers"
+ "T@\"NSSet\",R,N,V_permittedIdentifiers"
+ "T@\"NSString\",C,N,V_subtitle"
+ "T@\"NSString\",C,V_subtitle"
+ "T@\"_BGTaskIdentifierRegistry\",&,N,S_setIdentifierRegistry:,V__identifierRegistry"
+ "TaskIdentifierRegistry"
+ "Tq,N,V_requiredResources"
+ "Tq,N,V_strategy"
+ "Tq,R"
+ "Unrecognized Identifier"
+ "_BGTaskIdentifierRegistry"
+ "__identifierRegistry"
+ "_handleSubmissionWithoutRegistrationForTaskRequest:error:"
+ "_identifierRegistry"
+ "_permittedContinuedProcessingBaseNotationIdentifiers"
+ "_progress"
+ "_requiredResources"
+ "_setIdentifierRegistry:"
+ "_strategy"
+ "_subtitle"
+ "addObserver:forKeyPath:options:context:"
+ "bundleIdentifier"
+ "completeTaskRequest:withSuccess:"
+ "componentsJoinedByString:"
+ "componentsSeparatedByString:"
+ "containsString:"
+ "continuedProcessingDeviceCapabilities:"
+ "continuedProcessingWrapper"
+ "fractionCompleted"
+ "hasPrefix:"
+ "hasSuffix:"
+ "initWithContentsFromPlist"
+ "initWithIdentifier:title:subtitle:"
+ "initWithPermittedIdentifiers:"
+ "initWithTitle:subtitle:iconBundleIdentifier:resources:"
+ "initWithTitle:subtitle:resources:submissionStrategy:"
+ "isIdentifierValidContinuedProcessingBaseNotation:"
+ "isIdentifierValidContinuedProcessingComposedNotation:"
+ "isIdentifierValidContinuedProcessingWildcardNotation:"
+ "isPermissibleFullyComposedIdentifier:"
+ "length"
+ "log"
+ "numberWithInteger:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "permittedContinuedProcessingBaseNotationIdentifiers"
+ "permittedIdentifiers"
+ "progress"
+ "q"
+ "q16@0:8"
+ "registryWithContentsFromPlist"
+ "requestedResources"
+ "requiredResources"
+ "setContinuedProcessingWrapper:"
+ "setGroupName:"
+ "setLog:"
+ "setRequiredResources:"
+ "setStrategy:"
+ "setSubtitle:"
+ "strategy"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "subtitle"
+ "supportedResources"
+ "taskRequest"
+ "updateTitle:subtitle:"
+ "v16@?0q8"
+ "v24@0:8q16"
+ "v32@0:8@16^@24"
+ "v48@0:8@16@24@32^v40"
- ""
- "<BGContinuedProcessingTaskRequest: %@, title: %@>"
- "All launch handlers must be registered before application finishes launching"
- "T@\"NSSet\",&,N,S_setPermittedIdentifiers:,V__permittedIdentifiers"
- "T@\"NSString\",C,N,V_reason"
- "__permittedIdentifiers"
- "_setPermittedIdentifiers:"
- "activityWithName:priority:duration:startingAfter:startingBefore:userInfo:"
- "clientProvidedIconBundleIdentifier"
- "clientProvidedReason"
- "clientProvidedTitle"
- "completeTaskRequest:"
- "setClientProvidedReason:"
- "setClientProvidedTitle:"
- "setWithArray:"

```
