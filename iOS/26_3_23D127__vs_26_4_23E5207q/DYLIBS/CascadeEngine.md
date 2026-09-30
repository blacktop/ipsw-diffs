## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-200.6.0.0.0
-  __TEXT.__text: 0x20b5c
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x189c
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x7dc
-  __TEXT.__cstring: 0x13a0
-  __TEXT.__oslogstring: 0x37f9
+209.12.1.0.0
+  __TEXT.__text: 0x1eaa0
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x1674
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__cstring: 0x194b
+  __TEXT.__oslogstring: 0x2e61
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x888
-  __TEXT.__objc_classname: 0x465
-  __TEXT.__objc_methname: 0x5683
-  __TEXT.__objc_methtype: 0x10ba
-  __TEXT.__objc_stubs: 0x4760
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0xb78
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__objc_classname: 0x431
+  __TEXT.__objc_methname: 0x5383
+  __TEXT.__objc_methtype: 0x10f5
+  __TEXT.__objc_stubs: 0x4580
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__const: 0xae0
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1420
+  __DATA_CONST.__objc_selrefs: 0x1348
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x13e0
-  __AUTH_CONST.__objc_const: 0x3350
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_arraydata: 0x48
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__objc_const: 0x2e58
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x29c
-  __DATA.__data: 0x6c0
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x240
+  __DATA.__data: 0x660
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0x28
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 26E859F5-8014-3D26-BAE6-1946D3F791AA
-  Functions: 714
-  Symbols:   2825
-  CStrings:  1713
+  UUID: 2003DB4D-A1AD-3700-A42F-14D08EDF2E36
+  Functions: 615
+  Symbols:   2579
+  CStrings:  1607
 
Symbols:
+ +[CCSetVersionedMergeable writeOnlyInstanceForSet:donationServiceProvider:]
+ -[CCDifferentialSetUpdater .cxx_destruct]
+ -[CCDifferentialSetUpdater _deleteStaleItems:]
+ -[CCDifferentialSetUpdater _diffUpdateItemContentData:metaContentData:error:]
+ -[CCDifferentialSetUpdater _diffUpdateItemContentData:metaContentData:error:].cold.1
+ -[CCDifferentialSetUpdater _diffUpdateItemContentData:metaContentData:error:].cold.2
+ -[CCDifferentialSetUpdater _diffUpdateItemContentData:metaContentData:error:].cold.3
+ -[CCDifferentialSetUpdater _diffUpdateItemContentData:metaContentData:error:].cold.4
+ -[CCDifferentialSetUpdater _finishWithRevisionToken:designateAsFullSet:error:]
+ -[CCDifferentialSetUpdater _readLocalSourcePriorsFromDatabase]
+ -[CCDifferentialSetUpdater _statusForUpdate]
+ -[CCDifferentialSetUpdater _tombstoneSet:]
+ -[CCDifferentialSetUpdater _unsupportedUpdateTypeForMethod:]
+ -[CCDifferentialSetUpdater _unsupportedUpdateTypeForMethod:].cold.1
+ -[CCDifferentialSetUpdater abort]
+ -[CCDifferentialSetUpdater abort].cold.1
+ -[CCDifferentialSetUpdater addDocumentCacheContents:associatedItemContents:associatedItemMetaContents:associatedSet:error:]
+ -[CCDifferentialSetUpdater addItemsWithContents:metaContents:error:]
+ -[CCDifferentialSetUpdater clientAddOrUpdateCount]
+ -[CCDifferentialSetUpdater clientFinished]
+ -[CCDifferentialSetUpdater clientRemoveCount]
+ -[CCDifferentialSetUpdater description]
+ -[CCDifferentialSetUpdater finishUpdateWithRevisionToken:designateAsFullSet:tombstoneSet:error:]
+ -[CCDifferentialSetUpdater fullSetFallbackError]
+ -[CCDifferentialSetUpdater initWithRequest:databaseWriter:dataResource:error:]
+ -[CCDifferentialSetUpdater priorVersion]
+ -[CCDifferentialSetUpdater priors]
+ -[CCDifferentialSetUpdater removeItemsMatchingPredicate:error:]
+ -[CCDifferentialSetUpdater removeSourceItemIdentifier:error:]
+ -[CCDifferentialSetUpdater request]
+ -[CCDifferentialSetUpdater setStatus:]
+ -[CCDifferentialSetUpdater status]
+ -[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]
+ -[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:].cold.1
+ -[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:].cold.2
+ -[CCDifferentialSetUpdaterFactory .cxx_destruct]
+ -[CCDifferentialSetUpdaterFactory beginUpdateForDonationRequest:error:]
+ -[CCDifferentialSetUpdaterFactory initWithWriteAccess:]
+ -[CCDifferentialUpdateCache addUnwrittenSourceItemIdHash:]
+ -[CCDifferentialUpdateCache hasUnwrittenSourceItemIdHash:]
+ -[CCDifferentialUpdateCache unwrittenItemCount]
+ -[CCDonationRequest .cxx_destruct]
+ -[CCDonationRequest accessAssertion]
+ -[CCDonationRequest attributionFunction]
+ -[CCDonationRequest description]
+ -[CCDonationRequest hasInlineFallback]
+ -[CCDonationRequest hash]
+ -[CCDonationRequest initWithSet:sourceVersion:sourceValidity:options:accessAssertion:]
+ -[CCDonationRequest isEqual:]
+ -[CCDonationRequest isEqualToDonationRequest:]
+ -[CCDonationRequest isFullSet]
+ -[CCDonationRequest isRemoteSync]
+ -[CCDonationRequest noBusyWait]
+ -[CCDonationRequest options]
+ -[CCDonationRequest requestId]
+ -[CCDonationRequest set]
+ -[CCDonationRequest sourceValidity]
+ -[CCDonationRequest sourceVersion]
+ -[CCDonationServiceConnection .cxx_destruct]
+ -[CCDonationServiceConnection _cancelDonation:operation:forError:]
+ -[CCDonationServiceConnection _cancelDonation:operation:forError:].cold.1
+ -[CCDonationServiceConnection _cancelRequestedDonation:forError:]
+ -[CCDonationServiceConnection _cancelRequestedDonation:forError:].cold.1
+ -[CCDonationServiceConnection _performOperation:onUpdater:withBlock:error:]
+ -[CCDonationServiceConnection _performOperation:reply:withBlock:]
+ -[CCDonationServiceConnection _requestUpdateForSetWithIdentifier:descriptors:sourceVersion:sourceValidity:options:error:]
+ -[CCDonationServiceConnection _serviceError:operation:]
+ -[CCDonationServiceConnection _setDonationProgressTimerWithOperationCount:timeElapsed:]
+ -[CCDonationServiceConnection _startDonationProgressTimer]
+ -[CCDonationServiceConnection addItemsWithContents:metaContents:cacheContents:reply:]
+ -[CCDonationServiceConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:]
+ -[CCDonationServiceConnection cancelSetDonation:]
+ -[CCDonationServiceConnection description]
+ -[CCDonationServiceConnection endSetDonationWithOptions:revisionToken:reply:]
+ -[CCDonationServiceConnection initWithXPCConnection:updaterFactory:writeAccess:timeoutCheckInterval:timeoutCheckProgress:queue:]
+ -[CCDonationServiceConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:]
+ -[CCDonationServiceConnection removeItemsMatchingPredicate:reply:]
+ -[CCDonationServiceConnection removeSourceItemIdentifier:reply:]
+ -[CCDonationServiceFactory .cxx_destruct]
+ -[CCDonationServiceFactory initWithWriteAccess:]
+ -[CCDonationServiceFactory initWithWriteAccess:timeoutCheckInterval:timeoutCheckProgress:]
+ -[CCDonationServiceFactory makeConnection:]
+ -[CCDonationServiceFactory makeXPCConnection:]
+ -[CCRapportSyncEngine initWithQueue:rapportManager:readAccess:donationServiceProvider:localDeviceUUID:]
+ -[CCSetStoreUpdateServiceExported addItemsWithContents:metaContents:cacheContents:reply:]
+ -[CCSetStoreUpdateServiceExported beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:]
+ -[CCSetStoreUpdateServiceExported cancelSetDonation:]
+ -[CCSetStoreUpdateServiceExported endSetDonationWithOptions:revisionToken:reply:]
+ -[CCSetStoreUpdateServiceExported initWithQueue:process:connection:writeAccess:donationServiceFactory:]
+ -[CCSetStoreUpdateServiceExported remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:]
+ -[CCSetStoreUpdateServiceExported removeItemsMatchingPredicate:reply:]
+ -[CCSetStoreUpdateServiceExported removeSourceItemIdentifier:reply:]
+ -[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:].cold.2
+ -[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:].cold.3
+ -[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:].cold.4
+ -[CCSetVersionedMergeable initWithSet:readAccess:donationServiceProvider:mergeableDeltasFileURL:]
+ GCC_except_table17
+ GCC_except_table8
+ _BMAccessErrorDomain
+ _CCAttributionFunctionForSet
+ _CCDatabaseErrorDomain
+ _CCDatabaseUnderlyingError
+ _CCDonationServiceRequestDescription
+ _CCDonationServiceRequestParametersDescription
+ _CCDonationServiceStatusDescription
+ _CCItemErrorDomain
+ _CCSetDonationErrorDomain
+ _CCSetErrorWithDetails
+ _CCSourceItemIdentifierHash
+ _OBJC_CLASS_$_CCCachedDocumentUtilities
+ _OBJC_CLASS_$_CCDifferentialSetUpdater
+ _OBJC_CLASS_$_CCDifferentialSetUpdaterFactory
+ _OBJC_CLASS_$_CCDonationRequest
+ _OBJC_CLASS_$_CCDonationServiceConnection
+ _OBJC_CLASS_$_CCDonationServiceFactory
+ _OBJC_CLASS_$_CCDonationServicePriors
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._clientAddOrUpdateCount
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._clientFinished
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._clientRemoveCount
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._dataResource
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._databaseWriter
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._diffUpdateCache
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._fullSetFallbackError
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._itemType
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._priors
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._request
+ _OBJC_IVAR_$_CCDifferentialSetUpdater._status
+ _OBJC_IVAR_$_CCDifferentialSetUpdaterFactory._writeAccess
+ _OBJC_IVAR_$_CCDifferentialUpdateCache._unwritten_set
+ _OBJC_IVAR_$_CCDonationRequest._accessAssertion
+ _OBJC_IVAR_$_CCDonationRequest._attributionFunction
+ _OBJC_IVAR_$_CCDonationRequest._description
+ _OBJC_IVAR_$_CCDonationRequest._options
+ _OBJC_IVAR_$_CCDonationRequest._requestId
+ _OBJC_IVAR_$_CCDonationRequest._set
+ _OBJC_IVAR_$_CCDonationRequest._sourceValidity
+ _OBJC_IVAR_$_CCDonationRequest._sourceVersion
+ _OBJC_IVAR_$_CCDonationServiceConnection._cacheUpdater
+ _OBJC_IVAR_$_CCDonationServiceConnection._cancelationError
+ _OBJC_IVAR_$_CCDonationServiceConnection._queue
+ _OBJC_IVAR_$_CCDonationServiceConnection._setUpdater
+ _OBJC_IVAR_$_CCDonationServiceConnection._timeoutCheckInterval
+ _OBJC_IVAR_$_CCDonationServiceConnection._timeoutCheckProgress
+ _OBJC_IVAR_$_CCDonationServiceConnection._updaterFactory
+ _OBJC_IVAR_$_CCDonationServiceConnection._writeAccess
+ _OBJC_IVAR_$_CCDonationServiceConnection._xpcConnection
+ _OBJC_IVAR_$_CCDonationServiceFactory._queue
+ _OBJC_IVAR_$_CCDonationServiceFactory._timeoutCheckInterval
+ _OBJC_IVAR_$_CCDonationServiceFactory._timeoutCheckProgress
+ _OBJC_IVAR_$_CCDonationServiceFactory._updaterFactory
+ _OBJC_IVAR_$_CCDonationServiceFactory._writeAccess
+ _OBJC_IVAR_$_CCRapportSyncEngine._donationServiceProvider
+ _OBJC_IVAR_$_CCSetStoreUpdateService._donationServiceFactory
+ _OBJC_IVAR_$_CCSetStoreUpdateServiceExported._donationServiceConnection
+ _OBJC_IVAR_$_CCSetStoreUpdateServiceExported._donationServiceFactory
+ _OBJC_IVAR_$_CCSetVersionedMergeable._donationServiceProvider
+ _OBJC_METACLASS_$_CCDifferentialSetUpdater
+ _OBJC_METACLASS_$_CCDifferentialSetUpdaterFactory
+ _OBJC_METACLASS_$_CCDonationRequest
+ _OBJC_METACLASS_$_CCDonationServiceConnection
+ _OBJC_METACLASS_$_CCDonationServiceFactory
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ __OBJC_$_INSTANCE_METHODS_CCDifferentialSetUpdater
+ __OBJC_$_INSTANCE_METHODS_CCDifferentialSetUpdaterFactory
+ __OBJC_$_INSTANCE_METHODS_CCDonationRequest
+ __OBJC_$_INSTANCE_METHODS_CCDonationServiceConnection
+ __OBJC_$_INSTANCE_METHODS_CCDonationServiceFactory
+ __OBJC_$_INSTANCE_VARIABLES_CCDifferentialSetUpdater
+ __OBJC_$_INSTANCE_VARIABLES_CCDifferentialSetUpdaterFactory
+ __OBJC_$_INSTANCE_VARIABLES_CCDonationRequest
+ __OBJC_$_INSTANCE_VARIABLES_CCDonationServiceConnection
+ __OBJC_$_INSTANCE_VARIABLES_CCDonationServiceFactory
+ __OBJC_$_PROP_LIST_CCDifferentialSetUpdater
+ __OBJC_$_PROP_LIST_CCDonationRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDonationService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCDonationService
+ __OBJC_$_PROTOCOL_REFS_CCDonationServiceClient
+ __OBJC_$_PROTOCOL_REFS_CCDonationServiceServer
+ __OBJC_CLASS_PROTOCOLS_$_CCDonationServiceConnection
+ __OBJC_CLASS_RO_$_CCDifferentialSetUpdater
+ __OBJC_CLASS_RO_$_CCDifferentialSetUpdaterFactory
+ __OBJC_CLASS_RO_$_CCDonationRequest
+ __OBJC_CLASS_RO_$_CCDonationServiceConnection
+ __OBJC_CLASS_RO_$_CCDonationServiceFactory
+ __OBJC_LABEL_PROTOCOL_$_CCDonationService
+ __OBJC_LABEL_PROTOCOL_$_CCDonationServiceClient
+ __OBJC_LABEL_PROTOCOL_$_CCDonationServiceServer
+ __OBJC_METACLASS_RO_$_CCDifferentialSetUpdater
+ __OBJC_METACLASS_RO_$_CCDifferentialSetUpdaterFactory
+ __OBJC_METACLASS_RO_$_CCDonationRequest
+ __OBJC_METACLASS_RO_$_CCDonationServiceConnection
+ __OBJC_METACLASS_RO_$_CCDonationServiceFactory
+ __OBJC_PROTOCOL_$_CCDonationService
+ __OBJC_PROTOCOL_$_CCDonationServiceClient
+ __OBJC_PROTOCOL_$_CCDonationServiceServer
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___114-[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]_block_invoke
+ ___114-[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]_block_invoke.75
+ ___114-[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]_block_invoke.75.cold.1
+ ___114-[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]_block_invoke.76
+ ___114-[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]_block_invoke.cold.1
+ ___114-[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]_block_invoke.cold.2
+ ___121-[CCDonationServiceConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:]_block_invoke
+ ___122-[CCDonationServiceConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:]_block_invoke
+ ___46-[CCDifferentialSetUpdater _deleteStaleItems:]_block_invoke
+ ___46-[CCDifferentialSetUpdater _deleteStaleItems:]_block_invoke.cold.1
+ ___49-[CCDonationServiceConnection cancelSetDonation:]_block_invoke
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.86
+ ___63-[CCDifferentialSetUpdater removeItemsMatchingPredicate:error:]_block_invoke
+ ___64-[CCDonationServiceConnection removeSourceItemIdentifier:reply:]_block_invoke
+ ___65-[CCDonationServiceConnection _performOperation:reply:withBlock:]_block_invoke
+ ___66-[CCDonationServiceConnection removeItemsMatchingPredicate:reply:]_block_invoke
+ ___75-[CCDonationServiceConnection _performOperation:onUpdater:withBlock:error:]_block_invoke
+ ___77-[CCDonationServiceConnection endSetDonationWithOptions:revisionToken:reply:]_block_invoke
+ ___77-[CCSetVersionedMergeable mergeableDeltasForMetadata:atomBatchVersion:error:]_block_invoke.22
+ ___85-[CCDonationServiceConnection addItemsWithContents:metaContents:cacheContents:reply:]_block_invoke
+ ___87-[CCDonationServiceConnection _setDonationProgressTimerWithOperationCount:timeElapsed:]_block_invoke
+ ___block_descriptor_32_e38_B24?0"CCDifferentialSetUpdater"8^16l
+ ___block_descriptor_40_e8_32s_e38_B24?0"CCDifferentialSetUpdater"8^16ls32l8
+ ___block_descriptor_42_e8_32s_e38_B24?0"CCDifferentialSetUpdater"8^16ls32l8
+ ___block_descriptor_48_e8_32s40r_e18_B16?0"NSNumber"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e39_v24?0"CCContentProvenanceRecord"8^B16ls32l8s40l8
+ ___block_descriptor_64_e8_32r40w_e5_v8?0lw40l8r32l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s40l8s32l8r56l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e18_B16?0"NSNumber"8ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e30_v40?0{_NSRange=QQ}8C24C28^B32ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e38_B24?0"CCDifferentialSetUpdater"8^16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e28_v32?0"CKAtomProxy"8Q16^B24ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_74_e8_32s40s48s56s64s_e38_B24?0"CCDifferentialSetUpdater"8^16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e41_v24?0"CKDistributedSiteIdentifier"8^B16ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_literal_global.91
+ ___block_literal_global.93
+ ___block_literal_global.95
+ _bzero
+ _objc_msgSend$_cancelDonation:operation:forError:
+ _objc_msgSend$_cancelRequestedDonation:forError:
+ _objc_msgSend$_deleteStaleItems:
+ _objc_msgSend$_diffUpdateItemContentData:metaContentData:error:
+ _objc_msgSend$_finishWithRevisionToken:designateAsFullSet:error:
+ _objc_msgSend$_performOperation:onUpdater:withBlock:error:
+ _objc_msgSend$_performOperation:reply:withBlock:
+ _objc_msgSend$_remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:error:
+ _objc_msgSend$_requestUpdateForSetWithIdentifier:descriptors:sourceVersion:sourceValidity:options:error:
+ _objc_msgSend$_serviceError:operation:
+ _objc_msgSend$_setDonationProgressTimerWithOperationCount:timeElapsed:
+ _objc_msgSend$_startDonationProgressTimer
+ _objc_msgSend$_statusForUpdate
+ _objc_msgSend$_tombstoneSet:
+ _objc_msgSend$_unsupportedUpdateTypeForMethod:
+ _objc_msgSend$addDocumentCacheContents:associatedItemContents:associatedItemMetaContents:associatedSet:error:
+ _objc_msgSend$addItemsWithContents:metaContents:cacheContents:reply:
+ _objc_msgSend$addItemsWithContents:metaContents:error:
+ _objc_msgSend$addUnwrittenSourceItemIdHash:
+ _objc_msgSend$attributionFunction
+ _objc_msgSend$beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:
+ _objc_msgSend$beginUpdateForDonationRequest:error:
+ _objc_msgSend$cacheDescriptorsFromAssociatedSet:error:
+ _objc_msgSend$cancelSetDonation:
+ _objc_msgSend$commitUpdate:
+ _objc_msgSend$databaseWriterForDonationRequest:outDataResource:error:
+ _objc_msgSend$date
+ _objc_msgSend$deleteAllLocalInstances:
+ _objc_msgSend$deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord:
+ _objc_msgSend$deleteSourceItemIdHash:error:
+ _objc_msgSend$deltaProduced
+ _objc_msgSend$documentCachePredicateFromAssociatedSetPredicate:error:
+ _objc_msgSend$documentCacheSetIdentifier
+ _objc_msgSend$endSetDonationWithOptions:revisionToken:reply:
+ _objc_msgSend$enumerateAllSetsWithIdentifiers:descriptors:options:startAfterSet:error:usingBlock:
+ _objc_msgSend$enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
+ _objc_msgSend$enumerateLocalInstancesMatchingPredicate:error:usingBlock:
+ _objc_msgSend$enumerateUnwrittenLocalInstancesWithError:usingBlock:
+ _objc_msgSend$expireRemoteDeviceUUID:error:
+ _objc_msgSend$finishUpdateWithRevisionToken:designateAsFullSet:tombstoneSet:error:
+ _objc_msgSend$fullSetFallbackError
+ _objc_msgSend$hasUnwrittenSourceItemIdHash:
+ _objc_msgSend$initWithQueue:process:connection:writeAccess:donationServiceFactory:
+ _objc_msgSend$initWithQueue:rapportManager:readAccess:donationServiceProvider:localDeviceUUID:
+ _objc_msgSend$initWithRequest:databaseWriter:dataResource:error:
+ _objc_msgSend$initWithSet:readAccess:donationServiceProvider:mergeableDeltasFileURL:
+ _objc_msgSend$initWithSet:sourceVersion:sourceValidity:options:accessAssertion:
+ _objc_msgSend$initWithWriteAccess:timeoutCheckInterval:timeoutCheckProgress:
+ _objc_msgSend$initWithXPCConnection:updaterFactory:writeAccess:timeoutCheckInterval:timeoutCheckProgress:queue:
+ _objc_msgSend$insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:error:
+ _objc_msgSend$insertRemoteContent:contentHash:sequenceNumber:onDeviceRowId:error:
+ _objc_msgSend$isCacheEnabledAssociatedSet:
+ _objc_msgSend$isDocumentCacheSet:
+ _objc_msgSend$isEqualToDonationRequest:
+ _objc_msgSend$joinDonatedDocumentCacheContents:withAssociatedItemContents:associatedItemMetaContents:associatedSet:outContents:outMetaContents:error:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$prepareItemFieldIndexes:
+ _objc_msgSend$registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:error:
+ _objc_msgSend$remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:
+ _objc_msgSend$remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:
+ _objc_msgSend$removeItemsMatchingPredicate:error:
+ _objc_msgSend$removeItemsMatchingPredicate:reply:
+ _objc_msgSend$removeSourceItemIdentifier:error:
+ _objc_msgSend$removeSourceItemIdentifier:reply:
+ _objc_msgSend$rollbackUpdate:
+ _objc_msgSend$selectAllDeviceRecords:
+ _objc_msgSend$selectSourceItemIdHash:outInstanceHash:outContentHash:isDuplicate:error:
+ _objc_msgSend$sequenceNumber
+ _objc_msgSend$setStatus:
+ _objc_msgSend$sharedItemRevisedCount
+ _objc_msgSend$status
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$tombstoneContentSequenceNumbersInRange:forRemoteDeviceRowId:error:
+ _objc_msgSend$unwrittenItemCount
+ _objc_msgSend$updateContent:andMetaContent:sourceItemIdHash:contentHash:instanceHash:isDuplicate:error:
+ _objc_msgSend$updateLastLocalDonationDate:error:
+ _objc_msgSend$updateMetaContent:sourceItemIdHash:instanceHash:contentHash:isDuplicate:error:
+ _objc_msgSend$updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:
+ _objc_msgSend$updateRevisionToken:error:
+ _objc_msgSend$writeOnlyInstanceForSet:donationServiceProvider:
- +[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]
- +[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:].cold.1
- +[CCSetVersionedMergeable writeOnlyInstanceForSet:donateServiceProvider:]
- -[CCDifferentialUpdateCache addUnmodifiedSourceItemIdHash:]
- -[CCDifferentialUpdateCache hasUnmodifiedSourceItemIdHash:]
- -[CCDifferentialUpdateCache unmodifiedItemCount]
- -[CCDifferentialUpdater .cxx_destruct]
- -[CCDifferentialUpdater _clearSetTombstoneStatus]
- -[CCDifferentialUpdater _complete:]
- -[CCDifferentialUpdater _deleteStaleItems]
- -[CCDifferentialUpdater _diffUpdateItemsWithContents:metaContents:]
- -[CCDifferentialUpdater _diffUpdateItemsWithContents:metaContents:].cold.1
- -[CCDifferentialUpdater _diffUpdateItemsWithContents:metaContents:].cold.2
- -[CCDifferentialUpdater _finishWithRevisionToken:designateAsFullSet:]
- -[CCDifferentialUpdater _finishWithRevisionToken:designateAsFullSet:].cold.1
- -[CCDifferentialUpdater _interrupt]
- -[CCDifferentialUpdater _readLocalSourcePriorsFromDatabase]
- -[CCDifferentialUpdater _tombstoneSet]
- -[CCDifferentialUpdater _tombstoneSet].cold.1
- -[CCDifferentialUpdater _tombstoneSet].cold.2
- -[CCDifferentialUpdater abort]
- -[CCDifferentialUpdater addItemsWithContents:metaContents:]
- -[CCDifferentialUpdater addItemsWithContents:metaContents:].cold.1
- -[CCDifferentialUpdater addItemsWithContents:metaContents:].cold.2
- -[CCDifferentialUpdater addItemsWithContents:metaContents:].cold.3
- -[CCDifferentialUpdater clientAddOrUpdateCount]
- -[CCDifferentialUpdater clientFinished]
- -[CCDifferentialUpdater clientRemoveCount]
- -[CCDifferentialUpdater description]
- -[CCDifferentialUpdater didCommit]
- -[CCDifferentialUpdater finishUpdateWithRevisionToken:designateAsFullSet:]
- -[CCDifferentialUpdater incrementalErrorCode]
- -[CCDifferentialUpdater initWithSet:request:setWriter:database:changeNotifier:completion:]
- -[CCDifferentialUpdater modifiedRowCount]
- -[CCDifferentialUpdater priorVersion]
- -[CCDifferentialUpdater priors]
- -[CCDifferentialUpdater removeSourceItemIdentifier:]
- -[CCDifferentialUpdater removeSourceItemIdentifier:].cold.1
- -[CCDifferentialUpdater removeSourceItemIdentifier:].cold.2
- -[CCDifferentialUpdater setDidCommit:]
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.1
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.2
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.3
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.4
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.5
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.6
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.7
- -[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:].cold.8
- -[CCDifferentialUpdater updateType]
- -[CCDifferentialUpdater waitForCommit:]
- -[CCDifferentialUpdaterFactory .cxx_destruct]
- -[CCDifferentialUpdaterFactory initWithWriteAccess:changeNotifier:timeout:]
- -[CCDifferentialUpdaterFactory updaterForSet:withRequest:]
- -[CCDifferentialUpdaterFactory updaterForSet:withRequest:].cold.1
- -[CCDonateConnection .cxx_destruct]
- -[CCDonateConnection _cleanupDonation:]
- -[CCDonateConnection _cleanupRequestState]
- -[CCDonateConnection abortSetDonation]
- -[CCDonateConnection addItemsWithContents:metaContents:completion:]
- -[CCDonateConnection attributionFunction]
- -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:]
- -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:].cold.1
- -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:].cold.2
- -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:].cold.3
- -[CCDonateConnection beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:].cold.4
- -[CCDonateConnection endSetDonationWithOptions:revisionToken:completion:]
- -[CCDonateConnection initWithRequestManager:xpcConnection:]
- -[CCDonateConnection init]
- -[CCDonateConnection isAlive]
- -[CCDonateConnection isXPC]
- -[CCDonateConnection openStreamCompletion]
- -[CCDonateConnection queue]
- -[CCDonateConnection rejectConnection]
- -[CCDonateConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]
- -[CCDonateConnection removeSourceItemIdentifier:completion:]
- -[CCDonateConnection requestManager]
- -[CCDonateConnection request]
- -[CCDonateConnection resume]
- -[CCDonateConnection resume].cold.1
- -[CCDonateConnection resume].cold.2
- -[CCDonateConnection resume].cold.3
- -[CCDonateConnection setAttributionFunction:]
- -[CCDonateConnection setOpenStreamCompletion:]
- -[CCDonateConnection setQueue:]
- -[CCDonateConnection setRequest:]
- -[CCDonateConnection setRequestManager:]
- -[CCDonateConnection setSet:]
- -[CCDonateConnection setUpdater:]
- -[CCDonateConnection setXpcConnection:]
- -[CCDonateConnection set]
- -[CCDonateConnection timeout]
- -[CCDonateConnection updater]
- -[CCDonateConnection xpcConnection]
- -[CCDonateConnectionFactory .cxx_destruct]
- -[CCDonateConnectionFactory initWithRequestManager:]
- -[CCDonateConnectionFactory makeConnection:]
- -[CCDonateConnectionFactory makeXPCConnection:]
- -[CCDonateConnectionFactory terminateConnection:]
- -[CCDonateRequest .cxx_destruct]
- -[CCDonateRequest _connectionTypeString]
- -[CCDonateRequest accessAssertion]
- -[CCDonateRequest description]
- -[CCDonateRequest encodedDescriptors]
- -[CCDonateRequest handle]
- -[CCDonateRequest hasInlineFallback]
- -[CCDonateRequest hash]
- -[CCDonateRequest initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:sourceVersion:sourceValidity:options:accessAssertion:]
- -[CCDonateRequest isEqual:]
- -[CCDonateRequest isEqualToDonateRequest:]
- -[CCDonateRequest isFullSet]
- -[CCDonateRequest isRemoteSync]
- -[CCDonateRequest itemType]
- -[CCDonateRequest options]
- -[CCDonateRequest personaIdentifier]
- -[CCDonateRequest reject]
- -[CCDonateRequest requestId]
- -[CCDonateRequest sourceValidity]
- -[CCDonateRequest sourceVersion]
- -[CCDonateRequest terminateWithType:]
- -[CCDonateRequest timeout]
- -[CCDonateRequestManager .cxx_destruct]
- -[CCDonateRequestManager _beginTransaction]
- -[CCDonateRequestManager _beginTransaction].cold.1
- -[CCDonateRequestManager _dequeue]
- -[CCDonateRequestManager _endTransaction]
- -[CCDonateRequestManager _endTransaction].cold.1
- -[CCDonateRequestManager _enqueue:]
- -[CCDonateRequestManager _handleNextRequest]
- -[CCDonateRequestManager _handleNextRequest].cold.1
- -[CCDonateRequestManager _isActiveRequestId:]
- -[CCDonateRequestManager completeRequest:]
- -[CCDonateRequestManager initWithWriteAccess:]
- -[CCDonateRequestManager initWithWriteAccess:changeNotifier:donationTimeout:]
- -[CCDonateRequestManager init]
- -[CCDonateRequestManager requestAccessToResource:withMode:error:]
- -[CCDonateRequestManager resume]
- -[CCDonateRequestManager submitRequest:]
- -[CCDonateRequestManager suspend]
- -[CCDonateRequestManager updaterFactory]
- -[CCDonateRequestQueueNode .cxx_destruct]
- -[CCDonateRequestQueueNode next]
- -[CCDonateRequestQueueNode request]
- -[CCDonateRequestQueueNode setNext:]
- -[CCDonateRequestQueueNode setRequest:]
- -[CCRapportSyncEngine initWithQueue:rapportManager:readAccess:donateServiceProvider:localDeviceUUID:]
- -[CCSetStoreUpdateServiceExported _setupDonateConnectionWithItemType:]
- -[CCSetStoreUpdateServiceExported _setupDonateConnectionWithItemType:].cold.1
- -[CCSetStoreUpdateServiceExported _setupDonateConnectionWithItemType:].cold.2
- -[CCSetStoreUpdateServiceExported abortSetDonation]
- -[CCSetStoreUpdateServiceExported addItemsWithContents:metaContents:completion:]
- -[CCSetStoreUpdateServiceExported beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:]
- -[CCSetStoreUpdateServiceExported endSetDonationWithOptions:revisionToken:completion:]
- -[CCSetStoreUpdateServiceExported initWithQueue:process:connection:writeAccess:donateConnectionFactory:]
- -[CCSetStoreUpdateServiceExported remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]
- -[CCSetStoreUpdateServiceExported removeSourceItemIdentifier:completion:]
- -[CCSetVersionedMergeable initWithSet:readAccess:donateServiceProvider:mergeableDeltasFileURL:]
- GCC_except_table27
- GCC_except_table59
- GCC_except_table64
- GCC_except_table66
- _CCAttributionIdentifier
- _CCDifferentialUpdateTypeDescription
- _CCDonateRequestTerminationTypeDescription
- _CCDonateServiceRequestDescription
- _CCDonateServiceResponseDescription
- _CCHash64String
- _NSInternalInconsistencyException
- _OBJC_CLASS_$_CCDatabaseUpdater
- _OBJC_CLASS_$_CCDifferentialUpdater
- _OBJC_CLASS_$_CCDifferentialUpdaterFactory
- _OBJC_CLASS_$_CCDonateConnection
- _OBJC_CLASS_$_CCDonateConnectionFactory
- _OBJC_CLASS_$_CCDonateRequest
- _OBJC_CLASS_$_CCDonateRequestManager
- _OBJC_CLASS_$_CCDonateRequestQueueNode
- _OBJC_CLASS_$_CCDonateServicePriors
- _OBJC_CLASS_$_CCSetChangeRemoteXPCNotifier
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$_NSException
- _OBJC_IVAR_$_CCDifferentialUpdateCache._unmodified_set
- _OBJC_IVAR_$_CCDifferentialUpdater._changeNotifier
- _OBJC_IVAR_$_CCDifferentialUpdater._clientAddOrUpdateCount
- _OBJC_IVAR_$_CCDifferentialUpdater._clientFinished
- _OBJC_IVAR_$_CCDifferentialUpdater._clientRemoveCount
- _OBJC_IVAR_$_CCDifferentialUpdater._completion
- _OBJC_IVAR_$_CCDifferentialUpdater._databaseUpdater
- _OBJC_IVAR_$_CCDifferentialUpdater._deltaProduced
- _OBJC_IVAR_$_CCDifferentialUpdater._didCommit
- _OBJC_IVAR_$_CCDifferentialUpdater._diffUpdateCache
- _OBJC_IVAR_$_CCDifferentialUpdater._incrementalErrorCode
- _OBJC_IVAR_$_CCDifferentialUpdater._interrupt
- _OBJC_IVAR_$_CCDifferentialUpdater._priors
- _OBJC_IVAR_$_CCDifferentialUpdater._requestDescription
- _OBJC_IVAR_$_CCDifferentialUpdater._set
- _OBJC_IVAR_$_CCDifferentialUpdater._setWriter
- _OBJC_IVAR_$_CCDifferentialUpdater._updateType
- _OBJC_IVAR_$_CCDifferentialUpdaterFactory._changeNotifier
- _OBJC_IVAR_$_CCDifferentialUpdaterFactory._timeout
- _OBJC_IVAR_$_CCDifferentialUpdaterFactory._writeAccess
- _OBJC_IVAR_$_CCDonateConnection._attributionFunction
- _OBJC_IVAR_$_CCDonateConnection._isXPC
- _OBJC_IVAR_$_CCDonateConnection._openStreamCompletion
- _OBJC_IVAR_$_CCDonateConnection._queue
- _OBJC_IVAR_$_CCDonateConnection._request
- _OBJC_IVAR_$_CCDonateConnection._requestManager
- _OBJC_IVAR_$_CCDonateConnection._set
- _OBJC_IVAR_$_CCDonateConnection._updater
- _OBJC_IVAR_$_CCDonateConnection._xpcConnection
- _OBJC_IVAR_$_CCDonateConnectionFactory._requestManager
- _OBJC_IVAR_$_CCDonateRequest._accessAssertion
- _OBJC_IVAR_$_CCDonateRequest._connection
- _OBJC_IVAR_$_CCDonateRequest._encodedDescriptors
- _OBJC_IVAR_$_CCDonateRequest._itemType
- _OBJC_IVAR_$_CCDonateRequest._manager
- _OBJC_IVAR_$_CCDonateRequest._options
- _OBJC_IVAR_$_CCDonateRequest._personaIdentifier
- _OBJC_IVAR_$_CCDonateRequest._requestHandledSignpostId
- _OBJC_IVAR_$_CCDonateRequest._requestId
- _OBJC_IVAR_$_CCDonateRequest._requestQueuedSignpostId
- _OBJC_IVAR_$_CCDonateRequest._sourceValidity
- _OBJC_IVAR_$_CCDonateRequest._sourceVersion
- _OBJC_IVAR_$_CCDonateRequestManager._activeRequest
- _OBJC_IVAR_$_CCDonateRequestManager._changeNotifier
- _OBJC_IVAR_$_CCDonateRequestManager._donationTimeout
- _OBJC_IVAR_$_CCDonateRequestManager._eventIdCounter
- _OBJC_IVAR_$_CCDonateRequestManager._executionQueue
- _OBJC_IVAR_$_CCDonateRequestManager._firstNode
- _OBJC_IVAR_$_CCDonateRequestManager._lastNode
- _OBJC_IVAR_$_CCDonateRequestManager._registryQueue
- _OBJC_IVAR_$_CCDonateRequestManager._suspended
- _OBJC_IVAR_$_CCDonateRequestManager._transaction
- _OBJC_IVAR_$_CCDonateRequestManager._transactionCounter
- _OBJC_IVAR_$_CCDonateRequestManager._updaterFactory
- _OBJC_IVAR_$_CCDonateRequestManager._writeAccess
- _OBJC_IVAR_$_CCDonateRequestQueueNode._next
- _OBJC_IVAR_$_CCDonateRequestQueueNode._request
- _OBJC_IVAR_$_CCRapportSyncEngine._donateServiceProvider
- _OBJC_IVAR_$_CCSetStoreUpdateService._donateConnectionFactory
- _OBJC_IVAR_$_CCSetStoreUpdateService._donateRequestManager
- _OBJC_IVAR_$_CCSetStoreUpdateServiceExported._donateConnection
- _OBJC_IVAR_$_CCSetStoreUpdateServiceExported._donateConnectionFactory
- _OBJC_IVAR_$_CCSetVersionedMergeable._donateServiceProvider
- _OBJC_METACLASS_$_CCDifferentialUpdater
- _OBJC_METACLASS_$_CCDifferentialUpdaterFactory
- _OBJC_METACLASS_$_CCDonateConnection
- _OBJC_METACLASS_$_CCDonateConnectionFactory
- _OBJC_METACLASS_$_CCDonateRequest
- _OBJC_METACLASS_$_CCDonateRequestManager
- _OBJC_METACLASS_$_CCDonateRequestQueueNode
- __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.MobileSMS
- __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.mobilecal
- __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.mobilesafari
- __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.mobileslideshow
- __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.podcasts
- __ATTRIBUTE_WORK_TO__AppIntentsIndexedEntity-com.apple.reminders
- __ATTRIBUTE_WORK_TO__UNKNOWN
- __OBJC_$_CLASS_METHODS_CCDifferentialUpdater
- __OBJC_$_INSTANCE_METHODS_CCDifferentialUpdater
- __OBJC_$_INSTANCE_METHODS_CCDifferentialUpdaterFactory
- __OBJC_$_INSTANCE_METHODS_CCDonateConnection
- __OBJC_$_INSTANCE_METHODS_CCDonateConnectionFactory
- __OBJC_$_INSTANCE_METHODS_CCDonateRequest
- __OBJC_$_INSTANCE_METHODS_CCDonateRequestManager
- __OBJC_$_INSTANCE_METHODS_CCDonateRequestQueueNode
- __OBJC_$_INSTANCE_VARIABLES_CCDifferentialUpdater
- __OBJC_$_INSTANCE_VARIABLES_CCDifferentialUpdaterFactory
- __OBJC_$_INSTANCE_VARIABLES_CCDonateConnection
- __OBJC_$_INSTANCE_VARIABLES_CCDonateConnectionFactory
- __OBJC_$_INSTANCE_VARIABLES_CCDonateRequest
- __OBJC_$_INSTANCE_VARIABLES_CCDonateRequestManager
- __OBJC_$_INSTANCE_VARIABLES_CCDonateRequestQueueNode
- __OBJC_$_PROP_LIST_CCDifferentialUpdater
- __OBJC_$_PROP_LIST_CCDonateConnection
- __OBJC_$_PROP_LIST_CCDonateRequest
- __OBJC_$_PROP_LIST_CCDonateRequestManager
- __OBJC_$_PROP_LIST_CCDonateRequestQueueNode
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDonateService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCDonateServiceProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCDonateService
- __OBJC_$_PROTOCOL_METHOD_TYPES_CCDonateServiceProvider
- __OBJC_$_PROTOCOL_REFS_CCDonateServiceClient
- __OBJC_$_PROTOCOL_REFS_CCDonateServiceServer
- __OBJC_CLASS_PROTOCOLS_$_CCDonateConnection
- __OBJC_CLASS_PROTOCOLS_$_CCDonateConnectionFactory
- __OBJC_CLASS_RO_$_CCDifferentialUpdater
- __OBJC_CLASS_RO_$_CCDifferentialUpdaterFactory
- __OBJC_CLASS_RO_$_CCDonateConnection
- __OBJC_CLASS_RO_$_CCDonateConnectionFactory
- __OBJC_CLASS_RO_$_CCDonateRequest
- __OBJC_CLASS_RO_$_CCDonateRequestManager
- __OBJC_CLASS_RO_$_CCDonateRequestQueueNode
- __OBJC_LABEL_PROTOCOL_$_CCDonateService
- __OBJC_LABEL_PROTOCOL_$_CCDonateServiceClient
- __OBJC_LABEL_PROTOCOL_$_CCDonateServiceProvider
- __OBJC_LABEL_PROTOCOL_$_CCDonateServiceServer
- __OBJC_METACLASS_RO_$_CCDifferentialUpdater
- __OBJC_METACLASS_RO_$_CCDifferentialUpdaterFactory
- __OBJC_METACLASS_RO_$_CCDonateConnection
- __OBJC_METACLASS_RO_$_CCDonateConnectionFactory
- __OBJC_METACLASS_RO_$_CCDonateRequest
- __OBJC_METACLASS_RO_$_CCDonateRequestManager
- __OBJC_METACLASS_RO_$_CCDonateRequestQueueNode
- __OBJC_PROTOCOL_$_CCDonateService
- __OBJC_PROTOCOL_$_CCDonateServiceClient
- __OBJC_PROTOCOL_$_CCDonateServiceProvider
- __OBJC_PROTOCOL_$_CCDonateServiceServer
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.58
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.58.cold.1
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.59
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.59.cold.1
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.1
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.2
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.3
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.4
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.5
- ___105-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke.cold.6
- ___117-[CCDonateConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke
- ___117-[CCDonateConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke_2
- ___117-[CCDonateConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:]_block_invoke_2.cold.1
- ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke
- ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke.10
- ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke.10.cold.1
- ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke.10.cold.2
- ___123-[CCSetVersionedMergeable _donateRemoteUpdateWithType:fromPeerDeviceUUID:peerDeviceSite:relayedDeviceSites:mergeableDelta:]_block_invoke.cold.1
- ___25-[CCDonateRequest handle]_block_invoke
- ___25-[CCDonateRequest handle]_block_invoke.cold.1
- ___28-[CCDonateConnection resume]_block_invoke
- ___28-[CCDonateConnection resume]_block_invoke.48
- ___28-[CCDonateConnection resume]_block_invoke.49
- ___29-[CCDonateConnection isAlive]_block_invoke
- ___29-[CCDonateConnection timeout]_block_invoke
- ___32-[CCDonateRequestManager resume]_block_invoke
- ___33-[CCDonateRequestManager suspend]_block_invoke
- ___38-[CCDonateConnection abortSetDonation]_block_invoke
- ___38-[CCDonateConnection rejectConnection]_block_invoke
- ___39-[CCDifferentialUpdater waitForCommit:]_block_invoke
- ___40-[CCDonateRequestManager submitRequest:]_block_invoke
- ___42-[CCDifferentialUpdater _deleteStaleItems]_block_invoke
- ___42-[CCDifferentialUpdater _deleteStaleItems]_block_invoke.cold.1
- ___42-[CCDonateRequestManager completeRequest:]_block_invoke
- ___42-[CCDonateRequestManager completeRequest:]_block_invoke.cold.1
- ___44-[CCDonateRequestManager _handleNextRequest]_block_invoke
- ___44-[CCDonateRequestManager _handleNextRequest]_block_invoke.23
- ___44-[CCDonateRequestManager _handleNextRequest]_block_invoke.23.cold.1
- ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.83
- ___60-[CCDonateConnection removeSourceItemIdentifier:completion:]_block_invoke
- ___60-[CCDonateConnection removeSourceItemIdentifier:completion:]_block_invoke_2
- ___67-[CCDonateConnection addItemsWithContents:metaContents:completion:]_block_invoke
- ___67-[CCDonateConnection addItemsWithContents:metaContents:completion:]_block_invoke_2
- ___73-[CCDonateConnection endSetDonationWithOptions:revisionToken:completion:]_block_invoke
- ___73-[CCDonateConnection endSetDonationWithOptions:revisionToken:completion:]_block_invoke_2
- ___77-[CCSetVersionedMergeable mergeableDeltasForMetadata:atomBatchVersion:error:]_block_invoke.31
- ___84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke
- ___84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.11
- ___84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke.11.cold.1
- ___84+[CCDifferentialUpdater updaterForSet:withRequest:setWriter:changeNotifier:timeout:]_block_invoke_2
- ____sharedQueue_block_invoke
- ___block_descriptor_112_e8_32s40s48s56s64s72s80bs88r96r_e49_B24?0"NSObject<CCDatabaseReadWriteAccess>"8^Q16lr88l8s32l8s40l8s48l8s56l8s80l8s64l8s72l8r96l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80bs88r96r_e5_v8?0ls32l8s40l8r88l8s48l8s56l8s80l8s64l8s72l8r96l8
- ___block_descriptor_40_e8_32s_e18_B16?0"NSNumber"8ls32l8
- ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e32_v24?0"CCProvenanceRecord"8^B16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48r_e30_v40?0{_NSRange=QQ}8C24C28^B32ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e8_v12?0B8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56r_e28_v32?0"CKAtomProxy"8Q16^B24ls32l8s40l8s48l8r56l8
- ___block_descriptor_66_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_66_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e41_v24?0"CKDistributedSiteIdentifier"8^B16ls32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e45_v24?0"CCRemoteCRDTSetDonation"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_82_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_literal_global.88
- ___block_literal_global.90
- ___block_literal_global.92
- __os_signpost_emit_with_name_impl
- __recursivelyWaitForTransactionProgress
- __recursivelyWaitForTransactionProgress.cold.1
- __sharedQueue
- __sharedQueue.cold.1
- __sharedQueue.onceToken
- __sharedQueue.sharedQueue
- _objc_claimAutoreleasedReturnValue
- _objc_exception_throw
- _objc_msgSend$_beginTransaction
- _objc_msgSend$_cleanupDonation:
- _objc_msgSend$_cleanupRequestState
- _objc_msgSend$_clearSetTombstoneStatus
- _objc_msgSend$_complete:
- _objc_msgSend$_connectionTypeString
- _objc_msgSend$_deleteStaleItems
- _objc_msgSend$_dequeue
- _objc_msgSend$_diffUpdateItemsWithContents:metaContents:
- _objc_msgSend$_endTransaction
- _objc_msgSend$_enqueue:
- _objc_msgSend$_finishWithRevisionToken:designateAsFullSet:
- _objc_msgSend$_handleNextRequest
- _objc_msgSend$_interrupt
- _objc_msgSend$_isActiveRequestId:
- _objc_msgSend$_setupDonateConnectionWithItemType:
- _objc_msgSend$_tombstoneSet
- _objc_msgSend$abortSetDonation
- _objc_msgSend$accessAssertion
- _objc_msgSend$addItemsWithContents:metaContents:
- _objc_msgSend$addItemsWithContents:metaContents:completion:
- _objc_msgSend$addUnmodifiedSourceItemIdHash:
- _objc_msgSend$allowsAccessToSetStoreUpdateServiceForSet:
- _objc_msgSend$beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:
- _objc_msgSend$completeRequest:
- _objc_msgSend$contentSequenceNumber
- _objc_msgSend$deleteAllLocalInstances
- _objc_msgSend$deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord
- _objc_msgSend$deleteSourceItemIdHash:
- _objc_msgSend$descriptionOfProcessAndUseCase
- _objc_msgSend$endSetDonationWithOptions:revisionToken:completion:
- _objc_msgSend$enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:
- _objc_msgSend$enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
- _objc_msgSend$enumerateUnmodifiedLocalInstancesUsingBlock:
- _objc_msgSend$exceptionWithName:reason:userInfo:
- _objc_msgSend$expireRemoteDeviceUUID:
- _objc_msgSend$finishAndDetectDelta:updateRevisionToken:isFullSet:
- _objc_msgSend$finishUpdateWithRevisionToken:designateAsFullSet:
- _objc_msgSend$handle
- _objc_msgSend$hasUnmodifiedSourceItemIdHash:
- _objc_msgSend$incrementalErrorCode
- _objc_msgSend$initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:sourceVersion:sourceValidity:options:accessAssertion:
- _objc_msgSend$initWithQueue:process:connection:writeAccess:donateConnectionFactory:
- _objc_msgSend$initWithQueue:rapportManager:readAccess:donateServiceProvider:localDeviceUUID:
- _objc_msgSend$initWithRequestManager:
- _objc_msgSend$initWithRequestManager:xpcConnection:
- _objc_msgSend$initWithSet:readAccess:donateServiceProvider:mergeableDeltasFileURL:
- _objc_msgSend$initWithSet:request:setWriter:database:changeNotifier:completion:
- _objc_msgSend$initWithWriteAccess:changeNotifier:donationTimeout:
- _objc_msgSend$initWithWriteAccess:changeNotifier:timeout:
- _objc_msgSend$insertContent:contentHash:sequenceNumber:onDeviceRowId:
- _objc_msgSend$insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:
- _objc_msgSend$isAlive
- _objc_msgSend$isEqualToDonateRequest:
- _objc_msgSend$isXPC
- _objc_msgSend$modifiedRowCount
- _objc_msgSend$next
- _objc_msgSend$notifyChangeToSet:
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$numberWithUnsignedLongLong:
- _objc_msgSend$registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:
- _objc_msgSend$reject
- _objc_msgSend$rejectConnection
- _objc_msgSend$remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:
- _objc_msgSend$remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:
- _objc_msgSend$remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:
- _objc_msgSend$removeSourceItemIdentifier:
- _objc_msgSend$removeSourceItemIdentifier:completion:
- _objc_msgSend$requestAccessToResource:withMode:error:
- _objc_msgSend$selectAllDeviceRecords
- _objc_msgSend$selectProvenanceWithContentSequenceNumber:onDeviceRowId:outProvenanceRowId:
- _objc_msgSend$selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:
- _objc_msgSend$setDidCommit:
- _objc_msgSend$setNext:
- _objc_msgSend$setRequest:
- _objc_msgSend$setWriterForSet:accessAssertion:
- _objc_msgSend$sharedInstance
- _objc_msgSend$sharedItemProvenanceUpdatedCount
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$submitDatabaseTransactionUsingBlock:
- _objc_msgSend$submitRequest:
- _objc_msgSend$terminateWithType:
- _objc_msgSend$timeout
- _objc_msgSend$tombstoneContentSequenceNumbersInRange:forDeviceRowId:
- _objc_msgSend$unmodifiedItemCount
- _objc_msgSend$updateContent:andMetaContent:localInstanceRowId:priorProvenanceRowId:contentHash:instanceHash:isDuplicate:
- _objc_msgSend$updateMetaContent:localInstanceRowId:provenanceRowId:priorInstanceHash:instanceHash:contentHash:contentSequenceNumber:isDuplicate:
- _objc_msgSend$updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:
- _objc_msgSend$updateType
- _objc_msgSend$updaterFactory
- _objc_msgSend$updaterForDonateRequest:toDatabase:
- _objc_msgSend$updaterForSet:withRequest:
- _objc_msgSend$updaterForSet:withRequest:setWriter:changeNotifier:timeout:
- _objc_msgSend$waitForCommit:
- _objc_msgSend$writeOnlyInstanceForSet:donateServiceProvider:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_setProperty_nonatomic_copy
- _os_signpost_enabled
- _os_signpost_id_generate
- _requestCount
- _topDonatorsClientConfig
CStrings:
+ "%@ %@"
+ "%@ Abort failed to rollback database update: %@"
+ "%@ Abort rolled back database update"
+ "%@ Validity and version evolution verified - set is eligible for incremental update from version (%llu) to (%llu)"
+ "%@-%@ %@ %@"
+ "%@: %@ failed to be initialized and verified from itemBuffer length: %@ error: %@"
+ "%@: Canceling donation request: %@"
+ "%@: Canceling donation: %@"
+ "%@: Client has made insufficient progress since last check-in ~%.2lf seconds ago completing only %u operations with threshold %u. Aborting update (total elapsed %.2lf seconds and %u operations or ~%.2lf operations/s)"
+ "%@: Client progress check-in after ~%.2f seconds:\t {%u items added or updated, %u removed}\t[CLIENT FINISHED]"
+ "%@: Client progress check-in after ~%.2lf seconds:\t {%u items added or updated, %u removed}\t(~%.2lf operations/s)"
+ "%@: Committed update: %@ producing %@ changes%@"
+ "%@: Committing update: %@%@%@"
+ "%@: Completed attestation-only update for peer device site: %@ relayed device sites: %@"
+ "%@: Deleted %u item(s) matching predicate: %@"
+ "%@: Donated set contains multiple duplicate sourceItemIds (hash: %@) matching a previously donated item"
+ "%@: Donated set contains multiple duplicate sourceItemIds (hash: %@) not donated previously"
+ "%@: Enabling implicit deletes for incremental donation designated as full set"
+ "%@: Expiring remote deviceUUID: %@"
+ "%@: Failed to insert new sourceItemId (hash: %@)"
+ "%@: Failed to register peer device site: %@"
+ "%@: Failed to register relayed device site: %@"
+ "%@: Failed to update Content and MetaContent for existing sourceItemId (hash: %@)"
+ "%@: Failed to update MetaContent for existing sourceItemId (hash: %@) with unchanged content (hash: %@)"
+ "%@: Full set update contains no modified item(s)"
+ "%@: Full set update is empty - deleting stored items"
+ "%@: Local source updating set with stored local item instance count: %u"
+ "%@: Relaying changes not yet supported, dropping atoms for site: %@"
+ "%@: Skipping sourceItemId (hash: %@) for an item instance (hash: %@) that collides with an existing record unexpectedly"
+ "%@: failed to delete content with sequence numbers in range (%@, %@)"
+ "%@: failed to delete item matching predicate: %@ with sourceItemIdHash: %@"
+ "%@: failed to delete item with sourceItemIdentifier: %@ (hash: %@)"
+ "%@: failed to delete stale item with sourceItemIdHash: %@"
+ "%@: failed to insert content %@ with sequence number %@"
+ "%@: initialized with status: %@"
+ "%@: successfully tombstoned resource"
+ "-[CCDifferentialSetUpdater _tombstoneSet:]"
+ "-[CCDifferentialSetUpdater addDocumentCacheContents:associatedItemContents:associatedItemMetaContents:associatedSet:error:]"
+ "-[CCDifferentialSetUpdater addItemsWithContents:metaContents:error:]"
+ "-[CCDifferentialSetUpdater removeItemsMatchingPredicate:error:]"
+ "-[CCDifferentialSetUpdater removeSourceItemIdentifier:error:]"
+ "-[CCDifferentialSetUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:]"
+ "-[CCDonationServiceConnection addItemsWithContents:metaContents:cacheContents:reply:]"
+ "-[CCDonationServiceConnection cancelSetDonation:]"
+ "-[CCDonationServiceConnection endSetDonationWithOptions:revisionToken:reply:]"
+ "-[CCDonationServiceConnection remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:]"
+ "-[CCDonationServiceConnection removeItemsMatchingPredicate:reply:]"
+ "-[CCDonationServiceConnection removeSourceItemIdentifier:reply:]"
+ ": (%u added, %u updated, %u removed) and shared item changes (%u added, %u removed, %u revised)"
+ "@\"CCDataResource\""
+ "@\"CCDatabaseWriter\""
+ "@\"CCDifferentialSetUpdater\""
+ "@\"CCDifferentialSetUpdaterFactory\""
+ "@\"CCDonationRequest\""
+ "@\"CCDonationServiceConnection\""
+ "@\"CCDonationServiceFactory\""
+ "@\"CCDonationServicePriors\""
+ "@\"NSObject<CCDonationServiceProvider>\""
+ "@24@0:8r*16"
+ "@36@0:8@16B24^@28"
+ "@40@0:8@16d24Q32"
+ "@52@0:8@16@24@32S40@44"
+ "@60@0:8@16@24@32@40S48^@52"
+ "@64@0:8@16@24@32d40Q48@56"
+ "Accepting donation request: %@"
+ "B24@?0@\"CCDifferentialSetUpdater\"8^@16"
+ "B40@0:8@16@24^@32"
+ "B40@0:8@16B24B28^@32"
+ "B48@0:8@16@24@?32^@40"
+ "B56@0:8@16@24@32@40^@48"
+ "B60@0:8@16S24@28@36@44^@52"
+ "CCDifferentialSetUpdater"
+ "CCDifferentialSetUpdaterFactory"
+ "CCDonationRequest"
+ "CCDonationService"
+ "CCDonationServiceClient"
+ "CCDonationServiceConnection"
+ "CCDonationServiceFactory"
+ "CCDonationServiceServer"
+ "Cache content contains asymmetrical batch counts: {%@, %@, %@}"
+ "Cache content donation contains unexpected batch objects: {%@, %@, %@} expected: %@"
+ "Cannot tombstone set with nonzero items added or updated (%u)"
+ "Donation#%llX %@ %@"
+ "Failed to initialize CKAtomBatch from incoming mergeable delta"
+ "No prior set found - full set donation required"
+ "Remote CRDT donation completed for set %@ from deviceUUID: %@"
+ "Remote CRDT donation failed for set: %@ error: %@ "
+ "Requested set (%@) is not supported for outbound sync to platform (%@)"
+ "Requesting parallel update to %@ associated with set: %@"
+ "Set existence is required and resource %@ has not been prepared yet"
+ "T@\"CCDonationRequest\",R,N,V_request"
+ "T@\"CCDonationServicePriors\",R,N,V_priors"
+ "T@\"CCSet\",R,N,V_set"
+ "T@\"NSError\",R,N,V_fullSetFallbackError"
+ "T@\"NSNumber\",R,N,V_sourceVersion"
+ "TC,N,V_status"
+ "T^?,R,N,V_attributionFunction"
+ "Tq,R,N,V_requestId"
+ "Unexpected service state (%@) at donation request: %@"
+ "_cacheUpdater"
+ "_cancelDonation:operation:forError:"
+ "_cancelRequestedDonation:forError:"
+ "_cancelationError"
+ "_dataResource"
+ "_databaseWriter"
+ "_deleteStaleItems:"
+ "_description"
+ "_diffUpdateItemContentData:metaContentData:error:"
+ "_donationServiceConnection"
+ "_donationServiceFactory"
+ "_donationServiceProvider"
+ "_finishWithRevisionToken:designateAsFullSet:error:"
+ "_fullSetFallbackError"
+ "_performOperation:onUpdater:withBlock:error:"
+ "_performOperation:reply:withBlock:"
+ "_remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:error:"
+ "_requestUpdateForSetWithIdentifier:descriptors:sourceVersion:sourceValidity:options:error:"
+ "_serviceError:operation:"
+ "_setDonationProgressTimerWithOperationCount:timeElapsed:"
+ "_setUpdater"
+ "_startDonationProgressTimer"
+ "_status"
+ "_statusForUpdate"
+ "_timeoutCheckInterval"
+ "_timeoutCheckProgress"
+ "_tombstoneSet:"
+ "_unsupportedUpdateTypeForMethod:"
+ "_unwritten_set"
+ "addDocumentCacheContents:associatedItemContents:associatedItemMetaContents:associatedSet:error:"
+ "addItemsWithContents:metaContents:cacheContents:reply:"
+ "addItemsWithContents:metaContents:error:"
+ "addUnwrittenSourceItemIdHash:"
+ "beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:reply:"
+ "beginUpdateForDonationRequest:error:"
+ "cacheDescriptorsFromAssociatedSet:error:"
+ "cancelSetDonation:"
+ "commitUpdate:"
+ "databaseWriterForDonationRequest:outDataResource:error:"
+ "date"
+ "deleteAllLocalInstances:"
+ "deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord:"
+ "deleteSourceItemIdHash:error:"
+ "deltaProduced"
+ "documentCachePredicateFromAssociatedSetPredicate:error:"
+ "documentCacheSetIdentifier"
+ "endSetDonationWithOptions:revisionToken:reply:"
+ "enumerateAllSetsWithIdentifiers:descriptors:options:startAfterSet:error:usingBlock:"
+ "enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
+ "enumerateLocalInstancesMatchingPredicate:error:usingBlock:"
+ "enumerateUnwrittenLocalInstancesWithError:usingBlock:"
+ "expireRemoteDeviceUUID:error:"
+ "finishUpdateWithRevisionToken:designateAsFullSet:tombstoneSet:error:"
+ "fullSetFallbackError"
+ "hasUnwrittenSourceItemIdHash:"
+ "initWithQueue:process:connection:writeAccess:donationServiceFactory:"
+ "initWithQueue:rapportManager:readAccess:donationServiceProvider:localDeviceUUID:"
+ "initWithRequest:databaseWriter:dataResource:error:"
+ "initWithSet:readAccess:donationServiceProvider:mergeableDeltasFileURL:"
+ "initWithSet:sourceVersion:sourceValidity:options:accessAssertion:"
+ "initWithWriteAccess:timeoutCheckInterval:timeoutCheckProgress:"
+ "initWithXPCConnection:updaterFactory:writeAccess:timeoutCheckInterval:timeoutCheckProgress:queue:"
+ "insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:error:"
+ "insertRemoteContent:contentHash:sequenceNumber:onDeviceRowId:error:"
+ "isCacheEnabledAssociatedSet:"
+ "isDocumentCacheSet:"
+ "isEqualToDonationRequest:"
+ "joinDonatedDocumentCacheContents:withAssociatedItemContents:associatedItemMetaContents:associatedSet:outContents:outMetaContents:error:"
+ "method: %s unsupported for update: %@"
+ "noBusyWait"
+ "numberWithLongLong:"
+ "operation: %@ resulted in inconsistent status for set (%@) and cache (%@)"
+ "prepareItemFieldIndexes:"
+ "registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:error:"
+ "remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:reply:"
+ "remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:"
+ "removeItemsMatchingPredicate:error:"
+ "removeItemsMatchingPredicate:reply:"
+ "removeSourceItemIdentifier:error:"
+ "removeSourceItemIdentifier:reply:"
+ "rollbackUpdate:"
+ "selectAllDeviceRecords:"
+ "selectSourceItemIdHash:outInstanceHash:outContentHash:isDuplicate:error:"
+ "sequenceNumber"
+ "setStatus:"
+ "sharedItemRevisedCount"
+ "status"
+ "timeIntervalSince1970"
+ "tombstoneContentSequenceNumbersInRange:forRemoteDeviceRowId:error:"
+ "unwrittenItemCount"
+ "updateContent:andMetaContent:sourceItemIdHash:contentHash:instanceHash:isDuplicate:error:"
+ "updateLastLocalDonationDate:error:"
+ "updateMetaContent:sourceItemIdHash:instanceHash:contentHash:isDuplicate:error:"
+ "updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:error:"
+ "updateRevisionToken:error:"
+ "v24@0:8@?<v@?C@\"NSError\">16"
+ "v24@?0@\"CCContentProvenanceRecord\"8^B16"
+ "v28@0:8I16d20"
+ "v32@0:8@\"CCItemFieldPredicate\"16@?<v@?C@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?C@\"NSError\">24"
+ "v32@0:8@?16@24"
+ "v36@0:8S16@\"NSString\"20@?<v@?C@\"NSError\">28"
+ "v36@0:8S16@20@?28"
+ "v40@0:8@?16@24@32"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@?<v@?C@\"NSError\">40"
+ "v56@0:8S16@\"NSString\"20@\"NSNumber\"28@\"NSString\"36S44@?<v@?C@\"NSError\"@\"CCDonationServicePriors\">48"
+ "v56@0:8S16@20@28@36S44@?48"
+ "v60@0:8@\"NSUUID\"16S24@\"CKMergeableDelta\"28@\"CCDeviceSite\"36@\"NSArray\"44@?<v@?C@\"NSError\">52"
+ "writeOnlyInstanceForSet:donationServiceProvider:"
- " enableTelemetry=YES "
- " itemType=%{public,signpost.telemetry:number1}d  requestType=%{public,signpost.telemetry:string1}@  result=%{public,signpost.telemetry:string2}@ "
- " requestType=%{public,signpost.telemetry:string1}@  itemType=%{public,signpost.telemetry:number1}d "
- "\""
- "#%u [%@] %@"
- "%@ could not resolve set identifier for item type %hu'"
- "%@ failed to be initialized and verified from itemBuffer length: %@ error: %@"
- "%@ initialized with update type: %@"
- "%@ is not entitled to access the set store update service for set: %@"
- "-[CCDifferentialUpdater _tombstoneSet]"
- "-[CCDifferentialUpdater addItemsWithContents:metaContents:]"
- "-[CCDifferentialUpdater removeSourceItemIdentifier:]"
- "-[CCDifferentialUpdater updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:]"
- ": (%u added, %u updated, %u removed) and shared item changes (%u added, %u removed, %u provenance updated)"
- "@\"<CCSetChangeNotifierProtocol>\""
- "@\"CCDataResourceWriter\""
- "@\"CCDatabaseUpdater\""
- "@\"CCDifferentialUpdater\""
- "@\"CCDifferentialUpdaterFactory\""
- "@\"CCDonateConnection\""
- "@\"CCDonateConnectionFactory\""
- "@\"CCDonateRequest\""
- "@\"CCDonateRequestManager\""
- "@\"CCDonateRequestQueueNode\""
- "@\"CCDonateServicePriors\""
- "@\"NSObject<CCDonateService>\"24@0:8@\"NSString\"16"
- "@\"NSObject<CCDonateServiceProvider>\""
- "@40@0:8@16@24d32"
- "@40@0:8@16Q24^@32"
- "@56@0:8@16@24@32@40d48"
- "@64@0:8@16@24@32@40@48@?56"
- "@80@0:8@16@24S32@36@44Q52@60S68@72"
- "Aborting after failure to finish update"
- "Accepting request %@ with response: %@"
- "Acquired OS transaction: %@"
- "All enqueued donate requests have been handled."
- "AppIntentsIndexedEntity-com.apple.MobileSMS"
- "AppIntentsIndexedEntity-com.apple.mobilecal"
- "AppIntentsIndexedEntity-com.apple.mobilesafari"
- "AppIntentsIndexedEntity-com.apple.mobileslideshow"
- "AppIntentsIndexedEntity-com.apple.podcasts"
- "AppIntentsIndexedEntity-com.apple.reminders"
- "B20@0:8B16"
- "B20@0:8I16"
- "B20@0:8S16"
- "B24@?0@\"NSObject<CCDatabaseReadWriteAccess>\"8^Q16"
- "B28@0:8@16B24"
- "B52@0:8@16S24@28@36@44"
- "CCDifferentialUpdater"
- "CCDifferentialUpdaterFactory"
- "CCDonateConnection"
- "CCDonateConnectionFactory"
- "CCDonateRequest"
- "CCDonateRequestManager"
- "CCDonateRequestQueueNode"
- "CCDonateService"
- "CCDonateServiceClient"
- "CCDonateServiceProvider"
- "CCDonateServiceServer"
- "Cleaning up request %@ with termination type %@"
- "Client has made insufficient progress since last check-in ~%.2lf seconds ago completing only %u operations (%.2lf/s with threshold of %lf/s). Aborting update: %@"
- "Client progress check-in after ~%.2lf seconds:\t {%u items added or updated, %u removed}\t(~%.2lf operations/s)"
- "Client progress check-in after ~%.2lf seconds:\t {%u items added or updated, %u removed}\t[CLIENT FINISHED]"
- "ClientAborted"
- "Committed update: %@ producing %@ changes%@"
- "Committing update: %@%@%@"
- "Completed attestation-only update for peer device site: %@ relayed device sites: %@"
- "Completing request %@ with response %@"
- "Connection is invalidated for request %@"
- "Database update %@ for request %@"
- "DifferentialUpdater"
- "Donate request %@ handling complete"
- "Donate request %@ no longer active."
- "DonateConnection"
- "Donated set contains multiple duplicate sourceItemIds (hash: %@) matching a previously donated item"
- "Donated set contains multiple duplicate sourceItemIds (hash: %@) not donated previously"
- "Enabling implicit deletes for incremental donation designated as full set"
- "Expiring Donate requestId: %u after %lf seconds"
- "Expiring remote deviceUUID: %@"
- "Failed to assume persona with error %@, rejecting donate request %@"
- "Failed to construct device mapping: %@"
- "Failed to initialize CKAtomBatch from incoming mergeable delta %@, %@"
- "Failed to initialize content message: %@"
- "Failed to initialize instance from content: %@ metaContent: %@ error: %@"
- "Failed to initialize metaContent message: %@"
- "Failed to initialize updater - %@"
- "Failed to insert new sourceItemId (hash: %@)"
- "Failed to obtain data resource writer for set: %@, request: %@"
- "Failed to obtain read only access for mergeable deltas resource %@"
- "Failed to obtain write access for resource: %@, error: %@"
- "Failed to register peer device site: %@"
- "Failed to register relayed device site: %@"
- "Failed to remove sourceItemId: %@ (hash: %@)"
- "Failed to remove stale sourceItemId (hash: %@)"
- "Failed to resolve set: %@"
- "Failed to update Content and MetaContent for existing sourceItemId (hash: %@)"
- "Failed to update MetaContent for existing sourceItemId (hash: %@) with unchanged content (hash: %@)"
- "Full set update contains no modified item(s)"
- "Full set update is empty - deleting stored items"
- "FullSetDonation"
- "Handling donate request %@"
- "In Process"
- "IncrementalSetDonation"
- "Invalid descriptors: %@"
- "Invalid itemType: %@"
- "Local source updating set: %@ with stored local item instance count: %u"
- "No prior set found - full update required"
- "Rejecting request %@ after updater failed to be initialized"
- "Rejecting request %@ with unexpected update type: %@"
- "Relaying changes not yet supported, dropping atoms for site: %@"
- "Releasing OS transaction: %@"
- "Remote CRDT donation %@ for set %@ from deviceUUID: %@"
- "ServiceError"
- "ServiceRejected"
- "ServiceTimedOut"
- "Skipping sourceItemId (hash: %@) for an item instance (hash: %@) that collides with an existing record unexpectedly"
- "Submitting transaction for request %@"
- "T@\"CCDifferentialUpdater\",&,N,V_updater"
- "T@\"CCDifferentialUpdaterFactory\",R,N,V_updaterFactory"
- "T@\"CCDonateRequest\",&,N,V_request"
- "T@\"CCDonateRequest\",W,N,V_request"
- "T@\"CCDonateRequestManager\",&,N,V_requestManager"
- "T@\"CCDonateRequestQueueNode\",&,N,V_next"
- "T@\"CCDonateServicePriors\",R,N,V_priors"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",R,N,V_encodedDescriptors"
- "T@\"NSString\",R,N,V_personaIdentifier"
- "T@\"NSXPCConnection\",W,N,V_xpcConnection"
- "T@?,C,N,V_openStreamCompletion"
- "TB,N,V_didCommit"
- "TB,R,N,V_isXPC"
- "TC,R,N,V_updateType"
- "TI,R,N,V_requestId"
- "TQ,R,N,V_sourceVersion"
- "TS,R,N,V_itemType"
- "T^?,N,V_attributionFunction"
- "Timed out waiting for asynchronous donate operation. timeout=%@ seconds"
- "Timed out waiting for updater to be initialized for %lf seconds - %@"
- "Tq,R,N,V_incrementalErrorCode"
- "Transaction timed out after more than %lf seconds. Aborting update: %@"
- "UNKNOWN"
- "Undefined"
- "Unexpected state {completion: %@, request: %@, set: %@}"
- "Unsupported method: %s for update type: %@"
- "Updater cannot tombstone donations with added or modified items, aborting"
- "Updater successfully tombstoned resource"
- "Validity and version evolution verified - set is eligible for incremental update from version (%llu) to (%llu)"
- "Vv36@0:8S16@\"NSString\"20@?<v@?S>28"
- "Vv36@0:8S16@20@?28"
- "Vv56@0:8S16@\"NSString\"20Q28@\"NSString\"36S44@?<v@?Sq@\"CCDonateServicePriors\">48"
- "Vv56@0:8S16@20Q28@36S44@?48"
- "_activeRequest"
- "_beginTransaction"
- "_changeNotifier"
- "_cleanupDonation:"
- "_cleanupRequestState"
- "_clearSetTombstoneStatus"
- "_complete:"
- "_connectionTypeString"
- "_databaseUpdater"
- "_deleteStaleItems"
- "_deltaProduced"
- "_dequeue"
- "_didCommit"
- "_diffUpdateItemsWithContents:metaContents:"
- "_donateConnection"
- "_donateConnectionFactory"
- "_donateRequestManager"
- "_donateServiceProvider"
- "_donationTimeout"
- "_encodedDescriptors"
- "_endTransaction"
- "_enqueue:"
- "_eventIdCounter"
- "_executionQueue"
- "_finishWithRevisionToken:designateAsFullSet:"
- "_firstNode"
- "_handleNextRequest"
- "_incrementalErrorCode"
- "_interrupt"
- "_isActiveRequestId:"
- "_isXPC"
- "_lastNode"
- "_manager"
- "_next"
- "_openStreamCompletion"
- "_registryQueue"
- "_requestDescription"
- "_requestHandledSignpostId"
- "_requestManager"
- "_requestQueuedSignpostId"
- "_setWriter"
- "_setupDonateConnectionWithItemType:"
- "_suspended"
- "_timeout"
- "_tombstoneSet"
- "_transactionCounter"
- "_unmodified_set"
- "_updateType"
- "_updater"
- "abortSetDonation"
- "aborted"
- "addItemsWithContents:metaContents:"
- "addItemsWithContents:metaContents:completion:"
- "addUnmodifiedSourceItemIdHash:"
- "allowsAccessToSetStoreUpdateServiceForSet:"
- "beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:"
- "committed"
- "completeRequest:"
- "contentSequenceNumber"
- "deleteAllLocalInstances"
- "deleteContentRecordsNoLongerReferencedByAnyProvenanceRecord"
- "deleteSourceItemIdHash:"
- "descriptionOfProcessAndUseCase"
- "didCommit"
- "donateRequestHandled"
- "donateRequestQueued"
- "dropping atom with dot %@::%@ which we've already received"
- "endSetDonationWithOptions:revisionToken:completion:"
- "enumerateAllSets:withOptions:setIdentifiers:descriptors:startAfterSet:usingBlock:"
- "enumerateProvenanceRecordsForStateVector:withType:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"
- "enumerateUnmodifiedLocalInstancesUsingBlock:"
- "exceptionWithName:reason:userInfo:"
- "executionQueue"
- "expireRemoteDeviceUUID:"
- "failed"
- "failed to delete content with sequence numbers in range (%@, %@)"
- "failed to insert content %@ with sequence number %@"
- "failed to search for existing provenance row for content hash %@ with sequence number %@"
- "finishAndDetectDelta:updateRevisionToken:isFullSet:"
- "finishUpdateWithRevisionToken:designateAsFullSet:"
- "handle"
- "hasUnmodifiedSourceItemIdHash:"
- "incrementalErrorCode"
- "init unsupported"
- "initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:sourceVersion:sourceValidity:options:accessAssertion:"
- "initWithQueue:process:connection:writeAccess:donateConnectionFactory:"
- "initWithQueue:rapportManager:readAccess:donateServiceProvider:localDeviceUUID:"
- "initWithRequestManager:"
- "initWithRequestManager:xpcConnection:"
- "initWithSet:readAccess:donateServiceProvider:mergeableDeltasFileURL:"
- "initWithSet:request:setWriter:database:changeNotifier:completion:"
- "initWithWriteAccess:changeNotifier:donationTimeout:"
- "initWithWriteAccess:changeNotifier:timeout:"
- "insertContent:contentHash:sequenceNumber:onDeviceRowId:"
- "insertItemWithSourceItemIdHash:instanceHash:contentHash:metaContent:content:isDuplicate:"
- "inserting atom with dot %@::%@ contentHash %@"
- "isAlive"
- "isEqualToDonateRequest:"
- "isXPC"
- "modifiedRowCount"
- "next"
- "notifyChangeToSet:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "openStreamCompletion"
- "registerRemoteDeviceSite:peerDeviceUUID:isRelayed:hasDeltas:returningRowId:"
- "registryQueue"
- "reject"
- "rejectConnection"
- "remoteCRDTSetDonation"
- "remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:"
- "remoteUpdateFromDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:completion:"
- "remoteUpdateFromDeviceUUID:withType:mergeableDelta:peerDeviceSite:relayedDeviceSites:"
- "removeSourceItemIdentifier:"
- "removeSourceItemIdentifier:completion:"
- "requestAccessToResource:withMode:error:"
- "requestManager"
- "selectAllDeviceRecords"
- "selectProvenanceWithContentSequenceNumber:onDeviceRowId:outProvenanceRowId:"
- "selectSourceItemIdHash:outLocalInstanceRowId:outProvenanceRowId:outInstanceHash:outContentHash:outContentSequenceNumber:isDuplicate:"
- "setAttributionFunction:"
- "setDidCommit:"
- "setNext:"
- "setOpenStreamCompletion:"
- "setQueue:"
- "setRequest:"
- "setRequestManager:"
- "setUpdater:"
- "setWriterForSet:accessAssertion:"
- "setXpcConnection:"
- "sharedInstance"
- "sharedItemProvenanceUpdatedCount"
- "stringByAppendingString:"
- "submitDatabaseTransactionUsingBlock:"
- "submitRequest:"
- "succeeded"
- "suspend"
- "terminateConnection:"
- "terminateWithType:"
- "timeout"
- "tombstoneContentSequenceNumbersInRange:forDeviceRowId:"
- "unmodifiedItemCount"
- "updateContent:andMetaContent:localInstanceRowId:priorProvenanceRowId:contentHash:instanceHash:isDuplicate:"
- "updateMetaContent:localInstanceRowId:provenanceRowId:priorInstanceHash:instanceHash:contentHash:contentSequenceNumber:isDuplicate:"
- "updateRemoteDeviceUUID:options:mergeableDelta:peerDeviceSite:relayedDeviceSites:"
- "updateType"
- "updater"
- "updaterFactory"
- "updaterForDonateRequest:toDatabase:"
- "updaterForSet:withRequest:"
- "updaterForSet:withRequest:setWriter:changeNotifier:timeout:"
- "v24@0:8@\"NSObject<CCDonateService>\"16"
- "v24@0:8^?16"
- "v24@0:8q16"
- "v24@?0@\"CCProvenanceRecord\"8^B16"
- "v24@?0@\"CCRemoteCRDTSetDonation\"8@\"NSError\"16"
- "v32@0:8@\"NSString\"16@?<v@?S>24"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?S>32"
- "v60@0:8@\"NSUUID\"16S24@\"CKMergeableDelta\"28@\"CCDeviceSite\"36@\"NSArray\"44@?<v@?S>52"
- "waitForCommit:"
- "writeOnlyInstanceForSet:donateServiceProvider:"
- "xpcConnection"

```
