## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/Versions/A/CascadeEngine`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x1a744
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x1094
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x51c
-  __TEXT.__cstring: 0x8f8
-  __TEXT.__oslogstring: 0x30b4
+166.17.1.0.0
+  __TEXT.__text: 0x1e864
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0x160c
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x5e0
+  __TEXT.__cstring: 0xc94
+  __TEXT.__oslogstring: 0x344d
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x6d0
-  __TEXT.__objc_classname: 0x452
-  __TEXT.__objc_methname: 0x43c7
-  __TEXT.__objc_methtype: 0xfe2
-  __TEXT.__objc_stubs: 0x3940
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x760
+  __TEXT.__objc_classname: 0x46d
+  __TEXT.__objc_methname: 0x4a2d
+  __TEXT.__objc_methtype: 0x10a7
+  __TEXT.__objc_stubs: 0x3de0
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1020
+  __DATA_CONST.__objc_selrefs: 0x11d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x298
-  __AUTH_CONST.__const: 0x9e0
-  __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x31e0
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_arraydata: 0xb0
+  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__const: 0xb00
+  __AUTH_CONST.__cfstring: 0xa20
+  __AUTH_CONST.__objc_const: 0x3090
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x21c
+  __AUTH.__objc_data: 0x870
+  __DATA.__objc_ivar: 0x24c
   __DATA.__data: 0x720
   __DATA.__bss: 0x24
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34297A04-0298-348A-ACCE-004E81830E4B
-  Functions: 591
-  Symbols:   1739
-  CStrings:  1252
+  UUID: C1B0BCA8-E2FE-3E52-811A-03FA07075017
+  Functions: 673
+  Symbols:   1908
+  CStrings:  1402
 
Symbols:
+ +[CCFetchMergeableDeltasRequest fetchMergableDeltasRequestFromPeerToPeerMessage:deviceSite:set:stateVector:atomBatchVersion:requestOptions:]
+ +[CCFileTransferSessionInitiatedResponse fileTransferSessionInitiatedResponseFromPeerToPeerMessage:deviceSite:peerPublicKey:]
+ +[CCMergeableDeltaFileTransferMessageMetadata mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:deviceSite:set:mergeableDeltaMetadataVectors:fileFormatVersion:relayedDeviceSites:]
+ +[CCRapportFileTransferManager defaultInstance].cold.3
+ +[CCSetDiscoveryRequest setDiscoveryMessageFromPeerToPeerMessage:setUUIDsToDiscover:]
+ +[CCSetDiscoveryResponse setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:]
+ +[CCSetVersionedMergeable emptyStateVector]
+ +[CCSetVersionedMergeable readOnlyInstanceForSet:mergeableDeltasFileURL:database:]
+ +[CCSetVersionedMergeable writeOnlyInstanceForSet:donateServiceProvider:]
+ -[CCAdminConnection initWithConnection:writeAccess:]
+ -[CCAdminConnection performMaintenanceOnAllSets:completion:]
+ -[CCAdminConnection performMaintenanceOnAllSets:completion:].cold.1
+ -[CCAdminConnection removeAllSets:completion:]
+ -[CCAdminConnection removeAllSets:completion:].cold.1
+ -[CCAsyncBlockOperation cancel]
+ -[CCAsyncBlockOperation complete]
+ -[CCAsyncBlockOperation initWithPersonaIdentifier:asyncOperationBlock:]
+ -[CCAsyncBlockOperation isCancelled]
+ -[CCDifferentialUpdater _shouldCommit]
+ -[CCDifferentialUpdater _shouldCommit].cold.1
+ -[CCDifferentialUpdater addItemsWithContents:metaContents:].cold.3
+ -[CCDifferentialUpdater clientAddOrUpdateCount]
+ -[CCDifferentialUpdater clientRemoveCount]
+ -[CCDifferentialUpdater description]
+ -[CCDifferentialUpdater finish]
+ -[CCDifferentialUpdater initWithSet:request:setWriter:database:changeNotifier:completion:]
+ -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]
+ -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.1
+ -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.2
+ -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.3
+ -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.4
+ -[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:].cold.5
+ -[CCDifferentialUpdater removeSourceItemIdentifier:].cold.2
+ -[CCDifferentialUpdater updateType]
+ -[CCDifferentialUpdater waitForCommit:]
+ -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:]
+ -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:].cold.1
+ -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:].cold.2
+ -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:].cold.3
+ -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:].cold.4
+ -[CCDonateConnection mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]
+ -[CCDonateConnection rejectConnection]
+ -[CCDonateConnection resume].cold.3
+ -[CCDonateRequest initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:sourceVersion:sourceValidity:options:accessAssertion:]
+ -[CCDonateRequest isRemoteSync]
+ -[CCDonateRequest options]
+ -[CCDonateRequest reject]
+ -[CCDonateRequest sourceValidity]
+ -[CCDonateRequest sourceVersion]
+ -[CCFetchMergeableDeltasRequest deviceSite]
+ -[CCFetchMergeableDeltasRequest peerPublicKey]
+ -[CCFetchMergeableDeltasRequest requestOptions]
+ -[CCFetchMergeableDeltasRequest setDeviceSite:]
+ -[CCFetchMergeableDeltasRequest setPeerPublicKey:]
+ -[CCFetchMergeableDeltasRequest setRequestOptions:]
+ -[CCFileTransferSessionInitiatedResponse .cxx_destruct]
+ -[CCFileTransferSessionInitiatedResponse deviceSite]
+ -[CCFileTransferSessionInitiatedResponse dictionaryRepresentation]
+ -[CCFileTransferSessionInitiatedResponse initFromDictionary:]
+ -[CCFileTransferSessionInitiatedResponse peerPublicKey]
+ -[CCFileTransferSessionInitiatedResponse setDeviceSite:]
+ -[CCFileTransferSessionInitiatedResponse setPeerPublicKey:]
+ -[CCMergeableDeltaFileTransferMessageMetadata deviceSite]
+ -[CCMergeableDeltaFileTransferMessageMetadata relayedDeviceSites]
+ -[CCMergeableDeltaFileTransferMessageMetadata setDeviceSite:]
+ -[CCMergeableDeltaFileTransferMessageMetadata setRelayedDeviceSites:]
+ -[CCPeerToPeerMessage initWithSyncReason:protocolVersion:wallTime:]
+ -[CCPeerToPeerMessage syncReason]
+ -[CCPersonaSyncManager handleSetChanges:]
+ -[CCRapportRequest initWithUUID:reason:activity:setUUIDsSupportingSync:queue:completionHandler:]
+ -[CCRapportRequest resolvedSetsToSync]
+ -[CCRapportRequest setResolvedSetsToSync:]
+ -[CCRapportRequest setSetUUIDsSupportingSync:]
+ -[CCRapportRequest setSyncReason:]
+ -[CCRapportRequest setUUIDsSupportingSync]
+ -[CCRapportRequest syncReason]
+ -[CCRapportSyncEngine buildBasePeerToPeerMessage]
+ -[CCRapportSyncEngine buildMergeableDeltasRequestForSet:]
+ -[CCRapportSyncEngine description]
+ -[CCRapportSyncEngine lookupSetConfigurationForSet:]
+ -[CCRapportSyncEngine sendSetDiscoveryRequest:toDevice:completionHandler:]
+ -[CCRapportSyncEngine setDiscoveryRequestHandler]
+ -[CCRapportSyncEngine setUUIDsSupportingSync]
+ -[CCSetDiscoveryRequest .cxx_destruct]
+ -[CCSetDiscoveryRequest dictionaryRepresentation]
+ -[CCSetDiscoveryRequest initFromDictionary:]
+ -[CCSetDiscoveryRequest setSetUUIDsToDiscover:]
+ -[CCSetDiscoveryRequest setUUIDsToDiscover]
+ -[CCSetDiscoveryResponse .cxx_destruct]
+ -[CCSetDiscoveryResponse dictionaryRepresentation]
+ -[CCSetDiscoveryResponse discoveredSets]
+ -[CCSetDiscoveryResponse initFromDictionary:]
+ -[CCSetDiscoveryResponse setDiscoveredSets:]
+ -[CCSetStoreUpdateServiceExported _setupAdminConnection]
+ -[CCSetStoreUpdateServiceExported _setupAdminConnection].cold.1
+ -[CCSetStoreUpdateServiceExported beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:]
+ -[CCSetStoreUpdateServiceExported mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]
+ -[CCSetStoreUpdateServiceExported performMaintenanceOnAllSets:completion:]
+ -[CCSetStoreUpdateServiceExported removeAllSets:completion:]
+ -[CCSetVersionedMergeable _loadCachedDeviceMapping:]
+ -[CCSetVersionedMergeable localDeviceSite]
+ -[CCSetVersionedMergeable localDeviceSite].cold.1
+ -[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]
+ -[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:].cold.1
+ -[CCSetVersionedMergeable mergeableDeltaAfterStateVector:atomBatchVersion:options:]
+ -[CCSetVersionedMergeable relayedDeviceSitesNotIncludingRequestingDeviceSite:]
+ -[CCSetVersionedMergeable relayedDeviceSitesNotIncludingRequestingDeviceSite:].cold.1
+ -[CCSetVersionedMergeable stateVector].cold.2
+ GCC_except_table108
+ GCC_except_table116
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table4
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table71
+ GCC_except_table81
+ OBJC_IVAR_$_CCAsyncBlockOperation._cancelled
+ OBJC_IVAR_$_CCAsyncBlockOperation._lock
+ OBJC_IVAR_$_CCAsyncBlockOperation._personaIdentifier
+ OBJC_IVAR_$_CCDifferentialUpdater._deltaProduced
+ OBJC_IVAR_$_CCDifferentialUpdater._requestDescription
+ OBJC_IVAR_$_CCDifferentialUpdater._updateType
+ OBJC_IVAR_$_CCDonateConnection._isXPC
+ OBJC_IVAR_$_CCDonateRequest._options
+ OBJC_IVAR_$_CCDonateRequest._sourceValidity
+ OBJC_IVAR_$_CCDonateRequest._sourceVersion
+ OBJC_IVAR_$_CCFetchMergeableDeltasRequest._deviceSite
+ OBJC_IVAR_$_CCFetchMergeableDeltasRequest._peerPublicKey
+ OBJC_IVAR_$_CCFetchMergeableDeltasRequest._requestOptions
+ OBJC_IVAR_$_CCFileTransferSessionInitiatedResponse._deviceSite
+ OBJC_IVAR_$_CCFileTransferSessionInitiatedResponse._peerPublicKey
+ OBJC_IVAR_$_CCMergeableDeltaFileTransferMessageMetadata._deviceSite
+ OBJC_IVAR_$_CCMergeableDeltaFileTransferMessageMetadata._relayedDeviceSites
+ OBJC_IVAR_$_CCPeerToPeerMessage._syncReason
+ OBJC_IVAR_$_CCPersonaSyncManager._setChangeListener
+ OBJC_IVAR_$_CCRapportManager._personaIdentifier
+ OBJC_IVAR_$_CCRapportRequest._resolvedSetsToSync
+ OBJC_IVAR_$_CCRapportRequest._setUUIDsSupportingSync
+ OBJC_IVAR_$_CCRapportRequest._syncReason
+ OBJC_IVAR_$_CCRapportSyncEngine._personaIdentifier
+ OBJC_IVAR_$_CCSetDiscoveryRequest._setUUIDsToDiscover
+ OBJC_IVAR_$_CCSetDiscoveryResponse._discoveredSets
+ _BMUseCaseMaintenance
+ _CCDifferentialUpdateTypeDescription
+ _OBJC_CLASS_$_CCDatabaseDeviceMapping
+ _OBJC_CLASS_$_CCDeviceSite
+ _OBJC_CLASS_$_CCSetChangeXPCListener
+ _OBJC_CLASS_$_CCSetDiscoveryRequest
+ _OBJC_CLASS_$_CCSetDiscoveryResponse
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_METACLASS_$_CCSetDiscoveryRequest
+ _OBJC_METACLASS_$_CCSetDiscoveryResponse
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ _RPOptionSenderModelID
+ __25-[CCDonateRequest handle]_block_invoke.cold.1
+ __28-[CCDonateConnection resume]_block_invoke.49
+ __30-[CCAsyncBlockOperation start]_block_invoke.2
+ __34-[CCRapportManager didLoseDevice:]_block_invoke.cold.1
+ __38-[CCRapportManager didDiscoverDevice:]_block_invoke.cold.1
+ __39-[CCRapportManager localDeviceUpdated:]_block_invoke.cold.1
+ __41-[CCPersonaSyncManager handleSetChanges:]_block_invoke.cold.1
+ __49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.175
+ __49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.cold.1
+ __49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke.cold.2
+ __57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.185
+ __58-[CCRapportManager createDiscoveryClientWithControlFlags:]_block_invoke.10
+ __58-[CCRapportManager createDiscoveryClientWithControlFlags:]_block_invoke.14
+ __58-[CCRapportManager createDiscoveryClientWithControlFlags:]_block_invoke.6
+ __63-[CCRapportManager sendEvent:event:toDevice:completionHandler:]_block_invoke.30
+ __64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.186
+ __65-[CCRapportManager activateDirectLinkToDevice:completionHandler:]_block_invoke.32
+ __71-[CCRapportManager sendRequest:request:device:options:responseHandler:]_block_invoke.27
+ __72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10
+ __72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10.cold.1
+ __72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.10.cold.2
+ __72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke.cold.1
+ __74-[CCRapportSyncEngine sendSetDiscoveryRequest:toDevice:completionHandler:]_block_invoke.cold.1
+ __74-[CCRapportSyncEngine sendSetDiscoveryRequest:toDevice:completionHandler:]_block_invoke.cold.2
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.61
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.61.cold.1
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.62
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.62.cold.1
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.1
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.2
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.3
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.4
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.5
+ __76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.6
+ __77-[CCSetVersionedMergeable mergeableDeltasForMetadata:atomBatchVersion:error:]_block_invoke.25
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.120
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.127
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.134
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.135
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.136
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.137
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.140
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.141
+ __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke_2.cold.1
+ __82-[CCRapportSyncEngine fetchReciprocalMergeableDeltasFromDevice:completionHandler:]_block_invoke.118
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.151
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.151.cold.1
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.152
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.155
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.155.cold.1
+ __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.155.cold.2
+ __84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.11
+ __84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.12
+ __84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.12.cold.1
+ __84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.12.cold.2
+ __84-[CCDonateConnection mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke_2.cold.1
+ __OBJC_$_CLASS_METHODS_CCSetDiscoveryRequest
+ __OBJC_$_CLASS_METHODS_CCSetDiscoveryResponse
+ __OBJC_$_CLASS_METHODS_CCSetVersionedMergeable
+ __OBJC_$_INSTANCE_METHODS_CCFileTransferSessionInitiatedResponse
+ __OBJC_$_INSTANCE_METHODS_CCSetDiscoveryRequest
+ __OBJC_$_INSTANCE_METHODS_CCSetDiscoveryResponse
+ __OBJC_$_INSTANCE_VARIABLES_CCFileTransferSessionInitiatedResponse
+ __OBJC_$_INSTANCE_VARIABLES_CCSetDiscoveryRequest
+ __OBJC_$_INSTANCE_VARIABLES_CCSetDiscoveryResponse
+ __OBJC_$_PROP_LIST_CCFileTransferSessionInitiatedResponse
+ __OBJC_$_PROP_LIST_CCSetDiscoveryRequest
+ __OBJC_$_PROP_LIST_CCSetDiscoveryResponse
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMOPACKCodable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMOPACKCodable
+ __OBJC_CLASS_RO_$_CCSetDiscoveryRequest
+ __OBJC_CLASS_RO_$_CCSetDiscoveryResponse
+ __OBJC_LABEL_PROTOCOL_$_BMOPACKCodable
+ __OBJC_METACLASS_RO_$_CCSetDiscoveryRequest
+ __OBJC_METACLASS_RO_$_CCSetDiscoveryResponse
+ __OBJC_PROTOCOL_$_BMOPACKCodable
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___30-[CCAsyncBlockOperation start]_block_invoke_2
+ ___34-[CCRapportManager didLoseDevice:]_block_invoke
+ ___38-[CCDonateConnection rejectConnection]_block_invoke
+ ___38-[CCPersonaSyncManager initWithQueue:]_block_invoke
+ ___38-[CCRapportManager didDiscoverDevice:]_block_invoke
+ ___39-[CCDifferentialUpdater waitForCommit:]_block_invoke
+ ___39-[CCRapportManager localDeviceUpdated:]_block_invoke
+ ___41-[CCPersonaSyncManager handleSetChanges:]_block_invoke
+ ___49-[CCRapportSyncEngine setDiscoveryRequestHandler]_block_invoke
+ ___72-[CCSetVersionedMergeable mergeDelta:fromDeviceSite:relayedDeviceSites:]_block_invoke
+ ___74-[CCRapportSyncEngine sendSetDiscoveryRequest:toDevice:completionHandler:]_block_invoke
+ ___76-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
+ ___82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke_2
+ ___84-[CCDonateConnection mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke
+ ___84-[CCDonateConnection mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e15_v16?0"NSSet"8l
+ ___block_descriptor_40_e8_32w_e23_v24?0?<B?>8?<v?>16l
+ ___block_descriptor_40_e8_32w_e5_B8?0l
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSArray"16l
+ ___block_descriptor_48_e8_32s40w_e23_v24?0?<B?>8?<v?>16l
+ ___block_descriptor_49_e8_32s40w_e23_v24?0?<B?>8?<v?>16l
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48bs_e23_v24?0?<B?>8?<v?>16l
+ ___block_descriptor_56_e8_32s40s48bs_e44_v24?0"CCSetDiscoveryResponse"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24l
+ ___block_descriptor_64_e8_32s40s48s56r_e28_v32?0"CKAtomProxy"8Q16^B24l
+ ___block_descriptor_64_e8_32s40s48s56s_e15_v16?0"CCSet"8l
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e23_v24?0?<B?>8?<v?>16l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e45_v24?0"CCRemoteCRDTSetDonation"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56s64r_e41_v24?0"CKDistributedSiteIdentifier"8^B16l
+ ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32s40b48r
+ ___copy_helper_block_e8_32s40s48s56b64w
+ ___copy_helper_block_e8_32s40s48s56s64b72b
+ ___copy_helper_block_e8_32s40s48s56s64r
+ ___destroy_helper_block_e8_32s40s48s56s64r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s
+ ___destroy_helper_block_e8_32s40s48s56s64w
+ _objc_msgSend$_loadCachedDeviceMapping:
+ _objc_msgSend$_setupAdminConnection
+ _objc_msgSend$_shouldCommit
+ _objc_msgSend$allActiveDeviceSites
+ _objc_msgSend$allowsAccessToAllSetsWithMode:
+ _objc_msgSend$beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:
+ _objc_msgSend$buildBasePeerToPeerMessage
+ _objc_msgSend$buildMergeableDeltasRequestForSet:
+ _objc_msgSend$complete
+ _objc_msgSend$constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:
+ _objc_msgSend$copyWithExpirationDate:
+ _objc_msgSend$databaseReadAccessForSet:error:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$descriptionForSiteIdentifier:
+ _objc_msgSend$deviceSite
+ _objc_msgSend$deviceUUID
+ _objc_msgSend$discoveredSets
+ _objc_msgSend$emptyStateVector
+ _objc_msgSend$enumerateAllSets:withOptions:usingBlock:
+ _objc_msgSend$fetchMergableDeltasRequestFromPeerToPeerMessage:deviceSite:set:stateVector:atomBatchVersion:requestOptions:
+ _objc_msgSend$fileTransferSessionInitiatedResponseFromPeerToPeerMessage:deviceSite:peerPublicKey:
+ _objc_msgSend$handleSetChanges:
+ _objc_msgSend$initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:sourceVersion:sourceValidity:options:accessAssertion:
+ _objc_msgSend$initWithConnection:writeAccess:
+ _objc_msgSend$initWithDatabaseAccess:siteIdentifierFormat:
+ _objc_msgSend$initWithDeviceRecords:siteIdentifierFormat:error:
+ _objc_msgSend$initWithIdentifier:batchHandlerBlock:queue:useCase:
+ _objc_msgSend$initWithPersonaIdentifier:asyncOperationBlock:
+ _objc_msgSend$initWithSet:request:setWriter:database:changeNotifier:completion:
+ _objc_msgSend$initWithSyncReason:protocolVersion:wallTime:
+ _objc_msgSend$initWithUUID:reason:activity:setUUIDsSupportingSync:queue:completionHandler:
+ _objc_msgSend$isRemoteSync
+ _objc_msgSend$localDeviceRecord
+ _objc_msgSend$localDeviceSite
+ _objc_msgSend$lookupSetConfigurationForSet:
+ _objc_msgSend$mergeDelta:fromDeviceSite:relayedDeviceSites:
+ _objc_msgSend$mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:
+ _objc_msgSend$mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:
+ _objc_msgSend$mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:
+ _objc_msgSend$mergeableDeltaAfterStateVector:atomBatchVersion:options:
+ _objc_msgSend$mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:deviceSite:set:mergeableDeltaMetadataVectors:fileFormatVersion:relayedDeviceSites:
+ _objc_msgSend$options
+ _objc_msgSend$pathForResource:inContainer:
+ _objc_msgSend$performMaintenanceOnAllSets:completion:
+ _objc_msgSend$priorLocalSourceValidityHash
+ _objc_msgSend$priorLocalSourceVersion
+ _objc_msgSend$readOnlyInstanceForSet:mergeableDeltasFileURL:database:
+ _objc_msgSend$registerRemoteDeviceSite:isAttestation:returningRowId:
+ _objc_msgSend$reject
+ _objc_msgSend$rejectConnection
+ _objc_msgSend$relayedDeviceSites
+ _objc_msgSend$relayedDeviceSitesNotIncludingRequestingDeviceSite:
+ _objc_msgSend$remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:
+ _objc_msgSend$removeAllSets:completion:
+ _objc_msgSend$requestAccess:forResource:withMode:useCase:error:
+ _objc_msgSend$requestOptions
+ _objc_msgSend$resolvedSetsToSync
+ _objc_msgSend$selectAllDeviceRecords
+ _objc_msgSend$sendSetDiscoveryRequest:toDevice:completionHandler:
+ _objc_msgSend$setDeviceSite:
+ _objc_msgSend$setDiscoveredSets:
+ _objc_msgSend$setDiscoveryMessageFromPeerToPeerMessage:setUUIDsToDiscover:
+ _objc_msgSend$setDiscoveryRequestHandler
+ _objc_msgSend$setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:
+ _objc_msgSend$setRelayedDeviceSites:
+ _objc_msgSend$setRequestOptions:
+ _objc_msgSend$setResolvedSetsToSync:
+ _objc_msgSend$setSetUUIDsToDiscover:
+ _objc_msgSend$setUUID
+ _objc_msgSend$setUUIDsSupportingSync
+ _objc_msgSend$setUUIDsToDiscover
+ _objc_msgSend$sourceValidity
+ _objc_msgSend$sourceVersion
+ _objc_msgSend$startClient
+ _objc_msgSend$stopRequestTimeout
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$supportsTransport:direction:fromPlatform:
+ _objc_msgSend$syncEngineForCurrentPersona
+ _objc_msgSend$syncNowWithReason:activity:completionHandler:
+ _objc_msgSend$syncReason
+ _objc_msgSend$teardown
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateType
+ _objc_msgSend$updatedLocalSourceValidityHash
+ _objc_msgSend$updatedLocalSourceVersion
+ _objc_msgSend$updaterForDonateRequest:toDatabase:
+ _objc_msgSend$waitForCommit:
+ _objc_msgSend$writeOnlyInstanceForSet:donateServiceProvider:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sharedQueue.cold.1
- +[CCFetchMergeableDeltasRequest fetchMergableDeltasRequestFromPeerToPeerMessage:set:stateVector:atomBatchVersion:]
- +[CCFileTransferSessionInitiatedResponse fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:]
- +[CCMergeableDeltaFileTransferMessageMetadata mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:set:mergeableDeltaMetadataVectors:fileFormatVersion:peerPublicKey:]
- -[CCAdminConnection initWithConnection:writeAccess:accessAssertion:]
- -[CCAdminConnection removeSetsRootDirectory:]
- -[CCAdminConnection startMaintenanceActivity:]
- -[CCAsyncBlockOperation isAsynchronous]
- -[CCDifferentialUpdater _shouldCommit:]
- -[CCDifferentialUpdater _shouldCommit:].cold.1
- -[CCDifferentialUpdater finish:]
- -[CCDifferentialUpdater initWithSet:device:request:setWriter:database:changeNotifier:completion:]
- -[CCDifferentialUpdater isIncremental]
- -[CCDifferentialUpdater mergeDelta:]
- -[CCDifferentialUpdater mergeDelta:].cold.1
- -[CCDifferentialUpdater mergeDelta:].cold.2
- -[CCDonateConnection beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:]
- -[CCDonateConnection beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:].cold.1
- -[CCDonateConnection beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:].cold.2
- -[CCDonateConnection beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:].cold.3
- -[CCDonateConnection beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:].cold.4
- -[CCDonateConnection mergeDelta:completion:]
- -[CCDonateRequest initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:version:validity:remoteDevice:accessAssertion:]
- -[CCDonateRequest remoteDevice]
- -[CCDonateRequest validity]
- -[CCDonateRequest version]
- -[CCPeerToPeerMessage .cxx_destruct]
- -[CCPeerToPeerMessage device]
- -[CCPeerToPeerMessage initWithDevice:protocolVersion:wallTime:peerPublicKey:]
- -[CCPeerToPeerMessage peerPublicKey]
- -[CCPeerToPeerMessage setPeerPublicKey:]
- -[CCRapportRequest initWithUUID:activity:itemTypesSupportingSync:queue:completionHandler:]
- -[CCRapportRequest itemTypesSupportingSync]
- -[CCRapportRequest setItemTypesSupportingSync:]
- -[CCRapportSyncEngine buildMergeableDeltasRequestForSet:device:]
- -[CCRapportSyncEngine buildVersionedMergeableForSet:]
- -[CCRapportSyncEngine itemTypesSupportingSync]
- -[CCRapportSyncEngine setsWithItemType:]
- -[CCRapportSyncEngine setsWithItemType:].cold.1
- -[CCRapportSyncEngine syncPolicyForSet:]
- -[CCSetStoreUpdateServiceExported _setupAdminService]
- -[CCSetStoreUpdateServiceExported _setupAdminService].cold.1
- -[CCSetStoreUpdateServiceExported _setupAdminService].cold.2
- -[CCSetStoreUpdateServiceExported beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:]
- -[CCSetStoreUpdateServiceExported mergeDelta:completion:]
- -[CCSetStoreUpdateServiceExported removeSetsRootDirectory:]
- -[CCSetStoreUpdateServiceExported startMaintenanceActivity:]
- -[CCSetVersionedMergeable mergeDelta:fromDevice:]
- -[CCSetVersionedMergeable mergeDelta:fromDevice:].cold.1
- -[CCSetVersionedMergeable mergeableDeltaAfterStateVector:atomBatchVersion:]
- GCC_except_table0
- GCC_except_table106
- GCC_except_table109
- GCC_except_table110
- GCC_except_table111
- GCC_except_table17
- GCC_except_table20
- GCC_except_table30
- GCC_except_table51
- GCC_except_table56
- GCC_except_table57
- GCC_except_table58
- GCC_except_table77
- OBJC_IVAR_$_CCAdminConnection._accessAssertion
- OBJC_IVAR_$_CCAsyncBlockOperation._operationQueue
- OBJC_IVAR_$_CCDifferentialUpdater._device
- OBJC_IVAR_$_CCDifferentialUpdater._isIncremental
- OBJC_IVAR_$_CCDifferentialUpdater._stateReader
- OBJC_IVAR_$_CCDifferentialUpdaterFactory._localDevice
- OBJC_IVAR_$_CCDonateRequest._remoteDevice
- OBJC_IVAR_$_CCDonateRequest._validity
- OBJC_IVAR_$_CCDonateRequest._version
- OBJC_IVAR_$_CCPeerToPeerMessage._device
- OBJC_IVAR_$_CCPeerToPeerMessage._peerPublicKey
- OBJC_IVAR_$_CCRapportRequest._itemTypesSupportingSync
- OBJC_IVAR_$_CCRapportSyncEngine._localDeviceIdentifier
- OBJC_IVAR_$_CCSetVersionedMergeable._encodedSetDescriptors
- _BMSetsResource
- _CCPersistedKeyValueKeyLocalDeviceIdentifier
- _OBJC_CLASS_$_CCDevice
- _OBJC_CLASS_$_NSNull
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.40
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.40.cold.1
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.41
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.41.cold.1
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.cold.1
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.cold.2
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.cold.3
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.cold.4
- __36-[CCDifferentialUpdater mergeDelta:]_block_invoke.cold.5
- __44-[CCDonateConnection mergeDelta:completion:]_block_invoke_2.cold.1
- __49-[CCSetVersionedMergeable mergeDelta:fromDevice:]_block_invoke.6
- __49-[CCSetVersionedMergeable mergeDelta:fromDevice:]_block_invoke.6.cold.1
- __49-[CCSetVersionedMergeable mergeDelta:fromDevice:]_block_invoke.6.cold.2
- __49-[CCSetVersionedMergeable mergeDelta:fromDevice:]_block_invoke.cold.1
- __57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.156
- __57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.156.cold.1
- __58-[CCRapportManager createDiscoveryClientWithControlFlags:]_block_invoke.13
- __58-[CCRapportManager createDiscoveryClientWithControlFlags:]_block_invoke.5
- __58-[CCRapportManager createDiscoveryClientWithControlFlags:]_block_invoke.9
- __63-[CCRapportManager sendEvent:event:toDevice:completionHandler:]_block_invoke.29
- __64-[CCRapportSyncEngine doneFetchingMergeableDeltasRequestHandler]_block_invoke.162
- __65-[CCRapportManager activateDirectLinkToDevice:completionHandler:]_block_invoke.31
- __71-[CCRapportManager sendRequest:request:device:options:responseHandler:]_block_invoke.26
- __77-[CCSetVersionedMergeable mergeableDeltasForMetadata:atomBatchVersion:error:]_block_invoke.19
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.106
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.113
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.115
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.116
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.118
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.121
- __82-[CCRapportSyncEngine addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:]_block_invoke.122
- __82-[CCRapportSyncEngine fetchReciprocalMergeableDeltasFromDevice:completionHandler:]_block_invoke.103
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.126
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.130
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.130.cold.1
- __82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke.130.cold.2
- __84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.1
- __84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.2
- __84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.2.cold.1
- __84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.2.cold.2
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCPeerToPeerMessageOPACKCodable
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCPeerToPeerMessageOPACKCodable
- __OBJC_LABEL_PROTOCOL_$_CCPeerToPeerMessageOPACKCodable
- __OBJC_PROTOCOL_$_CCPeerToPeerMessageOPACKCodable
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___32-[CCDifferentialUpdater finish:]_block_invoke
- ___36-[CCDifferentialUpdater mergeDelta:]_block_invoke
- ___44-[CCDonateConnection mergeDelta:completion:]_block_invoke
- ___44-[CCDonateConnection mergeDelta:completion:]_block_invoke_2
- ___49-[CCSetVersionedMergeable mergeDelta:fromDevice:]_block_invoke
- ___82-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:toDevice:completionHandler:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24l
- ___block_descriptor_48_e8_32s40w_e14_v16?0?<v?>8l
- ___block_descriptor_56_e8_32s40bs_e5_v8?0l
- ___block_descriptor_56_e8_32s40s48bs_e14_v16?0?<v?>8l
- ___block_descriptor_56_e8_32s40s48bs_e45_v24?0"CCRemoteCRDTSetDonation"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48r_e28_v32?0"CKAtomProxy"8Q16^B24l
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8l
- ___block_descriptor_57_e8_32s40s48w_e14_v16?0?<v?>8l
- ___block_descriptor_64_e8_32s40s48bs56w_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16l
- ___block_descriptor_64_e8_32s40s48s56r_e41_v24?0"CKDistributedSiteIdentifier"8^B16l
- ___block_descriptor_64_e8_32s40s48s56s_e14_v16?0?<v?>8l
- ___block_descriptor_64_e8_32s40s48s56w_e14_v16?0?<v?>8l
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e5_v8?0l
- ___copy_helper_block_e8_32s40s48b56w
- ___copy_helper_block_e8_32s40s48s56b64b
- ___copy_helper_block_e8_32s40s48s56w
- ___copy_helper_block_e8_32s40s48w
- ___destroy_helper_block_e8_32s40s48s56w
- _objc_msgSend$_setupAdminService
- _objc_msgSend$_shouldCommit:
- _objc_msgSend$allSetsWithOptions:error:
- _objc_msgSend$allowsAccessToSetsWithMode:
- _objc_msgSend$beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:
- _objc_msgSend$buildMergeableDeltasRequestForSet:device:
- _objc_msgSend$buildVersionedMergeableForSet:
- _objc_msgSend$constructStateVectorsFromDatabaseOutContent:outMetaContent:outDeviceMapping:error:
- _objc_msgSend$databaseReadAccessForSet:
- _objc_msgSend$date
- _objc_msgSend$encodedStringFromDescriptors:error:
- _objc_msgSend$fetchMergableDeltasRequestFromPeerToPeerMessage:set:stateVector:atomBatchVersion:
- _objc_msgSend$fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:
- _objc_msgSend$initWithAsyncOperationBlock:
- _objc_msgSend$initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:version:validity:remoteDevice:accessAssertion:
- _objc_msgSend$initWithConnection:writeAccess:accessAssertion:
- _objc_msgSend$initWithData:encoding:
- _objc_msgSend$initWithDatabase:device:request:startTimeMicros:
- _objc_msgSend$initWithDatabaseAccess:
- _objc_msgSend$initWithDevice:protocolVersion:wallTime:peerPublicKey:
- _objc_msgSend$initWithIdentifier:options:
- _objc_msgSend$initWithItemType:personaIdentifier:descriptors:options:error:
- _objc_msgSend$initWithItemType:personaIdentifier:encodedDescriptors:options:error:
- _objc_msgSend$initWithSet:device:request:setWriter:database:changeNotifier:completion:
- _objc_msgSend$initWithType:name:
- _objc_msgSend$initWithUUID:activity:itemTypesSupportingSync:queue:completionHandler:
- _objc_msgSend$integerValue
- _objc_msgSend$isIncremental
- _objc_msgSend$itemTypesSupportingSync
- _objc_msgSend$legacySetsRootDirectoryURL
- _objc_msgSend$localDeviceIdForSet:
- _objc_msgSend$mergeDelta:
- _objc_msgSend$mergeDelta:completion:
- _objc_msgSend$mergeDelta:fromDevice:
- _objc_msgSend$mergeableDeltaAfterStateVector:atomBatchVersion:
- _objc_msgSend$mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:set:mergeableDeltaMetadataVectors:fileFormatVersion:peerPublicKey:
- _objc_msgSend$null
- _objc_msgSend$persistedKeyValueForKey:database:error:
- _objc_msgSend$priorValidityHash
- _objc_msgSend$remoteCRDTSetDonationWithItemType:forAccount:fromDevice:descriptors:serviceProvider:completion:
- _objc_msgSend$remoteDevice
- _objc_msgSend$removeSetsRootDirectory:
- _objc_msgSend$setsWithItemType:
- _objc_msgSend$startMaintenanceActivity:
- _objc_msgSend$stringValue
- _objc_msgSend$syncPolicyForSet:
- _objc_msgSend$timeIntervalSince1970
- _objc_msgSend$unsignedShortValue
- _objc_msgSend$updateValidityHash
- _objc_msgSend$updateVersion
- _objc_msgSend$validity
- _objc_msgSend$version
CStrings:
+ " and removed %u item(s)"
+ "\""
+ "%@ Failed to delete file %@ from file\u00a0transfer directory with error %@"
+ "%@ initialized with update type: %@"
+ "%@ sets root directory: %@"
+ "%@: Failed access database while handling fetch mergeable deltas request for set: %@ error: %@"
+ "%@: Failed to discover remote sets, cannot proceed to sync with device %@"
+ "%@: Failed to enumerate contents of file transfer directory %@"
+ "%@: Failed to fetch attributes of file at path: %@"
+ "%@: Failed to remove item at url %@ with error %@"
+ "%@: No database access - building fetch request with empty state vector for set: %@ (error: %@)"
+ "%@: Skipping pruning of temporary file with creation date: %@, not old enough"
+ "%@: activating file transfer session %@"
+ "%@: adding items %@ to file transfer session %@"
+ "%@: attempting to tear down sync engine but a request is still in progress %@"
+ "%@: barrier hit, all deltas fetched for device %@"
+ "%@: beginning to fetch deltas for set %@ from device %@"
+ "%@: cannot determine set or device from incoming file transfer metadata %@"
+ "%@: completeRequest:deliveredToDevices %@ withErrors:%@"
+ "%@: completing request, still inflight: %@"
+ "%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@"
+ "%@: could not find device to reciprocate with fallback identifier %@"
+ "%@: creating operations for syncing sets with device %@"
+ "%@: discovered %@ sets with device %@"
+ "%@: discovered devices: %@"
+ "%@: discovered local device %@"
+ "%@: discovered synable set %@ for platform %@"
+ "%@: done fetching all deltas from device, signalling remote device we are done fetching %@"
+ "%@: done fetching deltas for set %@ from device %@"
+ "%@: encountered rapport messaging error %@"
+ "%@: engaging with device: %@"
+ "%@: evaluating whether device is supported for messaging %@"
+ "%@: expecting reciprocal request from device %@"
+ "%@: failed to assume persona to handle incoming file with error %@"
+ "%@: failed to enumerate sets with error %@"
+ "%@: fetchMergeableDeltasWithReason persona is %@"
+ "%@: found syncable set %@"
+ "%@: initiated file transfer session with device %@ fileTransferSession %@"
+ "%@: initiating file transfer session with device %@"
+ "%@: item completion handler invoked for url %@ with error %@"
+ "%@: local device %@"
+ "%@: mismatched protocol version %lu, expected %d"
+ "%@: no syncable sets"
+ "%@: other device is already syncing so will not reciprocate with us, complete the request %@"
+ "%@: parent fetch all deltas operation cancelled, cancelling all operations on device operation queue"
+ "%@: protocol version mismatch %@, cannot initiate file transfer with device %@"
+ "%@: received done fetching mergeable deltas message %@ %@"
+ "%@: received fetch mergeable deltas request %@ %@"
+ "%@: received file transfer item with url %@ from device %@"
+ "%@: received item over file transfer session %@"
+ "%@: received response from initating file transfer %@ with error %@"
+ "%@: received response from set discovery %@ with error %@"
+ "%@: received response from signalling end of fetching %@ with error %@"
+ "%@: received set discovery request %@ %@"
+ "%@: reciprocal request completed with %@ %@"
+ "%@: registering to receive incoming files with peer key %@"
+ "%@: request %@ already finished running"
+ "%@: request timed out because no devices are nearby"
+ "%@: request timed out because no devices are nearby or messages in flight to devices failed to respond in time"
+ "%@: sending request for set: %@ to device %@"
+ "%@: set does not exist on device %@"
+ "%@: signalled remote device we are done fetching %@ with error %@"
+ "%@: syncing to platform %@ is not supported from this device"
+ "%@: unable to determine sender model info: %@"
+ "%@: unsupported file format version %@"
+ "%@[%@]"
+ ", client added or updated %u item(s)"
+ "-[CCDifferentialUpdater _tombstoneSet]"
+ "-[CCDifferentialUpdater addItemsWithContents:metaContents:]"
+ "-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]"
+ "-[CCDifferentialUpdater removeSourceItemIdentifier:]"
+ "@\"CCDeviceSite\""
+ "@\"CCSetChangeXPCListener\""
+ "@32@0:8@16@?24"
+ "@32@0:8@16C24S28"
+ "@40@0:8Q16Q24d32"
+ "@60@0:8@16@24@32@40Q48S56"
+ "@64@0:8@16@24@32@40@48@?56"
+ "@64@0:8@16@24@32@40Q48@56"
+ "@64@0:8@16Q24@32@40@48@?56"
+ "@84@0:8@16@24S32@36@44Q52@60Q68@76"
+ "App.InstalledApp"
+ "App.IntentVocabulary.CustomContactGroupName"
+ "App.IntentVocabulary.CustomContactName"
+ "App.IntentVocabulary.CustomMediaPlaylistTitle"
+ "App.IntentVocabulary.CustomVoiceCommandName"
+ "App.Shortcut.Entity"
+ "App.Shortcut.Phrase"
+ "B24@0:8^@16"
+ "B40@0:8@16@24@32"
+ "BMOPACKCodable"
+ "C"
+ "C16@0:8"
+ "CCRapportFileTransferManager: access assertion does not contain a valid path to sync directory %@"
+ "CCSetDiscoveryRequest"
+ "CCSetDiscoveryResponse"
+ "Cannot construct mergeable deltas without device mapping: %@"
+ "Cannot resolve local device site without device mapping: %@"
+ "Committed update: %@ producing %@ changes%@"
+ "Committing update: %@%@%@"
+ "Completed merge of atom batch for set %@ from device site %@"
+ "Contacts.Contact"
+ "Done syncing in response to set changes with site identifiers %@"
+ "Evaluated set change requiring immmediate sync %@"
+ "Failed to assume persona %@ for didDiscoverDevice handler %@"
+ "Failed to assume persona %@ for didLoseDevice handler %@"
+ "Failed to assume persona %@ for localDeviceUpdated handler %@"
+ "Failed to assume persona with error %@, rejecting donate request %@"
+ "Failed to decode deviceSite from opack encoding %@"
+ "Failed to decode set from opack encoded set %@"
+ "Failed to obtain access for maintenance at resource: %@, error: %@"
+ "Failed to obtain access to remove sets root directory with resource: %@, error: %@"
+ "Failed to register peer device site: %@"
+ "Failed to register relayed device site: %@"
+ "Failed to remove"
+ "FullSetDonation"
+ "IncrementalSetDonation"
+ "Local source updating set: %@ with stored local item instance count: %@"
+ "No sets requiring immediate sync, returning from notification handler"
+ "Notified of changes to sets, evaluating policy %@"
+ "Rejecting request %@ with unexpected update type: %@"
+ "Relaying changes not yet supported, dropping atoms for site: %@"
+ "Skipping related device site resolution after device mapping failed: %@"
+ "Skipping relayed device site (%@) matching local device (%@)"
+ "Skipping relayed device site (%@) matching peer device (%@)"
+ "Skipping state vector construction after device mapping failed: %@"
+ "Successfully removed"
+ "Syncing in response to set changes with site identifiers %@ encountered errors %@"
+ "T@\"CCDeviceSite\",&,N,V_deviceSite"
+ "T@\"NSArray\",&,N,V_discoveredSets"
+ "T@\"NSArray\",&,N,V_relayedDeviceSites"
+ "T@\"NSArray\",&,N,V_resolvedSetsToSync"
+ "T@\"NSArray\",&,N,V_setUUIDsSupportingSync"
+ "T@\"NSArray\",&,N,V_setUUIDsToDiscover"
+ "T@\"NSString\",R,N,V_sourceValidity"
+ "TB,R,N,V_isXPC"
+ "TC,R,N,V_updateType"
+ "TI,R,N,V_clientAddOrUpdateCount"
+ "TI,R,N,V_clientRemoveCount"
+ "TQ,N,V_syncReason"
+ "TQ,R,N,V_options"
+ "TQ,R,N,V_sourceVersion"
+ "TQ,R,N,V_syncReason"
+ "TS,N,V_requestOptions"
+ "Transaction timed out after %lf seconds. Aborting update: %@"
+ "Triggering immediate sync due to set change for sets %@"
+ "Unknown (%u)"
+ "Unsupported method: %s for update type: %@"
+ "Updater cannot tombstone donations with added or modified items, aborting"
+ "Vv32@0:8@\"BMResourceSpecifier\"16@?<v@?S>24"
+ "Vv32@0:8@16@?24"
+ "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?SqQ>52"
+ "Vv60@0:8S16@20Q28@36Q44@?52"
+ "_cancelled"
+ "_deltaProduced"
+ "_deviceSite"
+ "_discoveredSets"
+ "_isXPC"
+ "_loadCachedDeviceMapping:"
+ "_lock"
+ "_options"
+ "_relayedDeviceSites"
+ "_requestDescription"
+ "_requestOptions"
+ "_resolvedSetsToSync"
+ "_setChangeListener"
+ "_setUUIDsSupportingSync"
+ "_setUUIDsToDiscover"
+ "_setupAdminConnection"
+ "_shouldCommit"
+ "_sourceValidity"
+ "_sourceVersion"
+ "_syncReason"
+ "_updateType"
+ "allActiveDeviceSites"
+ "allowsAccessToAllSetsWithMode:"
+ "beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:"
+ "buildBasePeerToPeerMessage"
+ "buildMergeableDeltasRequestForSet:"
+ "cancel"
+ "clientAddOrUpdateCount"
+ "clientRemoveCount"
+ "com.apple.biomesyncd.cascade.setDiscoveryRequest"
+ "com.apple.biomesyncd.cascadeSetChange"
+ "complete"
+ "constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:"
+ "copyWithExpirationDate:"
+ "databaseReadAccessForSet:error:"
+ "dateWithTimeIntervalSinceNow:"
+ "descriptionForSiteIdentifier:"
+ "deviceSite"
+ "deviceUUID"
+ "discoveredSets"
+ "emptyStateVector"
+ "enumerateAllSets:withOptions:usingBlock:"
+ "fetchDeltasRequestOptions"
+ "fetchMergableDeltasRequestFromPeerToPeerMessage:deviceSite:set:stateVector:atomBatchVersion:requestOptions:"
+ "fileTransferSessionInitiatedResponseFromPeerToPeerMessage:deviceSite:peerPublicKey:"
+ "handleSetChanges:"
+ "initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:sourceVersion:sourceValidity:options:accessAssertion:"
+ "initWithConnection:writeAccess:"
+ "initWithDatabaseAccess:siteIdentifierFormat:"
+ "initWithDeviceRecords:siteIdentifierFormat:error:"
+ "initWithIdentifier:batchHandlerBlock:queue:useCase:"
+ "initWithPersonaIdentifier:asyncOperationBlock:"
+ "initWithSet:request:setWriter:database:changeNotifier:completion:"
+ "initWithSyncReason:protocolVersion:wallTime:"
+ "initWithUUID:reason:activity:setUUIDsSupportingSync:queue:completionHandler:"
+ "isRemoteSync"
+ "localDeviceRecord"
+ "localDeviceSite"
+ "lookupSetConfigurationForSet:"
+ "mergeDelta:fromDeviceSite:relayedDeviceSites:"
+ "mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:"
+ "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:"
+ "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:"
+ "mergeableDeltaAfterStateVector:atomBatchVersion:options:"
+ "mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:deviceSite:set:mergeableDeltaMetadataVectors:fileFormatVersion:relayedDeviceSites:"
+ "options"
+ "pathForResource:inContainer:"
+ "performMaintenanceOnAllSets:completion:"
+ "priorLocalSourceValidityHash"
+ "priorLocalSourceVersion"
+ "readOnlyInstanceForSet:mergeableDeltasFileURL:database:"
+ "registerRemoteDeviceSite:isAttestation:returningRowId:"
+ "reject"
+ "rejectConnection"
+ "relayedDeviceSites"
+ "relayedDeviceSitesNotIncludingRequestingDeviceSite:"
+ "remoteCRDTSetDonation"
+ "remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:"
+ "removeAllSets:completion:"
+ "requestAccess:forResource:withMode:useCase:error:"
+ "requestOptions"
+ "resolvedSetsToSync"
+ "selectAllDeviceRecords"
+ "sendSetDiscoveryRequest:toDevice:completionHandler:"
+ "senderRapportWorkaroundIdentifier"
+ "setDeviceSite:"
+ "setDiscoveredSets:"
+ "setDiscoveryMessageFromPeerToPeerMessage:setUUIDsToDiscover:"
+ "setDiscoveryRequestHandler"
+ "setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:"
+ "setIdentifiersToDiscover"
+ "setRelayedDeviceSites:"
+ "setRequestOptions:"
+ "setResolvedSetsToSync:"
+ "setSetUUIDsSupportingSync:"
+ "setSetUUIDsToDiscover:"
+ "setSyncReason:"
+ "setUUID"
+ "setUUIDsSupportingSync"
+ "setUUIDsToDiscover"
+ "sourceValidity"
+ "sourceVersion"
+ "stringByAppendingString:"
+ "supportsTransport:direction:fromPlatform:"
+ "syncReason"
+ "unsignedIntValue"
+ "unsignedLongLongValue"
+ "updateType"
+ "updatedLocalSourceValidityHash"
+ "updatedLocalSourceVersion"
+ "updaterForDonateRequest:toDatabase:"
+ "v16@?0@\"CCSet\"8"
+ "v16@?0@\"NSSet\"8"
+ "v20@0:8S16"
+ "v24@?0@\"CCSetDiscoveryResponse\"8@\"NSError\"16"
+ "v24@?0@?<B@?>8@?<v@?>16"
+ "v48@0:8@\"CKMergeableDelta\"16@\"CCDeviceSite\"24@\"NSArray\"32@?<v@?S>40"
+ "waitForCommit:"
+ "writeOnlyInstanceForSet:donateServiceProvider:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "@\"CCDevice\""
- "@28@0:8@16C24"
- "@48@0:8@16@24@32Q40"
- "@48@0:8@16Q24d32@40"
- "@56@0:8@16@24@32@40@?48"
- "@56@0:8@16@24@32Q40@48"
- "@72@0:8@16@24@32@40@48@56@?64"
- "@84@0:8@16@24S32@36@44Q52@60@68@76"
- "B24@0:8^B16"
- "CCPeerToPeerMessageOPACKCodable"
- "CCRapportSyncEngine%@: all sets %@"
- "CCRapportSyncEngine%@: attempting to tear down sync engine but a request is still in progress %@"
- "CCRapportSyncEngine%@: barrier hit, all deltas fetched for device %@"
- "CCRapportSyncEngine%@: beginning to fetch deltas for set %@ from device %@"
- "CCRapportSyncEngine%@: completeRequest:deliveredToDevices %@ withErrors:%@"
- "CCRapportSyncEngine%@: completing request, still inflight: %@"
- "CCRapportSyncEngine%@: could not find device to reciprocate with RPOptionSenderIDSDeviceID %@"
- "CCRapportSyncEngine%@: could not find device to reciprocate with fallback identifier %@"
- "CCRapportSyncEngine%@: creating operations for syncing sets with device %@"
- "CCRapportSyncEngine%@: discovered devices: %@"
- "CCRapportSyncEngine%@: discovered local device %@"
- "CCRapportSyncEngine%@: done fetching all deltas from device, signalling remote device we are done fetching %@"
- "CCRapportSyncEngine%@: done fetching deltas for set %@ from device %@"
- "CCRapportSyncEngine%@: engaging with device: %@"
- "CCRapportSyncEngine%@: evaluating whether device is supported for messaging %@"
- "CCRapportSyncEngine%@: expecting reciprocal request from device %@"
- "CCRapportSyncEngine%@: found syncable set %@"
- "CCRapportSyncEngine%@: local device %@"
- "CCRapportSyncEngine%@: mismatched protocol version %lu, expected %d"
- "CCRapportSyncEngine%@: no set found on device, but set is registered for sync, initiating day zero request for item type %@"
- "CCRapportSyncEngine%@: no syncable sets"
- "CCRapportSyncEngine%@: other device is already syncing so will not reciprocate with us, complete the request %@"
- "CCRapportSyncEngine%@: received done fetching mergeable deltas message %@ %@"
- "CCRapportSyncEngine%@: received request %@ %@"
- "CCRapportSyncEngine%@: reciprocal request completed with %@ %@"
- "CCRapportSyncEngine%@: request %@ already finished running"
- "CCRapportSyncEngine%@: request timed out because no devices are nearby"
- "CCRapportSyncEngine%@: request timed out because no devices are nearby or messages in flight to devices failed to respond in time"
- "CCRapportSyncEngine%@: sending request for set: %@ to device %@"
- "CCRapportSyncEngine%@: set does not exist on device %@"
- "CCRapportSyncEngine%@: signalled remote device we are done fetching %@ with error %@"
- "CCRapportSyncEngine%@: syncing to platform %@ is not supported from this device"
- "CCRapportSyncEngine%@: unable to determine sender model info: %@"
- "CCRapportSyncEngine: activating file transfer session %@"
- "CCRapportSyncEngine: adding items %@ to file transfer session %@"
- "CCRapportSyncEngine: cannot determine set or device from incoming file transfer metadata %@"
- "CCRapportSyncEngine: encountered rapport messaging error %@"
- "CCRapportSyncEngine: initiated file transfer session with device %@ fileTransferSession %@"
- "CCRapportSyncEngine: initiating file transfer session with device %@"
- "CCRapportSyncEngine: item completion handler invoked with error %@"
- "CCRapportSyncEngine: protocol version mismatch %@, cannot initiate file transfer with device %@"
- "CCRapportSyncEngine: received file transfer item with url %@ from device %@"
- "CCRapportSyncEngine: received item over file transfer session %@"
- "CCRapportSyncEngine: received response from initating file transfer %@ with error %@"
- "CCRapportSyncEngine: received response from signalling end of fetching %@ with error %@"
- "CCRapportSyncEngine: registering to receive incoming files with peer key %@"
- "CCRapportSyncEngine: unsupported file format version %@"
- "Committed dataset update producing %@ changes%@"
- "Committing full set update. Client registered %u item(s)"
- "Committing incremental set update. Client added or updated %u item(s) and removed %u item(s)"
- "Completed merge of atom batch for set %@ from device %@"
- "Could not resolve access assertion for specifier: %@, error: %@"
- "Failed to delete file %@ from file\u00a0transfer directory with error %@"
- "Failed to enumerate contents of file transfer directory %@"
- "Failed to fetch attributes of file at path: %@"
- "Failed to find local device identifier for set: %@, request: %@, error: %@"
- "Failed to remove item at url %@ with error %@"
- "Failed to resolve device mapping: %@"
- "Relaying changes not yet supported, dropping atoms for site identifier %@"
- "Removed sets root directory URL: %@ success: %@"
- "Skipping pruning of temporary file with creation date: %@, not old enough"
- "T@\"CCDevice\",R,N,V_device"
- "T@\"CCDevice\",R,N,V_remoteDevice"
- "T@\"NSArray\",&,N,V_itemTypesSupportingSync"
- "T@\"NSString\",R,N,V_validity"
- "TQ,R,N,V_version"
- "Transaction timed out after %lf seconds. Aborting update - %@"
- "Updater can not tombstone donations with added or modified items, aborting"
- "Updater can not tombstone incremental donations, aborting"
- "Updating set: %@ stored local item instance count: %@"
- "Vv24@0:8@?<v@?S>16"
- "Vv60@0:8S16@\"CCDevice\"20@\"NSString\"28Q36@\"NSString\"44@?<v@?SQ>52"
- "Vv60@0:8S16@20@28Q36@44@?52"
- "YES"
- "_encodedSetDescriptors"
- "_isIncremental"
- "_itemTypesSupportingSync"
- "_localDevice"
- "_localDeviceIdentifier"
- "_remoteDevice"
- "_setupAdminService"
- "_shouldCommit:"
- "_validity"
- "_version"
- "a"
- "allSetsWithOptions:error:"
- "allowsAccessToSetsWithMode:"
- "beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:"
- "buildMergeableDeltasRequestForSet:device:"
- "buildVersionedMergeableForSet:"
- "constructStateVectorsFromDatabaseOutContent:outMetaContent:outDeviceMapping:error:"
- "databaseReadAccessForSet:"
- "date"
- "deviceIdentifier"
- "encodedStringFromDescriptors:error:"
- "fetchMergableDeltasRequestFromPeerToPeerMessage:set:stateVector:atomBatchVersion:"
- "fetchMergeableDeltasWithReason persona is %@"
- "fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:"
- "initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:version:validity:remoteDevice:accessAssertion:"
- "initWithConnection:writeAccess:accessAssertion:"
- "initWithData:encoding:"
- "initWithDatabase:device:request:startTimeMicros:"
- "initWithDatabaseAccess:"
- "initWithDevice:protocolVersion:wallTime:peerPublicKey:"
- "initWithIdentifier:options:"
- "initWithItemType:personaIdentifier:descriptors:options:error:"
- "initWithItemType:personaIdentifier:encodedDescriptors:options:error:"
- "initWithSet:device:request:setWriter:database:changeNotifier:completion:"
- "initWithType:name:"
- "initWithUUID:activity:itemTypesSupportingSync:queue:completionHandler:"
- "integerValue"
- "isAsynchronous"
- "isIncremental"
- "itemTypesSupportingSync"
- "legacySetsRootDirectoryURL"
- "localDeviceIdForSet:"
- "mergeDelta:"
- "mergeDelta:completion:"
- "mergeDelta:fromDevice:"
- "mergeableDeltaAfterStateVector:atomBatchVersion:"
- "mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:set:mergeableDeltaMetadataVectors:fileFormatVersion:peerPublicKey:"
- "null"
- "persistedKeyValueForKey:database:error:"
- "priorValidityHash"
- "remoteCRDTSetDonationWithItemType:forAccount:fromDevice:descriptors:serviceProvider:completion:"
- "remoteDevice"
- "removeSetsRootDirectory:"
- "senderIdsIdentifier"
- "setItemTypesSupportingSync:"
- "setsWithItemType:"
- "startMaintenanceActivity:"
- "stringValue"
- "syncPolicyForSet:"
- "timeIntervalSince1970"
- "unsignedShortValue"
- "updateValidityHash"
- "updateVersion"
- "v16@?0@?<v@?>8"
- "v32@0:8@\"CKMergeableDelta\"16@?<v@?S>24"
- "validity"
- "version"

```
