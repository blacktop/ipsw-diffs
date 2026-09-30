## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-166.23.1.0.0
-  __TEXT.__text: 0x1ba50
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x1604
-  __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x5dc
-  __TEXT.__cstring: 0xc6d
-  __TEXT.__oslogstring: 0x3428
+192.0.0.0.0
+  __TEXT.__text: 0x1e1d8
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x176c
+  __TEXT.__const: 0x100
+  __TEXT.__gcc_except_tab: 0x64c
+  __TEXT.__cstring: 0xfe8
+  __TEXT.__oslogstring: 0x36b3
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x730
-  __TEXT.__objc_classname: 0x46d
-  __TEXT.__objc_methname: 0x4a19
-  __TEXT.__objc_methtype: 0x10a7
-  __TEXT.__objc_stubs: 0x3de0
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x9c8
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__unwind_info: 0x7f8
+  __TEXT.__objc_classname: 0x476
+  __TEXT.__objc_methname: 0x4f76
+  __TEXT.__objc_methtype: 0xf44
+  __TEXT.__objc_stubs: 0x42a0
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0xb58
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11d0
+  __DATA_CONST.__objc_selrefs: 0x1310
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xa40
-  __AUTH_CONST.__objc_const: 0x3090
+  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0xee0
+  __AUTH_CONST.__objc_const: 0x31b0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x24c
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x258
   __DATA.__data: 0x720
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x690
+  __DATA.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5BA0025-32C1-37B3-99AB-84CC12A6C26F
-  Functions: 632
-  Symbols:   2555
-  CStrings:  1401
+  UUID: E5085A92-319B-306A-AA6C-E0256E8455DD
+  Functions: 675
+  Symbols:   2708
+  CStrings:  1542
 
Symbols:
+ +[CCDiscoveredSet addOptions:toSets:]
+ +[CCFetchMergeableDeltasRequest fetchMergableDeltasRequestFromPeerToPeerMessage:set:stateVector:atomBatchVersion:requestOptions:]
+ +[CCFileTransferSessionInitiatedResponse fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:]
+ +[CCMergeableDeltaFileTransferMessageMetadata mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:set:mergeableDeltaMetadataVectors:fileFormatVersion:deviceSite:relayedDeviceSites:]
+ +[CCRapportFileTransferManager defaultInstance:]
+ +[CCRapportFileTransferManager defaultInstance:].cold.1
+ -[CCDifferentialUpdater _diffUpdateItemsWithContents:metaContents:].cold.2
+ -[CCDifferentialUpdater _finishWithRevisionToken:designateAsFullSet:]
+ -[CCDifferentialUpdater _finishWithRevisionToken:designateAsFullSet:].cold.1
+ -[CCDifferentialUpdater _readLocalSourcePriorsFromDatabase]
+ -[CCDifferentialUpdater finishUpdateWithRevisionToken:designateAsFullSet:]
+ -[CCDifferentialUpdater priors]
+ -[CCDiscoveredSet .cxx_destruct]
+ -[CCDiscoveredSet copyWithOptions:error:]
+ -[CCDiscoveredSet copyWithZone:]
+ -[CCDiscoveredSet deviceSite]
+ -[CCDiscoveredSet dictionaryRepresentation]
+ -[CCDiscoveredSet discoveryErrorCode]
+ -[CCDiscoveredSet hash]
+ -[CCDiscoveredSet initFromDictionary:]
+ -[CCDiscoveredSet initWithSet:deviceSite:relayedDeviceSites:discoveryErrorCode:error:]
+ -[CCDiscoveredSet isEqual:]
+ -[CCDiscoveredSet isEqualToDiscoveredSet:]
+ -[CCDiscoveredSet relayedDeviceSites]
+ -[CCDiscoveredSet setDeviceSite:]
+ -[CCDiscoveredSet setDiscoveryErrorCode:]
+ -[CCDiscoveredSet setRelayedDeviceSites:]
+ -[CCDonateConnection endSetDonationWithOptions:revisionToken:completion:]
+ -[CCDonateRequest hasInlineFallback]
+ -[CCDonateRequest isFullSet]
+ -[CCPeerToPeerMessage .cxx_destruct]
+ -[CCPeerToPeerMessage initWithSyncReason:senderDeviceUUID:protocolVersion:wallTime:]
+ -[CCPeerToPeerMessage senderDeviceUUID]
+ -[CCPeerToPeerMessage setSenderDeviceUUID:]
+ -[CCRapportDevice cascadeDeviceUUID]
+ -[CCRapportDevice setCascadeDeviceUUID:]
+ -[CCRapportFileTransferManager deleteDanglingFilesFromFileTransferDirectory]
+ -[CCRapportFileTransferManager deleteDanglingFilesFromFileTransferDirectory].cold.1
+ -[CCRapportFileTransferManager deleteMergeableDeltaFileURL:]
+ -[CCRapportManager sendRequest:request:device:options:responseHandler:].cold.4
+ -[CCRapportRequest description]
+ -[CCRapportRequest deviceAttributedErrors]
+ -[CCRapportRequest initWithUUID:reason:activity:queue:completionHandler:]
+ -[CCRapportSyncEngine currentPlatformHasSetsSupportingSync:]
+ -[CCRapportSyncEngine determineSyncOperationForDiscoveredSet:outFetchRequest:]
+ -[CCRapportSyncEngine initWithQueue:error:]
+ -[CCRapportSyncEngine initWithQueue:error:].cold.1
+ -[CCRapportSyncEngine initWithQueue:error:].cold.2
+ -[CCRapportSyncEngine initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:localDeviceUUID:]
+ -[CCRapportSyncEngine reciprocateSyncRequestWithDevice:completionHandler:]
+ -[CCRapportSyncEngine setUUIDsSupportingInboundSync]
+ -[CCRapportSyncEngine setUUIDsSupportingInboundSync].cold.1
+ -[CCRapportSyncEngine setUUIDsSupportingOutboundSync]
+ -[CCRapportSyncEngine setUUIDsSupportingOutboundSync].cold.1
+ -[CCRapportSyncEngine startSyncRequestWithReason:activity:completionHandler:]
+ -[CCRapportSyncEngine startSyncRequestWithReason:activity:completionHandler:].cold.1
+ -[CCRapportSyncEngine startSyncRequestWithReason:activity:completionHandler:].cold.2
+ -[CCRapportSyncEngine syncOperationForDiscoveredSet:versionedMergeable:]
+ -[CCSetStoreUpdateServiceExported endSetDonationWithOptions:revisionToken:completion:]
+ -[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]
+ -[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:].cold.1
+ -[CCSetVersionedMergeable attestInSyncDeviceSite:relayedDeviceSites:]
+ -[CCSetVersionedMergeable localDeviceSiteAddingExpirationDate:]
+ -[CCSetVersionedMergeable localDeviceSiteAddingExpirationDate:].cold.1
+ -[CCSetVersionedMergeable mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:]
+ -[CCSetVersionedMergeable mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:].cold.1
+ -[CCSetVersionedMergeable relayedDeviceSitesExcludingRequestingDeviceUUID:]
+ -[CCSetVersionedMergeable relayedDeviceSitesExcludingRequestingDeviceUUID:].cold.1
+ -[CCSetVersionedMergeable storedEquivalentForDeviceSite:]
+ -[CCSetVersionedMergeable storedEquivalentForDeviceSite:].cold.1
+ -[CCSyncManager .cxx_destruct]
+ -[CCSyncManager _handleSetChanges:]
+ -[CCSyncManager _syncCurrentPersonaNowWithReason:activity:completionHandler:]
+ -[CCSyncManager _syncEngineForCurrentPersona:]
+ -[CCSyncManager _syncPersonasNow:withReason:activity:completionHandler:]
+ -[CCSyncManager handleIncomingSyncRequestsWithCompletionHandler:]
+ -[CCSyncManager initWithQueue:]
+ -[CCSyncManager syncAllPersonasNowWithReason:activity:completionHandler:]
+ -[CCSyncManager syncCurrentPersonaNowWithReason:activity:completionHandler:]
+ GCC_except_table15
+ GCC_except_table19
+ GCC_except_table27
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table6
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table8
+ GCC_except_table90
+ GCC_except_table95
+ GCC_except_table98
+ _BMDevicePlatformToString
+ _BMResourceOptionsDescription
+ _CCRapportSyncError
+ _CCRapportSyncErrorDescription
+ _CCRapportSyncErrorDomain
+ _CCRapportSyncErrorWithDetails
+ _CCRapportSyncErrorWithDevice
+ _CCRapportSyncErrorWithUnderlying
+ _CCSyncReasonDescription
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_CCDatabaseEmptyAccess
+ _OBJC_CLASS_$_CCDiscoveredSet
+ _OBJC_CLASS_$_CCDonateServicePriors
+ _OBJC_CLASS_$_CCSetsAccessDaemonDelegate
+ _OBJC_CLASS_$_CCSyncManager
+ _OBJC_IVAR_$_CCDifferentialUpdater._priors
+ _OBJC_IVAR_$_CCDiscoveredSet._deviceSite
+ _OBJC_IVAR_$_CCDiscoveredSet._discoveryErrorCode
+ _OBJC_IVAR_$_CCDiscoveredSet._relayedDeviceSites
+ _OBJC_IVAR_$_CCPeerToPeerMessage._senderDeviceUUID
+ _OBJC_IVAR_$_CCRapportDevice._cascadeDeviceUUID
+ _OBJC_IVAR_$_CCRapportSyncEngine._localDeviceUUID
+ _OBJC_IVAR_$_CCSyncManager._queue
+ _OBJC_IVAR_$_CCSyncManager._setChangeListener
+ _OBJC_IVAR_$_CCSyncManager._syncEngine
+ _OBJC_METACLASS_$_CCDiscoveredSet
+ _OBJC_METACLASS_$_CCSet
+ _OBJC_METACLASS_$_CCSyncManager
+ _RPOptionSenderFileTransferTargetID
+ __OBJC_$_CLASS_METHODS_CCDiscoveredSet
+ __OBJC_$_INSTANCE_METHODS_CCDiscoveredSet
+ __OBJC_$_INSTANCE_METHODS_CCSyncManager
+ __OBJC_$_INSTANCE_VARIABLES_CCDiscoveredSet
+ __OBJC_$_INSTANCE_VARIABLES_CCSyncManager
+ __OBJC_$_PROP_LIST_CCDiscoveredSet
+ __OBJC_CLASS_RO_$_CCDiscoveredSet
+ __OBJC_CLASS_RO_$_CCSyncManager
+ __OBJC_METACLASS_RO_$_CCDiscoveredSet
+ __OBJC_METACLASS_RO_$_CCSyncManager
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ ___31-[CCSyncManager initWithQueue:]_block_invoke
+ ___35-[CCSyncManager _handleSetChanges:]_block_invoke
+ ___42-[CCRapportRequest deviceAttributedErrors]_block_invoke
+ ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.164
+ ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.cold.3
+ ___52-[CCRapportSyncEngine setUUIDsSupportingInboundSync]_block_invoke
+ ___53-[CCRapportSyncEngine setUUIDsSupportingOutboundSync]_block_invoke
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.181
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.cold.3
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.cold.4
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.cold.5
+ ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.185
+ ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke_2
+ ___65-[CCSyncManager handleIncomingSyncRequestsWithCompletionHandler:]_block_invoke
+ ___65-[CCSyncManager handleIncomingSyncRequestsWithCompletionHandler:]_block_invoke.3
+ ___72-[CCSyncManager _syncPersonasNow:withReason:activity:completionHandler:]_block_invoke
+ ___72-[CCSyncManager _syncPersonasNow:withReason:activity:completionHandler:]_block_invoke_2
+ ___73-[CCDonateConnection endSetDonationWithOptions:revisionToken:completion:]_block_invoke
+ ___73-[CCDonateConnection endSetDonationWithOptions:revisionToken:completion:]_block_invoke_2
+ ___74-[CCRapportSyncEngine reciprocateSyncRequestWithDevice:completionHandler:]_block_invoke
+ ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.58
+ ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.58.cold.1
+ ___76-[CCSyncManager syncCurrentPersonaNowWithReason:activity:completionHandler:]_block_invoke
+ ___77-[CCRapportSyncEngine startSyncRequestWithReason:activity:completionHandler:]_block_invoke
+ ___77-[CCSetVersionedMergeable mergeableDeltasForMetadata:atomBatchVersion:error:]_block_invoke.31
+ ___77-[CCSyncManager _syncCurrentPersonaNowWithReason:activity:completionHandler:]_block_invoke
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.133
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.135
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.135.cold.1
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.137
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.138
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.139
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.141
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.145
+ ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.150
+ ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.150.cold.1
+ ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.151
+ ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.153
+ ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.153.cold.1
+ ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke
+ ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10
+ ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10.cold.1
+ ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10.cold.2
+ ___93-[CCSetVersionedMergeable _remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSArray"16ls32l8
+ ___block_descriptor_40_e8_32r_e41_v32?0"CCRapportDevice"8"NSError"16^B24lr32l8
+ ___block_descriptor_40_e8_32w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v24?0?<B?>8?<v?>16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s48l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e45_v24?0"CCRemoteCRDTSetDonation"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs_e23_v24?0?<B?>8?<v?>16ls64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.188
+ __recursivelyWaitForTransactionProgress
+ __recursivelyWaitForTransactionProgress.cold.1
+ _objc_msgSend$_finishWithRevisionToken:designateAsFullSet:
+ _objc_msgSend$_handleSetChanges:
+ _objc_msgSend$_readLocalSourcePriorsFromDatabase
+ _objc_msgSend$_remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:
+ _objc_msgSend$_syncCurrentPersonaNowWithReason:activity:completionHandler:
+ _objc_msgSend$_syncEngineForCurrentPersona:
+ _objc_msgSend$_syncPersonasNow:withReason:activity:completionHandler:
+ _objc_msgSend$activeDeviceSiteWithDeviceUUID:
+ _objc_msgSend$attestInSyncDeviceSite:relayedDeviceSites:
+ _objc_msgSend$cascadeDeviceUUID
+ _objc_msgSend$clientAddOrUpdateCount
+ _objc_msgSend$clientRemoveCount
+ _objc_msgSend$copyWithOptions:error:
+ _objc_msgSend$currentPlatformHasSetsSupportingSync:
+ _objc_msgSend$defaultInstance:
+ _objc_msgSend$deleteMergeableDeltaFileURL:
+ _objc_msgSend$deltaGeneration
+ _objc_msgSend$determineSyncOperationForDiscoveredSet:outFetchRequest:
+ _objc_msgSend$deviceAttributedErrors
+ _objc_msgSend$discoveryErrorCode
+ _objc_msgSend$endSetDonationWithOptions:revisionToken:completion:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$expirationDate
+ _objc_msgSend$fetchMergableDeltasRequestFromPeerToPeerMessage:set:stateVector:atomBatchVersion:requestOptions:
+ _objc_msgSend$fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:
+ _objc_msgSend$fileTransferTargetID
+ _objc_msgSend$finishAndDetectDelta:updateRevisionToken:isFullSet:
+ _objc_msgSend$finishUpdateWithRevisionToken:designateAsFullSet:
+ _objc_msgSend$hasInlineFallback
+ _objc_msgSend$initWithQueue:error:
+ _objc_msgSend$initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:localDeviceUUID:
+ _objc_msgSend$initWithSet:deviceSite:relayedDeviceSites:discoveryErrorCode:error:
+ _objc_msgSend$initWithSet:error:
+ _objc_msgSend$initWithSyncReason:senderDeviceUUID:protocolVersion:wallTime:
+ _objc_msgSend$initWithUUID:reason:activity:queue:completionHandler:
+ _objc_msgSend$initWithVersion:instanceCount:donationDate:fullSetDonationDate:revisionToken:options:
+ _objc_msgSend$instanceCount
+ _objc_msgSend$isEqualToDiscoveredSet:
+ _objc_msgSend$isFullSet
+ _objc_msgSend$localDeviceSiteAddingExpirationDate:
+ _objc_msgSend$mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:set:mergeableDeltaMetadataVectors:fileFormatVersion:deviceSite:relayedDeviceSites:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$priorLocalDonationDate
+ _objc_msgSend$priorLocalFullSetDonationDate
+ _objc_msgSend$priorLocalSourceRevisionToken
+ _objc_msgSend$priors
+ _objc_msgSend$readDefaultLocalDeviceUUID:
+ _objc_msgSend$reciprocateSyncRequestWithDevice:completionHandler:
+ _objc_msgSend$registerRemoteDeviceSite:isPeer:hasDeltas:returningRowId:
+ _objc_msgSend$relayedDeviceSitesExcludingRequestingDeviceUUID:
+ _objc_msgSend$resourceGeneration
+ _objc_msgSend$senderDeviceUUID
+ _objc_msgSend$setCascadeDeviceUUID:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setSenderDeviceUUID:
+ _objc_msgSend$setUUIDsSupportingInboundSync
+ _objc_msgSend$setUUIDsSupportingOutboundSync
+ _objc_msgSend$startServerWithCompletion:
+ _objc_msgSend$startSyncRequestWithReason:activity:completionHandler:
+ _objc_msgSend$storedEquivalentForDeviceSite:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$syncOperationForDiscoveredSet:versionedMergeable:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$userInfo
+ _setUUIDsSupportingInboundSync.inboundSetUUIDs
+ _setUUIDsSupportingInboundSync.onceToken
+ _setUUIDsSupportingOutboundSync.onceToken
+ _setUUIDsSupportingOutboundSync.outboundSetUUIDs
- +[CCFetchMergeableDeltasRequest fetchMergableDeltasRequestFromPeerToPeerMessage:deviceSite:set:stateVector:atomBatchVersion:requestOptions:]
- +[CCFileTransferSessionInitiatedResponse fileTransferSessionInitiatedResponseFromPeerToPeerMessage:deviceSite:peerPublicKey:]
- +[CCMergeableDeltaFileTransferMessageMetadata mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:deviceSite:set:mergeableDeltaMetadataVectors:fileFormatVersion:relayedDeviceSites:]
- +[CCRapportFileTransferManager defaultInstance]
- +[CCRapportFileTransferManager defaultInstance].cold.1
- +[CCRapportFileTransferManager defaultInstance].cold.2
- +[CCRapportFileTransferManager defaultInstance].cold.3
- -[CCDifferentialUpdater _shouldCommit]
- -[CCDifferentialUpdater _shouldCommit].cold.1
- -[CCDifferentialUpdater finish]
- -[CCDonateConnection endSetDonationWithOptions:completion:]
- -[CCFetchMergeableDeltasRequest deviceSite]
- -[CCFetchMergeableDeltasRequest setDeviceSite:]
- -[CCFileTransferSessionInitiatedResponse deviceSite]
- -[CCFileTransferSessionInitiatedResponse setDeviceSite:]
- -[CCPeerToPeerMessage initWithSyncReason:protocolVersion:wallTime:]
- -[CCPersonaSyncManager .cxx_destruct]
- -[CCPersonaSyncManager handleSetChanges:]
- -[CCPersonaSyncManager initWithQueue:]
- -[CCPersonaSyncManager setupSyncEngineToHandleIncomingRequestsForPersona:completionHandler:]
- -[CCPersonaSyncManager syncAllPersonasNowWithReason:activity:completionHandler:]
- -[CCPersonaSyncManager syncEngineForCurrentPersona]
- -[CCRapportDevice ccDeviceIdentifier]
- -[CCRapportDevice setCcDeviceIdentifier:]
- -[CCRapportRequest initWithUUID:reason:activity:setUUIDsSupportingSync:queue:completionHandler:]
- -[CCRapportRequest setSetUUIDsSupportingSync:]
- -[CCRapportRequest setUUIDsSupportingSync]
- -[CCRapportSyncEngine buildMergeableDeltasRequestForSet:]
- -[CCRapportSyncEngine deleteDanglingFilesFromFileTransferDirectory]
- -[CCRapportSyncEngine deleteDanglingFilesFromFileTransferDirectory].cold.1
- -[CCRapportSyncEngine fetchMergeableDeltasWithReason:activity:completionHandler:]
- -[CCRapportSyncEngine fetchMergeableDeltasWithReason:activity:completionHandler:].cold.1
- -[CCRapportSyncEngine fetchReciprocalMergeableDeltasFromDevice:completionHandler:]
- -[CCRapportSyncEngine fetchReciprocalMergeableDeltasFromDevice:completionHandler:].cold.1
- -[CCRapportSyncEngine initWithQueue:]
- -[CCRapportSyncEngine initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:]
- -[CCRapportSyncEngine lookupSetConfigurationForSet:]
- -[CCRapportSyncEngine setUUIDsSupportingSync]
- -[CCSetStoreUpdateServiceExported endSetDonationWithOptions:completion:]
- -[CCSetVersionedMergeable localDeviceSite]
- -[CCSetVersionedMergeable localDeviceSite].cold.1
- -[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]
- -[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:].cold.1
- -[CCSetVersionedMergeable mergeableDeltasForMetadata:atomBatchVersion:error:].cold.4
- -[CCSetVersionedMergeable relayedDeviceSitesNotIncludingRequestingDeviceSite:]
- -[CCSetVersionedMergeable relayedDeviceSitesNotIncludingRequestingDeviceSite:].cold.1
- GCC_except_table13
- GCC_except_table18
- GCC_except_table26
- GCC_except_table48
- GCC_except_table51
- GCC_except_table53
- GCC_except_table55
- GCC_except_table59
- GCC_except_table68
- GCC_except_table94
- GCC_except_table97
- _CCRapportErrorDomain
- _NSTemporaryDirectory
- _OBJC_CLASS_$_CCPersonaSyncManager
- _OBJC_IVAR_$_CCFetchMergeableDeltasRequest._deviceSite
- _OBJC_IVAR_$_CCFileTransferSessionInitiatedResponse._deviceSite
- _OBJC_IVAR_$_CCPersonaSyncManager._queue
- _OBJC_IVAR_$_CCPersonaSyncManager._setChangeListener
- _OBJC_IVAR_$_CCPersonaSyncManager._syncEngine
- _OBJC_IVAR_$_CCRapportDevice._ccDeviceIdentifier
- _OBJC_IVAR_$_CCRapportRequest._setUUIDsSupportingSync
- _OBJC_METACLASS_$_CCPersonaSyncManager
- __OBJC_$_INSTANCE_METHODS_CCPersonaSyncManager
- __OBJC_$_INSTANCE_VARIABLES_CCPersonaSyncManager
- __OBJC_CLASS_RO_$_CCPersonaSyncManager
- __OBJC_METACLASS_RO_$_CCPersonaSyncManager
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___38-[CCPersonaSyncManager initWithQueue:]_block_invoke
- ___41-[CCPersonaSyncManager handleSetChanges:]_block_invoke
- ___41-[CCPersonaSyncManager handleSetChanges:]_block_invoke.cold.1
- ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.158
- ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.165
- ___59-[CCDonateConnection endSetDonationWithOptions:completion:]_block_invoke
- ___59-[CCDonateConnection endSetDonationWithOptions:completion:]_block_invoke_2
- ___64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.166
- ___72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke
- ___72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10
- ___72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10.cold.1
- ___72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10.cold.2
- ___72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.cold.1
- ___74-[CCRapportSyncEngine sendSetDiscoveryRequest:toDevice:completionHandler:]_block_invoke.cold.2
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.56
- ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.56.cold.1
- ___77-[CCSetVersionedMergeable mergeableDeltasForMetadata:atomBatchVersion:error:]_block_invoke.25
- ___81-[CCRapportSyncEngine fetchMergeableDeltasWithReason:activity:completionHandler:]_block_invoke
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.121
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.124
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.127
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.128
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.129
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.131
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.132
- ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke_2.cold.1
- ___82-[CCRapportSyncEngine fetchReciprocalMergeableDeltasFromDevice:completionHandler:]_block_invoke
- ___82-[CCRapportSyncEngine fetchReciprocalMergeableDeltasFromDevice:completionHandler:]_block_invoke.119
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.137
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.137.cold.1
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.138
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.140
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.140.cold.1
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.140.cold.2
- ___84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.11.cold.2
- ___89-[CCRapportSyncEngine sendDoneFetchingMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.cold.1
- ___89-[CCRapportSyncEngine sendDoneFetchingMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.cold.2
- ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e23_v24?0?<B?>8?<v?>16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16lw64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e23_v24?0?<B?>8?<v?>16ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e45_v24?0"CCRemoteCRDTSetDonation"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8ls32l8s64l8s40l8s48l8s56l8s72l8
- _objc_msgSend$_shouldCommit
- _objc_msgSend$addBarrierBlock:
- _objc_msgSend$buildMergeableDeltasRequestForSet:
- _objc_msgSend$ccDeviceIdentifier
- _objc_msgSend$endSetDonationWithOptions:completion:
- _objc_msgSend$errorFromDevice
- _objc_msgSend$fetchMergableDeltasRequestFromPeerToPeerMessage:deviceSite:set:stateVector:atomBatchVersion:requestOptions:
- _objc_msgSend$fetchMergeableDeltasWithReason:activity:completionHandler:
- _objc_msgSend$fetchReciprocalMergeableDeltasFromDevice:completionHandler:
- _objc_msgSend$fileTransferSessionInitiatedResponseFromPeerToPeerMessage:deviceSite:peerPublicKey:
- _objc_msgSend$fileURLWithPathComponents:
- _objc_msgSend$handleSetChanges:
- _objc_msgSend$initWithQueue:
- _objc_msgSend$initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:
- _objc_msgSend$initWithSyncReason:protocolVersion:wallTime:
- _objc_msgSend$initWithUUID:reason:activity:setUUIDsSupportingSync:queue:completionHandler:
- _objc_msgSend$localDeviceRecord
- _objc_msgSend$lookupSetConfigurationForSet:
- _objc_msgSend$mergeDelta:fromDeviceSite:relayedDeviceSites:
- _objc_msgSend$mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:deviceSite:set:mergeableDeltaMetadataVectors:fileFormatVersion:relayedDeviceSites:
- _objc_msgSend$priorVersion
- _objc_msgSend$registerRemoteDeviceSite:isAttestation:returningRowId:
- _objc_msgSend$relayedDeviceSitesNotIncludingRequestingDeviceSite:
- _objc_msgSend$setCcDeviceIdentifier:
- _objc_msgSend$setUUIDsSupportingSync
- _objc_msgSend$syncEngineForCurrentPersona
CStrings:
+ "\n"
+ " current persona: %@"
+ " for persona: %@"
+ " | %@"
+ "%@ -> %@"
+ "%@ cannot be initialized. %@ failed to be initialized: %@"
+ "%@ cannot be initialized. Failed to read local device UUID: %@"
+ "%@: %@"
+ "%@: Adding sync operations for discovered device: %@"
+ "%@: Expiration is imminent for stored device site: %@"
+ "%@: Failed to downcast discovered set: %@ error: %@"
+ "%@: Found no active stored equivalent for device site of discovered set: %@"
+ "%@: No database access for discovered set: %@ (error: %@)"
+ "%@: Responding to set discovery request with %u set(s) matching request criteria"
+ "%@: Set enumeration hit error %@"
+ "%@: Started sync request"
+ "%@: all operations to fetch deltas completed"
+ "%@: client activating file transfer session %@ after receiving fetch mergeable deltas response: %@"
+ "%@: client registering to receive incoming files with peer key %@"
+ "%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@, trying alternate identifier %@"
+ "%@: could not find device to reciprocate with alternate identifier %@"
+ "%@: creating operations to fetch deltas for %u set(s) with device %@"
+ "%@: deltaGeneration (%@) already synced - stored expiration date (%@) is within the skip attestation interval (%lfs) of discovered (%@)"
+ "%@: deltaGeneration (%@) already synced - stored expiration date (%@) to be extended"
+ "%@: deltaGeneration (%@) out of sync with discovered (%@)"
+ "%@: discovered %u set(s) eligible for inbound sync from device %@ sets: %@"
+ "%@: discovered syncable set %@ for platform %@"
+ "%@: done fetching all deltas and %@expecting reciprocation from device %@"
+ "%@: failed to discover remote sets, cannot proceed to sync with device %@"
+ "%@: failed to send done fetching deltas: %@ with device: %@"
+ "%@: file transfer session initiated: %@"
+ "%@: handling discovered set (%u / %u): %@ from device: %@"
+ "%@: handling mergeable delta file transfer with metadata: %@ from device %@"
+ "%@: initiating file transfer session to send deltas for set %@ from device %@"
+ "%@: item completion handler invoked %@ for url %@"
+ "%@: parent fetch all deltas operation cancelled, cancelling remaining %u / %u sync set operations"
+ "%@: peer device is already syncing so will not reciprocate, completing the request %@"
+ "%@: received fetch mergeable deltas request for set: %@ %@ %@"
+ "%@: received item over file transfer session with url: %@"
+ "%@: received response from set discovery %@ %@"
+ "%@: received response from signalling end of fetching %@ %@"
+ "%@: reciprocateSyncRequestWithDevice: %@%@"
+ "%@: request already finished running"
+ "%@: resolved sync operation (%@) for discovered set: %@"
+ "%@: resourceGeneration (%@) is out of sync with discovered (%@)"
+ "%@: signalled remote device we are done fetching %@"
+ "%@: skipping set discovery with no sets configured for inbound sync."
+ "%@: startSyncRequestWithReason: %@%@"
+ "%@: zero sets resolved to sync with device %@"
+ "%@[%@] %@"
+ "(%@-%@)"
+ "@\"CCDonateServicePriors\""
+ "@24@0:8^@16"
+ "@28@0:8C16@20"
+ "@28@0:8C16^@20"
+ "@44@0:8C16@20Q28d36"
+ "@52@0:8@16@24@32Q40S48"
+ "@52@0:8@16C24@28@36@?44"
+ "@56@0:8@16@24@32Q40^@48"
+ "@64@0:8@16@24@32@40@48@56"
+ "@64@0:8@16@24@32Q40@48@56"
+ "Already syncing"
+ "Asked to defer"
+ "Attestation"
+ "B28@0:8@16B24"
+ "C32@0:8@16@24"
+ "C32@0:8@16^@24"
+ "CCDiscoveredSet"
+ "CCRapportFileTransferManager: initializing file transfer directory with url %@"
+ "CCRapportManager: all known devices %@"
+ "CCRapportSyncErrorDomain"
+ "CCSyncManager"
+ "Cannot access database"
+ "Cannot access file transfer directory"
+ "Cannot merge nil delta: %@ from device site: %@ relayed: %@"
+ "Cannot start sync server: %@"
+ "Cannot sync%@ with reason (%@): %@"
+ "Client has made insufficient progress since last check-in ~%.2lf seconds ago completing only %u operations (%.2lf/s with threshold of %lf/s). Aborting update: %@"
+ "Client progress check-in after ~%.2lf seconds:\t {%u items added or updated, %u removed}\t(~%.2lf operations/s)"
+ "Completed attestation-only update for peer device site: %@ relayed device sites: %@"
+ "Constructed content state vector from database for set: %@: %@ with device mapping: %@"
+ "Database failed to be read"
+ "DeltaFetch"
+ "Device lost"
+ "Enabling implicit deletes for incremental donation designated as full set"
+ "Failed to add options %@ to set %@ with error %@"
+ "Failed to decode opack encoded discovered set %@"
+ "Failed to decode relayed device site: %@"
+ "FullFetch"
+ "Initializing %@"
+ "Invalid parameter"
+ "Invalid state"
+ "Local source updating set: %@ with stored local item instance count: %u"
+ "Max request depth hit"
+ "Mergeable deltas contents vector is empty %@"
+ "NOT "
+ "Periodic"
+ "Protocol version mismatch"
+ "Rapport discovery Timeout"
+ "Rapport sender model not supported"
+ "Reciprocal"
+ "Remote CRDT donation %@ for set %@ from device site %@"
+ "Remote CRDT donation rejected for set: %@ error: %@ "
+ "Request timed out because no devices are nearby or devices failed to respond in time"
+ "Requested set does not exist"
+ "Sending requestID: \"%@\" from %@ to CCRapportDevice[%@]: %@ options: %@"
+ "SetChange"
+ "Skip"
+ "Skipped"
+ "Sync policy requires immmediate sync for set: %@"
+ "Sync prohibited by policy defined in set configuration"
+ "Sync with reason (%@) completed%@. Engaged with %u device(s): %@ %@"
+ "T@\"CCDonateServicePriors\",R,N,V_priors"
+ "T@\"NSUUID\",&,N,V_cascadeDeviceUUID"
+ "T@\"NSUUID\",&,N,V_senderDeviceUUID"
+ "TC,N,V_syncReason"
+ "TC,R,N,V_syncReason"
+ "TQ,N,V_discoveryErrorCode"
+ "Temporarily unavailable"
+ "The current device platform (%@) has no inbound or outbound sets configured for sync"
+ "Transaction timed out after more than %lf seconds. Aborting update: %@"
+ "Triggering immediate sync following change(s) to set(s) %@"
+ "Unknown (%@)"
+ "VolumeAvailable"
+ "Vv40@0:8Q16@\"NSString\"24@?<v@?S>32"
+ "Vv40@0:8Q16@24@?32"
+ "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?Sq@\"CCDonateServicePriors\">52"
+ "_cascadeDeviceUUID"
+ "_discoveryErrorCode"
+ "_finishWithRevisionToken:designateAsFullSet:"
+ "_handleSetChanges:"
+ "_localDeviceUUID"
+ "_priors"
+ "_readLocalSourcePriorsFromDatabase"
+ "_remoteCRDTSetDonationWithDelta:fromDeviceSite:relayedDeviceSites:"
+ "_senderDeviceUUID"
+ "_syncCurrentPersonaNowWithReason:activity:completionHandler:"
+ "_syncEngineForCurrentPersona:"
+ "_syncPersonasNow:withReason:activity:completionHandler:"
+ "activeDeviceSiteWithDeviceUUID:"
+ "addOptions:toSets:"
+ "attestInSyncDeviceSite:relayedDeviceSites:"
+ "cascadeDeviceUUID"
+ "copyWithOptions:error:"
+ "currentPlatformHasSetsSupportingSync:"
+ "defaultInstance:"
+ "deleteMergeableDeltaFileURL:"
+ "deltaGeneration"
+ "determineSyncOperationForDiscoveredSet:outFetchRequest:"
+ "deviceAttributedErrors"
+ "discoveryErrorCode"
+ "endSetDonationWithOptions:revisionToken:completion:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "errorCode"
+ "expirationDate"
+ "failed"
+ "fetchMergableDeltasRequestFromPeerToPeerMessage:set:stateVector:atomBatchVersion:requestOptions:"
+ "fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:"
+ "fileTransferTargetID"
+ "finishAndDetectDelta:updateRevisionToken:isFullSet:"
+ "finishUpdateWithRevisionToken:designateAsFullSet:"
+ "handleIncomingSyncRequestsWithCompletionHandler:"
+ "hasInlineFallback"
+ "initWithQueue:error:"
+ "initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:localDeviceUUID:"
+ "initWithSet:deviceSite:relayedDeviceSites:discoveryErrorCode:error:"
+ "initWithSet:error:"
+ "initWithSyncReason:senderDeviceUUID:protocolVersion:wallTime:"
+ "initWithUUID:reason:activity:queue:completionHandler:"
+ "initWithVersion:instanceCount:donationDate:fullSetDonationDate:revisionToken:options:"
+ "instanceCount"
+ "isEqualToDiscoveredSet:"
+ "isFullSet"
+ "localDeviceSiteAddingExpirationDate:"
+ "mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:set:mergeableDeltaMetadataVectors:fileFormatVersion:deviceSite:relayedDeviceSites:"
+ "mismatched protocol version %lu, expected %d"
+ "numberWithUnsignedChar:"
+ "priorLocalDonationDate"
+ "priorLocalFullSetDonationDate"
+ "priorLocalSourceRevisionToken"
+ "priors"
+ "readDefaultLocalDeviceUUID:"
+ "reciprocateSyncRequestWithDevice:completionHandler:"
+ "registerRemoteDeviceSite:isPeer:hasDeltas:returningRowId:"
+ "relayedDeviceSitesExcludingRequestingDeviceUUID:"
+ "resourceGeneration"
+ "senderDeviceUUID"
+ "setCascadeDeviceUUID:"
+ "setDiscoveryErrorCode:"
+ "setObject:forKey:"
+ "setSenderDeviceUUID:"
+ "setUUIDsSupportingInboundSync"
+ "setUUIDsSupportingOutboundSync"
+ "startSyncRequestWithReason:activity:completionHandler:"
+ "storedEquivalentForDeviceSite:"
+ "stringByAppendingFormat:"
+ "succeeded"
+ "successfully"
+ "syncCurrentPersonaNowWithReason:activity:completionHandler:"
+ "syncOperationForDiscoveredSet:versionedMergeable:"
+ "timeIntervalSinceNow"
+ "userInfo"
+ "v20@0:8C16"
+ "v32@?0@\"CCRapportDevice\"8@\"NSError\"16^B24"
+ "v36@0:8C16@20@?28"
+ "v44@0:8@16C24@28@?36"
+ "while handling fetchMergeableDeltas for set %@"
+ "while handling set discovery request for set %@"
+ "{unordered_set<long long, std::hash<long long>, std::equal_to<long long>, std::allocator<long long>>=\"__table_\"{__hash_table<long long, std::hash<long long>, std::equal_to<long long>, std::allocator<long long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<long long, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "\t"
- "%@: Failed access database while handling fetch mergeable deltas request for set: %@ error: %@"
- "%@: Failed to discover remote sets, cannot proceed to sync with device %@"
- "%@: No database access - building fetch request with empty state vector for set: %@ (error: %@)"
- "%@: activating file transfer session %@"
- "%@: barrier hit, all deltas fetched for device %@"
- "%@: beginning to fetch deltas for set %@ from device %@"
- "%@: completeRequest:deliveredToDevices %@ withErrors:%@"
- "%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@"
- "%@: could not find device to reciprocate with fallback identifier %@"
- "%@: creating operations for syncing sets with device %@"
- "%@: discovered %@ sets with device %@"
- "%@: discovered devices: %@"
- "%@: discovered synable set %@ for platform %@"
- "%@: done fetching all deltas from device, signalling remote device we are done fetching %@"
- "%@: done fetching deltas for set %@ from device %@"
- "%@: expecting reciprocal request from device %@"
- "%@: failed to enumerate sets with error %@"
- "%@: fetchMergeableDeltasWithReason persona is %@"
- "%@: found syncable set %@"
- "%@: initiated file transfer session with device %@ fileTransferSession %@"
- "%@: initiating file transfer session with device %@"
- "%@: item completion handler invoked for url %@ with error %@"
- "%@: mismatched protocol version %lu, expected %d"
- "%@: no syncable sets"
- "%@: other device is already syncing so will not reciprocate with us, complete the request %@"
- "%@: parent fetch all deltas operation cancelled, cancelling all operations on device operation queue"
- "%@: protocol version mismatch %@, cannot initiate file transfer with device %@"
- "%@: received fetch mergeable deltas request %@ %@"
- "%@: received file transfer item with url %@ from device %@"
- "%@: received item over file transfer session %@"
- "%@: received response from initating file transfer %@ with error %@"
- "%@: received response from set discovery %@ with error %@"
- "%@: received response from signalling end of fetching %@ with error %@"
- "%@: registering to receive incoming files with peer key %@"
- "%@: request %@ already finished running"
- "%@: request timed out because no devices are nearby"
- "%@: request timed out because no devices are nearby or messages in flight to devices failed to respond in time"
- "%@: sending request for set: %@ to device %@"
- "%@: set does not exist on device %@"
- "%@: signalled remote device we are done fetching %@ with error %@"
- "%@: syncing to platform %@ is not supported from this device"
- "%@: unable to determine sender model info: %@"
- "%@[%@]"
- "@40@0:8Q16Q24d32"
- "@60@0:8@16@24@32@40Q48S56"
- "@64@0:8@16@24@32@40Q48@56"
- "@64@0:8@16Q24@32@40@48@?56"
- "CCPersonaSyncManager"
- "CCRapportDevice[%@]: being sent request %@ with options %@"
- "CCRapportErrorDomain"
- "CCRapportFileTransferManager could not get access to sync directory %@"
- "CCRapportFileTransferManager: created directory at path %@ with error %@"
- "CCRapportFileTransferManager: failed to create file transfer directory %@ with error %@"
- "CCRapportFileTransferManager: initializing file transfer diretory with url %@"
- "CloudKitDistributedSync"
- "Completed merge of atom batch for set %@ from device site %@"
- "Done syncing in response to set changes with site identifiers %@"
- "Evaluated set change requiring immmediate sync %@"
- "Failed to decode set from opack encoded set %@"
- "Local source updating set: %@ with stored local item instance count: %@"
- "Remote CRDT merge rejected for set: %@ error: %@ "
- "Skipping relayed device site (%@) matching local device (%@)"
- "Skipping relayed device site (%@) matching peer device (%@)"
- "Syncing in response to set changes with site identifiers %@ encountered errors %@"
- "T@\"NSArray\",&,N,V_setUUIDsSupportingSync"
- "T@\"NSString\",&,N,V_ccDeviceIdentifier"
- "TQ,N,V_syncReason"
- "TQ,R,N,V_syncReason"
- "Transaction timed out after %lf seconds. Aborting update: %@"
- "Triggering immediate sync due to set change for sets %@"
- "Unable to determine sender model info"
- "Vv32@0:8Q16@?24"
- "Vv32@0:8Q16@?<v@?S>24"
- "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?SqQ>52"
- "_ccDeviceIdentifier"
- "_setUUIDsSupportingSync"
- "_shouldCommit"
- "addBarrierBlock:"
- "buildMergeableDeltasRequestForSet:"
- "ccDeviceIdentifier"
- "contents vector is empty %@"
- "endSetDonationWithOptions:completion:"
- "fetchMergableDeltasRequestFromPeerToPeerMessage:deviceSite:set:stateVector:atomBatchVersion:requestOptions:"
- "fetchMergeableDeltasWithReason:activity:completionHandler:"
- "fetchReciprocalMergeableDeltasFromDevice:completionHandler:"
- "fileTransferSessionInitiatedResponseFromPeerToPeerMessage:deviceSite:peerPublicKey:"
- "fileURLWithPathComponents:"
- "handleSetChanges:"
- "initWithQueue:rapportManager:rapportFileTransferManager:readAccess:donateServiceProvider:"
- "initWithSyncReason:protocolVersion:wallTime:"
- "initWithUUID:reason:activity:setUUIDsSupportingSync:queue:completionHandler:"
- "localDeviceRecord"
- "lookupSetConfigurationForSet:"
- "mergeDelta:fromDeviceSite:relayedDeviceSites:"
- "mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:deviceSite:set:mergeableDeltaMetadataVectors:fileFormatVersion:relayedDeviceSites:"
- "registerRemoteDeviceSite:isAttestation:returningRowId:"
- "relayedDeviceSitesNotIncludingRequestingDeviceSite:"
- "senderModelID"
- "setCcDeviceIdentifier:"
- "setSetUUIDsSupportingSync:"
- "setUUIDsSupportingSync"
- "setupSyncEngineToHandleIncomingRequestsForPersona:completionHandler:"
- "syncEngineForCurrentPersona"
- "v40@0:8Q16@24@?32"
- "{unordered_set<long long, std::hash<long long>, std::equal_to<long long>, std::allocator<long long>>=\"__table_\"{__hash_table<long long, std::hash<long long>, std::equal_to<long long>, std::allocator<long long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<long long, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<long long, void *> *>, std::allocator<std::__hash_node<long long, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<long long, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::hash<long long>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::equal_to<long long>>=\"__value_\"f}}}"

```
