## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/Versions/A/RunningBoard`

```diff

-945.80.1.0.1
-  __TEXT.__text: 0x850c8
-  __TEXT.__auth_stubs: 0x1300
-  __TEXT.__objc_methlist: 0x5008
-  __TEXT.__const: 0x208
-  __TEXT.__cstring: 0x6a1b
-  __TEXT.__oslogstring: 0xae83
-  __TEXT.__gcc_except_tab: 0xc98
-  __TEXT.__unwind_info: 0x1998
+961.100.17.0.0
+  __TEXT.__text: 0x84104
+  __TEXT.__auth_stubs: 0x1310
+  __TEXT.__objc_methlist: 0x5e94
+  __TEXT.__const: 0x210
+  __TEXT.__cstring: 0x6a35
+  __TEXT.__oslogstring: 0xafd7
+  __TEXT.__gcc_except_tab: 0xc58
+  __TEXT.__unwind_info: 0x1a28
   __TEXT.__objc_classname: 0xee8
-  __TEXT.__objc_methname: 0xc85c
-  __TEXT.__objc_methtype: 0x2c2a
-  __TEXT.__objc_stubs: 0x96c0
-  __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x2d0
+  __TEXT.__objc_methname: 0xc9e4
+  __TEXT.__objc_methtype: 0x2c94
+  __TEXT.__objc_stubs: 0x97c0
+  __DATA_CONST.__got: 0x728
+  __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x360
-  __DATA_CONST.__objc_catlist: 0x160
+  __DATA_CONST.__objc_catlist: 0x168
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a60
+  __DATA_CONST.__objc_selrefs: 0x2b30
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x688
-  __AUTH_CONST.__auth_got: 0x990
-  __AUTH_CONST.__const: 0x1be0
-  __AUTH_CONST.__cfstring: 0x5860
-  __AUTH_CONST.__objc_const: 0xe8b0
+  __AUTH_CONST.__auth_got: 0x998
+  __AUTH_CONST.__const: 0x1cd0
+  __AUTH_CONST.__cfstring: 0x5820
+  __AUTH_CONST.__objc_const: 0xd150
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH.__objc_data: 0x21c0
-  __DATA.__objc_ivar: 0x9e4
+  __DATA.__objc_ivar: 0x9f8
   __DATA.__data: 0x12d0
   __DATA.__bss: 0x250
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 598713B7-125C-36E9-BB10-7B29D38E8A25
-  Functions: 2598
-  Symbols:   6411
-  CStrings:  4993
+  UUID: B801457C-E76D-346C-9877-9F1561704327
+  Functions: 2726
+  Symbols:   6563
+  CStrings:  5009
 
Symbols:
+ +[RBAssertionAcquisitionContext contextForProcess:withDescriptor:daemonContext:].cold.1
+ +[RBAssertionAcquisitionContext contextForProcess:withDescriptor:daemonContext:].cold.2
+ +[RBAssertionBatchContext contextForProcess:acquisitionCompletionPolicy:withDescriptorsToAcquire:identifiersToInvalidate:daemonContext:].cold.1
+ +[RBAssertionBatchContext contextForProcess:acquisitionCompletionPolicy:withDescriptorsToAcquire:identifiersToInvalidate:daemonContext:].cold.2
+ +[RBAssertionBatchContext contextForProcess:acquisitionCompletionPolicy:withDescriptorsToAcquire:identifiersToInvalidate:daemonContext:].cold.3
+ +[RBAssertionBatchContext contextForProcess:withDescriptorsToAcquire:identifiersToInvalidate:daemonContext:].cold.1
+ +[RBAssertionBatchContext contextForProcess:withDescriptorsToAcquire:identifiersToInvalidate:daemonContext:].cold.2
+ +[RBAssertionBatchContext contextForProcess:withDescriptorsToAcquire:identifiersToInvalidate:daemonContext:].cold.3
+ +[RBAssertionManager sharedWorkloop].cold.1
+ +[RBAttributeFactory _attributeClassesByName].cold.1
+ +[RBAttributeFactory _legalPropertyNamesAndValuesByClassName].cold.1
+ +[RBConcreteTarget systemTarget].cold.1
+ +[RBConcreteTarget targetWithProcess:environment:].cold.1
+ +[RBConnectionClient sharedLaunchWorkloop].cold.1
+ +[RBConnectionClient sharedTerminationWorkloop].cold.1
+ +[RBConnectionListener sharedConnectionWorkloop].cold.1
+ +[RBDaemon _sharedInstance].cold.1
+ +[RBDaemon run].cold.1
+ +[RBEntitlementManager _hardCodedEntitlements].cold.1
+ +[RBEntitlements _entitlementsForOption:]
+ +[RBEntitlements _entitlementsForOption:].cold.1
+ +[RBEntitlements _entitlementsForOptions:]
+ +[RBJetsamPropertyManager _taskLimit].cold.1
+ +[RBLessThanConditionDomainRestriction domainRestrictionForDictionary:withError:].cold.1
+ +[RBProcess _runOnDiagnosticQueue:].cold.1
+ +[RBProcess processStateApplicationQueue].cold.1
+ +[RBProcessAppNapState defaultState].cold.1
+ +[RBProcessManager stateApplicationQueue].cold.1
+ +[RBProcessMonitor _clientStateForServerState:process:].cold.1
+ +[RBResourceViolationHandler sharedInstance].cold.1
+ +[RBTargetsHostedDomainRestriction domainRestrictionForDictionary:withError:].cold.1
+ +[RBTargetsSelfDomainRestriction domainRestrictionForDictionary:withError:].cold.1
+ +[RBTimeProvider sharedInstance].cold.1
+ +[RBXNUWrapper sharedWrapper].cold.1
+ -[LSApplicationProxy(RBEntitlements) rb_hasEntitlement:]
+ -[LSApplicationProxy(RBEntitlements) rb_hasEntitlementDomain:]
+ -[RBAssertion isLaunchAssertion]
+ -[RBAssertion setLaunchAssertion:]
+ -[RBAssertionAcquisitionContext launchAssertion]
+ -[RBAssertionAcquisitionContext setLaunchAssertion:]
+ -[RBAssertionBatchContext launchAssertion]
+ -[RBAssertionBatchContext setLaunchAssertion:]
+ -[RBAssertionDescriptorValidator isAssertionValidForContext:error:].cold.1
+ -[RBAssertionDescriptorValidator isAssertionValidForContext:error:].cold.2
+ -[RBAssertionDescriptorValidator isAssertionValidForContext:error:].cold.3
+ -[RBAssertionDescriptorValidator isAssertionValidForContext:error:].cold.4
+ -[RBAssertionDescriptorValidator isAssertionValidForContext:error:].cold.5
+ -[RBAssertionDescriptorValidator isAssertionValidForContext:error:].cold.6
+ -[RBAssertionDescriptorValidator isAssertionValidForContext:error:].cold.7
+ -[RBAssertionManager _concreteTargetForTarget:allowAbstractTarget:].cold.1
+ -[RBAssertionManager _lock_deactivateAssertions:].cold.1
+ -[RBAssertionManager _lock_validateDescriptor:originatorProcess:originatorState:concreteTarget:targetProcess:targetIdentity:targetIdentifier:targetState:acquisitionContext:error:].cold.1
+ -[RBAssertionManager assertionWithIdentifier:]
+ -[RBAssertionManager commitBatchWithContext:completion:].cold.2
+ -[RBAssertionManager hasAssertionWithIdentifierForTarget:identifier:]
+ -[RBAssertionManager initWithDelegate:bundlePropertiesManager:originatorPidStore:assertionDescriptorValidator:timeProvider:daemonContext:maxOperationsInFlight:maxAssertionsPerOriginator:].cold.1
+ -[RBAssertionManager initWithDelegate:bundlePropertiesManager:originatorPidStore:assertionDescriptorValidator:timeProvider:daemonContext:maxOperationsInFlight:maxAssertionsPerOriginator:].cold.2
+ -[RBAssertionManager initWithDelegate:bundlePropertiesManager:originatorPidStore:assertionDescriptorValidator:timeProvider:daemonContext:maxOperationsInFlight:maxAssertionsPerOriginator:].cold.3
+ -[RBAssertionManager initWithDelegate:bundlePropertiesManager:originatorPidStore:assertionDescriptorValidator:timeProvider:daemonContext:maxOperationsInFlight:maxAssertionsPerOriginator:].cold.4
+ -[RBAssertionManager initWithDelegate:bundlePropertiesManager:originatorPidStore:assertionDescriptorValidator:timeProvider:daemonContext:maxOperationsInFlight:maxAssertionsPerOriginator:].cold.5
+ -[RBAssertionManager invalidateAssertionWithIdentifier:].cold.1
+ -[RBAssertionResolutionContext _resolveProcessStateForTarget:ofType:viaAssertion:].cold.1
+ -[RBConnectionClient rb_hasEntitlement:]
+ -[RBConnectionClient rb_hasEntitlementDomain:]
+ -[RBContainerManager _allowedContainerOverrideIdentifiers].cold.1
+ -[RBEntitlementManager initWithDomainAttributeEntitlements:].cold.1
+ -[RBEntitlements rb_hasEntitlement:]
+ -[RBEntitlements rb_hasEntitlementDomain:]
+ -[RBIgnoreAllEntitlementsManager rb_hasEntitlement:]
+ -[RBIgnoreAllEntitlementsManager rb_hasEntitlementDomain:]
+ -[RBLaunchdJobManager _removeJobWithInstance:orJob:error:].cold.3
+ -[RBLaunchdJobManager synchronizeJobs].cold.7
+ -[RBMutableInheritanceCollection addInheritance:].cold.1
+ -[RBMutableInheritanceCollection removeInheritance:].cold.1
+ -[RBPowerAssertion dealloc].cold.1
+ -[RBPowerAssertionManager _queue_invalidateAssertion:].cold.1
+ -[RBPrewarmManager initWithDelegate:timeProvider:].cold.1
+ -[RBPrewarmManager initWithDelegate:timeProvider:].cold.2
+ -[RBProcess _initWithInstance:auditToken:bundleProperties:jetsamProperties:initialState:hostProcess:properties:systemPreventsIdleSleep:cache:].cold.3
+ -[RBProcess _initWithInstance:auditToken:bundleProperties:jetsamProperties:initialState:hostProcess:properties:systemPreventsIdleSleep:cache:].cold.4
+ -[RBProcess launchAssertionIdentifier]
+ -[RBProcess setLaunchAssertionIdentifier:]
+ -[RBProcess setTerminating:].cold.1
+ -[RBProcessManager _executeLaunchRequest:withError:].cold.1
+ -[RBProcessManager _executeLifecycleEventForIdentity:sync:withBlock:].cold.1
+ -[RBProcessManager _getLifecycleQueueForIdentity:].cold.2
+ -[RBProcessManager _getLifecycleQueueForIdentity:].cold.3
+ -[RBProcessManager _lifecycleQueue_addProcessWithInstance:properties:].cold.5
+ -[RBProcessManager _releaseLifecycleQueueForIdentity:].cold.2
+ -[RBProcessManager executeLaunchRequest:withCompletion:].cold.1
+ -[RBProcessManager executeTerminateRequest:completion:].cold.4
+ -[RBProcessMap addIdentity:].cold.1
+ -[RBProcessMap removeIdentity:].cold.1
+ -[RBProcessMap setValue:forIdentity:].cold.1
+ -[RBProcessMonitorObserver _checkForBadActorWithPendingStates:].cold.1
+ -[RBProcessMonitorObserver _checkForBadActorWithPendingStates:].cold.2
+ -[RBProcessMonitorObserver _checkForBadActorWithPendingStates:].cold.3
+ -[RBProcessMonitorObserver _lock_sendPendingStateUpdates].cold.3
+ -[RBProcessMonitorObserver _lock_sendPendingStateUpdates].cold.4
+ -[RBProcessMonitorObserver _lock_sendPendingStateUpdates].cold.5
+ -[RBProcessMonitorObserver dealloc].cold.1
+ -[RBProcessMonitorObserver initWithMonitor:forProcess:connection:].cold.1
+ -[RBProcessMonitorObserver initWithMonitor:forProcess:connection:].cold.2
+ -[RBProcessMonitorObserver initWithMonitor:forProcess:connection:].cold.3
+ -[RBProcessState initWithIdentity:].cold.1
+ -[RBSLegacyAttribute(RBProcessState) applyToAssertionIntransientState:attributePath:context:].cold.2
+ -[RBSLegacyAttribute(RBProcessState) applyToAssertionTransientState:attributePath:context:].cold.2
+ -[RBSLegacyAttribute(RBProcessState) isValidForContext:withError:].cold.2
+ -[RBSLegacyAttribute(RBProcessState) isValidForContext:withError:].cold.3
+ -[RBXPCBundleProperties initWithPID:].cold.1
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table137
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table56
+ GCC_except_table57
+ OBJC_IVAR_$_RBAssertion._launchAssertion
+ OBJC_IVAR_$_RBAssertionAcquisitionContext._launchAssertion
+ OBJC_IVAR_$_RBAssertionBatchContext._launchAssertion
+ OBJC_IVAR_$_RBProcess._launchAssertion
+ OBJC_IVAR_$_RBProcess._launchAssertionIdentifier
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _RBLogAddStateCaptureBlockWithTitle.cold.1
+ _RBLogAddStateCaptureBlockWithTitle.cold.2
+ _RBLogAddStateCaptureBlockWithTitle.cold.3
+ _RBSAppViewServiceSessionVendingEntitlement
+ __140-[RBAssertionManager _acquireAssertions:invalidateIdentifiers:forOriginatorProcess:completionPolicy:acquisitionErrorsByIndex:completeStage:]_block_invoke.145
+ __36-[RBConnectionClient handleMessage:]_block_invoke.46.cold.1
+ __39-[RBAssertionManager processDidLaunch:]_block_invoke.70
+ __54-[RBProcessManager didUpdateProcessStates:completion:]_block_invoke.89
+ __56-[RBAssertionManager commitBatchWithContext:completion:]_block_invoke.cold.2
+ __60-[RBLaunchdJobManager invokeOnProcessDeath:handler:onQueue:]_block_invoke.152
+ __70-[RBProcessManager _enqueueGuaranteedRunningLaunchForIdentity:atTime:]_block_invoke.85
+ __80-[RBRequestManager executeLaunchRequest:euid:requestor:entitlements:completion:]_block_invoke.21
+ __88-[RBLaunchdJobManager _addAppPropertiesToData:forIdentity:context:actualIdentity:error:]_block_invoke.46
+ __MergedGlobals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_LSApplicationProxy_$_RBEntitlements
+ __OBJC_$_CATEGORY_LSApplicationProxy_$_RBEntitlements
+ __OBJC_$_PROP_LIST_LSApplicationProxy_$_RBEntitlements
+ __OBJC_CATEGORY_PROTOCOLS_$_LSApplicationProxy_$_RBEntitlements
+ ___42+[RBEntitlements _entitlementsForOptions:]_block_invoke
+ ___42-[RBEntitlements rb_hasEntitlementDomain:]_block_invoke
+ ___69-[RBAssertionManager hasAssertionWithIdentifierForTarget:identifier:]_block_invoke
+ ___88-[RBLaunchdJobManager _addAppPropertiesToData:forIdentity:context:actualIdentity:error:]_block_invoke
+ ____addRBProperties_block_invoke
+ ___block_descriptor_40_e8_32s_e22_v24?0"NSString"8^B16l
+ ___block_descriptor_48_e8_32s40r_e25_v24?0"RBAssertion"8^B16l
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"816^B24l
+ ___block_descriptor_48_e8_32s_e15_v28?0Q8i16^B20l
+ ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"816^B24l
+ __block_literal_global.147
+ __block_literal_global.72
+ __block_literal_global.91
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$entitlementValuesForKeys:
+ _objc_msgSend$isLaunchAssertion
+ _objc_msgSend$launchAssertion
+ _objc_msgSend$launchAssertionIdentifier
+ _objc_msgSend$launchRequestIdentifierToMachNameMap
+ _objc_msgSend$rb_hasEntitlement:
+ _objc_msgSend$rb_hasEntitlementDomain:
+ _objc_msgSend$setLaunchAssertion:
+ _objc_msgSend$setLaunchAssertionIdentifier:
+ _objc_msgSend$setWithCapacity:
+ _xpc_array_create_empty
- -[RBAssertion _initWithTarget:identifier:explanation:attributes:originator:context:creationTime:].cold.1
- -[RBAssertion applyToProcessState:withAttributeContext:].cold.1
- -[RBAssertion applyToSystemState:withAttributeContext:].cold.1
- -[RBAssertionManagerEventQueue _queue_enqueueEventsForAssertion:].cold.1
- -[RBAssertionManagerEventQueue _queue_removeEventsForContext:].cold.1
- -[RBAssertionManagerEventQueue _queue_updateEventsForAssertion:].cold.1
- -[RBAssertionOriginatorPidStore _lock_addPidToSharedMemory:].cold.1
- -[RBAssertionOriginatorPidStore _lock_allocSharedMemoryWithName:size:address:fileDescriptor:created:].cold.1
- -[RBAssertionOriginatorPidStore _lock_allocSharedMemoryWithName:size:address:fileDescriptor:created:].cold.2
- -[RBAssertionOriginatorPidStore _lock_isHeaderValid].cold.1
- -[RBAssertionOriginatorPidStore _lock_removePidFromSharedMemory:].cold.1
- -[RBAssertionOriginatorPidStore _lock_resizeSharedMemoryIfNecessary].cold.1
- -[RBAssertionOriginatorPidStore _lock_resizeSharedMemoryIfNecessary].cold.2
- -[RBAssertionOriginatorPidStore _lock_resizeSharedMemoryIfNecessary].cold.3
- -[RBConnectionClient _canInvalidateAssertionWithIdentifier:error:].cold.1
- -[RBConnectionClient _requestPluginHoldForProxy:terminate:completion:].cold.1
- -[RBConnectionClient didInvalidateAssertions:].cold.1
- -[RBConnectionClient executeTerminateRequest:withReply:].cold.1
- -[RBConnectionClient executeTerminateRequest:withReply:].cold.2
- -[RBConnectionClient handshakeWithRequest:].cold.1
- -[RBConnectionClient hasEntitlement:]
- -[RBConnectionClient hasEntitlementDomain:]
- -[RBConnectionClient hostProcessForInstance:error:].cold.1
- -[RBConnectionClient infoPlistResultForInstance:forKeys:error:].cold.1
- -[RBConnectionClient isIdentityAnAngel:withError:].cold.1
- -[RBConnectionClient isIdentityAnAngel:withError:].cold.2
- -[RBConnectionClient lastExitContextForInstance:error:].cold.1
- -[RBConnectionClient limitationsForInstance:error:].cold.1
- -[RBConnectionClient lookupHandleForKey:error:].cold.1
- -[RBConnectionClient lookupHandleForKey:error:].cold.2
- -[RBConnectionClient lookupHandleForPredicate:error:].cold.1
- -[RBConnectionClient lookupHandleForPredicate:error:].cold.2
- -[RBConnectionClient lookupHandleForPredicate:error:].cold.3
- -[RBConnectionClient lookupPortForIdentifier:error:].cold.1
- -[RBConnectionClient lookupProcessName:error:].cold.1
- -[RBConnectionClient preventLaunchPredicates].cold.1
- -[RBConnectionClient saveEndowment:withError:].cold.1
- -[RBConnectionClient statesForPredicate:withDescriptor:withReply:].cold.1
- -[RBConnectionClient subscribeToProcessDeath:error:].cold.1
- -[RBConnectionClient subscribeToProcessStateChangesWithConfiguration:error:].cold.1
- -[RBDomainAttributeManagerDataProvider _attributeTemplateGroupsFromArray:forDomainAttributeWithDomain:name:errors:].cold.1
- -[RBDomainAttributeManagerDataProvider _attributeTemplatesFromArray:forDomainAttributeWithDomain:name:errors:].cold.1
- -[RBDomainAttributeManagerDataProvider _attributeTemplatesFromArray:forDomainAttributeWithDomain:name:errors:].cold.2
- -[RBDomainAttributeManagerDataProvider _isPropertyLegalForClassName:propertyName:value:error:].cold.1
- -[RBDomainAttributeManagerDataProvider _preAttributeTemplateFromAttributeTemplate:domainAttributeTemplate:generateDependenciesByFullyQualifiedName:].cold.1
- -[RBDomainAttributeManagerDataProvider _templateWithDomain:name:dictionary:errors:].cold.1
- -[RBDomainAttributeManagerDataProvider _templateWithDomain:name:dictionary:errors:].cold.2
- -[RBDomainAttributeManagerDataProvider _templateWithDomain:name:dictionary:errors:].cold.3
- -[RBDomainAttributeManagerDataProvider _templatesByDomainWithErrors:].cold.1
- -[RBDomainAttributeManagerDataProvider _templatesByDomainWithErrors:].cold.2
- -[RBDomainAttributeManagerDataProvider _templatesByDomainWithErrors:].cold.3
- -[RBDomainAttributeManagerDataProvider _validatedAttributeTemplateFromAttributeTemplate:domainAttributeTemplate:dependenciesByFullyQualifiedName:errors:].cold.1
- -[RBDomainAttributeManagerDataProvider _validatedAttributeTemplateFromAttributeTemplate:domainAttributeTemplate:dependenciesByFullyQualifiedName:errors:].cold.2
- -[RBEntitlementManager _entitlementsForProcess:].cold.1
- -[RBEntitlementManager _entitlementsForProcess:].cold.2
- -[RBEntitlementManager _secTask:hasEntitlement:].cold.1
- -[RBEntitlements _entitlementsForOption:]
- -[RBEntitlements hasEntitlement:]
- -[RBEntitlements hasEntitlementDomain:]
- -[RBEventQueue _queue_processEvents].cold.1
- -[RBEventQueue _queue_processEvents].cold.2
- -[RBEventQueue _queue_startEventTimer].cold.1
- -[RBEventQueue _queue_startEventTimer].cold.2
- -[RBEventQueue _queue_startEventTimer].cold.3
- -[RBEventQueue _queue_startEventTimer].cold.4
- -[RBEventQueue _queue_startEventTimer].cold.5
- -[RBIgnoreAllEntitlementsManager hasEntitlement:]
- -[RBIgnoreAllEntitlementsManager hasEntitlementDomain:]
- -[RBJetsamPropertyManager _addJetsamValuesForSection:fromPlist:toDatabase:].cold.1
- -[RBJetsamPropertyManager _addJetsamValuesForSection:fromPlist:toDatabase:].cold.2
- -[RBJetsamPropertyManager _jetsamTargetType].cold.1
- -[RBJetsamPropertyManager _jetsamTargetType].cold.2
- -[RBJetsamPropertyManager _loadJetsamProperties].cold.1
- -[RBJetsamPropertyManager _prepareJetsamData:].cold.1
- -[RBJetsamPropertyManager _prepareJetsamData:].cold.2
- -[RBJetsamPropertyManager _taskLimitForProcess:].cold.1
- -[RBJetsamPropertyManager _unLimitForProcess:].cold.1
- -[RBPowerAssertion updateWithAcquisitionHandler:invalidationHander:].cold.1
- -[RBPowerAssertion updateWithAcquisitionHandler:invalidationHander:].cold.2
- -[RBPowerAssertion updateWithAcquisitionHandler:invalidationHander:].cold.3
- -[RBProcess _allowedLockedFilePaths].cold.1
- -[RBProcess _allowedLockedFilePaths].cold.2
- -[RBProcess _allowedLockedFilePaths].cold.3
- -[RBProcess _allowedLockedFilePaths].cold.4
- -[RBProcess _allowedLockedFilePaths].cold.5
- -[RBProcess _allowedLockedFilePaths].cold.6
- -[RBProcess _allowedLockedFilePaths].cold.7
- -[RBProcess _applyJetsamLenientModeState:].cold.1
- -[RBProcess _applyJetsamLenientModeState:].cold.2
- -[RBProcess _lock_applyCurrentStateIfPossible].cold.1
- -[RBProcess _lock_applyGPU].cold.1
- -[RBProcess _lock_applyMemoryLimits].cold.1
- -[RBProcess _lock_applyMemoryLimits].cold.2
- -[RBProcess _lock_applyMemoryLimits].cold.3
- -[RBProcess _lock_applyRole].cold.1
- -[RBProcess _lock_disableCPULimits].cold.1
- -[RBProcess _lock_lockedFilePathsIgnoring:].cold.1
- -[RBProcess _lock_restoreCPULimitDefaults].cold.1
- -[RBProcess _lock_resumeCPUMonitoring].cold.1
- -[RBProcess _lock_resume].cold.1
- -[RBProcess _lock_resume].cold.2
- -[RBProcess _lock_resume].cold.3
- -[RBProcess _lock_setCPULimits:violationPolicy:].cold.1
- -[RBProcess _lock_shutdownSocketsAndLog:].cold.1
- -[RBProcess _lock_suspend].cold.1
- -[RBProcess _lock_suspend].cold.2
- -[RBProcess _memoryStatusControl:flags:].cold.1
- -[RBProcessMonitor _queue_adjustMemoryPageThresholdLimitationForProcess:oldState:newState:].cold.1
- -[RBProcessMonitor _queue_publishState:forIdentity:].cold.1
- -[RBProcessMonitor _queue_suppressUpdatesForIdentity:].cold.1
- -[RBProcessMonitor _queue_suppressUpdatesForIdentity:].cold.2
- -[RBProcessMonitor _queue_unsuppressUpdatesForIdentity:].cold.1
- -[RBProcessMonitor _queue_unsuppressUpdatesForIdentity:].cold.2
- -[RBProcessMonitor _queue_updateServerState:forProcess:force:].cold.1
- -[RBProcessReconnectManager _assertionAttributes].cold.1
- -[RBResourceViolationHandler handleCPUViolationMessage:fromConnection:].cold.1
- -[RBResourceViolationHandler handleCPUViolationMessage:fromConnection:].cold.2
- -[RBResourceViolationHandler handleMessage:fromConnection:].cold.1
- -[RBResourceViolationHandler startWithAssertionManager:].cold.1
- GCC_except_table123
- GCC_except_table130
- GCC_except_table132
- GCC_except_table48
- GCC_except_table49
- _RBViewServicesEntitlement
- __140-[RBAssertionManager _acquireAssertions:invalidateIdentifiers:forOriginatorProcess:completionPolicy:acquisitionErrorsByIndex:completeStage:]_block_invoke.143
- __39-[RBAssertionManager processDidLaunch:]_block_invoke.69
- __54-[RBProcessManager didUpdateProcessStates:completion:]_block_invoke.91
- __60-[RBLaunchdJobManager invokeOnProcessDeath:handler:onQueue:]_block_invoke.146
- __70-[RBProcessManager _enqueueGuaranteedRunningLaunchForIdentity:atTime:]_block_invoke.87
- __80-[RBRequestManager executeLaunchRequest:euid:requestor:entitlements:completion:]_block_invoke.22
- __83-[RBDomainAttributeManagerDataProvider _templatesWithDomain:fromDictionary:errors:]_block_invoke.cold.1
- __89-[RBDomainAttributeManagerDataProvider _templatesWithDomain:fromFilename:dirpath:errors:]_block_invoke.cold.1
- ___39-[RBEntitlements hasEntitlementDomain:]_block_invoke
- __block_literal_global.145
- __block_literal_global.71
- __block_literal_global.95
- _applyJetsamLenientModeState:.count
- _applyJetsamLenientModeState:.lock
- _backgroundContentFetchingProcessAssertionDuration.__backgroundContentFetchingProcessAssertionDuration
- _backgroundContentFetchingProcessAssertionDuration.onceToken
- _backgroundTaskCompletionDurationAllowedAfterContentFetchingAssertion.__backgroundTaskCompletionDurationAllowedAfterContentFetchingAssertion
- _backgroundTaskCompletionDurationAllowedAfterContentFetchingAssertion.onceToken
- _legalClassNames.legalClassNames
- _legalClassNames.onceToken
- _legalPropertyNamesByClassName.legalPropertyNamesByClassName
- _legalPropertyNamesByClassName.onceToken
- _objc_msgSend$entitlementValueForKey:ofClass:
- _objc_msgSend$hasEntitlement:
- _objc_msgSend$hasEntitlementDomain:
CStrings:
+ "\v3"
+ "%{public}@ ignoring unsupported LaunchRequestEndpointIdentifiers value for launchIdentifier %{public}@: value=%{public}@"
+ "%{public}@ ignoring unsupported MANAGEDBY_SERVICES value for launchIdentifier %{public}@: value=%{public}@"
+ "@\"RBAssertion\"24@0:8@\"RBSAssertionIdentifier\"16"
+ "B32@0:8@\"RBSProcessIdentity\"16@\"RBSAssertionIdentifier\"24"
+ "BUG IN %@: RunningBoard terminated %@ because it was suspended while holding a shared file lock:\n%@\nFile locks MUST be held in one of the following directories:\n%@"
+ "Invalidating %{public}lu assertions synchronously"
+ "Process: %@ with pid: %d; launch assertion: %@"
+ "Skipping assertion: %@ for invalidation as this doesn't belong to the terminating process: %@ with pid: %d"
+ "Specified target process %@ does not exist"
+ "T@\"RBSAssertionIdentifier\",&,N,V_launchAssertionIdentifier"
+ "TB,N,GisLaunchAssertion,V_launchAssertion"
+ "TB,N,V_launchAssertion"
+ "_ManagedBy_Services"
+ "_launchAssertion"
+ "_launchAssertionIdentifier"
+ "assertion failure: \"lassProps != ((void*)0)\" -> %llu"
+ "boolForKey:"
+ "entitlementValuesForKeys:"
+ "hasAssertionWithIdentifierForTarget:identifier:"
+ "isLaunchAssertion"
+ "launchAssertion"
+ "launchAssertionIdentifier"
+ "launchRequestIdentifierToMachNameMap"
+ "rb_hasEntitlement:"
+ "rb_hasEntitlementDomain:"
+ "setLaunchAssertion:"
+ "setLaunchAssertionIdentifier:"
+ "setWithCapacity:"
- "\v#"
- "%@ was suspended with locked system files:\n%@\nnot in allowed directories:\n%@"
- "Executing launch request for %{public}@ (%{public}@)"
- "Invalidating assertions synchronously"
- "Specified target process does not exist"
- "The running process did not match the expected."
- "assertion failure: \"lassProps != ((void *)0)\" -> %lld"
- "com.apple.UIKit.vends-view-services"
- "entitlementValueForKey:ofClass:"
- "hasEntitlement:"
- "hasEntitlementDomain:"

```
