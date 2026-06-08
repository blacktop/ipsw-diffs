## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer`

```diff

-252.5.1.0.0
-  __TEXT.__text: 0x1eb70
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x1be0
+274.0.0.0.0
+  __TEXT.__text: 0x1fb88
+  __TEXT.__objc_methlist: 0x1d90
   __TEXT.__const: 0xd0
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__cstring: 0x1a07
-  __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__oslogstring: 0xa5e
-  __TEXT.__unwind_info: 0x7b8
-  __TEXT.__objc_classname: 0x87f
-  __TEXT.__objc_methname: 0x5368
-  __TEXT.__objc_methtype: 0x18e2
-  __TEXT.__objc_stubs: 0x3c00
-  __DATA_CONST.__got: 0x420
-  __DATA_CONST.__const: 0xd58
-  __DATA_CONST.__objc_classlist: 0x118
-  __DATA_CONST.__objc_protolist: 0xf0
+  __TEXT.__cstring: 0x1c7a
+  __TEXT.__gcc_except_tab: 0x328
+  __TEXT.__oslogstring: 0xaee
+  __TEXT.__unwind_info: 0x868
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xdd8
+  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1280
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x390
+  __DATA_CONST.__objc_selrefs: 0x1358
+  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__got: 0x410
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0x3e50
-  __DATA.__objc_ivar: 0x274
-  __DATA.__data: 0xb40
-  __DATA.__bss: 0x10
+  __AUTH_CONST.__cfstring: 0x1760
+  __AUTH_CONST.__objc_const: 0x4260
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x2a4
+  __DATA.__data: 0xba0
   __DATA_DIRTY.__objc_ivar: 0x8
-  __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__objc_data: 0xb90
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0BC32EDF-35D2-3B54-8C63-38CB7EE1D0A0
-  Functions: 702
-  Symbols:   2792
-  CStrings:  1517
+  UUID: 97FDBECB-C443-3E4C-89D5-85C6835320D7
+  Functions: 740
+  Symbols:   2930
+  CStrings:  472
 
Symbols:
+ +[STAttributionBundleRecord recordType]
+ -[STAttributedEntityResolver attributionBundleRecords]
+ -[STAttributedEntityResolver setAttributionBundleRecords:]
+ -[STAttributedEntityResolverProvider attributionBundleRecords]
+ -[STAttributedEntityResolverProvider initWithIdentityResolver:hasExternalIdentityResolver:]
+ -[STAttributedEntityResolverProvider setAttributionBundleRecords:]
+ -[STAttributionBundleManager .cxx_destruct]
+ -[STAttributionBundleManager _updateBundleRecords]
+ -[STAttributionBundleManager attributionBundleRecords]
+ -[STAttributionBundleManager bundleManager]
+ -[STAttributionBundleManager init]
+ -[STAttributionBundleManager observeAttributionBundleRecordChangesWithBlock:]
+ -[STAttributionBundleManager observerBlock]
+ -[STAttributionBundleManager recordBundlesChangedForBundleManager:]
+ -[STAttributionBundleManager setAttributionBundleRecords:]
+ -[STAttributionBundleManager setObserverBlock:]
+ -[STAttributionBundleRecord initWithBundleInfoDictionary:bundleRecordIdentifier:bundleURL:]
+ -[STDataAccessStatusDomainDisplayNameTransformer initWithEntityResolver:dynamicAttributionEntityResolver:]
+ -[STDataAccessStatusDomainDisplayNameTransformerProvider initWithEntityResolverProvider:dynamicAttributionEntityResolverProvider:]
+ -[STExecutableIdentityResolver attributionBundleRecords]
+ -[STExecutableIdentityResolver setAttributionBundleRecords:]
+ -[STMutableTelephonySubscriptionInfo setNumberSharingState:]
+ -[STMutableTelephonySubscriptionInfo setSlicingSuffix:]
+ -[STReferenceCountedCache purgeCachedObjectsPassingTest:]
+ -[STTelephonyStateProvider _backgroundQueryQueue_handleNetworkReselectionNeeded:forCTContext:]
+ -[STTelephonyStateProvider _backgroundQueryQueue_updateNetworkCountryCode:inContext:withCTContext:]
+ -[STTelephonyStateProvider _internalQueue_cancelFakeCellularRegistrationForContext:]
+ -[STTelephonyStateProvider _internalQueue_cancelFakeRegistrationForContext:]
+ -[STTelephonyStateProvider _internalQueue_cancelFakeServiceAndRegistrationForContext:]
+ -[STTelephonyStateProvider _internalQueue_cancelFakeServiceForContext:]
+ -[STTelephonyStateProvider _internalQueue_handleCellChangedForContext:withCTContext:]
+ -[STTelephonyStateProvider _internalQueue_handleTelephonyDaemonRestart]
+ -[STTelephonyStateProvider _internalQueue_hasCTContextForSlot:]
+ -[STTelephonyStateProvider _internalQueue_logSubscriptionEvent:]
+ -[STTelephonyStateProvider _internalQueue_logSubscriptionEvent:forCTContext:]
+ -[STTelephonyStateProvider _internalQueue_logSubscriptionEvent:forContext:]
+ -[STTelephonyStateProvider _internalQueue_purgeSlot1SubscriptionState]
+ -[STTelephonyStateProvider _internalQueue_purgeSlot2SubscriptionState]
+ -[STTelephonyStateProvider _internalQueue_queryCallForwardingStateForCTContext:]
+ -[STTelephonyStateProvider _internalQueue_reallySetOperatorName:inSubscriptionContext:]
+ -[STTelephonyStateProvider _internalQueue_serverConnectionDidError:]
+ -[STTelephonyStateProvider _internalQueue_serverConnection]
+ -[STTelephonyStateProvider _internalQueue_setCachedRadioModuleDead:]
+ -[STTelephonyStateProvider _internalQueue_setCallForwardingIndicator:inSubscriptionContext:]
+ -[STTelephonyStateProvider _internalQueue_setCellRegistrationStatus:inSubscriptionContext:]
+ -[STTelephonyStateProvider _internalQueue_setOperatorName:allowingFakeService:inSubscriptionContext:]
+ -[STTelephonyStateProvider _internalQueue_setRegistrationStatus:inSubscriptionContext:]
+ -[STTelephonyStateProvider _internalQueue_setSuppressesCellIndicators:]
+ -[STTelephonyStateProvider _internalQueue_stopFakeServiceForContext:]
+ -[STTelephonyStateProvider _internalQueue_stopFakingServiceAndRegistrationForContext:]
+ -[STTelephonyStateProvider _internalQueue_subscriptionContextForCTContext:]
+ -[STTelephonyStateProvider _internalQueue_subscriptionSlotForContext:]
+ -[STTelephonyStateProvider _internalQueue_updateCallForwardingIndicatorForContext:]
+ -[STTelephonyStateProvider _internalQueue_updateDataConnectedSubscriptionContextForCTContext:]
+ -[STTelephonyStateProvider _internalQueue_updateDataConnectionTypeForContext:]
+ -[STTelephonyStateProvider _internalQueue_updateDataConnectionType]
+ -[STTelephonyStateProvider _internalQueue_updateDualSIMCapabilitySendingNotification:]
+ -[STTelephonyStateProvider _internalQueue_updateLastKnownNetworkCountryCodeInContext:withCTContext:]
+ -[STTelephonyStateProvider _internalQueue_updateRegistrationNowInSubscriptionContext:]
+ -[STTelephonyStateProvider _internalQueue_updateState]
+ -[STTelephonyStateProvider quickSwitchDataSuppressionDidChange:forContext:]
+ -[STTelephonyStateProvider slicingStatusNameChanged:name:]
+ -[STTelephonySubscriptionInfo numberSharingState]
+ -[STTelephonySubscriptionInfo slicingSuffix]
+ GCC_except_table129
+ GCC_except_table139
+ GCC_except_table174
+ GCC_except_table3
+ OBJC_IVAR_$_STTelephonySubscriptionInfo._numberSharingState
+ OBJC_IVAR_$_STTelephonySubscriptionInfo._slicingSuffix
+ _BSEqualArrays
+ _BSEqualStrings
+ _OBJC_CLASS_$_STAttributionBundleManager
+ _OBJC_CLASS_$_STAttributionBundleRecord
+ _OBJC_IVAR_$_STAttributedEntityResolver._attributionBundleRecords
+ _OBJC_IVAR_$_STAttributedEntityResolverProvider._attributionBundleRecords
+ _OBJC_IVAR_$_STAttributedEntityResolverProvider._hasExternalIdentityResolver
+ _OBJC_IVAR_$_STAttributionBundleManager._attributionBundleRecords
+ _OBJC_IVAR_$_STAttributionBundleManager._bundleManager
+ _OBJC_IVAR_$_STAttributionBundleManager._observerBlock
+ _OBJC_IVAR_$_STDataAccessStatusDomainDisplayNameTransformer._dynamicAttributionEntityResolver
+ _OBJC_IVAR_$_STDataAccessStatusDomainDisplayNameTransformerProvider._dynamicAttributionEntityResolverProvider
+ _OBJC_IVAR_$_STExecutableIdentityResolver._attributionBundleRecordsByIdentifier
+ _OBJC_IVAR_$_STTelephonyStateProvider.__internalQueue_airplaneModeEnabled
+ _OBJC_IVAR_$_STTelephonyStateProvider._suppressesCellDataIndicator
+ _OBJC_METACLASS_$_STAttributionBundleManager
+ _OBJC_METACLASS_$_STAttributionBundleRecord
+ _STExecutableIdentityAuditTokenEqualToAuditToken
+ _STTelephonyNumberSharingStateDebugName
+ __OBJC_$_CLASS_METHODS_STAttributionBundleRecord
+ __OBJC_$_INSTANCE_METHODS_STAttributionBundleManager
+ __OBJC_$_INSTANCE_METHODS_STAttributionBundleRecord
+ __OBJC_$_INSTANCE_VARIABLES_STAttributionBundleManager
+ __OBJC_$_PROP_LIST_STAttributionBundleManager
+ __OBJC_$_PROP_LIST_STExecutableIdentityResolver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientQuickSwitchStateDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientQuickSwitchStateDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientQuickSwitchStateDelegate
+ __OBJC_CLASS_PROTOCOLS_$_STAttributionBundleManager
+ __OBJC_CLASS_RO_$_STAttributionBundleManager
+ __OBJC_CLASS_RO_$_STAttributionBundleRecord
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientQuickSwitchStateDelegate
+ __OBJC_METACLASS_RO_$_STAttributionBundleManager
+ __OBJC_METACLASS_RO_$_STAttributionBundleRecord
+ __OBJC_PROTOCOL_$_CoreTelephonyClientQuickSwitchStateDelegate
+ ___100-[STLocalStatusServer _internalQueue_replaceVolatileDataChangeRecord:forPublisherClient:completion:]_block_invoke.145
+ ___100-[STTelephonyStateProvider _internalQueue_updateLastKnownNetworkCountryCodeInContext:withCTContext:]_block_invoke
+ ___100-[STTelephonyStateProvider _internalQueue_updateLastKnownNetworkCountryCodeInContext:withCTContext:]_block_invoke.47
+ ___32-[STTelephonyStateProvider init]_block_invoke_5
+ ___53-[STAttributedEntityResolver setDynamicAttributions:]_block_invoke
+ ___54-[STTelephonyStateProvider _internalQueue_updateState]_block_invoke
+ ___57-[STReferenceCountedCache purgeCachedObjectsPassingTest:]_block_invoke
+ ___58-[STAttributedEntityResolver setAttributionBundleRecords:]_block_invoke
+ ___58-[STTelephonyStateProvider slicingStatusNameChanged:name:]_block_invoke
+ ___59-[STTelephonyStateProvider _internalQueue_serverConnection]_block_invoke
+ ___60-[STExecutableIdentityResolver setAttributionBundleRecords:]_block_invoke
+ ___65-[STTelephonyStateProvider _internalQueue_airplaneModeDidChange:]_block_invoke
+ ___65-[STTelephonyStateProvider _internalQueue_airplaneModeDidChange:]_block_invoke_2
+ ___66-[STAttributedEntityResolverProvider setAttributionBundleRecords:]_block_invoke
+ ___67-[STAttributionBundleManager recordBundlesChangedForBundleManager:]_block_invoke
+ ___68-[STTelephonyStateProvider _internalQueue_serverConnectionDidError:]_block_invoke
+ ___68-[STTelephonyStateProvider _internalQueue_serverConnectionDidError:]_block_invoke_2
+ ___73-[STStatusDomainXPCClientHandle observeData:forDomain:withChangeContext:]_block_invoke_5
+ ___75-[STTelephonyStateProvider quickSwitchDataSuppressionDidChange:forContext:]_block_invoke
+ ___78-[STTelephonyStateProvider _internalQueue_querySubscriptionStateForCTContext:]_block_invoke
+ ___78-[STTelephonyStateProvider _internalQueue_querySubscriptionStateForCTContext:]_block_invoke_2
+ ___78-[STTelephonyStateProvider _internalQueue_querySubscriptionStateForCTContext:]_block_invoke_3
+ ___78-[STTelephonyStateProvider _internalQueue_querySubscriptionStateForCTContext:]_block_invoke_4
+ ___78-[STTelephonyStateProvider _internalQueue_querySubscriptionStateForCTContext:]_block_invoke_5
+ ___78-[STTelephonyStateProvider _internalQueue_querySubscriptionStateForCTContext:]_block_invoke_6
+ ___78-[STTelephonyStateProvider _internalQueue_querySubscriptionStateForCTContext:]_block_invoke_7
+ ___78-[STTelephonyStateProvider _internalQueue_querySubscriptionStateForCTContext:]_block_invoke_8
+ ___79-[STTelephonyStateProvider _internalQueue_queryRegistrationStatusForCTContext:]_block_invoke
+ ___80-[STTelephonyStateProvider _internalQueue_queryCallForwardingStateForCTContext:]_block_invoke
+ ___80-[STTelephonyStateProvider _internalQueue_queryCallForwardingStateForCTContext:]_block_invoke_2
+ ___81-[STTelephonyStateProvider _internalQueue_startFakeServiceIfNecessaryForContext:]_block_invoke
+ ___82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.151
+ ___83-[STTelephonyStateProvider _internalQueue_registerForServerConnectionNotifications]_block_invoke
+ ___83-[STTelephonyStateProvider _internalQueue_registerForServerConnectionNotifications]_block_invoke_2
+ ___83-[STTelephonyStateProvider _internalQueue_registerForServerConnectionNotifications]_block_invoke_3
+ ___83-[STTelephonyStateProvider _internalQueue_registerForServerConnectionNotifications]_block_invoke_4
+ ___83-[STTelephonyStateProvider _internalQueue_registerForServerConnectionNotifications]_block_invoke_5
+ ___83-[STTelephonyStateProvider _internalQueue_registerForServerConnectionNotifications]_block_invoke_6
+ ___83-[STTelephonyStateProvider _internalQueue_registerForServerConnectionNotifications]_block_invoke_7
+ ___83-[STTelephonyStateProvider _internalQueue_registerForServerConnectionNotifications]_block_invoke_8
+ ___83-[STTelephonyStateProvider _internalQueue_updateCallForwardingIndicatorForContext:]_block_invoke
+ ___83-[STTelephonyStateProvider _internalQueue_updateCallForwardingIndicatorForContext:]_block_invoke_2
+ ___83-[STTelephonyStateProvider _internalQueue_updateCallForwardingIndicatorForContext:]_block_invoke_3
+ ___86-[STTelephonyStateProvider _internalQueue_startFakeRegistrationIfNecessaryForContext:]_block_invoke
+ ___86-[STTelephonyStateProvider _internalQueue_updateDualSIMCapabilitySendingNotification:]_block_invoke
+ ___86-[STTelephonyStateProvider _internalQueue_updateDualSIMCapabilitySendingNotification:]_block_invoke_2
+ ___92-[STLocalStatusServer _internalQueue_replaceDataChangeRecord:forPublisherClient:completion:]_block_invoke.141
+ ___94-[STTelephonyStateProvider _backgroundQueryQueue_handleNetworkReselectionNeeded:forCTContext:]_block_invoke
+ ___94-[STTelephonyStateProvider _internalQueue_startFakeCellularRegistrationIfNecessaryForContext:]_block_invoke
+ ___99-[STTelephonyStateProvider _backgroundQueryQueue_updateNetworkCountryCode:inContext:withCTContext:]_block_invoke
+ ___block_descriptor_40_e8_32s_e55_B24?0"STExecutableIdentity"8"STExecutableIdentity"16ls32l8
+ ___block_descriptor_40_e8_32s_e69_B24?0"STAttributedEntity"8"<STAttributedEntityResolutionResult>"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e15_v32?0816^B24ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e33_16?0"STDataAccessAttribution"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e52_v24?0"CTQuickSwitchNumberSharingInfo"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e30_v16?0"<STStatusDomainData>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e34_v16?0"<STStatusDomainDataDiff>"8ls32l8s40l8s48l8
+ ___block_literal_global.144
+ ___block_literal_global.147
+ _dispatch_block_create
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_updateBundleRecords
+ _objc_msgSend$attributionBundleRecords
+ _objc_msgSend$copyReplacingActivityAttribution:
+ _objc_msgSend$copySlicingStatus:completion:
+ _objc_msgSend$distinctActiveEntity
+ _objc_msgSend$getNumberSharingInfoWithCompletion:completion:
+ _objc_msgSend$graphicIconType
+ _objc_msgSend$initWithEntityResolver:dynamicAttributionEntityResolver:
+ _objc_msgSend$initWithEntityResolverProvider:dynamicAttributionEntityResolverProvider:
+ _objc_msgSend$initWithExecutableIdentity:website:systemService:localizedDisplayName:localizedExecutableDisplayName:graphicIconType:
+ _objc_msgSend$isQuickSwitchStatePassiveDataSuppressed
+ _objc_msgSend$numberSharingState
+ _objc_msgSend$observeData:forDomain:withChangeContext:reply:
+ _objc_msgSend$observeDiff:forDomain:withChangeContext:reply:
+ _objc_msgSend$observerBlock
+ _objc_msgSend$purgeCachedObjectsPassingTest:
+ _objc_msgSend$quickSwitchDataSuppressionDidChange:forContext:
+ _objc_msgSend$recordBundleURL
+ _objc_msgSend$recordIdentifier
+ _objc_msgSend$setAttributionBundleRecords:
+ _objc_msgSend$setNumberSharingState:
+ _objc_msgSend$setObserverBlock:
+ _objc_msgSend$setServiceSuffixDescription:
+ _objc_msgSend$setSlicingSuffix:
+ _objc_msgSend$slicingStatusNameChanged:name:
+ _objc_msgSend$slicingSuffix
+ _objc_msgSend$stateChanged:
+ _objc_msgSend$substringFromIndex:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
- -[STDataAccessStatusDomainDisplayNameTransformer initWithEntityResolver:]
- -[STDataAccessStatusDomainDisplayNameTransformerProvider initWithEntityResolverProvider:]
- -[STTelephonyStateProvider _cancelFakeCellularRegistrationForContext:]
- -[STTelephonyStateProvider _cancelFakeRegistrationForContext:]
- -[STTelephonyStateProvider _cancelFakeServiceAndRegistrationForContext:]
- -[STTelephonyStateProvider _cancelFakeServiceForContext:]
- -[STTelephonyStateProvider _handleNetworkReselectionNeeded:forCTContext:]
- -[STTelephonyStateProvider _hasCTContextForSlot:]
- -[STTelephonyStateProvider _logSubscriptionEvent:]
- -[STTelephonyStateProvider _logSubscriptionEvent:forCTContext:]
- -[STTelephonyStateProvider _logSubscriptionEvent:forContext:]
- -[STTelephonyStateProvider _purgeSlot1SubscriptionState]
- -[STTelephonyStateProvider _purgeSlot2SubscriptionState]
- -[STTelephonyStateProvider _queryCallForwardingStateForCTContext:]
- -[STTelephonyStateProvider _reallySetOperatorName:inSubscriptionContext:]
- -[STTelephonyStateProvider _serverConnectionDidError:]
- -[STTelephonyStateProvider _serverConnection]
- -[STTelephonyStateProvider _setCallForwardingIndicator:inSubscriptionContext:]
- -[STTelephonyStateProvider _setCellRegistrationStatus:inSubscriptionContext:]
- -[STTelephonyStateProvider _setOperatorName:inSubscriptionContext:]
- -[STTelephonyStateProvider _setRegistrationStatus:inSubscriptionContext:]
- -[STTelephonyStateProvider _setSIMStatus:inSubscriptionContext:]
- -[STTelephonyStateProvider _setSuppressesCellIndicators:]
- -[STTelephonyStateProvider _stopFakeServiceForContext:]
- -[STTelephonyStateProvider _stopFakingServiceAndRegistrationForContext:]
- -[STTelephonyStateProvider _subscriptionContextForCTContext:]
- -[STTelephonyStateProvider _subscriptionSlotForContext:]
- -[STTelephonyStateProvider _updateCallForwardingIndicatorForContext:]
- -[STTelephonyStateProvider _updateDataConnectedSubscriptionContextForCTContext:]
- -[STTelephonyStateProvider _updateDataConnectionTypeForContext:]
- -[STTelephonyStateProvider _updateDataConnectionType]
- -[STTelephonyStateProvider _updateDualSIMCapabilitySendingNotification:]
- -[STTelephonyStateProvider _updateLastKnownNetworkCountryCodeInContext:withCTContext:]
- -[STTelephonyStateProvider _updateNetworkCountryCode:inContext:withCTContext:]
- -[STTelephonyStateProvider _updateRegistrationNowInSubscriptionContext:]
- -[STTelephonyStateProvider _updateState]
- -[STTelephonyStateProvider setCachedRadioModuleDead:]
- -[STTelephonyStateProvider setStewieState:]
- GCC_except_table127
- GCC_except_table135
- GCC_except_table167
- _OBJC_CLASS_$_STMediaStatusDomainCameraCaptureAttribution
- _OBJC_CLASS_$_STMediaStatusDomainMicrophoneRecordingAttribution
- _OBJC_CLASS_$_STMediaStatusDomainScreenCaptureAttribution
- _OBJC_IVAR_$_STTelephonyStateProvider._airplaneModeEnabled
- ___100-[STLocalStatusServer _internalQueue_replaceVolatileDataChangeRecord:forPublisherClient:completion:]_block_invoke.146
- ___40-[STTelephonyStateProvider _updateState]_block_invoke
- ___45-[STTelephonyStateProvider _serverConnection]_block_invoke
- ___51-[STTelephonyStateProvider _airplaneModeDidChange:]_block_invoke
- ___51-[STTelephonyStateProvider _airplaneModeDidChange:]_block_invoke_2
- ___54-[STTelephonyStateProvider _serverConnectionDidError:]_block_invoke
- ___54-[STTelephonyStateProvider _serverConnectionDidError:]_block_invoke_2
- ___64-[STTelephonyStateProvider _querySubscriptionStateForCTContext:]_block_invoke
- ___64-[STTelephonyStateProvider _querySubscriptionStateForCTContext:]_block_invoke_2
- ___64-[STTelephonyStateProvider _querySubscriptionStateForCTContext:]_block_invoke_3
- ___64-[STTelephonyStateProvider _querySubscriptionStateForCTContext:]_block_invoke_4
- ___64-[STTelephonyStateProvider _querySubscriptionStateForCTContext:]_block_invoke_5
- ___64-[STTelephonyStateProvider _querySubscriptionStateForCTContext:]_block_invoke_6
- ___65-[STTelephonyStateProvider _queryRegistrationStatusForCTContext:]_block_invoke
- ___66-[STTelephonyStateProvider _queryCallForwardingStateForCTContext:]_block_invoke
- ___66-[STTelephonyStateProvider _queryCallForwardingStateForCTContext:]_block_invoke_2
- ___67-[STTelephonyStateProvider _startFakeServiceIfNecessaryForContext:]_block_invoke
- ___69-[STTelephonyStateProvider _registerForServerConnectionNotifications]_block_invoke
- ___69-[STTelephonyStateProvider _registerForServerConnectionNotifications]_block_invoke_2
- ___69-[STTelephonyStateProvider _registerForServerConnectionNotifications]_block_invoke_3
- ___69-[STTelephonyStateProvider _registerForServerConnectionNotifications]_block_invoke_4
- ___69-[STTelephonyStateProvider _registerForServerConnectionNotifications]_block_invoke_5
- ___69-[STTelephonyStateProvider _registerForServerConnectionNotifications]_block_invoke_6
- ___69-[STTelephonyStateProvider _registerForServerConnectionNotifications]_block_invoke_7
- ___69-[STTelephonyStateProvider _registerForServerConnectionNotifications]_block_invoke_8
- ___69-[STTelephonyStateProvider _updateCallForwardingIndicatorForContext:]_block_invoke
- ___69-[STTelephonyStateProvider _updateCallForwardingIndicatorForContext:]_block_invoke_2
- ___69-[STTelephonyStateProvider _updateCallForwardingIndicatorForContext:]_block_invoke_3
- ___72-[STTelephonyStateProvider _startFakeRegistrationIfNecessaryForContext:]_block_invoke
- ___72-[STTelephonyStateProvider _updateDualSIMCapabilitySendingNotification:]_block_invoke
- ___72-[STTelephonyStateProvider _updateDualSIMCapabilitySendingNotification:]_block_invoke_2
- ___73-[STTelephonyStateProvider _handleNetworkReselectionNeeded:forCTContext:]_block_invoke
- ___78-[STTelephonyStateProvider _updateNetworkCountryCode:inContext:withCTContext:]_block_invoke
- ___80-[STDataAccessStatusDomainDisplayNameTransformer transformedDataForData:domain:]_block_invoke_2
- ___80-[STTelephonyStateProvider _startFakeCellularRegistrationIfNecessaryForContext:]_block_invoke
- ___82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.152
- ___86-[STTelephonyStateProvider _updateLastKnownNetworkCountryCodeInContext:withCTContext:]_block_invoke
- ___86-[STTelephonyStateProvider _updateLastKnownNetworkCountryCodeInContext:withCTContext:]_block_invoke.47
- ___92-[STLocalStatusServer _internalQueue_replaceDataChangeRecord:forPublisherClient:completion:]_block_invoke.142
- ___block_descriptor_32_e33_16?0"STDataAccessAttribution"8l
- ___block_descriptor_40_e8_32s_e33_16?0"STDataAccessAttribution"8ls32l8
- ___block_descriptor_56_e8_32s40s_e30_v16?0"<STStatusDomainData>"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e34_v16?0"<STStatusDomainDataDiff>"8ls32l8s40l8
- ___block_literal_global.145
- ___block_literal_global.148
- _objc_msgSend$cameraDescriptor
- _objc_msgSend$initWithActivityAttribution:
- _objc_msgSend$initWithActivityAttribution:maximumHistoryAccessed:
- _objc_msgSend$initWithAttributedEntity:
- _objc_msgSend$initWithCameraDescriptor:activityAttribution:
- _objc_msgSend$initWithExecutableIdentity:
- _objc_msgSend$initWithExecutableIdentity:website:systemService:localizedDisplayName:localizedExecutableDisplayName:
- _objc_msgSend$initWithIdentityResolver:
- _objc_msgSend$observeDiff:forDomain:withChangeContext:
CStrings:
+ "-[STTelephonyStateProvider _backgroundQueryQueue_handleNetworkReselectionNeeded:forCTContext:]_block_invoke"
+ "-[STTelephonyStateProvider _internalQueue_queryCallForwardingStateForCTContext:]_block_invoke_2"
+ "-[STTelephonyStateProvider quickSwitchDataSuppressionDidChange:forContext:]_block_invoke"
+ "-[STTelephonyStateProvider slicingStatusNameChanged:name:]_block_invoke"
+ ":"
+ "Attribution"
+ "B24@?0@\"STAttributedEntity\"8@\"<STAttributedEntityResolutionResult>\"16"
+ "B24@?0@\"STExecutableIdentity\"8@\"STExecutableIdentity\"16"
+ "Bundle %{private}@ is of unexpected type, expected 'Attribution'"
+ "Bundle manager reports attribution bundle identifiers changed: %{public}@"
+ "Entity resolver: %{public}@ -- updating attribution bundle records from: %{public}@ to: %{public}@"
+ "_STAttributionGraphicIconType"
+ "got new slicing name: %@"
+ "none"
+ "numberSharingState"
+ "passive-data-suppressed"
+ "slicingSuffix"
+ "slicingSuffix changed from '%@' to '%@'"
+ "updated number sharing state"
+ "v24@?0@\"CTQuickSwitchNumberSharingInfo\"8@\"NSError\"16"
+ "v32@?0@8@16^B24"
- "#16@0:8"
- "-[STTelephonyStateProvider _handleNetworkReselectionNeeded:forCTContext:]_block_invoke"
- "-[STTelephonyStateProvider _queryCallForwardingStateForCTContext:]_block_invoke_2"
- ".cxx_destruct"
- "@\"<BSDefaultObserver>\""
- "@\"<STAttributedEntityBatchResolving>\""
- "@\"<STAttributedEntityResolutionResult>\"24@0:8@\"STAttributedEntity\"16"
- "@\"<STAttributedEntityResolverProviding>\""
- "@\"<STAttributedEntityResolving>\""
- "@\"<STExecutableIdentityBatchResolving>\""
- "@\"<STExecutableIdentityResolving>\""
- "@\"<STLocalStatusServerDelegate>\""
- "@\"<STStatusDomainClientHandle>\""
- "@\"<STStatusDomainData>\"32@0:8@\"<STStatusDomainData>\"16Q24"
- "@\"<STStatusDomainData>\"32@0:8Q16@\"<STStatusDomainClientHandle>\"24"
- "@\"<STStatusDomainData><STStatusDomainDataDifferencing>\"24@0:8Q16"
- "@\"<STStatusDomainDataTransforming>\"24@0:8@\"<STStatusDomainClientHandle>\"16"
- "@\"<STStatusDomainPublisherServerHandle>\""
- "@\"<STStatusDomainServerHandle>\""
- "@\"<STStatusServerDelegate>\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"BSMutableIntegerMap\""
- "@\"CTStewieState\""
- "@\"CTStewieStateMonitor\""
- "@\"CoreTelephonyClient\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"RadiosPreferences\""
- "@\"STAttributedEntityResolver\"24@0:8@\"NSArray\"16"
- "@\"STBackgroundActivityManager\""
- "@\"STBundleManager\""
- "@\"STDataAccessStatusDomainData\""
- "@\"STDataAccessStatusDomainDataProvider\""
- "@\"STDataAccessStatusDomainPublisher\""
- "@\"STExecutableIdentity\"24@0:8@\"STExecutableIdentity\"16"
- "@\"STExecutableIdentityResolver\""
- "@\"STLocalStatusServer\""
- "@\"STLocationStatusDomainData\""
- "@\"STMediaStatusDomainData\""
- "@\"STMutableTelephonyCarrierBundleInfo\""
- "@\"STMutableTelephonyMobileEquipmentInfo\""
- "@\"STMutableTelephonySubscriptionInfo\""
- "@\"STReferenceCountedCache\""
- "@\"STStatusDomainDataChangeLog\""
- "@\"STStatusDomainPublisherXPCClientListener\""
- "@\"STStatusDomainXPCClientListener\""
- "@\"STStatusItemsManager\""
- "@\"STSystemStatusDefaults\""
- "@\"STTelephonyStateProvider\""
- "@\"STTelephonyStatusDomainPublisher\""
- "@\"STTelephonySubscriptionContext\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8Q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8{?=[8I]}16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "BSDebugDescriptionProviding"
- "BSDescriptionProviding"
- "BSInvalidatable"
- "CTStewieStateMonitorDelegate"
- "CoreTelephonyClientCarrierBundleDelegate"
- "CoreTelephonyClientDataDelegate"
- "CoreTelephonyClientDelegate"
- "CoreTelephonyClientRegistrationDelegate"
- "CoreTelephonyClientSubscriberDelegate"
- "CoreTelephonyClientSuppServicesDelegate"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q"
- "Q16@0:8"
- "RadiosPreferencesDelegate"
- "STAttributedEntityBatchResolving"
- "STAttributedEntityResolutionSession"
- "STAttributedEntityResolver"
- "STAttributedEntityResolverProvider"
- "STAttributedEntityResolverProviding"
- "STAttributedEntityResolving"
- "STBackgroundActivitiesStatusDomainVisualDescriptorTransformer"
- "STBundleManagerObserver"
- "STDataAccessStatusDomainDataProvider"
- "STDataAccessStatusDomainDataProviderTransformer"
- "STDataAccessStatusDomainDisplayNameTransformer"
- "STDataAccessStatusDomainDisplayNameTransformerProvider"
- "STExecutableIdentityBatchResolving"
- "STExecutableIdentityResolutionSession"
- "STExecutableIdentityResolver"
- "STExecutableIdentityResolving"
- "STLocalStatusServer"
- "STLocationStatusDomainDisplayNameTransformer"
- "STLocationStatusDomainDisplayNameTransformerProvider"
- "STMediaStatusDomainDisplayNameTransformer"
- "STMediaStatusDomainDisplayNameTransformerProvider"
- "STMutableTelephonyCarrierBundleInfo"
- "STMutableTelephonyMobileEquipmentInfo"
- "STMutableTelephonySubscriptionInfo"
- "STReferenceCountedCache"
- "STStatusDomainClientDataTransformerProviding"
- "STStatusDomainClientHandle"
- "STStatusDomainClientHandleWrapper"
- "STStatusDomainDataTransforming"
- "STStatusDomainPublisherClientHandle"
- "STStatusDomainPublisherServerHandle"
- "STStatusDomainPublisherXPCClientHandle"
- "STStatusDomainPublisherXPCClientListener"
- "STStatusDomainPublisherXPCServer"
- "STStatusDomainServerHandle"
- "STStatusDomainXPCClientHandle"
- "STStatusDomainXPCClientListener"
- "STStatusDomainXPCServer"
- "STStatusItemsBundleRecord"
- "STStatusItemsManager"
- "STStatusItemsStatusDomainVisualDescriptorTransformer"
- "STStatusServer"
- "STTelephonyCarrierBundleInfo"
- "STTelephonyMobileEquipmentInfo"
- "STTelephonyStateObserver"
- "STTelephonyStateProvider"
- "STTelephonyStateProvider - queried for _suppressesCellDataIndicator with new state=%{public}@"
- "STTelephonyStatusDomainDataProvider"
- "STTelephonySubscriptionContext"
- "STTelephonySubscriptionInfo"
- "T#,R"
- "T@\"<STLocalStatusServerDelegate>\",W,N,V_delegate"
- "T@\"<STStatusDomainClientHandle>\",R,W,N,V_wrappedClientHandle"
- "T@\"<STStatusServerDelegate>\",W,N,V_delegate"
- "T@\"BSIntegerSet\",R,N"
- "T@\"NSArray\",C,D,N"
- "T@\"NSArray\",C,N,V_dynamicAttributions"
- "T@\"NSArray\",C,N,V_statusBarImages"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_disabledApplicationIDs"
- "T@\"NSArray\",R,C,N,V_preferredLocalizations"
- "T@\"NSSet\",R,C,N,V_statusItemIdentifiers"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,D,N"
- "T@\"NSString\",C,N,V_cachedCTOperatorName"
- "T@\"NSString\",C,N,V_cachedCTRegistrationCellularStatus"
- "T@\"NSString\",C,N,V_cachedCTRegistrationDisplayStatus"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_CSN"
- "T@\"NSString\",R,C,N,V_ICCID"
- "T@\"NSString\",R,C,N,V_IMEI"
- "T@\"NSString\",R,C,N,V_MEID"
- "T@\"NSString\",R,C,N,V_SIMLabel"
- "T@\"NSString\",R,C,N,V_SIMStatus"
- "T@\"NSString\",R,C,N,V_bootstrapICCID"
- "T@\"NSString\",R,C,N,V_carrierName"
- "T@\"NSString\",R,C,N,V_customerServicePhoneNumber"
- "T@\"NSString\",R,C,N,V_homeCountryCode"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_lastKnownNetworkCountryCode"
- "T@\"NSString\",R,C,N,V_operatorName"
- "T@\"NSString\",R,C,N,V_shortSIMLabel"
- "T@\"STDataAccessStatusDomainData\",R,C,N"
- "T@\"STLocalStatusServer\",R,N,V_server"
- "T@\"STLocationStatusDomainData\",R,C,N"
- "T@\"STMediaStatusDomainData\",R,C,N"
- "T@\"STMutableTelephonyCarrierBundleInfo\",&,N,V_carrierBundleInfo"
- "T@\"STMutableTelephonyMobileEquipmentInfo\",&,N,V_mobileEquipmentInfo"
- "T@\"STMutableTelephonySubscriptionInfo\",&,N,V_subscriptionInfo"
- "T@?,C,N,V_dataChangedHandler"
- "TB,D,N"
- "TB,D,N,GisBootstrap"
- "TB,D,N,GisHiddenSIM"
- "TB,D,N,GisNetworkReselectionNeeded"
- "TB,D,N,GisPreferredForDataConnections"
- "TB,D,N,GisProvidingDataConnection"
- "TB,D,N,GisRegisteredWithoutCellular"
- "TB,D,N,GisReinitiatingActivationDisabled"
- "TB,N,GisPretendingToSearch,V_pretendingToSearch"
- "TB,N,V_isSatelliteSystem"
- "TB,R,N"
- "TB,R,N,GisBootstrap,V_bootstrap"
- "TB,R,N,GisCellularRadioCapabilityActive"
- "TB,R,N,GisDualSIMEnabled"
- "TB,R,N,GisFakingCellularRegistration"
- "TB,R,N,GisFakingRegistration"
- "TB,R,N,GisFakingService"
- "TB,R,N,GisHiddenSIM,V_hiddenSIM"
- "TB,R,N,GisInactiveSOSEnabled"
- "TB,R,N,GisNetworkReselectionNeeded,V_networkReselectionNeeded"
- "TB,R,N,GisOnBootstrap"
- "TB,R,N,GisPreferredForDataConnections,V_preferredForDataConnections"
- "TB,R,N,GisProvidingDataConnection,V_providingDataConnection"
- "TB,R,N,GisRadioModuleDead"
- "TB,R,N,GisRegisteredWithoutCellular,V_registeredWithoutCellular"
- "TB,R,N,GisReinitiatingActivationDisabled,V_reinitiatingActivationDisabled"
- "TB,R,N,GisUsingStewieConnection"
- "TB,R,N,GisUsingStewieConnectionOverInternet"
- "TB,R,N,GisUsingStewieForSOS"
- "TB,R,N,V_LTEConnectionShows4G"
- "TB,R,N,V_hasCellularTelephony"
- "TB,R,N,V_suppressSOSOnlyWithLimitedService"
- "TQ,D,N"
- "TQ,N,V_modemDataConnectionType"
- "TQ,R"
- "TQ,R,N,V_callForwardingIndicator"
- "TQ,R,N,V_cellularRegistrationStatus"
- "TQ,R,N,V_dataConnectionType"
- "TQ,R,N,V_maxSignalStrengthBars"
- "TQ,R,N,V_registrationStatus"
- "TQ,R,N,V_signalStrengthBars"
- "T^B,N,V_fakeCellularRegistrationCanceled"
- "T^B,N,V_fakeRegistrationCanceled"
- "T^B,N,V_fakeServiceCanceled"
- "Tq,D,N"
- "Tq,R,N,V_registrationRejectionCauseCode"
- "URL"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^B"
- "^B16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CTServerConnection=}"
- "_CSN"
- "_ICCID"
- "_IMEI"
- "_LTEConnectionShows4G"
- "_MEID"
- "_SIMLabel"
- "_SIMStatus"
- "_STInternalQueueLocalStatusServerWrapper"
- "_activeAttributionMinimumDisplayTimers"
- "_activeAttributions"
- "_airplaneModeEnabled"
- "_allowAllStatusItems"
- "_attributionsWaitingForMinimumDisplayTime"
- "_backgroundActivityManager"
- "_backgroundQueryQueue"
- "_bootstrap"
- "_bootstrapICCID"
- "_bundleManager"
- "_cache"
- "_cachedCTContexts"
- "_cachedCTOperatorName"
- "_cachedCTRegistrationCellularStatus"
- "_cachedCTRegistrationDisplayStatus"
- "_cachedDualSIMEnabled"
- "_cachedEntities"
- "_cachedIdentities"
- "_cachedNeedsUserIdentificationModule"
- "_cachedRadioModuleDead"
- "_cachedSuppressesCellDataIndicator"
- "_cachedSuppressesCellIndicators"
- "_callForwardingIndicator"
- "_carrierBundleInfo"
- "_carrierName"
- "_cellularRegistrationStatus"
- "_changeLogKeysByPublisherClient"
- "_clientDataTransformerProvidersByDomain"
- "_clientHandleWrappersByDomain"
- "_clientQueue"
- "_clientXPCConnection"
- "_clientsByDomain"
- "_containsCellularRadio"
- "_coreTelephonyClient"
- "_currentData"
- "_customerServicePhoneNumber"
- "_dataAccessPublisher"
- "_dataByDomain"
- "_dataChangeLog"
- "_dataChangedHandler"
- "_dataConnectionType"
- "_dataProvider"
- "_dataTransformersByDomain"
- "_delegate"
- "_descriptionBuilderWithMultilinePrefix:forDebug:"
- "_disabledApplicationIDs"
- "_domainsByChangeLogKey"
- "_dynamicAttributions"
- "_entitledDomains"
- "_entityResolver"
- "_entityResolverProvider"
- "_entityResolversByLocalization"
- "_fakeCellularRegistrationCanceled"
- "_fakeRegistrationCanceled"
- "_fakeServiceCanceled"
- "_fallbackDataByDomain"
- "_hasCellularTelephony"
- "_hiddenSIM"
- "_hideDataIndicatorChanged:"
- "_homeCountryCode"
- "_identifier"
- "_identityResolver"
- "_internalDefaultsObserver"
- "_internalQueue"
- "_invalidated"
- "_isSatelliteSystem"
- "_lastKnownNetworkCountryCode"
- "_localStatusServer"
- "_locationData"
- "_maxSignalStrengthBars"
- "_mediaData"
- "_mobileEquipmentInfo"
- "_modemDataConnectionType"
- "_networkReselectionNeeded"
- "_observerQueue"
- "_observers"
- "_observingDomains"
- "_operatorName"
- "_preferredForDataConnections"
- "_preferredLocalizations"
- "_pretendingToSearch"
- "_providingDataConnection"
- "_publisherClientsByDomain"
- "_publisherServerHandle"
- "_publisherXPCClientListener"
- "_publishingDomains"
- "_radiosPreferences"
- "_recentAttributionExpirationTimers"
- "_recentAttributions"
- "_referenceCounts"
- "_registerForInternalDefaultsChanges"
- "_registeredWithoutCellular"
- "_registrationRejectionCauseCode"
- "_registrationStatus"
- "_reinitiatingActivationDisabled"
- "_resolver"
- "_server"
- "_serverConnection"
- "_serverHandle"
- "_shortSIMLabel"
- "_signalStrengthBars"
- "_slot1SubscriptionContext"
- "_slot2SubscriptionContext"
- "_statusBarImages"
- "_statusItemIdentifiers"
- "_statusItemsManager"
- "_statusItemsToVisualDescriptors"
- "_stewieState"
- "_stewieStateMonitor"
- "_subscriptionInfo"
- "_suppressSOSOnlyWithLimitedService"
- "_systemStatusDefaults"
- "_telephonyDaemonRestartHandlerCanceled"
- "_telephonyDomainPublisher"
- "_telephonyStateProvider"
- "_transformersByLocalization"
- "_updateSupportedStatusItemsAndVisualDescriptorsFromBundleRecords"
- "_visualDescriptors"
- "_volatileDataByDomain"
- "_wrappedClientHandle"
- "_xpcClientListener"
- "_xpcListener"
- "accessDuration"
- "accessEndTimestamp"
- "accessStartTimestamp"
- "activeBackgroundActivities"
- "activeDisplayModes"
- "activeEntity"
- "activeStatusItems"
- "activeSubscriptionsDidChange"
- "activityAttribution"
- "addClientDataTransformerProvider:forDomain:"
- "addDataTransformer:forDomain:"
- "addDiff:forClientKey:domain:"
- "addEntriesFromDataChangeRecord:forDomain:replacingClientKeysWithKey:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "airplaneMode"
- "airplaneModeChanged"
- "allKeys"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "anbrActivationState:enabled:"
- "anbrBitrateRecommendation:bitrate:direction:"
- "anyObject"
- "appendArraySection:withName:skipIfEmpty:"
- "appendBodySectionWithName:multilinePrefix:block:"
- "appendBool:withName:"
- "appendBool:withName:ifEqualTo:"
- "appendDictionarySection:withName:skipIfEmpty:"
- "appendInteger:withName:"
- "appendObject:withName:"
- "appendString:withName:"
- "appendUnsignedInteger:withName:"
- "applyDiff:"
- "array"
- "arrayWithObjects:count:"
- "attributedEntity"
- "attributions"
- "audioRecordingActivityAttribution"
- "auditToken"
- "authTokenChanged:"
- "autorelease"
- "backgroundActivitiesWithVisualDescriptors"
- "backgroundActivityIdentifier"
- "baseId"
- "beginBatchResolutionSession"
- "boolValue"
- "bootstrap"
- "bs_filter:"
- "bs_firstObjectPassingTest:"
- "bs_map:"
- "bs_safeArrayForKey:"
- "bs_safeDictionaryForKey:"
- "bs_safeStringForKey:"
- "build"
- "builderWithObject:"
- "bundleForClass:"
- "bundleIdentifier"
- "bundlePath"
- "bundleRecordForRecordIdentifier:"
- "cacheObject:forKey:"
- "cachedObjectForKey:"
- "callStackReturnAddresses"
- "cameraAttributions"
- "cameraCaptureAttribution"
- "cameraDescriptor"
- "carrierBundleChange:"
- "carrierBundleInfoDidChangeForStateProvider:slot:"
- "carrierBundleInfoForSlot:"
- "cellChanged:cell:"
- "cellMonitorUpdate:info:"
- "cellularRadioCapabilityActive"
- "cfBundle"
- "changedDueToSimRemoval"
- "class"
- "clearObjectForKey:"
- "clientAuditToken"
- "clientExecutablePath"
- "compare:"
- "compare:options:"
- "conformsToProtocol:"
- "connectionActivationError:connection:error:"
- "connectionAvailability:availableConnections:"
- "connectionStateChanged:connection:dataConnectionStatusInfo:"
- "containsObject:"
- "containsString:"
- "containsValue:"
- "copy"
- "copyCarrierBundleValueWithDefault:key:bundleType:completion:"
- "copyCarrierBundleValueWithDefault:key:bundleType:error:"
- "copyLastKnownMobileCountryCode:completion:"
- "copyMobileCountryCode:completion:"
- "copyOperatorName:completion:"
- "copyRegistrationDisplayStatus:completion:"
- "copyRegistrationStatus:completion:"
- "copyRejectCauseCode:completion:"
- "copyReplacingAttributedEntity:activeEntity:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentDataForDomain:"
- "currentDataServiceDescriptorChanged:"
- "currentDataSimChanged:"
- "customerServiceProfileChanged:visible:"
- "dataAccessAttributions"
- "dataAccessData"
- "dataAccessType"
- "dataChangedHandler"
- "dataForDomain:client:"
- "dataRatesChanged"
- "dataRoamingSettingsChanged:status:"
- "dataSettingsChanged:"
- "dataStatus:dataStatusInfo:"
- "dataTransformerForClient:"
- "dealloc"
- "debugDescription"
- "debugDescriptionWithMultilinePrefix:"
- "decrementReferenceCountForKey:"
- "defaultBundleChange"
- "delegate"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "dictionary"
- "dictionaryWithCapacity:"
- "didDetectSimDeactivation:info:"
- "diffFromData:"
- "displayBars"
- "displayInactiveSOSInStatusBar"
- "displayStatusChanged:status:"
- "displayStewieInStatusBar"
- "domainsWithData"
- "domainsWithSignificantData"
- "dualSimCapabilityDidChange"
- "dynamicAttributions"
- "eligibleDisplayModes"
- "encryptionStatusChanged:info:"
- "enhancedDataLinkQualityChanged:metric:"
- "enhancedVoiceLinkQualityChanged:metric:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateWithBlock:"
- "executableIdentity"
- "executablePath"
- "executableURL"
- "fakeCellularRegistrationCanceled"
- "fakeRegistrationCanceled"
- "fakeServiceCanceled"
- "fallbackDataForClientKey:domain:"
- "firstObject"
- "formattedString"
- "getCurrentDataSubscriptionContextSync:"
- "getDataStatus:completion:"
- "getDualSimCapability:"
- "getMobileEquipmentInfoFor:error:"
- "getSIMStatus:error:"
- "getShortLabel:error:"
- "getSignalStrengthInfo:completion:"
- "getState"
- "getSubscriptionInfo:"
- "handleForIdentifier:error:"
- "handleUserInteraction:forDomain:"
- "hasAuditToken"
- "hash"
- "hostProcess"
- "identifierWithPid:"
- "imsRegistrationChanged:info:"
- "incrementReferenceCountForKey:"
- "indexOfObjectPassingTest:"
- "indicator"
- "indicatorOverride"
- "infoDictionary"
- "init"
- "initWithActivityAttribution:"
- "initWithActivityAttribution:maximumHistoryAccessed:"
- "initWithAttributedEntity:"
- "initWithAttributedEntity:activeEntity:"
- "initWithAudioRecordingActivityAttribution:recent:startTimestamp:endTimestamp:"
- "initWithAuditToken:"
- "initWithAuditToken:bundlePath:executablePath:bundleIdentifier:personaUniqueString:systemExecutable:"
- "initWithBackgroundActivityManager:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithBundleInfoDictionary:bundleRecordIdentifier:bundleURL:"
- "initWithBundleRecordClass:"
- "initWithBundleType:"
- "initWithCameraCaptureAttribution:recent:startTimestamp:endTimestamp:"
- "initWithCameraDescriptor:activityAttribution:"
- "initWithCapacity:"
- "initWithDataProvider:publisherServerHandle:"
- "initWithDefaults:"
- "initWithDelegate:queue:"
- "initWithEntityResolver:"
- "initWithEntityResolver:identityResolver:cache:"
- "initWithEntityResolverProvider:"
- "initWithExecutableIdentity:"
- "initWithExecutableIdentity:website:systemService:localizedDisplayName:localizedExecutableDisplayName:"
- "initWithExecutablePath:"
- "initWithIdentifier:"
- "initWithIdentityResolver:"
- "initWithLocationAttribution:recent:startTimestamp:endTimestamp:"
- "initWithLocationState:activityAttribution:eligibleDisplayModes:"
- "initWithMachServiceName:"
- "initWithMicrophoneRecordingAttribution:recent:startTimestamp:endTimestamp:"
- "initWithMutedMicrophoneRecordingActivityAttribution:recent:startTimestamp:endTimestamp:"
- "initWithOptions:capacity:"
- "initWithPath:"
- "initWithPlistRepresentation:"
- "initWithPreferredLocalizations:"
- "initWithPreferredLocalizations:identityResolver:"
- "initWithQueue:"
- "initWithRecordKeys:"
- "initWithResolver:cache:"
- "initWithServer:"
- "initWithServerHandle:"
- "initWithServerHandle:stateProvider:"
- "initWithStateProvider:"
- "initWithStatusItemsManager:"
- "initWithWrappedClientHandle:preferredLocalizations:"
- "initWithXPCConnection:serverHandle:"
- "integerValue"
- "internalQueuePublisherServerHandle"
- "internetConnectionActivationError:"
- "internetConnectionAvailability:"
- "internetConnectionStateChanged:"
- "internetDataStatus:"
- "internetDataStatusBasic:"
- "intersectSet:"
- "invalidate"
- "isCellularRadioCapabilityActive"
- "isDualSIMEnabled"
- "isEmpty"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToString:"
- "isFakingCellularRegistration"
- "isFakingRegistration"
- "isFakingService"
- "isHiddenSIM"
- "isInactiveSOSEnabled"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNetworkReselectionNeeded:completion:"
- "isOnBootstrap"
- "isProxy"
- "isRadioModuleDead"
- "isRecent"
- "isRegistrationForcedHome"
- "isReinitiatingActivationDisabled"
- "isSIMPresentForSlot:"
- "isSimHidden"
- "isStewieActiveOverBB"
- "isStewieActiveOverInternet"
- "isSubsetOfSet:"
- "isSystemExecutable"
- "isSystemService"
- "isUnconditionalCallForwardingActive:completion:"
- "isUsingStewieConnection"
- "isUsingStewieConnectionOverInternet"
- "isUsingStewieForSOS"
- "label"
- "labelID"
- "lastPathComponent"
- "length"
- "listener:shouldAcceptNewConnection:"
- "localizationKey"
- "localizations"
- "localizedDisplayName"
- "localizedExecutableDisplayName"
- "localizedStringForKey:value:table:"
- "localizedStringForKey:value:table:localization:"
- "localizedStringWithFormat:"
- "locationAttribution"
- "locationData"
- "locationState"
- "mainBundle"
- "maskingClientExecutablePath"
- "maxDisplayBars"
- "maximumHistoryAccessed"
- "mediaData"
- "microphoneAttributions"
- "microphoneRecordingAttribution"
- "minusSet:"
- "mobileEquipmentInfo"
- "mobileEquipmentInfoDidChangeForStateProvider:slot:"
- "mobileEquipmentInfoForSlot:"
- "modifyClientDataTransformerProvider:forDomain:usingBlock:"
- "modifyDataTransformer:forDomain:usingBlock:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "mutedMicrophoneRecordingActivityAttribution"
- "mutedMicrophoneRecordingAttributions"
- "networkListAvailable:list:"
- "networkReselectionNeeded"
- "networkReselectionNeeded:"
- "networkSelected:success:mode:"
- "nrDisableStatusChanged:status:"
- "nrSliceAppStateChanged:status:trafficDescriptors:"
- "nrSlicedRunningAppStateChanged:"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeData:forDomain:withChangeContext:"
- "observeDefault:onQueue:withBlock:"
- "observeDiff:forDomain:withChangeContext:"
- "observeDomain:withPreferredLocalizations:"
- "onBootstrap"
- "operatorBundleChange:"
- "operatorNameChanged:name:"
- "orderedSetWithArray:"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personaUniqueString"
- "phoneBookError:"
- "phoneBookFetched:"
- "phoneBookSelected:"
- "phoneBookWritten:"
- "phoneNumberAvailable:"
- "phoneNumberChanged:"
- "plmnChanged:plmn:"
- "preferredDataServiceDescriptorChanged:"
- "preferredDataSimChanged:"
- "preferredForDataConnections"
- "preferredLocalizations"
- "preferredLocalizationsFromArray:forPreferences:"
- "pretendingToSearch"
- "prlVersionDidChange:version:"
- "providingDataConnection"
- "publishData:forDomain:withChangeContext:discardingOnExit:reply:"
- "publishData:forPublisherClient:domain:withChangeContext:completion:"
- "publishDiff:forDomain:withChangeContext:replacingData:discardingOnExit:reply:"
- "publishVolatileData:forPublisherClient:domain:withChangeContext:completion:"
- "publishedDataForDomain:"
- "publishedDomains"
- "publishedVolatileDataForDomain:"
- "q"
- "q16@0:8"
- "radioTechnology"
- "rangeOfString:"
- "rangeOfString:options:"
- "ratSelectionChanged:selection:"
- "recordBundlesChangedForBundleManager:"
- "recordForKey:"
- "recordIdentifiers"
- "recordType"
- "refresh"
- "regDataModeChanged:dataMode:"
- "registerClient:forDomain:"
- "registerPublisherClient:forDomain:fallbackData:"
- "registerToPublishDomain:fallbackData:"
- "registeredWithoutCellular"
- "registrationDisplayStatus"
- "rejectCauseCodeChanged:causeCode:"
- "release"
- "removeAllEntriesForClientKey:domain:"
- "removeAllObjects"
- "removeAttribution:"
- "removeClient:forDomain:"
- "removeClientDataTransformerProvider:forDomain:"
- "removeDataTransformer:forDomain:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsInArray:"
- "removeObserver:"
- "removePublisherClient:forDomain:"
- "replaceDataChangeRecord:discardingOnExit:reply:"
- "replaceDataChangeRecord:forPublisherClient:completion:"
- "replaceVolatileDataChangeRecord:forPublisherClient:completion:"
- "reportUserInteraction:forClient:domain:"
- "reportUserInteraction:forDomain:"
- "resolveEntities:"
- "resolveEntity:"
- "resolveIdentities:"
- "resolvedIdentityForIdentity:"
- "resolvedStatusItemFromStatusItems:"
- "resolverForPreferredLocalizations:"
- "respondsToSelector:"
- "responsibleIdentityForAuditToken:"
- "resume"
- "retain"
- "retainCount"
- "scheduleWithFireInterval:leewayInterval:queue:handler:"
- "screenCaptureAttributions"
- "self"
- "server"
- "serverDataForDomains:preferredLocalizations:reply:"
- "serviceDisconnection:status:"
- "servingNetworkChanged:"
- "set"
- "setActiveDisplayModes:"
- "setActiveMultilinePrefix:"
- "setAttributions:"
- "setBootstrap:"
- "setBootstrapICCID:"
- "setCSN:"
- "setCachedCTOperatorName:"
- "setCachedCTRegistrationCellularStatus:"
- "setCachedCTRegistrationDisplayStatus:"
- "setCallForwardingEnabled:"
- "setCallForwardingIndicator:"
- "setCameraAttributions:"
- "setCarrierBundleInfo:"
- "setCarrierName:"
- "setCellularRadioCapabilityEnabled:"
- "setCellularRegistrationStatus:"
- "setCellularServiceState:"
- "setCustomerServicePhoneNumber:"
- "setData:forClientKey:domain:"
- "setDataAccessAttributions:"
- "setDataChangedHandler:"
- "setDataConnectionType:"
- "setDataNetworkType:"
- "setDelegate:"
- "setDisabledApplicationIDs:"
- "setDualSIMEnabled:"
- "setDynamicAttributions:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFakeCellularRegistrationCanceled:"
- "setFakeRegistrationCanceled:"
- "setFakeServiceCanceled:"
- "setFallbackData:forClientKey:domain:"
- "setHiddenSIM:"
- "setHomeCountryCode:"
- "setICCID:"
- "setIMEI:"
- "setIdentifier:"
- "setInactiveSOSEnabled:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsSatelliteSystem:"
- "setLTEConnectionShows4G:"
- "setLabel:"
- "setLastKnownNetworkCountryCode:"
- "setLocationData:mediaData:"
- "setMEID:"
- "setMaxSignalStrengthBars:"
- "setMicrophoneAttributions:"
- "setMobileEquipmentInfo:"
- "setModemDataConnectionType:"
- "setMutedMicrophoneRecordingAttributions:"
- "setNetworkReselectionNeeded:"
- "setObject:forKey:"
- "setOperatorName:"
- "setPreferredForDataConnections:"
- "setPretendingToSearch:"
- "setProvidingDataConnection:"
- "setRadioModuleDead:"
- "setRegisteredWithoutCellular:"
- "setRegistrationRejectionCauseCode:"
- "setRegistrationStatus:"
- "setReinitiatingActivationDisabled:"
- "setRemoteObjectInterface:"
- "setRepresentation"
- "setSIMLabel:"
- "setSIMOneInfo:"
- "setSIMPresent:"
- "setSIMStatus:"
- "setSIMTwoInfo:"
- "setScreenCaptureAttributions:"
- "setSecondaryServiceDescription:"
- "setServiceDescription:"
- "setServiceState:"
- "setShortLabel:"
- "setShortSIMLabel:"
- "setSignalStrengthBars:"
- "setStatusBarImages:"
- "setSubscriptionInfo:"
- "setSuppressSOSOnlyWithLimitedService:"
- "setSystemAudioRecordingAttributions:"
- "setUseDebugDescription:"
- "setUsingStewieConnection:"
- "setUsingStewieConnectionOverInternet:"
- "setUsingStewieForSOS:"
- "setValue:forKey:"
- "setVisualDescriptor:forBackgroundActivityWithIdentifier:"
- "setVisualDescriptor:forStatusItemWithIdentifier:"
- "setVolatileData:"
- "setWithArray:"
- "setWithSet:"
- "sharedInstance"
- "shortLabelsDidChange"
- "signalStrengthChanged:info:"
- "simLessSubscriptionsDidChange"
- "simLockSaveRequestDidComplete:success:"
- "simPinChangeRequestDidComplete:success:"
- "simPinEntryErrorDidOccur:status:"
- "simPukEntryErrorDidOccur:status:"
- "simStatusDidChange:status:"
- "slotID"
- "spcUnlockSuccessful:"
- "st_removeFirstOccurrenceOfObject:"
- "st_subtractArray:"
- "standardDefaults"
- "start"
- "stateChanged:"
- "statusItemIdentifier"
- "statusItemIdentifiers"
- "statusItemsWithVisualDescriptors"
- "stewieStateDidChangeForStateProvider:usingStewieForSOS:isInactiveSOSEnabled:"
- "stewieStateDidChangeForStateProvider:usingStewieForSOS:isInactiveSOSEnabled:usingStewieConnection:usingStewieConnectionOverInternet:"
- "stopObservingDomain:"
- "stringByDeletingPathExtension"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "strongToStrongObjectsMapTable"
- "subscriberCountryCodeDidChange:"
- "subscriptionInfoDidChange"
- "subscriptionInfoDidChangeForStateProvider:slot:"
- "subscriptionInfoForSlot:"
- "subscriptions"
- "subscriptionsInUse"
- "substringToIndex:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "superclass"
- "suppServicesCompleted:"
- "suppServicesError:error:"
- "suppServicesEvent:event:settingsType:data:"
- "suppServicesStarted:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemAudioRecordingAttributions"
- "systemStatusServer:publishedDomainsDidChange:"
- "tetheringStatus:"
- "tetheringStatus:connectionType:"
- "transformedDataForData:domain:"
- "unionSet:"
- "unregisterFromPublishingDomain:"
- "unsignedIntegerValue"
- "updateDataForPublisherClient:domain:usingDiffProvider:completion:"
- "updateDataWithBlock:"
- "updateVolatileDataForPublisherClient:domain:usingDiffProvider:completion:"
- "userDataPreferred"
- "userDefaultVoiceSlotDidChange:"
- "usingStewieConnection"
- "usingStewieConnectionOverInternet"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"CTDataConnectionStatus\"16"
- "v24@0:8@\"CTDataSettings\"16"
- "v24@0:8@\"CTDataStatus\"16"
- "v24@0:8@\"CTDataStatusBasic\"16"
- "v24@0:8@\"CTServiceDescriptor\"16"
- "v24@0:8@\"CTSlicedRunningAppInfoContainer\"16"
- "v24@0:8@\"CTStewieState\"16"
- "v24@0:8@\"CTTetheringStatus\"16"
- "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@\"STBundleManager\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^B16"
- "v24@0:8q16"
- "v28@0:8@\"CTServiceDescriptor\"16B24"
- "v28@0:8@\"CTTetheringStatus\"16i24"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16i24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v32@0:8@\"<STStatusDomainClientHandle>\"16Q24"
- "v32@0:8@\"<STStatusDomainPublisherClientHandle>\"16Q24"
- "v32@0:8@\"<STStatusDomainUserInteraction>\"16Q24"
- "v32@0:8@\"CTServiceDescriptor\"16@\"CTEncryptionStatusInfo\"24"
- "v32@0:8@\"CTServiceDescriptor\"16@\"CTNRStatus\"24"
- "v32@0:8@\"CTServiceDescriptor\"16@\"CTPlmnInfo\"24"
- "v32@0:8@\"CTServiceDescriptor\"16@\"CTRatSelection\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTCellInfo\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTDataStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTEnhancedDataLinkQualityMetric\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTEnhancedLinkQualityMetric\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTIMSRegistrationTransportInfo\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTNetworkList\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTRegistrationDisplayStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTServiceDisconnectionStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSignalStrengthInfo\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSimDeactivationInfo\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTVoiceLinkQualityMetric\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSArray\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSDictionary\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSError\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSString\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16i24i28"
- "v32@0:8@\"NSNumber\"16@\"NSArray\"24"
- "v32@0:8@\"STTelephonyStateProvider\"16B24B28"
- "v32@0:8@\"STTelephonyStateProvider\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16B24B28"
- "v32@0:8@16Q24"
- "v32@0:8@16i24i28"
- "v32@0:8@16q24"
- "v32@0:8Q16@\"<STStatusDomainData><STStatusDomainDataDifferencing>\"24"
- "v32@0:8Q16@24"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24i32"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16B24@\"NSString\"28"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16i24@\"CTDataConnectionStatus\"28"
- "v36@0:8@\"NSString\"16B24@\"CTTrafficDescriptorsContainer\"28"
- "v36@0:8@\"STStatusDomainDataChangeRecord\"16B24@?<v@?>28"
- "v36@0:8@16@24i32"
- "v36@0:8@16B24@28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16i24@28"
- "v40@0:8@\"<STStatusDomainData>\"16Q24@\"<STStatusDomainDataChangeContext>\"32"
- "v40@0:8@\"<STStatusDomainPublisherClientHandle>\"16Q24@\"<STStatusDomainData><STStatusDomainDataDifferencing>\"32"
- "v40@0:8@\"<STStatusDomainUserInteraction>\"16@\"<STStatusDomainClientHandle>\"24Q32"
- "v40@0:8@\"CTXPCServiceSubscriptionContext\"16i24i28@\"CTSuppServicesNotificationData\"32"
- "v40@0:8@\"NSSet\"16@\"NSArray\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"STStatusDomainDataChangeRecord\"16@\"<STStatusDomainPublisherClientHandle>\"24@?<v@?>32"
- "v40@0:8@\"STTelephonyStateProvider\"16B24B28B32B36"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "v40@0:8@16B24B28B32B36"
- "v40@0:8@16Q24@32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16i24i28@32"
- "v48@0:8@\"<STStatusDomainPublisherClientHandle>\"16Q24@?<@\"<STStatusDomainDataDiff>\"@?@\"<STStatusDomainData><STStatusDomainDataDifferencing>\"^@>32@?<v@?>40"
- "v48@0:8@16Q24@?32@?40"
- "v52@0:8@\"<STStatusDomainData>\"16Q24@\"<STStatusDomainDataChangeContext>\"32B40@?<v@?>44"
- "v52@0:8@16Q24@32B40@?44"
- "v56@0:8@\"<STStatusDomainData><STStatusDomainDataDifferencing>\"16@\"<STStatusDomainPublisherClientHandle>\"24Q32@\"<STStatusDomainDataChangeContext>\"40@?<v@?>48"
- "v56@0:8@\"<STStatusDomainDataDiff>\"16Q24@\"<STStatusDomainDataChangeContext>\"32B40B44@?<v@?>48"
- "v56@0:8@16@24Q32@40@?48"
- "v56@0:8@16Q24@32B40B44@?48"
- "validBackgroundActivitiesForBackgroundActivities:"
- "validStatusItemsForStatusItems:"
- "valueForEntitlement:"
- "visualDescriptorForBackgroundActivityWithIdentifier:"
- "visualDescriptorForStatusItemWithIdentifier:"
- "voiceLinkQualityChanged:metric:"
- "wantsUntransformedData"
- "weakObjectsHashTable"
- "weakToStrongObjectsMapTable"
- "website"
- "wrappedClientHandle"
- "zone"

```
