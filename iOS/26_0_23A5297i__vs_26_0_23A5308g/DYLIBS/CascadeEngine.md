## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-198.0.0.0.0
-  __TEXT.__text: 0x1f744
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x17dc
+200.0.0.0.0
+  __TEXT.__text: 0x20330
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x1864
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x69c
-  __TEXT.__cstring: 0x107c
-  __TEXT.__oslogstring: 0x3bbb
+  __TEXT.__gcc_except_tab: 0x79c
+  __TEXT.__cstring: 0x127a
+  __TEXT.__oslogstring: 0x372b
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x848
-  __TEXT.__objc_classname: 0x46e
-  __TEXT.__objc_methname: 0x523e
-  __TEXT.__objc_methtype: 0xfcb
-  __TEXT.__objc_stubs: 0x4480
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0xb88
+  __TEXT.__unwind_info: 0x880
+  __TEXT.__objc_classname: 0x46f
+  __TEXT.__objc_methname: 0x551e
+  __TEXT.__objc_methtype: 0x1066
+  __TEXT.__objc_stubs: 0x4680
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0xb10
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1390
+  __DATA_CONST.__objc_selrefs: 0x13e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x3b0
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__objc_const: 0x3150
+  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__objc_const: 0x3330
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x25c
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x298
   __DATA.__data: 0x720
-  __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0x5f0
-  __DATA_DIRTY.__bss: 0x18
+  __DATA.__bss: 0x40
+  __DATA_DIRTY.__objc_data: 0x460
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A5FE258-ADA9-319A-907F-73E78ECF2EEB
-  Functions: 695
-  Symbols:   2771
-  CStrings:  1590
+  UUID: E347FCA0-A743-30AC-BB11-1DBD8BEF0DD0
+  Functions: 708
+  Symbols:   2809
+  CStrings:  1681
 
Symbols:
+ +[CCSetDiscoveryRequest setDiscoveryRequestFromPeerToPeerMessage:setUUIDsToDiscover:requestOptions:startAfterSet:sizeThreshold:]
+ +[CCSetDiscoveryResponse setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:responseOptions:]
+ +[CCSignalDoneFetchingMergeableDeltas doneFetchingMergeableDeltasMessageFromPeerToPeerMessage:isReciprocal:]
+ -[CCDonateRequestManager requestAccessToResource:withMode:error:]
+ -[CCRapportDevice prefix]
+ -[CCRapportManager activateDiscoveryClientWithCompletion:].cold.3
+ -[CCRapportManager activateFileTransferSessions:]
+ -[CCRapportManager buildFileTransferSessionWithTargetDeviceIdentifier:]
+ -[CCRapportManager buildFileTransferSessionWithTargetDeviceIdentifier:].cold.1
+ -[CCRapportManager buildFileTransferSessionWithTargetDeviceIdentifier:].cold.2
+ -[CCRapportManager closeAllFileTransferSessions]
+ -[CCRapportManager closeFileTransferSessionWithDeviceIdentifier:]
+ -[CCRapportManager deleteDanglingFilesFromFileTransferDirectory]
+ -[CCRapportManager deleteDanglingFilesFromFileTransferDirectory].cold.1
+ -[CCRapportManager deleteMergeableDeltaFileURL:]
+ -[CCRapportManager fileTransferDirectory]
+ -[CCRapportManager fileTransferQueue]
+ -[CCRapportManager fileTransferSessions]
+ -[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]
+ -[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:].cold.1
+ -[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:].cold.2
+ -[CCRapportManager setFileTransferDirectory:]
+ -[CCRapportSyncEngine _activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:]
+ -[CCRapportSyncEngine _deactivateSession]
+ -[CCRapportSyncEngine _failToActivateSessionWithError:activationHandler:sessionCompletionHandler:]
+ -[CCRapportSyncEngine _failToActivateSessionWithError:activationHandler:sessionCompletionHandler:].cold.1
+ -[CCRapportSyncEngine activateClientWithReason:activity:completionHandler:]
+ -[CCRapportSyncEngine activateServerWithReason:activationHandler:]
+ -[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:forInteraction:]
+ -[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:forInteraction:].cold.1
+ -[CCRapportSyncEngine buildBasePeerToPeerMessageForInteraction:]
+ -[CCRapportSyncEngine buildDoneFetchingMergeableDeltasMessageForInteraction:]
+ -[CCRapportSyncEngine continueAfterHandlingAllSetsToSyncForInteraction:]
+ -[CCRapportSyncEngine continueToDiscoverSetsToSyncForInteraction:]
+ -[CCRapportSyncEngine continueToHandleNextSetToSyncAtIndex:forInteraction:]
+ -[CCRapportSyncEngine determineSyncOperationForDiscoveredSet:forInteraction:outFetchRequest:]
+ -[CCRapportSyncEngine initWithQueue:rapportManager:readAccess:donateServiceProvider:localDeviceUUID:]
+ -[CCRapportSyncEngine readSetForDiscovery:senderDeviceUUID:]
+ -[CCRapportSyncEngine recordDiscoveredSetResources:forInteraction:]
+ -[CCRapportSyncEngine sendDoneFetchingMergeableDeltasRequest:forInteraction:]
+ -[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:]
+ -[CCRapportSyncEngine sendSetDiscoveryRequest:forInteraction:continueSync:]
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:]
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:].cold.1
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:].cold.2
+ -[CCRapportSyncEngine validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:].cold.3
+ -[CCRapportSyncInteraction .cxx_destruct]
+ -[CCRapportSyncInteraction cancelRapportRequestTimeout]
+ -[CCRapportSyncInteraction complete]
+ -[CCRapportSyncInteraction description]
+ -[CCRapportSyncInteraction detailedDescription]
+ -[CCRapportSyncInteraction device]
+ -[CCRapportSyncInteraction discoveredResources]
+ -[CCRapportSyncInteraction error]
+ -[CCRapportSyncInteraction initWithQueue:reason:device:index:type:options:completion:]
+ -[CCRapportSyncInteraction isRunning]
+ -[CCRapportSyncInteraction options]
+ -[CCRapportSyncInteraction reason]
+ -[CCRapportSyncInteraction repeatDiscoveryAfterSet]
+ -[CCRapportSyncInteraction setError:]
+ -[CCRapportSyncInteraction setRepeatDiscoveryAfterSet:]
+ -[CCRapportSyncInteraction setSetsToSync:]
+ -[CCRapportSyncInteraction setTimeoutForRapportRequest:]
+ -[CCRapportSyncInteraction setsToSync]
+ -[CCRapportSyncInteraction state]
+ -[CCRapportSyncInteraction type]
+ -[CCRapportSyncInteraction updateState:]
+ -[CCRapportSyncSession .cxx_destruct]
+ -[CCRapportSyncSession _addFlags:forInteractionType:]
+ -[CCRapportSyncSession _cancelNextInteractionTimeout]
+ -[CCRapportSyncSession _completeSession:]
+ -[CCRapportSyncSession _completeSession:].cold.1
+ -[CCRapportSyncSession _hasFlags:forInteractionType:]
+ -[CCRapportSyncSession _isRunningInteractionType:]
+ -[CCRapportSyncSession _runInteraction:]
+ -[CCRapportSyncSession _runInteraction:].cold.1
+ -[CCRapportSyncSession _runNextInteraction]
+ -[CCRapportSyncSession _setNextInteractionTimeout]
+ -[CCRapportSyncSession cancelInteractionType:withDevice:error:]
+ -[CCRapportSyncSession cancelInteractionType:withDevice:error:].cold.1
+ -[CCRapportSyncSession description]
+ -[CCRapportSyncSession initWithQueue:interactionHandler:]
+ -[CCRapportSyncSession interactionOfType:withDevice:]
+ -[CCRapportSyncSession operationId]
+ -[CCRapportSyncSession registerSessionActivationReason:forInteractionType:withOptions:completionHandler:]
+ -[CCRapportSyncSession submitInteractionType:withDevice:]
+ -[CCRapportSyncSession submitInteractionType:withDevice:reason:]
+ -[CCRapportSyncSession submitInteractionType:withDevice:reason:].cold.1
+ -[CCRapportSyncSession unblockInteractionType:]
+ -[CCRapportSyncSession uuid]
+ -[CCSetDiscoveryRequest requestOptions]
+ -[CCSetDiscoveryRequest setRequestOptions:]
+ -[CCSetDiscoveryRequest setSizeThreshold:]
+ -[CCSetDiscoveryRequest setStartAfterSet:]
+ -[CCSetDiscoveryRequest sizeThreshold]
+ -[CCSetDiscoveryRequest startAfterSet]
+ -[CCSetDiscoveryResponse responseOptions]
+ -[CCSetDiscoveryResponse setResponseOptions:]
+ -[CCSyncManager handleIncomingSyncRequestsWithReason:completionHandler:]
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table13
+ GCC_except_table15
+ GCC_except_table18
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table32
+ GCC_except_table99
+ _CCRapportSyncInteractionStateDescription
+ _CCRapportSyncInteractionTypeDescription
+ _CCRapportSyncOptionsDescription
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_CCRapportSyncInteraction
+ _OBJC_CLASS_$_CCRapportSyncSession
+ _OBJC_IVAR_$_CCRapportManager._fileTransferAccessAssertion
+ _OBJC_IVAR_$_CCRapportManager._fileTransferDirectory
+ _OBJC_IVAR_$_CCRapportManager._fileTransferQueue
+ _OBJC_IVAR_$_CCRapportManager._fileTransferSessions
+ _OBJC_IVAR_$_CCRapportSyncEngine._currentSession
+ _OBJC_IVAR_$_CCRapportSyncInteraction._completion
+ _OBJC_IVAR_$_CCRapportSyncInteraction._device
+ _OBJC_IVAR_$_CCRapportSyncInteraction._discoveredResources
+ _OBJC_IVAR_$_CCRapportSyncInteraction._error
+ _OBJC_IVAR_$_CCRapportSyncInteraction._index
+ _OBJC_IVAR_$_CCRapportSyncInteraction._options
+ _OBJC_IVAR_$_CCRapportSyncInteraction._queue
+ _OBJC_IVAR_$_CCRapportSyncInteraction._reason
+ _OBJC_IVAR_$_CCRapportSyncInteraction._repeatDiscoveryAfterSet
+ _OBJC_IVAR_$_CCRapportSyncInteraction._requestTimeout
+ _OBJC_IVAR_$_CCRapportSyncInteraction._setsToSync
+ _OBJC_IVAR_$_CCRapportSyncInteraction._state
+ _OBJC_IVAR_$_CCRapportSyncInteraction._type
+ _OBJC_IVAR_$_CCRapportSyncSession._activationReasons
+ _OBJC_IVAR_$_CCRapportSyncSession._completedInteractions
+ _OBJC_IVAR_$_CCRapportSyncSession._completionHandlers
+ _OBJC_IVAR_$_CCRapportSyncSession._flags
+ _OBJC_IVAR_$_CCRapportSyncSession._interactionHandler
+ _OBJC_IVAR_$_CCRapportSyncSession._interactionIndex
+ _OBJC_IVAR_$_CCRapportSyncSession._nextInteractionTimeout
+ _OBJC_IVAR_$_CCRapportSyncSession._operationId
+ _OBJC_IVAR_$_CCRapportSyncSession._options
+ _OBJC_IVAR_$_CCRapportSyncSession._queue
+ _OBJC_IVAR_$_CCRapportSyncSession._registeredInteractions
+ _OBJC_IVAR_$_CCRapportSyncSession._runningInteractions
+ _OBJC_IVAR_$_CCRapportSyncSession._transaction
+ _OBJC_IVAR_$_CCRapportSyncSession._uuid
+ _OBJC_IVAR_$_CCSetDiscoveryRequest._requestOptions
+ _OBJC_IVAR_$_CCSetDiscoveryRequest._sizeThreshold
+ _OBJC_IVAR_$_CCSetDiscoveryRequest._startAfterSet
+ _OBJC_IVAR_$_CCSetDiscoveryResponse._responseOptions
+ _OBJC_METACLASS_$_CCRapportSyncInteraction
+ _OBJC_METACLASS_$_CCRapportSyncSession
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ __OBJC_$_INSTANCE_METHODS_CCRapportSyncInteraction
+ __OBJC_$_INSTANCE_METHODS_CCRapportSyncSession
+ __OBJC_$_INSTANCE_VARIABLES_CCRapportSyncInteraction
+ __OBJC_$_INSTANCE_VARIABLES_CCRapportSyncSession
+ __OBJC_$_PROP_LIST_CCRapportSyncInteraction
+ __OBJC_$_PROP_LIST_CCRapportSyncSession
+ __OBJC_CLASS_RO_$_CCRapportSyncInteraction
+ __OBJC_CLASS_RO_$_CCRapportSyncSession
+ __OBJC_METACLASS_RO_$_CCRapportSyncInteraction
+ __OBJC_METACLASS_RO_$_CCRapportSyncSession
+ ___106-[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]_block_invoke
+ ___106-[CCRapportManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]_block_invoke.cold.1
+ ___116-[CCRapportSyncEngine _activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:]_block_invoke
+ ___116-[CCRapportSyncEngine _activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:]_block_invoke.27
+ ___116-[CCRapportSyncEngine _activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:]_block_invoke_2
+ ___40-[CCRapportSyncSession _runInteraction:]_block_invoke
+ ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.64
+ ___50-[CCRapportSyncSession _setNextInteractionTimeout]_block_invoke
+ ___56-[CCRapportSyncInteraction setTimeoutForRapportRequest:]_block_invoke
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.77
+ ___64-[CCRapportSyncSession submitInteractionType:withDevice:reason:]_block_invoke
+ ___66-[CCRapportSyncEngine activateServerWithReason:activationHandler:]_block_invoke
+ ___66-[CCRapportSyncEngine continueToDiscoverSetsToSyncForInteraction:]_block_invoke
+ ___69-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:forInteraction:]_block_invoke
+ ___69-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:forInteraction:]_block_invoke.cold.1
+ ___72-[CCSyncManager handleIncomingSyncRequestsWithReason:completionHandler:]_block_invoke
+ ___72-[CCSyncManager handleIncomingSyncRequestsWithReason:completionHandler:]_block_invoke.3
+ ___75-[CCRapportSyncEngine activateClientWithReason:activity:completionHandler:]_block_invoke
+ ___75-[CCRapportSyncEngine continueToHandleNextSetToSyncAtIndex:forInteraction:]_block_invoke
+ ___75-[CCRapportSyncEngine sendSetDiscoveryRequest:forInteraction:continueSync:]_block_invoke
+ ___77-[CCRapportSyncEngine sendDoneFetchingMergeableDeltasRequest:forInteraction:]_block_invoke
+ ___83-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:]_block_invoke
+ ___83-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:]_block_invoke.46
+ ___83-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:]_block_invoke.49
+ ___83-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:]_block_invoke_2
+ ___83-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e32_v16?0"RPFileTransferProgress"8ls32l8
+ ___block_descriptor_40_e8_32w_e34_v16?0"CCRapportSyncInteraction"8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e29_v24?0"NSArray"8"NSArray"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e19_v24?0"CCSet"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw56l8s32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e19_v24?0"CCSet"8^B16ls32l8r56l8s40l8r64l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8ls32l8s64l8s40l8s48l8s56l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw72l8s32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8s80l8
+ ___block_literal_global.82
+ ___block_literal_global.84
+ ___block_literal_global.86
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _objc_msgSend$_activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:
+ _objc_msgSend$_addFlags:forInteractionType:
+ _objc_msgSend$_cancelNextInteractionTimeout
+ _objc_msgSend$_completeSession:
+ _objc_msgSend$_deactivateSession
+ _objc_msgSend$_failToActivateSessionWithError:activationHandler:sessionCompletionHandler:
+ _objc_msgSend$_hasFlags:forInteractionType:
+ _objc_msgSend$_isRunningInteractionType:
+ _objc_msgSend$_runInteraction:
+ _objc_msgSend$_runNextInteraction
+ _objc_msgSend$_setNextInteractionTimeout
+ _objc_msgSend$activateClientWithReason:activity:completionHandler:
+ _objc_msgSend$activateFileTransferSessions:
+ _objc_msgSend$activateServerWithReason:activationHandler:
+ _objc_msgSend$addOmittedSetsFromSetDiscovery:forInteraction:
+ _objc_msgSend$buildBasePeerToPeerMessageForInteraction:
+ _objc_msgSend$buildDoneFetchingMergeableDeltasMessageForInteraction:
+ _objc_msgSend$cancelInteractionType:withDevice:error:
+ _objc_msgSend$cancelRapportRequestTimeout
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$container
+ _objc_msgSend$continueAfterHandlingAllSetsToSyncForInteraction:
+ _objc_msgSend$continueToDiscoverSetsToSyncForInteraction:
+ _objc_msgSend$continueToHandleNextSetToSyncAtIndex:forInteraction:
+ _objc_msgSend$detailedDescription
+ _objc_msgSend$determineSyncOperationForDiscoveredSet:forInteraction:outFetchRequest:
+ _objc_msgSend$discoveredResources
+ _objc_msgSend$doneFetchingMergeableDeltasMessageFromPeerToPeerMessage:isReciprocal:
+ _objc_msgSend$enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:
+ _objc_msgSend$error
+ _objc_msgSend$fileTransferDirectory
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$initWithQueue:interactionHandler:
+ _objc_msgSend$initWithQueue:rapportManager:readAccess:donateServiceProvider:localDeviceUUID:
+ _objc_msgSend$initWithQueue:reason:device:index:type:options:completion:
+ _objc_msgSend$interactionOfType:withDevice:
+ _objc_msgSend$isRunning
+ _objc_msgSend$lastObject
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$prefix
+ _objc_msgSend$readSetForDiscovery:senderDeviceUUID:
+ _objc_msgSend$reason
+ _objc_msgSend$recordDiscoveredSetResources:forInteraction:
+ _objc_msgSend$registerSessionActivationReason:forInteractionType:withOptions:completionHandler:
+ _objc_msgSend$repeatDiscoveryAfterSet
+ _objc_msgSend$requestAccessToResource:withMode:error:
+ _objc_msgSend$requestAccessToResource:withMode:useCase:error:
+ _objc_msgSend$responseOptions
+ _objc_msgSend$sendDoneFetchingMergeableDeltasRequest:forInteraction:
+ _objc_msgSend$sendFetchMergeableDeltasRequest:forInteraction:continueSync:
+ _objc_msgSend$sendSetDiscoveryRequest:forInteraction:continueSync:
+ _objc_msgSend$setDiscoveryRequestFromPeerToPeerMessage:setUUIDsToDiscover:requestOptions:startAfterSet:sizeThreshold:
+ _objc_msgSend$setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:responseOptions:
+ _objc_msgSend$setError:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setRepeatDiscoveryAfterSet:
+ _objc_msgSend$setResponseOptions:
+ _objc_msgSend$setSetsToSync:
+ _objc_msgSend$setSizeThreshold:
+ _objc_msgSend$setStartAfterSet:
+ _objc_msgSend$setTimeoutForRapportRequest:
+ _objc_msgSend$setsToSync
+ _objc_msgSend$sizeThreshold
+ _objc_msgSend$startAfterSet
+ _objc_msgSend$submitInteractionType:withDevice:
+ _objc_msgSend$submitInteractionType:withDevice:reason:
+ _objc_msgSend$type
+ _objc_msgSend$unblockInteractionType:
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$updateState:
+ _objc_msgSend$validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:
+ _objc_release_x1
+ _objc_retain_x6
- +[CCRapportFileTransferManager defaultInstance:]
- +[CCRapportFileTransferManager defaultInstance:].cold.1
- +[CCSetDiscoveryRequest setDiscoveryMessageFromPeerToPeerMessage:setUUIDsToDiscover:]
- +[CCSetDiscoveryResponse setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:]
- +[CCSignalDoneFetchingMergeableDeltas doneFetchingMergeableDeltasMessageFromPeerToPeerMessage:isReciprocal:rapportIdentifier:]
- -[CCDonateRequestManager requestAccess:forResource:withMode:error:]
- -[CCRapportDevice shortenedRapportIdentifier]
- -[CCRapportFileTransferManager .cxx_destruct]
- -[CCRapportFileTransferManager buildFileTransferSessionWithTargetDeviceIdentifier:]
- -[CCRapportFileTransferManager buildFileTransferSessionWithTargetDeviceIdentifier:].cold.1
- -[CCRapportFileTransferManager buildFileTransferSessionWithTargetDeviceIdentifier:].cold.2
- -[CCRapportFileTransferManager buildFileTransferSessionWithTargetDeviceIdentifier:].cold.3
- -[CCRapportFileTransferManager closeAllFileTransferSessions]
- -[CCRapportFileTransferManager closeFileTransferSessionWithDeviceIdentifier:]
- -[CCRapportFileTransferManager deleteDanglingFilesFromFileTransferDirectory]
- -[CCRapportFileTransferManager deleteDanglingFilesFromFileTransferDirectory].cold.1
- -[CCRapportFileTransferManager deleteMergeableDeltaFileURL:]
- -[CCRapportFileTransferManager directoryURL]
- -[CCRapportFileTransferManager fileTransferQueue]
- -[CCRapportFileTransferManager initWithDirectoryURL:accessAssertion:]
- -[CCRapportFileTransferManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]
- -[CCRapportFileTransferManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:].cold.1
- -[CCRapportFileTransferManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:].cold.2
- -[CCRapportFileTransferManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:].cold.3
- -[CCRapportManager didDiscoverDevice:].cold.4
- -[CCRapportRequest .cxx_destruct]
- -[CCRapportRequest activity]
- -[CCRapportRequest completionHandler]
- -[CCRapportRequest deliveredToDevices]
- -[CCRapportRequest description]
- -[CCRapportRequest deviceAttributedErrors]
- -[CCRapportRequest errorFromDevice]
- -[CCRapportRequest inFlightToDevices]
- -[CCRapportRequest initWithUUID:reason:activity:queue:completionHandler:]
- -[CCRapportRequest markAsDeliveredToDevice:withError:]
- -[CCRapportRequest markAsInFlightToDevice:]
- -[CCRapportRequest queue]
- -[CCRapportRequest requestTimeoutDidFire]
- -[CCRapportRequest requestTimeoutHandler]
- -[CCRapportRequest requestTimeout]
- -[CCRapportRequest setActivity:]
- -[CCRapportRequest setCompletionHandler:]
- -[CCRapportRequest setDeliveredToDevices:]
- -[CCRapportRequest setErrorFromDevice:]
- -[CCRapportRequest setInFlightToDevices:]
- -[CCRapportRequest setQueue:]
- -[CCRapportRequest setRequestTimeout:]
- -[CCRapportRequest setRequestTimeoutHandler:]
- -[CCRapportRequest setSetsToSyncFromDevice:]
- -[CCRapportRequest setState:]
- -[CCRapportRequest setSyncReason:]
- -[CCRapportRequest setUuid:]
- -[CCRapportRequest setsToSyncFromDevice]
- -[CCRapportRequest startRequestTimeout]
- -[CCRapportRequest state]
- -[CCRapportRequest stopRequestTimeout]
- -[CCRapportRequest syncReason]
- -[CCRapportRequest uuid]
- -[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:]
- -[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:].cold.1
- -[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]
- -[CCRapportSyncEngine buildBasePeerToPeerMessage]
- -[CCRapportSyncEngine buildDoneFetchingMergeableDeltasMessageToDevice:withIsReciprocal:]
- -[CCRapportSyncEngine completeRequestAsDeliveredToDevices:withErrors:]
- -[CCRapportSyncEngine completeRequestIfDeliveredToAllNearbyDevices]
- -[CCRapportSyncEngine determineSyncOperationForDiscoveredSet:withDevice:outFetchRequest:]
- -[CCRapportSyncEngine initWithQueue:error:].cold.2
- -[CCRapportSyncEngine initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:localDeviceUUID:]
- -[CCRapportSyncEngine reciprocateSyncRequestWithDevice:completionHandler:]
- -[CCRapportSyncEngine registerRequestsWithCompletionHandler:]
- -[CCRapportSyncEngine sendDoneFetchingMergeableDeltasRequest:toDevice:completionHandler:]
- -[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]
- -[CCRapportSyncEngine sendSetDiscoveryRequest:toDevice:completionHandler:]
- -[CCRapportSyncEngine startClient]
- -[CCRapportSyncEngine startServerWithCompletion:]
- -[CCRapportSyncEngine startSyncRequestWithReason:activity:completionHandler:]
- -[CCRapportSyncEngine startSyncRequestWithReason:activity:completionHandler:].cold.1
- -[CCRapportSyncEngine startSyncRequestWithReason:activity:completionHandler:].cold.2
- -[CCRapportSyncEngine syncNowWithReason:activity:completionHandler:]
- -[CCRapportSyncEngine teardown]
- -[CCRapportSyncEngine teardown].cold.1
- -[CCSignalDoneFetchingMergeableDeltas .cxx_destruct]
- -[CCSignalDoneFetchingMergeableDeltas rapportIdentifier]
- -[CCSignalDoneFetchingMergeableDeltas setRapportIdentifier:]
- -[CCSyncManager handleIncomingSyncRequestsWithCompletionHandler:]
- GCC_except_table50
- GCC_except_table52
- GCC_except_table54
- GCC_except_table71
- GCC_except_table8
- GCC_except_table89
- GCC_except_table90
- GCC_except_table95
- GCC_except_table98
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_CCRapportFileTransferManager
- _OBJC_CLASS_$_CCRapportRequest
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_IVAR_$_CCRapportFileTransferManager._accessAssertion
- _OBJC_IVAR_$_CCRapportFileTransferManager._directoryURL
- _OBJC_IVAR_$_CCRapportFileTransferManager._fileTransferQueue
- _OBJC_IVAR_$_CCRapportFileTransferManager._fileTransferSessions
- _OBJC_IVAR_$_CCRapportRequest._activity
- _OBJC_IVAR_$_CCRapportRequest._completionHandler
- _OBJC_IVAR_$_CCRapportRequest._deliveredToDevices
- _OBJC_IVAR_$_CCRapportRequest._errorFromDevice
- _OBJC_IVAR_$_CCRapportRequest._inFlightToDevices
- _OBJC_IVAR_$_CCRapportRequest._queue
- _OBJC_IVAR_$_CCRapportRequest._requestTimeout
- _OBJC_IVAR_$_CCRapportRequest._requestTimeoutHandler
- _OBJC_IVAR_$_CCRapportRequest._setsToSyncFromDevice
- _OBJC_IVAR_$_CCRapportRequest._state
- _OBJC_IVAR_$_CCRapportRequest._syncReason
- _OBJC_IVAR_$_CCRapportRequest._transaction
- _OBJC_IVAR_$_CCRapportRequest._uuid
- _OBJC_IVAR_$_CCRapportSyncEngine._currentRequest
- _OBJC_IVAR_$_CCRapportSyncEngine._fileTransferSessionManager
- _OBJC_IVAR_$_CCRapportSyncEngine._operationQueue
- _OBJC_IVAR_$_CCSignalDoneFetchingMergeableDeltas._rapportIdentifier
- _OBJC_METACLASS_$_CCRapportFileTransferManager
- _OBJC_METACLASS_$_CCRapportRequest
- __OBJC_$_CLASS_METHODS_CCRapportFileTransferManager
- __OBJC_$_INSTANCE_METHODS_CCRapportFileTransferManager
- __OBJC_$_INSTANCE_METHODS_CCRapportRequest
- __OBJC_$_INSTANCE_VARIABLES_CCRapportFileTransferManager
- __OBJC_$_INSTANCE_VARIABLES_CCRapportRequest
- __OBJC_$_PROP_LIST_CCRapportFileTransferManager
- __OBJC_$_PROP_LIST_CCRapportRequest
- __OBJC_CLASS_RO_$_CCRapportFileTransferManager
- __OBJC_CLASS_RO_$_CCRapportRequest
- __OBJC_METACLASS_RO_$_CCRapportFileTransferManager
- __OBJC_METACLASS_RO_$_CCRapportRequest
- ___118-[CCRapportFileTransferManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]_block_invoke
- ___118-[CCRapportFileTransferManager initiateFileTransferSesionBackToTargetDeviceWithIdentifier:withExchangedPeerPublicKey:]_block_invoke.cold.1
- ___34-[CCRapportSyncEngine startClient]_block_invoke
- ___39-[CCRapportRequest startRequestTimeout]_block_invoke
- ___42-[CCRapportRequest deviceAttributedErrors]_block_invoke
- ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.162
- ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.cold.3
- ___49-[CCRapportSyncEngine startServerWithCompletion:]_block_invoke
- ___49-[CCRapportSyncEngine startServerWithCompletion:]_block_invoke_2
- ___54-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:]_block_invoke
- ___54-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:]_block_invoke.cold.1
- ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.175
- ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.cold.5
- ___61-[CCRapportSyncEngine registerRequestsWithCompletionHandler:]_block_invoke
- ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.179
- ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.cold.1
- ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke_2
- ___65-[CCSyncManager handleIncomingSyncRequestsWithCompletionHandler:]_block_invoke
- ___65-[CCSyncManager handleIncomingSyncRequestsWithCompletionHandler:]_block_invoke.3
- ___68-[CCRapportSyncEngine syncNowWithReason:activity:completionHandler:]_block_invoke
- ___74-[CCRapportSyncEngine reciprocateSyncRequestWithDevice:completionHandler:]_block_invoke
- ___74-[CCRapportSyncEngine sendSetDiscoveryRequest:toDevice:completionHandler:]_block_invoke
- ___77-[CCRapportSyncEngine startSyncRequestWithReason:activity:completionHandler:]_block_invoke
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.129
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.132
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.134
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.135
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.137
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.138
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.146
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.146.cold.1
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.147
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.150
- ___89-[CCRapportSyncEngine sendDoneFetchingMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke
- ___block_descriptor_32_e32_v16?0"RPFileTransferProgress"8l
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_40_e8_32r_e41_v32?0"CCRapportDevice"8"NSError"16^B24lr32l8
- ___block_descriptor_40_e8_32w_e23_v24?0?<B?>8?<v?>16lw32l8
- ___block_descriptor_40_e8_32w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw32l8
- ___block_descriptor_48_e8_32s40bs_e23_v24?0?<B?>8?<v?>16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e31_v16?0"RPCompanionLinkDevice"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e23_v24?0?<B?>8?<v?>16lw40l8s32l8
- ___block_descriptor_49_e8_32s40w_e23_v24?0?<B?>8?<v?>16lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e15_v16?0"CCSet"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e15_v16?0"CCSet"8ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48bs_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56w_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16lw56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw56l8s32l8s48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64bs_e23_v24?0?<B?>8?<v?>16ls64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.182
- ___block_literal_global.184
- ___block_literal_global.186
- __dispatch_source_type_timer
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_set_timer
- _objc_msgSend$addDependency:
- _objc_msgSend$addOmittedSetsFromSetDiscovery:
- _objc_msgSend$addOperation:
- _objc_msgSend$addOperations:waitUntilFinished:
- _objc_msgSend$addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:
- _objc_msgSend$buildBasePeerToPeerMessage
- _objc_msgSend$buildDoneFetchingMergeableDeltasMessageToDevice:withIsReciprocal:
- _objc_msgSend$cancelAllOperations
- _objc_msgSend$completeRequestAsDeliveredToDevices:withErrors:
- _objc_msgSend$completeRequestIfDeliveredToAllNearbyDevices
- _objc_msgSend$completionHandler
- _objc_msgSend$defaultInstance:
- _objc_msgSend$deliveredToDevices
- _objc_msgSend$determineSyncOperationForDiscoveredSet:withDevice:outFetchRequest:
- _objc_msgSend$deviceAttributedErrors
- _objc_msgSend$directoryURL
- _objc_msgSend$discoveredDevices
- _objc_msgSend$doneFetchingMergeableDeltasMessageFromPeerToPeerMessage:isReciprocal:rapportIdentifier:
- _objc_msgSend$enumerateAllSets:withOptions:setIdentifiers:usingBlock:
- _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
- _objc_msgSend$fileTransferQueue
- _objc_msgSend$inFlightToDevices
- _objc_msgSend$initWithDirectoryURL:accessAssertion:
- _objc_msgSend$initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:localDeviceUUID:
- _objc_msgSend$initWithUUID:reason:activity:queue:completionHandler:
- _objc_msgSend$isSubsetOfSet:
- _objc_msgSend$markAsDeliveredToDevice:withError:
- _objc_msgSend$markAsInFlightToDevice:
- _objc_msgSend$reciprocateSyncRequestWithDevice:completionHandler:
- _objc_msgSend$registerLocalDeviceUpdatedHandler:
- _objc_msgSend$registerRequestsWithCompletionHandler:
- _objc_msgSend$requestAccess:forResource:withMode:error:
- _objc_msgSend$requestAccess:forResource:withMode:useCase:error:
- _objc_msgSend$requestTimeoutDidFire
- _objc_msgSend$requestTimeoutHandler
- _objc_msgSend$sendDoneFetchingMergeableDeltasRequest:toDevice:completionHandler:
- _objc_msgSend$sendFetchMergeableDeltasRequest:toDevice:completionHandler:
- _objc_msgSend$sendSetDiscoveryRequest:toDevice:completionHandler:
- _objc_msgSend$setDiscoveryMessageFromPeerToPeerMessage:setUUIDsToDiscover:
- _objc_msgSend$setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:
- _objc_msgSend$setMaxConcurrentOperationCount:
- _objc_msgSend$setRapportIdentifier:
- _objc_msgSend$setRequestTimeoutHandler:
- _objc_msgSend$setState:
- _objc_msgSend$setUnderlyingQueue:
- _objc_msgSend$setsToSyncFromDevice
- _objc_msgSend$shortenedRapportIdentifier
- _objc_msgSend$startClient
- _objc_msgSend$startRequestTimeout
- _objc_msgSend$startServerWithCompletion:
- _objc_msgSend$startSyncRequestWithReason:activity:completionHandler:
- _objc_msgSend$stopRequestTimeout
- _objc_msgSend$syncNowWithReason:activity:completionHandler:
- _objc_msgSend$teardown
- _objc_msgSend$unionSet:
CStrings:
+ "\n!"
+ " CascadeDeviceUUID: %@"
+ " and ubmitting reciprocal interaction"
+ " error: %@"
+ "%@ RSSI changed"
+ "%@ Running interaction: %@"
+ "%@ SSID changed"
+ "%@ activating client"
+ "%@ activation %@%@"
+ "%@ advertisement data changed"
+ "%@ cancelling (%@) interaction: %@"
+ "%@ determined to not support service com.apple.biomesyncd.cascade.rapport"
+ "%@ distance changed: %s"
+ "%@ distance wifi information element changed"
+ "%@ distance/angle/something changed"
+ "%@ enqueueing request"
+ "%@ expected request id and response handler in %@"
+ "%@ got unexpected change flag: RPDeviceChangeFlags(%x)"
+ "%@ ignoring cancellation for (%@) interaction: %@"
+ "%@ ignoring device not listing service from serviceTypescom.apple.biomesyncd.cascade.rapport"
+ "%@ interrupted"
+ "%@ invalidated"
+ "%@ lost"
+ "%@ name changed: %@"
+ "%@ no transports available; expect a lost callback"
+ "%@ pairing flags/attributes changed"
+ "%@ proximity changed: %s"
+ "%@ registered interaction: %@"
+ "%@ request queue empty, invalidating client"
+ "%@ tearing down client"
+ "%@: %@ discovered device: %@"
+ "%@: %@ sync session with reason: %@ type: %@"
+ "%@: %@%@"
+ "%@: Cumulative response size (%lu) exceeds requested size threshold: %@. Stopping enumeration and setting %@"
+ "%@: Responding with %@ as server interaction is not running"
+ "%@: Skipping set discovery based on request options: %@"
+ "%@: Skipping set enumeration per request options: %@"
+ "%@: access assertion does not contain a valid path to sync directory: %@"
+ "%@: activated successfully"
+ "%@: activating %@"
+ "%@: all known devices %@"
+ "%@: all sync operations for %lu set(s) completed"
+ "%@: already activated %@"
+ "%@: already activating %@"
+ "%@: already discovered device, %@ as %@"
+ "%@: buildFileTransferSessionWithTargetDeviceIdentifier %@"
+ "%@: could not determine appropriate control flags for device platform: %@"
+ "%@: createSharedDiscoveryClientIfNotExists not currently supported"
+ "%@: discovered %u set(s) eligible for inbound sync: %@"
+ "%@: discovering sets to sync"
+ "%@: done syncing sets and %@expecting reciprocation"
+ "%@: failed to activate file transfer sessions: %@"
+ "%@: failed to activate session: %@"
+ "%@: failed to activate with error: %@"
+ "%@: failed to prepare file transfer template %@"
+ "%@: failed to resolve device from request inOptions: %@"
+ "%@: fetch mergeable deltas response error code (%@) requires immediate expiration for any active contents stored in set: %@"
+ "%@: handling mergeable delta file transfer with metadata: %@"
+ "%@: handling set (%u / %u): %@"
+ "%@: initializing file transfer directory: %@"
+ "%@: initiateFileTransferSesionBackToTargetDeviceWithIdentifier %@"
+ "%@: invalidated"
+ "%@: peer device is already syncing so will not reciprocate: %@"
+ "%@: progress %@"
+ "%@: received SIGTERM"
+ "%@: repeating set discovery to sync additional sets"
+ "%@: resolved sync operation (%@) for set: %@"
+ "%@: set discovery response indicates %@ sets to discover (size threshold: %@): %@"
+ "%@: shared discovery client already exists"
+ "%@: shared-use only supported internally"
+ "%@: signalled remote device we are done fetching%@"
+ "%@: skipping RPCompanionLinkDevice missing identifier: %@"
+ "%@: skipping RPCompanionLinkDevice missing model: %@"
+ "%@: starting sync interaction: %@"
+ "%@: stop"
+ "%@: zero discovered sets to sync"
+ "%@[%@]"
+ "%lu-%@-%@-%@"
+ "%lu. [%@] %@ -> %@%@"
+ "(Session:%@|%@)"
+ "-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:forInteraction:]_block_invoke"
+ "@\"CCRapportDevice\""
+ "@\"CCRapportSyncSession\""
+ "@\"NSError\""
+ "@\"NSNumber\""
+ "@36@0:8@16@24S32"
+ "@40@0:8@16Q24^@32"
+ "@52@0:8@16@24@?32B40^q44"
+ "@52@0:8@16@24S32@36@44"
+ "@60@0:8@16C24@28Q36C44S48@?52"
+ "ADDITIONAL"
+ "Activating"
+ "AdditionalSetsToDiscover"
+ "B20@0:8C16"
+ "B24@0:8C16C20"
+ "CCRapportSyncInteraction"
+ "CCRapportSyncSession"
+ "Client"
+ "Completing interaction %@ after %lf seconds waiting for request: %@"
+ "Completing interaction: %@"
+ "Completing sync session %@ after %lf seconds waiting to run interactions"
+ "Failed to assume persona %@ for didDiscoverDevice handler %@ for device: %@"
+ "Idle"
+ "Ignoring"
+ "IncludeRelayedDeltas"
+ "Pending"
+ "RapportWake"
+ "Request timed out because a nearby device failed to respond in time"
+ "Reusing"
+ "Running"
+ "Sending requestID: \"%@\" from %@ to %@ %@ options: %@"
+ "Server"
+ "SkipSetDiscovery"
+ "Sync session %@ already completed, ignoring (%@)"
+ "Sync session %@ completed with %lu interaction(s) %@ %@"
+ "Sync with reason (%@) completed%@"
+ "T@\"CCRapportDevice\",R,N,V_device"
+ "T@\"CCSet\",&,N,V_repeatDiscoveryAfterSet"
+ "T@\"CCSet\",&,N,V_startAfterSet"
+ "T@\"NSArray\",&,N,V_setsToSync"
+ "T@\"NSError\",&,N,V_error"
+ "T@\"NSMutableDictionary\",R,N,V_fileTransferSessions"
+ "T@\"NSMutableSet\",R,N,V_discoveredResources"
+ "T@\"NSNumber\",&,N,V_sizeThreshold"
+ "T@\"NSURL\",&,N,V_fileTransferDirectory"
+ "T@\"NSUUID\",R,N,V_uuid"
+ "TC,R,N,V_reason"
+ "TC,R,N,V_state"
+ "TC,R,N,V_type"
+ "TQ,R,N,V_operationId"
+ "TS,N,V_responseOptions"
+ "Timed out waiting to discover nearby devices eligible for sync"
+ "Will engage with"
+ "[%@]"
+ "_activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:"
+ "_activationReasons"
+ "_addFlags:forInteractionType:"
+ "_cancelNextInteractionTimeout"
+ "_completeSession:"
+ "_completedInteractions"
+ "_completionHandlers"
+ "_currentSession"
+ "_deactivateSession"
+ "_discoveredResources"
+ "_error"
+ "_failToActivateSessionWithError:activationHandler:sessionCompletionHandler:"
+ "_fileTransferAccessAssertion"
+ "_fileTransferDirectory"
+ "_flags"
+ "_hasFlags:forInteractionType:"
+ "_index"
+ "_interactionHandler"
+ "_interactionIndex"
+ "_isRunningInteractionType:"
+ "_nextInteractionTimeout"
+ "_operationId"
+ "_reason"
+ "_registeredInteractions"
+ "_repeatDiscoveryAfterSet"
+ "_responseOptions"
+ "_runInteraction:"
+ "_runNextInteraction"
+ "_runningInteractions"
+ "_setNextInteractionTimeout"
+ "_setsToSync"
+ "_sizeThreshold"
+ "_startAfterSet"
+ "_type"
+ "activateClientWithReason:activity:completionHandler:"
+ "activateFileTransferSessions:"
+ "activateServerWithReason:activationHandler:"
+ "addOmittedSetsFromSetDiscovery:forInteraction:"
+ "buildBasePeerToPeerMessageForInteraction:"
+ "buildDoneFetchingMergeableDeltasMessageForInteraction:"
+ "cancelInteractionType:withDevice:error:"
+ "cancelRapportRequestTimeout"
+ "componentsJoinedByString:"
+ "container"
+ "continueAfterHandlingAllSetsToSyncForInteraction:"
+ "continueToDiscoverSetsToSyncForInteraction:"
+ "continueToHandleNextSetToSyncAtIndex:forInteraction:"
+ "detailedDescription"
+ "determineSyncOperationForDiscoveredSet:forInteraction:outFetchRequest:"
+ "discoveredResources"
+ "doneFetchingMergeableDeltasMessageFromPeerToPeerMessage:isReciprocal:"
+ "enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:"
+ "error"
+ "fileTransferDirectory"
+ "fileTransferSessions"
+ "handleIncomingSyncRequestsWithReason:completionHandler:"
+ "initWithObjects:"
+ "initWithQueue:interactionHandler:"
+ "initWithQueue:rapportManager:readAccess:donateServiceProvider:localDeviceUUID:"
+ "initWithQueue:reason:device:index:type:options:completion:"
+ "interactionOfType:withDevice:"
+ "isRunning"
+ "lastObject"
+ "no remaining"
+ "objectAtIndexedSubscript:"
+ "operationId"
+ "prefix"
+ "readSetForDiscovery:senderDeviceUUID:"
+ "reason"
+ "recordDiscoveredSetResources:forInteraction:"
+ "registerSessionActivationReason:forInteractionType:withOptions:completionHandler:"
+ "repeatDiscoveryAfterSet"
+ "requestAccessToResource:withMode:error:"
+ "requestAccessToResource:withMode:useCase:error:"
+ "responseOptions"
+ "sendDoneFetchingMergeableDeltasRequest:forInteraction:"
+ "sendFetchMergeableDeltasRequest:forInteraction:continueSync:"
+ "sendSetDiscoveryRequest:forInteraction:continueSync:"
+ "setDiscoveryRequestFromPeerToPeerMessage:setUUIDsToDiscover:requestOptions:startAfterSet:sizeThreshold:"
+ "setDiscoveryRequestOptions"
+ "setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:responseOptions:"
+ "setDiscoveryResponseOptions"
+ "setError:"
+ "setFileTransferDirectory:"
+ "setObject:atIndexedSubscript:"
+ "setRepeatDiscoveryAfterSet:"
+ "setResponseOptions:"
+ "setSetsToSync:"
+ "setSizeThreshold:"
+ "setStartAfterSet:"
+ "setTimeoutForRapportRequest:"
+ "setsToSync"
+ "sizeThreshold"
+ "startAfterSet"
+ "submitInteractionType:withDevice:"
+ "submitInteractionType:withDevice:reason:"
+ "type"
+ "unblockInteractionType:"
+ "unsignedLongValue"
+ "updateState:"
+ "v16@?0@\"CCRapportSyncInteraction\"8"
+ "v24@0:8C16C20"
+ "v24@?0@\"CCSet\"8^B16"
+ "v28@0:8C16@20"
+ "v28@0:8C16@?20"
+ "v32@0:8C16@20C28"
+ "v32@0:8Q16@24"
+ "v36@0:8C16@20@28"
+ "v36@0:8C16C20S24@?28"
+ "v40@0:8@16@?24@?32"
+ "v40@0:8C16C20@?24@?32"
+ "validateInRequest:inOptions:inResponseHandler:createInteraction:outPlatform:"
+ "|"
+ "\x81"
- "\n"
- " current persona: %@"
- "%@ cannot be initialized. %@ failed to be initialized: %@"
- "%@: Adding sync operations for discovered device: %@"
- "%@: Started sync request"
- "%@: all operations to fetch deltas completed"
- "%@: attempting to tear down sync engine but a request is still in progress %@"
- "%@: candidate set (%u / %u): %@"
- "%@: completing request, still inflight: %@"
- "%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@, trying alternate identifier %@"
- "%@: could not find device to reciprocate with alternate identifier %@"
- "%@: discovered %u set(s) eligible for inbound sync from device %@ sets: %@"
- "%@: discovered local device %@"
- "%@: done fetching all deltas and %@expecting reciprocation from device %@"
- "%@: engaging with device: %@"
- "%@: enqueueing sync operations for %u candidate set(s) with device %@"
- "%@: evaluating whether device is supported for messaging %@"
- "%@: fetch mergeable deltas response error code (%@) requires immediate expiration for any active contents stored in set: %@ from device: %@"
- "%@: handling mergeable delta file transfer with metadata: %@ from device %@"
- "%@: local device %@"
- "%@: parent fetch all deltas operation cancelled, cancelling remaining %u / %u sync set operations"
- "%@: peer device is already syncing so will not reciprocate, completing the request %@"
- "%@: reciprocal request completed with %@ %@"
- "%@: reciprocateSyncRequestWithDevice: %@%@"
- "%@: request already finished running"
- "%@: resolved sync operation (%@) for set: %@ with device: %@"
- "%@: signalled remote device we are done fetching %@"
- "%@: skipping set discovery with no sets configured for inbound sync."
- "%@: startSyncRequestWithReason: %@%@"
- "%@: zero sets resolved to sync with device %@"
- "(%@-%@)"
- "-[CCRapportSyncEngine addOmittedSetsFromSetDiscovery:]_block_invoke"
- "@\"CCRapportFileTransferManager\""
- "@\"CCRapportRequest\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSOperationQueue\""
- "@36@0:8@16B24@28"
- "@48@0:8^@16@24Q32^@40"
- "@52@0:8@16C24@28@36@?44"
- "@64@0:8@16@24@32@40@48@56"
- "BMRapportManager: could not determine appropriate control flags for device platform: %@"
- "CCRapportDevice[%@]: \"%@\" model: %@ RapportID: %@ CascadeID: %@"
- "CCRapportDevice[%@]: RSSI changed"
- "CCRapportDevice[%@]: SSID changed"
- "CCRapportDevice[%@]: activating client"
- "CCRapportDevice[%@]: activation %@%@"
- "CCRapportDevice[%@]: advertisement data changed"
- "CCRapportDevice[%@]: determined to not support service com.apple.biomesyncd.cascade.rapport"
- "CCRapportDevice[%@]: discovered"
- "CCRapportDevice[%@]: distance changed: %s"
- "CCRapportDevice[%@]: distance wifi information element changed"
- "CCRapportDevice[%@]: distance/angle/something changed"
- "CCRapportDevice[%@]: enqueueing request"
- "CCRapportDevice[%@]: expected request id and response handler in %@"
- "CCRapportDevice[%@]: got unexpected change flag: RPDeviceChangeFlags(%x)"
- "CCRapportDevice[%@]: ignoring device not listing service from serviceTypescom.apple.biomesyncd.cascade.rapport"
- "CCRapportDevice[%@]: ignoring unsupported device"
- "CCRapportDevice[%@]: interrupted"
- "CCRapportDevice[%@]: invalidated"
- "CCRapportDevice[%@]: lost"
- "CCRapportDevice[%@]: name changed: %@"
- "CCRapportDevice[%@]: no transports available; expect a lost callback"
- "CCRapportDevice[%@]: pairing flags/attributes changed"
- "CCRapportDevice[%@]: proximity changed: %s"
- "CCRapportDevice[%@]: request queue empty, invalidating client"
- "CCRapportDevice[%@]: tearing down client"
- "CCRapportFileTransferManager"
- "CCRapportFileTransferManager: access assertion does not contain a valid path to sync directory %@"
- "CCRapportFileTransferManager: buildFileTransferSessionWithTargetDeviceIdentifier %@"
- "CCRapportFileTransferManager: failed to prepare file transfer template %@"
- "CCRapportFileTransferManager: initializing file transfer directory with url %@"
- "CCRapportFileTransferManager: initiateFileTransferSesionBackToTargetDeviceWithIdentifier %@"
- "CCRapportFileTransferManager: prepareTemplateAndReturnError %@"
- "CCRapportFileTransferManager: progress %@"
- "CCRapportManager: activated successfully"
- "CCRapportManager: activating %@"
- "CCRapportManager: all known devices %@"
- "CCRapportManager: already activated %@"
- "CCRapportManager: already activating %@"
- "CCRapportManager: already discovered device, %@ as %@"
- "CCRapportManager: createSharedDiscoveryClientIfNotExists not currently supported"
- "CCRapportManager: failed to activate with error: %@"
- "CCRapportManager: invalidated"
- "CCRapportManager: received SIGTERM"
- "CCRapportManager: shared discovery client already exists"
- "CCRapportManager: shared-use only supported internally"
- "CCRapportManager: skipping RPCompanionLinkDevice missing identifier: %@"
- "CCRapportManager: skipping RPCompanionLinkDevice missing model: %@"
- "CCRapportManager: stop"
- "CCRapportRequest"
- "Failed to assume persona %@ for didDiscoverDevice handler %@"
- "Rapport discovery Timeout"
- "Request timed out because no devices are nearby or devices failed to respond in time"
- "Sending requestID: \"%@\" from %@ to CCRapportDevice[%@]: %@ options: %@"
- "Sync with reason (%@) completed%@. Engaged with %u device(s): %@ %@"
- "T@\"NSDictionary\",&,N,V_errorFromDevice"
- "T@\"NSMutableDictionary\",&,N,V_setsToSyncFromDevice"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_requestTimeout"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_activity"
- "T@\"NSSet\",&,N,V_deliveredToDevices"
- "T@\"NSSet\",&,N,V_inFlightToDevices"
- "T@\"NSString\",&,N,V_rapportIdentifier"
- "T@\"NSURL\",R,N,V_directoryURL"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_requestTimeoutHandler"
- "TC,N,V_syncReason"
- "TQ,N,V_state"
- "_activity"
- "_completionHandler"
- "_currentRequest"
- "_deliveredToDevices"
- "_directoryURL"
- "_errorFromDevice"
- "_fileTransferSessionManager"
- "_inFlightToDevices"
- "_operationQueue"
- "_requestTimeoutHandler"
- "_setsToSyncFromDevice"
- "activity"
- "addDependency:"
- "addOmittedSetsFromSetDiscovery:"
- "addOperation:"
- "addOperations:waitUntilFinished:"
- "addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:"
- "buildBasePeerToPeerMessage"
- "buildDoneFetchingMergeableDeltasMessageToDevice:withIsReciprocal:"
- "cancelAllOperations"
- "completeRequestAsDeliveredToDevices:withErrors:"
- "completeRequestIfDeliveredToAllNearbyDevices"
- "completionHandler"
- "defaultInstance:"
- "deliveredToDevices"
- "determineSyncOperationForDiscoveredSet:withDevice:outFetchRequest:"
- "deviceAttributedErrors"
- "directoryURL"
- "doneFetchingMergeableDeltasMessageFromPeerToPeerMessage:isReciprocal:rapportIdentifier:"
- "enumerateAllSets:withOptions:setIdentifiers:usingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorFromDevice"
- "handleIncomingSyncRequestsWithCompletionHandler:"
- "inFlightToDevices"
- "initWithDirectoryURL:accessAssertion:"
- "initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:localDeviceUUID:"
- "initWithUUID:reason:activity:queue:completionHandler:"
- "isSubsetOfSet:"
- "markAsDeliveredToDevice:withError:"
- "markAsInFlightToDevice:"
- "reciprocateSyncRequestWithDevice:completionHandler:"
- "registerRequestsWithCompletionHandler:"
- "requestAccess:forResource:withMode:error:"
- "requestAccess:forResource:withMode:useCase:error:"
- "requestTimeout"
- "requestTimeoutDidFire"
- "requestTimeoutHandler"
- "sendDoneFetchingMergeableDeltasRequest:toDevice:completionHandler:"
- "sendFetchMergeableDeltasRequest:toDevice:completionHandler:"
- "sendSetDiscoveryRequest:toDevice:completionHandler:"
- "senderRapportWorkaroundIdentifier"
- "setActivity:"
- "setDeliveredToDevices:"
- "setDiscoveryMessageFromPeerToPeerMessage:setUUIDsToDiscover:"
- "setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:"
- "setErrorFromDevice:"
- "setInFlightToDevices:"
- "setMaxConcurrentOperationCount:"
- "setRapportIdentifier:"
- "setRequestTimeout:"
- "setRequestTimeoutHandler:"
- "setSetsToSyncFromDevice:"
- "setState:"
- "setSyncReason:"
- "setUnderlyingQueue:"
- "setUuid:"
- "setsToSyncFromDevice"
- "shortenedRapportIdentifier"
- "startClient"
- "startRequestTimeout"
- "startServerWithCompletion:"
- "startSyncRequestWithReason:activity:completionHandler:"
- "stopRequestTimeout"
- "syncNowWithReason:activity:completionHandler:"
- "teardown"
- "unionSet:"
- "v16@?0@\"CCSet\"8"
- "v24@?0@?<B@?>8@?<v@?>16"
- "v28@0:8@16B24"
- "v32@?0@\"CCRapportDevice\"8@\"NSError\"16^B24"

```
