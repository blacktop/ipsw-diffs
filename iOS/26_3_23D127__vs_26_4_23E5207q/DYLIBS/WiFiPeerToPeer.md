## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-838.4.0.0.0
-  __TEXT.__text: 0x215c4
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x33a4
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x5483
-  __TEXT.__oslogstring: 0xb0e
+855.25.0.0.0
+  __TEXT.__text: 0x28fe4
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x3b5c
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x6467
+  __TEXT.__oslogstring: 0xb97
   __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__unwind_info: 0x970
-  __TEXT.__objc_classname: 0x779
-  __TEXT.__objc_methname: 0x820d
-  __TEXT.__objc_methtype: 0x1ba1
-  __TEXT.__objc_stubs: 0x41c0
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0xd38
-  __DATA_CONST.__objc_classlist: 0x140
-  __DATA_CONST.__objc_protolist: 0xc0
+  __TEXT.__unwind_info: 0xab0
+  __TEXT.__objc_classname: 0x884
+  __TEXT.__objc_methname: 0x9462
+  __TEXT.__objc_methtype: 0x1e4d
+  __TEXT.__objc_stubs: 0x4a40
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0xee8
+  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1738
-  __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x130
-  __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x3560
-  __AUTH_CONST.__objc_const: 0x5920
-  __AUTH.__objc_data: 0x1b8
-  __DATA.__objc_ivar: 0x42c
-  __DATA.__data: 0x900
-  __DATA_DIRTY.__objc_data: 0xac8
+  __DATA_CONST.__objc_selrefs: 0x1a38
+  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x168
+  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0x4920
+  __AUTH_CONST.__objc_const: 0x6ac0
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x51c
+  __DATA.__data: 0x9c0
+  __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5734B53-F3FC-3691-B6E2-1C6559CAE27B
-  Functions: 1036
-  Symbols:   3701
-  CStrings:  2448
+  UUID: 32990D28-8CA3-3D22-B691-60F4CA9B1716
+  Functions: 1190
+  Symbols:   4225
+  CStrings:  2987
 
Symbols:
+ +[WiFiAwareDataPathInfoPerDataAddress supportsSecureCoding]
+ +[WiFiAwareDataPathSessionInfo supportsSecureCoding]
+ +[WiFiAwareDataPathState currentState]
+ +[WiFiAwareDataPathState queryNANDataPathState]
+ +[WiFiAwareDataPathState supportsSecureCoding]
+ +[WiFiAwareDataPathState(BoldFormatting) queryNANDataPathState]
+ +[WiFiAwareState currentState]
+ +[WiFiAwareState supportsSecureCoding]
+ +[WiFiAwareStateMonitorConfiguration supportsSecureCoding]
+ -[WiFiAwareDataPathInfoPerDataAddress .cxx_destruct]
+ -[WiFiAwareDataPathInfoPerDataAddress copyWithZone:]
+ -[WiFiAwareDataPathInfoPerDataAddress dataAddress]
+ -[WiFiAwareDataPathInfoPerDataAddress encodeWithCoder:]
+ -[WiFiAwareDataPathInfoPerDataAddress initWithCoder:]
+ -[WiFiAwareDataPathInfoPerDataAddress initWithInterfaceName:dataAddress:sessionCount:]
+ -[WiFiAwareDataPathInfoPerDataAddress init]
+ -[WiFiAwareDataPathInfoPerDataAddress interfaceName]
+ -[WiFiAwareDataPathInfoPerDataAddress sessionCount]
+ -[WiFiAwareDataPathSessionInfo .cxx_destruct]
+ -[WiFiAwareDataPathSessionInfo copyWithZone:]
+ -[WiFiAwareDataPathSessionInfo dpId]
+ -[WiFiAwareDataPathSessionInfo dpRole]
+ -[WiFiAwareDataPathSessionInfo encodeWithCoder:]
+ -[WiFiAwareDataPathSessionInfo initWithCoder:]
+ -[WiFiAwareDataPathSessionInfo initWithDpId:dpRole:serviceId:security:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:qosType:sessionState:]
+ -[WiFiAwareDataPathSessionInfo init]
+ -[WiFiAwareDataPathSessionInfo initiatorDataAddress]
+ -[WiFiAwareDataPathSessionInfo peerDataAddress]
+ -[WiFiAwareDataPathSessionInfo peerNmiMacAddress]
+ -[WiFiAwareDataPathSessionInfo qosType]
+ -[WiFiAwareDataPathSessionInfo security]
+ -[WiFiAwareDataPathSessionInfo serviceId]
+ -[WiFiAwareDataPathSessionInfo sessionState]
+ -[WiFiAwareDataPathState .cxx_destruct]
+ -[WiFiAwareDataPathState copyWithZone:]
+ -[WiFiAwareDataPathState customPreferredChannelClass]
+ -[WiFiAwareDataPathState customPreferredChannelNumber]
+ -[WiFiAwareDataPathState description]
+ -[WiFiAwareDataPathState encodeWithCoder:]
+ -[WiFiAwareDataPathState establishedSessionCounter]
+ -[WiFiAwareDataPathState initWithCoder:]
+ -[WiFiAwareDataPathState initWithInterfaceName:macAddress:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiDataAddressCount:ndiSessions:customPreferredChannelNumber:customPreferredChannelClass:sessionInfos:]
+ -[WiFiAwareDataPathState interfaceName]
+ -[WiFiAwareDataPathState isEnabled]
+ -[WiFiAwareDataPathState macAddress]
+ -[WiFiAwareDataPathState mapSessionStateToNumber:]
+ -[WiFiAwareDataPathState ndiDataAddressCount]
+ -[WiFiAwareDataPathState ndiSessions]
+ -[WiFiAwareDataPathState rtmLowLatencySessionRefCount]
+ -[WiFiAwareDataPathState rtmSessionRefCount]
+ -[WiFiAwareDataPathState rtmSessionWith24GOnlyCount]
+ -[WiFiAwareDataPathState sessionInfos]
+ -[WiFiAwareDataPathState sessionWith24GOnlyPeerCount]
+ -[WiFiAwareDataPathState stringForQosType:]
+ -[WiFiAwareDataPathState stringForSecurity:]
+ -[WiFiAwareDataPathState stringForSessionState:]
+ -[WiFiAwareDataPathState totalSessionCounter]
+ -[WiFiAwareDataPathState(BoldFormatting) descriptionWithChangedOptions:]
+ -[WiFiAwareDataPathState(BoldFormatting) getFormattedDataPathStateDescription]
+ -[WiFiAwareDataSession datapathID]
+ -[WiFiAwareDataSession multicastConfiguration]
+ -[WiFiAwareDataSession setMulticastConfiguration:]
+ -[WiFiAwareDatapathConfiguration initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:multicastConfiguration:]
+ -[WiFiAwareDatapathConfiguration multicastConfigurationEqual:]
+ -[WiFiAwareDatapathConfiguration multicastConfiguration]
+ -[WiFiAwareDatapathConfiguration setMulticastConfiguration:]
+ -[WiFiAwareDatapathInfo .cxx_destruct]
+ -[WiFiAwareDatapathInfo activate]
+ -[WiFiAwareDatapathInfo deactivate]
+ -[WiFiAwareDatapathInfo deriveSharedSecretForProtocolName:context:derivationMethod:completion:]
+ -[WiFiAwareDatapathInfo handleError:]
+ -[WiFiAwareDatapathInfo initWithDatapathID:role:peerMacAddress:]
+ -[WiFiAwareDatapathInfo performance:]
+ -[WiFiAwareDatapathInfo remoteObjectInterface]
+ -[WiFiAwareDatapathInfo startConnectionUsingProxy:completionHandler:]
+ -[WiFiAwareMulticastConfiguration gtkKey]
+ -[WiFiAwareMulticastConfiguration igtkKey]
+ -[WiFiAwareMulticastConfiguration keyBlob]
+ -[WiFiAwareMulticastConfiguration keyExchangeOverMedium]
+ -[WiFiAwareMulticastConfiguration setGtkKey:]
+ -[WiFiAwareMulticastConfiguration setIgtkKey:]
+ -[WiFiAwareMulticastConfiguration setKeyBlob:]
+ -[WiFiAwareMulticastConfiguration setKeyExchangeOverMedium:]
+ -[WiFiAwarePublisher publishKeysBlobForMulticastSession:]
+ -[WiFiAwarePublisher publishPairingRequestEndedWithSubscriber:reason:]
+ -[WiFiAwareState .cxx_destruct]
+ -[WiFiAwareState ambtt]
+ -[WiFiAwareState anchorMasterRankM]
+ -[WiFiAwareState anchorMasterRankR]
+ -[WiFiAwareState anchorMaster]
+ -[WiFiAwareState clusterId]
+ -[WiFiAwareState copyWithZone:]
+ -[WiFiAwareState description]
+ -[WiFiAwareState encodeWithCoder:]
+ -[WiFiAwareState hopCount]
+ -[WiFiAwareState immediateMasterRankM]
+ -[WiFiAwareState immediateMasterRankR]
+ -[WiFiAwareState immediateMaster]
+ -[WiFiAwareState initInternal]
+ -[WiFiAwareState initWithCoder:]
+ -[WiFiAwareState initWithInterfaceName:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfAddress:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:]
+ -[WiFiAwareState init]
+ -[WiFiAwareState interfaceName]
+ -[WiFiAwareState isEnabled]
+ -[WiFiAwareState isFWElection]
+ -[WiFiAwareState nanRole]
+ -[WiFiAwareState selfAddress]
+ -[WiFiAwareState selfRankM]
+ -[WiFiAwareState selfRankR]
+ -[WiFiAwareState tsf]
+ -[WiFiAwareState(BoldFormatting) descriptionWithChangedOptions:]
+ -[WiFiAwareStateMonitor .cxx_destruct]
+ -[WiFiAwareStateMonitor beginMonitoring]
+ -[WiFiAwareStateMonitor dpStateUpdatedHandler]
+ -[WiFiAwareStateMonitor endMonitoring]
+ -[WiFiAwareStateMonitor exportedInterface]
+ -[WiFiAwareStateMonitor exportedObject]
+ -[WiFiAwareStateMonitor getFormattedDataPathStateDescription:]
+ -[WiFiAwareStateMonitor getFormattedStateDescription:]
+ -[WiFiAwareStateMonitor handleConnectionEstablishedWithProxy:]
+ -[WiFiAwareStateMonitor init]
+ -[WiFiAwareStateMonitor lastDataPathStateChangedOptions]
+ -[WiFiAwareStateMonitor lastStateChangedOptions]
+ -[WiFiAwareStateMonitor queryNANDataPathState]
+ -[WiFiAwareStateMonitor queryNANEnabled]
+ -[WiFiAwareStateMonitor queryNANState]
+ -[WiFiAwareStateMonitor setDpStateUpdatedHandler:]
+ -[WiFiAwareStateMonitor setLastDataPathStateChangedOptions:]
+ -[WiFiAwareStateMonitor setLastStateChangedOptions:]
+ -[WiFiAwareStateMonitor setStateUpdatedHandler:]
+ -[WiFiAwareStateMonitor startConnectionUsingProxy:completionHandler:]
+ -[WiFiAwareStateMonitor stateUpdatedHandler]
+ -[WiFiAwareStateMonitor updatedNANDpState:]
+ -[WiFiAwareStateMonitor updatedNANDpStateWithChangedOptions:changedOptions:]
+ -[WiFiAwareStateMonitor updatedNANState:]
+ -[WiFiAwareStateMonitor updatedNANStateWithChangedOptions:changedOptions:]
+ -[WiFiAwareStateMonitorConfiguration copyWithZone:]
+ -[WiFiAwareStateMonitorConfiguration description]
+ -[WiFiAwareStateMonitorConfiguration encodeWithCoder:]
+ -[WiFiAwareStateMonitorConfiguration initWithCoder:]
+ -[WiFiAwareStateMonitorConfiguration init]
+ -[WiFiAwareStateMonitorConfiguration options]
+ -[WiFiAwareStateMonitorConfiguration setOptions:]
+ GCC_except_table43
+ _AWDLTrafficRegistrationServiceContinuityRealTimeGroup
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_WiFiAwareDataPathInfoPerDataAddress
+ _OBJC_CLASS_$_WiFiAwareDataPathSessionInfo
+ _OBJC_CLASS_$_WiFiAwareDataPathState
+ _OBJC_CLASS_$_WiFiAwareDatapathInfo
+ _OBJC_CLASS_$_WiFiAwareState
+ _OBJC_CLASS_$_WiFiAwareStateMonitor
+ _OBJC_CLASS_$_WiFiAwareStateMonitorConfiguration
+ _OBJC_IVAR_$_WiFiAwareDataPathInfoPerDataAddress._dataAddress
+ _OBJC_IVAR_$_WiFiAwareDataPathInfoPerDataAddress._interfaceName
+ _OBJC_IVAR_$_WiFiAwareDataPathInfoPerDataAddress._sessionCount
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._dpId
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._dpRole
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._initiatorDataAddress
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._peerDataAddress
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._peerNmiMacAddress
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._qosType
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._security
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._serviceId
+ _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._sessionState
+ _OBJC_IVAR_$_WiFiAwareDataPathState._customPreferredChannelClass
+ _OBJC_IVAR_$_WiFiAwareDataPathState._customPreferredChannelNumber
+ _OBJC_IVAR_$_WiFiAwareDataPathState._establishedSessionCounter
+ _OBJC_IVAR_$_WiFiAwareDataPathState._interfaceName
+ _OBJC_IVAR_$_WiFiAwareDataPathState._isEnabled
+ _OBJC_IVAR_$_WiFiAwareDataPathState._macAddress
+ _OBJC_IVAR_$_WiFiAwareDataPathState._ndiDataAddressCount
+ _OBJC_IVAR_$_WiFiAwareDataPathState._ndiSessions
+ _OBJC_IVAR_$_WiFiAwareDataPathState._rtmLowLatencySessionRefCount
+ _OBJC_IVAR_$_WiFiAwareDataPathState._rtmSessionRefCount
+ _OBJC_IVAR_$_WiFiAwareDataPathState._rtmSessionWith24GOnlyCount
+ _OBJC_IVAR_$_WiFiAwareDataPathState._sessionInfos
+ _OBJC_IVAR_$_WiFiAwareDataPathState._sessionWith24GOnlyPeerCount
+ _OBJC_IVAR_$_WiFiAwareDataPathState._totalSessionCounter
+ _OBJC_IVAR_$_WiFiAwareDataSession._multicastConfiguration
+ _OBJC_IVAR_$_WiFiAwareDatapathConfiguration._multicastConfiguration
+ _OBJC_IVAR_$_WiFiAwareDatapathInfo._datapathID
+ _OBJC_IVAR_$_WiFiAwareDatapathInfo._peerMacAddress
+ _OBJC_IVAR_$_WiFiAwareDatapathInfo._role
+ _OBJC_IVAR_$_WiFiAwareDatapathInfo._xpcConnection
+ _OBJC_IVAR_$_WiFiAwareMulticastConfiguration._gtkKey
+ _OBJC_IVAR_$_WiFiAwareMulticastConfiguration._igtkKey
+ _OBJC_IVAR_$_WiFiAwareMulticastConfiguration._keyBlob
+ _OBJC_IVAR_$_WiFiAwareMulticastConfiguration._keyExchangeOverMedium
+ _OBJC_IVAR_$_WiFiAwareState._ambtt
+ _OBJC_IVAR_$_WiFiAwareState._anchorMaster
+ _OBJC_IVAR_$_WiFiAwareState._anchorMasterRankM
+ _OBJC_IVAR_$_WiFiAwareState._anchorMasterRankR
+ _OBJC_IVAR_$_WiFiAwareState._clusterId
+ _OBJC_IVAR_$_WiFiAwareState._hopCount
+ _OBJC_IVAR_$_WiFiAwareState._immediateMaster
+ _OBJC_IVAR_$_WiFiAwareState._immediateMasterRankM
+ _OBJC_IVAR_$_WiFiAwareState._immediateMasterRankR
+ _OBJC_IVAR_$_WiFiAwareState._interfaceName
+ _OBJC_IVAR_$_WiFiAwareState._isEnabled
+ _OBJC_IVAR_$_WiFiAwareState._isFWElection
+ _OBJC_IVAR_$_WiFiAwareState._nanRole
+ _OBJC_IVAR_$_WiFiAwareState._selfAddress
+ _OBJC_IVAR_$_WiFiAwareState._selfRankM
+ _OBJC_IVAR_$_WiFiAwareState._selfRankR
+ _OBJC_IVAR_$_WiFiAwareState._tsf
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._dpStateUpdatedHandler
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastDataPathStateChangedOptions
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastStateChangedOptions
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._remoteProxy
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._stateUpdatedHandler
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._xpcConnection
+ _OBJC_IVAR_$_WiFiAwareStateMonitorConfiguration._options
+ _OBJC_METACLASS_$_WiFiAwareDataPathInfoPerDataAddress
+ _OBJC_METACLASS_$_WiFiAwareDataPathSessionInfo
+ _OBJC_METACLASS_$_WiFiAwareDataPathState
+ _OBJC_METACLASS_$_WiFiAwareDatapathInfo
+ _OBJC_METACLASS_$_WiFiAwareState
+ _OBJC_METACLASS_$_WiFiAwareStateMonitor
+ _OBJC_METACLASS_$_WiFiAwareStateMonitorConfiguration
+ __OBJC_$_CLASS_METHODS_WiFiAwareDataPathInfoPerDataAddress
+ __OBJC_$_CLASS_METHODS_WiFiAwareDataPathSessionInfo
+ __OBJC_$_CLASS_METHODS_WiFiAwareDataPathState(BoldFormatting)
+ __OBJC_$_CLASS_METHODS_WiFiAwareState
+ __OBJC_$_CLASS_METHODS_WiFiAwareStateMonitorConfiguration
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareDataPathInfoPerDataAddress
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareDataPathSessionInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareDataPathState
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareState
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareStateMonitorConfiguration
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareDataPathInfoPerDataAddress
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareDataPathSessionInfo
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareDataPathState(BoldFormatting)
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareDatapathInfo
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareState(BoldFormatting)
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareStateMonitor
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareStateMonitorConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareDataPathInfoPerDataAddress
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareDataPathSessionInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareDataPathState
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareDatapathInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareState
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareStateMonitor
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareStateMonitorConfiguration
+ __OBJC_$_PROP_LIST_WiFiAwareDataPathInfoPerDataAddress
+ __OBJC_$_PROP_LIST_WiFiAwareDataPathSessionInfo
+ __OBJC_$_PROP_LIST_WiFiAwareDataPathState
+ __OBJC_$_PROP_LIST_WiFiAwareDatapathInfo
+ __OBJC_$_PROP_LIST_WiFiAwareState
+ __OBJC_$_PROP_LIST_WiFiAwareStateMonitor
+ __OBJC_$_PROP_LIST_WiFiAwareStateMonitorConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwareDatapathInfoXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwareStateMonitorXPCDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwareDatapathInfoXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwareStateMonitorXPCDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiAwareDatapathInfoXPC
+ __OBJC_$_PROTOCOL_REFS_WiFiAwareStateMonitorXPCDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareDataPathInfoPerDataAddress
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareDataPathSessionInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareDataPathState
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareDatapathInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareState
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareStateMonitor
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareStateMonitorConfiguration
+ __OBJC_CLASS_RO_$_WiFiAwareDataPathInfoPerDataAddress
+ __OBJC_CLASS_RO_$_WiFiAwareDataPathSessionInfo
+ __OBJC_CLASS_RO_$_WiFiAwareDataPathState
+ __OBJC_CLASS_RO_$_WiFiAwareDatapathInfo
+ __OBJC_CLASS_RO_$_WiFiAwareState
+ __OBJC_CLASS_RO_$_WiFiAwareStateMonitor
+ __OBJC_CLASS_RO_$_WiFiAwareStateMonitorConfiguration
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwareDatapathInfoXPC
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwareStateMonitorXPCDelegate
+ __OBJC_METACLASS_RO_$_WiFiAwareDataPathInfoPerDataAddress
+ __OBJC_METACLASS_RO_$_WiFiAwareDataPathSessionInfo
+ __OBJC_METACLASS_RO_$_WiFiAwareDataPathState
+ __OBJC_METACLASS_RO_$_WiFiAwareDatapathInfo
+ __OBJC_METACLASS_RO_$_WiFiAwareState
+ __OBJC_METACLASS_RO_$_WiFiAwareStateMonitor
+ __OBJC_METACLASS_RO_$_WiFiAwareStateMonitorConfiguration
+ __OBJC_PROTOCOL_$_WiFiAwareDatapathInfoXPC
+ __OBJC_PROTOCOL_$_WiFiAwareStateMonitorXPCDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwareDatapathInfoXPC
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwareStateMonitorXPCDelegate
+ ___30+[WiFiAwareState currentState]_block_invoke
+ ___30+[WiFiAwareState currentState]_block_invoke_2
+ ___37-[WiFiAwareDatapathInfo performance:]_block_invoke
+ ___38-[WiFiAwareStateMonitor queryNANState]_block_invoke
+ ___38-[WiFiAwareStateMonitor queryNANState]_block_invoke_2
+ ___40-[WiFiAwareStateMonitor queryNANEnabled]_block_invoke
+ ___40-[WiFiAwareStateMonitor queryNANEnabled]_block_invoke_2
+ ___47+[WiFiAwareDataPathState queryNANDataPathState]_block_invoke
+ ___47+[WiFiAwareDataPathState queryNANDataPathState]_block_invoke_2
+ ___63+[WiFiAwareDataPathState(BoldFormatting) queryNANDataPathState]_block_invoke
+ ___63+[WiFiAwareDataPathState(BoldFormatting) queryNANDataPathState]_block_invoke_2
+ ___64-[WiFiAwareState(BoldFormatting) descriptionWithChangedOptions:]_block_invoke
+ ___72-[WiFiAwareDataPathState(BoldFormatting) descriptionWithChangedOptions:]_block_invoke
+ ___79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.145
+ ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke.159
+ ___95-[WiFiAwareDatapathInfo deriveSharedSecretForProtocolName:context:derivationMethod:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e24_v16?0"WiFiAwareState"8ls32l8
+ ___block_descriptor_40_e8_32bs_e32_v16?0"WiFiAwareDataPathState"8ls32l8
+ ___block_descriptor_40_e8_32bs_e36_v16?0"<WiFiAwareDatapathInfoXPC>"8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_40_e8_32s_e41_"NSString"24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_64_e8_32s40s48bs_e36_v16?0"<WiFiAwareDatapathInfoXPC>"8ls32l8s40l8s48l8
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.220
+ ___block_literal_global.257
+ ___block_literal_global.261
+ ___block_literal_global.276
+ ___block_literal_global.372
+ ___block_literal_global.482
+ ___block_literal_global.614
+ ___block_literal_global.616
+ ___block_literal_global.618
+ _objc_msgSend$allKeys
+ _objc_msgSend$containsString:
+ _objc_msgSend$createDatapathInfoWithDatapathID:role:peerMacAddress:completion:
+ _objc_msgSend$customPreferredChannelClass
+ _objc_msgSend$customPreferredChannelNumber
+ _objc_msgSend$dataAddress
+ _objc_msgSend$deactivate
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$decodeIntForKey:
+ _objc_msgSend$deleteCharactersInRange:
+ _objc_msgSend$deriveSharedSecretForProtocolName:context:derivationMethod:completion:
+ _objc_msgSend$descriptionWithChangedOptions:
+ _objc_msgSend$dpId
+ _objc_msgSend$dpRole
+ _objc_msgSend$dpStateUpdatedHandler
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$encodeInt:forKey:
+ _objc_msgSend$establishedSessionCounter
+ _objc_msgSend$getFormattedDataPathStateDescription
+ _objc_msgSend$gtkKey
+ _objc_msgSend$igtkKey
+ _objc_msgSend$initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:multicastConfiguration:
+ _objc_msgSend$initWithDpId:dpRole:serviceId:security:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:qosType:sessionState:
+ _objc_msgSend$initWithInterfaceName:dataAddress:sessionCount:
+ _objc_msgSend$initWithInterfaceName:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfAddress:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:
+ _objc_msgSend$initWithInterfaceName:macAddress:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiDataAddressCount:ndiSessions:customPreferredChannelNumber:customPreferredChannelClass:sessionInfos:
+ _objc_msgSend$keyBlob
+ _objc_msgSend$keyExchangeOverMedium
+ _objc_msgSend$lastDataPathStateChangedOptions
+ _objc_msgSend$lastStateChangedOptions
+ _objc_msgSend$ndiSessions
+ _objc_msgSend$null
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$pairingRequestEndedForPublisher:bySubscriber:reason:
+ _objc_msgSend$peerDataAddress
+ _objc_msgSend$peerNmiMacAddress
+ _objc_msgSend$performance:
+ _objc_msgSend$publisher:getKeysBlobForMulticastSession:
+ _objc_msgSend$qosType
+ _objc_msgSend$queryNANDataPathState
+ _objc_msgSend$queryNANDataPathStateWithCompletionHandler:
+ _objc_msgSend$queryNANEnabledWithCompletionHandler:
+ _objc_msgSend$queryNANStateWithCompletionHandler:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$rtmLowLatencySessionRefCount
+ _objc_msgSend$rtmSessionRefCount
+ _objc_msgSend$rtmSessionWith24GOnlyCount
+ _objc_msgSend$security
+ _objc_msgSend$selfAddress
+ _objc_msgSend$serviceId
+ _objc_msgSend$sessionCount
+ _objc_msgSend$sessionInfos
+ _objc_msgSend$sessionState
+ _objc_msgSend$sessionWith24GOnlyPeerCount
+ _objc_msgSend$setGtkKey:
+ _objc_msgSend$setIgtkKey:
+ _objc_msgSend$setKeyBlob:
+ _objc_msgSend$setKeyExchangeOverMedium:
+ _objc_msgSend$setLastDataPathStateChangedOptions:
+ _objc_msgSend$setLastStateChangedOptions:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$startMonitoringNANStateWithConfiguration:completionHandler:
+ _objc_msgSend$stringForQosType:
+ _objc_msgSend$stringForSecurity:
+ _objc_msgSend$stringForSessionState:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$totalSessionCounter
- +[WiFiAwareDatapathPerformanceReport performanceFor:datapathType:peerMacAddress:]
- -[WiFiAwareDatapathConfiguration initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:]
- GCC_except_table42
- ___79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.137
- ___81+[WiFiAwareDatapathPerformanceReport performanceFor:datapathType:peerMacAddress:]_block_invoke
- ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke.151
- ___block_descriptor_49_e8_32s_e40_v24?0"<WiFiP2PXPCProtocol>"8?<v?>16ls32l8
- ___block_literal_global.166
- ___block_literal_global.168
- ___block_literal_global.170
- ___block_literal_global.172
- ___block_literal_global.212
- ___block_literal_global.268
- ___block_literal_global.364
- ___block_literal_global.606
- ___block_literal_global.608
- ___block_literal_global.610
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:
- _objc_msgSend$queryPerformanceReportFor:datapathType:peerMacAddress:completion:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
CStrings:
+ "\n "
+ "\n DpId=%u SrvId=%u Role=%@ "
+ "\x1b[1m%@\x1b[0m"
+ "\x1b[1m%@: %@, disabled\x1b[0m>"
+ " "
+ " DpId=%u SrvId=%u Role=%@ "
+ "%@ is currently using Continuity Real Time Group."
+ "%@ unable to connect to Continuity Real Time Group while active with another device."
+ "%@: %@, "
+ "%@: %@, %@"
+ "%@: %@, %@>"
+ "%@: %@, disabled"
+ "%@: %@, no session"
+ "%@: disabled, %@"
+ "%ld"
+ "%u"
+ "0 NDI"
+ "00:00:00:00:00:00"
+ "<"
+ "<\x1b[1m%@: %@, disabled\x1b[0m>"
+ "<%@: %@, Election=%@, Role=%@, HopCount=%ld, Cluster ID=%@,\nSelf/IM/AM-Rank(M:R)=(%ld:%ld)/%@(%ld:%ld)/%@(%ld:%ld)>"
+ "<%@: %@, disabled>"
+ "<%@: %@, election=%@, Role=%@, HopCount=%@, Cluster ID=%@,\nSelf/IM/AM-Rank(M:R)=%@(%@:%@)/%@(%@:%@)/%@(%@:%@)>"
+ "<%@: %p, options: [%@]>"
+ "<%u/%u/%u/%u/%u/%u> "
+ "<WiFiAwareDatapathConfiguration: discoveryResult=%@, serviceType=%s, passphrase=%@, pmk=%@, pmkID=%@, serviceSpecificInfo=%@, internetSharing=%@, pairingMethod=%s, pairingCaching=%s, pairSetupServiceSpecificInfo=%@>, connectionMode=%ld, pairingMetadata=%@, multicastConfiguration=%@"
+ "<WiFiAwareMulticastConfiguration: multicastAddress=%@, dynamicLinkRate=%s keyExchangeMedium=%ld>"
+ "<no state available>"
+ ">"
+ "@\"<WiFiAwareStateMonitorXPCDelegate>\""
+ "@\"NSString\"24@?0@\"NSString\"8@\"NSString\"16"
+ "@116@0:8@16q24@32@40@48@56@64q72B80@84q92@100@108"
+ "@144@0:8@16B24B28Q32q40@48@56q64q72@80q88q96@104q112q120q128Q136"
+ "@20@0:8C16"
+ "@20@0:8I16"
+ "@36@0:8@16@24I32"
+ "@72@0:8C16Q20C28C32@36@44@52I60Q64"
+ "@96@0:8@16@24B32I36I40I44I48I52I56I60@64@72@80@88"
+ "ADP"
+ "ASSOCWAIT"
+ "Anchor Master"
+ "Automatic"
+ "BoldFormatting"
+ "CACHEWAIT"
+ "CONF"
+ "CONFWAIT"
+ "CS-128"
+ "CS-256"
+ "ContinuityRealTimeGroup"
+ "CountOf Total/Est/2GOnly/RTM/RTM2GOnly/RTM-LLW= "
+ "DataPathStateUpdate"
+ "DpId=%@ SrvId=%@ Role=%@ "
+ "ESTB"
+ "F"
+ "FW"
+ "GCR: WiFiAwarePublisher.m: publishKeysBlobForMulticastSession - Received key blob from daemon: %@"
+ "GTK-128"
+ "GTK-256"
+ "HOST"
+ "INIT"
+ "Init/P-NMI/P-NDI=%@/%@/%@ "
+ "LLW"
+ "Master"
+ "Non-Master, Non-Sync"
+ "Non-Master, Sync"
+ "OPEN"
+ "Optimizing Continuity Real Time Group connection."
+ "PAIRWAIT"
+ "PASN-128"
+ "PASN-256"
+ "PK-128"
+ "PK-256"
+ "PrefChannel=%@/%@>"
+ "PrefChannel=%d/%d"
+ "PrefChannel=%d/%d\n"
+ "QoS=%@ Enc=%@ State=%@"
+ "QoS=%@ Enc=%@ State=%@\n"
+ "REESTAB"
+ "REQ"
+ "REQRECVD"
+ "REQWAIT"
+ "RESP"
+ "RSPWAIT"
+ "RTM"
+ "StateUpdate"
+ "T@\"NSArray\",&,N,V_lastDataPathStateChangedOptions"
+ "T@\"NSArray\",&,N,V_lastStateChangedOptions"
+ "T@\"NSArray\",R,N,V_ndiSessions"
+ "T@\"NSArray\",R,N,V_sessionInfos"
+ "T@\"NSData\",C,N,V_gtkKey"
+ "T@\"NSData\",C,N,V_igtkKey"
+ "T@\"NSData\",C,N,V_keyBlob"
+ "T@\"NSNumber\",R,N,V_customPreferredChannelClass"
+ "T@\"NSNumber\",R,N,V_customPreferredChannelNumber"
+ "T@\"WiFiMACAddress\",R,N,V_anchorMaster"
+ "T@\"WiFiMACAddress\",R,N,V_clusterId"
+ "T@\"WiFiMACAddress\",R,N,V_dataAddress"
+ "T@\"WiFiMACAddress\",R,N,V_immediateMaster"
+ "T@\"WiFiMACAddress\",R,N,V_peerDataAddress"
+ "T@\"WiFiMACAddress\",R,N,V_peerNmiMacAddress"
+ "T@\"WiFiMACAddress\",R,N,V_selfAddress"
+ "T@?,C,N,V_dpStateUpdatedHandler"
+ "TB,R,N,V_isFWElection"
+ "TC,R,N,V_dpId"
+ "TC,R,N,V_security"
+ "TC,R,N,V_serviceId"
+ "TEARING"
+ "TERM"
+ "TI,R,N,V_establishedSessionCounter"
+ "TI,R,N,V_ndiDataAddressCount"
+ "TI,R,N,V_qosType"
+ "TI,R,N,V_rtmLowLatencySessionRefCount"
+ "TI,R,N,V_rtmSessionRefCount"
+ "TI,R,N,V_rtmSessionWith24GOnlyCount"
+ "TI,R,N,V_sessionCount"
+ "TI,R,N,V_sessionWith24GOnlyPeerCount"
+ "TI,R,N,V_totalSessionCounter"
+ "TQ,R,N,V_dpRole"
+ "TQ,R,N,V_nanRole"
+ "TQ,R,N,V_sessionState"
+ "TQ,R,N,V_tsf"
+ "To connect Continuity Real Time Group to another device, disconnect the previous one first."
+ "To use AirPlay, disconnect Continuity Real Time Group first."
+ "To use Continuity Camera, disconnect Continuity Real Time Group first."
+ "To use Continuity Real Time Group, disconnect AirPlay first."
+ "To use Continuity Real Time Group, disconnect Continuity Camera first."
+ "To use Continuity Real Time Group, disconnect Mac Virtual Display first."
+ "To use Continuity Real Time Group, disconnect Sidecar first."
+ "To use Continuity Real Time Group, disconnect iPhone Mirroring first."
+ "To use Continuity Real Time Group, disconnect macOS Spatial Rendering first."
+ "To use Mac Virtual Display, disconnect Continuity Real Time Group first."
+ "To use Sidecar, disconnect Continuity Real Time Group first."
+ "To use iPhone Mirroring, disconnect Continuity Real Time Group first."
+ "To use macOS Spatial Rendering, disconnect Continuity Real Time Group first."
+ "Total/Est/2GOnly/RTM/RTM2GOnly/RTM-LLW=%@/%@/%@/%@/%@/%@ "
+ "Tq,N,V_keyExchangeOverMedium"
+ "Tq,R,N,V_ambtt"
+ "Tq,R,N,V_anchorMasterRankM"
+ "Tq,R,N,V_anchorMasterRankR"
+ "Tq,R,N,V_hopCount"
+ "Tq,R,N,V_immediateMasterRankM"
+ "Tq,R,N,V_immediateMasterRankR"
+ "Tq,R,N,V_selfRankM"
+ "Tq,R,N,V_selfRankR"
+ "UNKNOWN"
+ "Unable to Connect to Continuity Real Time Group"
+ "Unable to connect while the other device is active in a different Continuity Real Time Group session."
+ "Unable to connect while the other device is running Continuity Real Time Group."
+ "WiFiAwareDataPathInfoPerDataAddress"
+ "WiFiAwareDataPathSessionInfo"
+ "WiFiAwareDataPathState"
+ "WiFiAwareDataRequest.multicastConfiguration"
+ "WiFiAwareDatapathInfo"
+ "WiFiAwareDatapathInfo.PerformanceReport.durationActive"
+ "WiFiAwareDatapathInfo.PerformanceReport.localTimestamp"
+ "WiFiAwareDatapathInfo.PerformanceReport.signalStrength"
+ "WiFiAwareDatapathInfo.PerformanceReport.throughputCapacity"
+ "WiFiAwareDatapathInfo.PerformanceReport.throughputCeiling"
+ "WiFiAwareDatapathInfo.PerformanceReport.timestamp"
+ "WiFiAwareDatapathInfo.PerformanceReport.txLatency"
+ "WiFiAwareDatapathInfoXPC"
+ "WiFiAwareMulticastConfiguration.dynamicLinkRate"
+ "WiFiAwareMulticastConfiguration.gtkKey"
+ "WiFiAwareMulticastConfiguration.igtkKey"
+ "WiFiAwareMulticastConfiguration.keyBlob"
+ "WiFiAwareMulticastConfiguration.keyExchangeOverMedium"
+ "WiFiAwareMulticastConfiguration.multicastAddress"
+ "WiFiAwareState"
+ "WiFiAwareStateMonitor"
+ "WiFiAwareStateMonitorConfiguration"
+ "WiFiAwareStateMonitorXPCDelegate"
+ "["
+ "]"
+ "_ambtt"
+ "_anchorMaster"
+ "_anchorMasterRankM"
+ "_anchorMasterRankR"
+ "_clusterId"
+ "_customPreferredChannelClass"
+ "_customPreferredChannelNumber"
+ "_dataAddress"
+ "_dpId"
+ "_dpRole"
+ "_dpStateUpdatedHandler"
+ "_establishedSessionCounter"
+ "_gtkKey"
+ "_hopCount"
+ "_igtkKey"
+ "_immediateMaster"
+ "_immediateMasterRankM"
+ "_immediateMasterRankR"
+ "_isFWElection"
+ "_keyBlob"
+ "_keyExchangeOverMedium"
+ "_lastDataPathStateChangedOptions"
+ "_lastStateChangedOptions"
+ "_nanRole"
+ "_ndiDataAddressCount"
+ "_ndiSessions"
+ "_peerDataAddress"
+ "_peerMacAddress"
+ "_peerNmiMacAddress"
+ "_qosType"
+ "_remoteProxy"
+ "_role"
+ "_rtmLowLatencySessionRefCount"
+ "_rtmSessionRefCount"
+ "_rtmSessionWith24GOnlyCount"
+ "_security"
+ "_selfAddress"
+ "_selfRankM"
+ "_selfRankR"
+ "_serviceId"
+ "_sessionCount"
+ "_sessionInfos"
+ "_sessionState"
+ "_sessionWith24GOnlyPeerCount"
+ "_totalSessionCounter"
+ "_tsf"
+ "address"
+ "allKeys"
+ "ambtt"
+ "anchorMaster"
+ "anchorMasterRankM"
+ "anchorMasterRankR"
+ "clusterId"
+ "com.apple.wifip2p.WiFiAwareDatapthInfo"
+ "com.apple.wifip2p.WiFiAwareStateMonitor"
+ "compare:"
+ "containsString:"
+ "createDatapathInfoWithDatapathID:role:peerMacAddress:completion:"
+ "customPreferredChannelClass"
+ "customPreferredChannelNumber"
+ "dataAddress"
+ "decodeInt64ForKey:"
+ "decodeIntForKey:"
+ "deleteCharactersInRange:"
+ "deriveSharedSecretForProtocolName:context:derivationMethod:completion:"
+ "descriptionWithChangedOptions:"
+ "dpId"
+ "dpRole"
+ "dpStateUpdatedHandler"
+ "encodeInt64:forKey:"
+ "encodeInt:forKey:"
+ "establishedSessionCounter"
+ "getFormattedDataPathStateDescription"
+ "getFormattedDataPathStateDescription:"
+ "getFormattedStateDescription:"
+ "gtkKey"
+ "hopCount"
+ "i24@0:8Q16"
+ "igtkKey"
+ "immediateMaster"
+ "immediateMasterRankM"
+ "immediateMasterRankR"
+ "initInternal"
+ "initWithDatapathID:role:peerMacAddress:"
+ "initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:multicastConfiguration:"
+ "initWithDpId:dpRole:serviceId:security:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:qosType:sessionState:"
+ "initWithInterfaceName:dataAddress:sessionCount:"
+ "initWithInterfaceName:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfAddress:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:"
+ "initWithInterfaceName:macAddress:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiDataAddressCount:ndiSessions:customPreferredChannelNumber:customPreferredChannelClass:sessionInfos:"
+ "isFWElection"
+ "keyBlob"
+ "keyExchangeOverMedium"
+ "lastDataPathStateChangedOptions"
+ "lastStateChangedOptions"
+ "mapSessionStateToNumber:"
+ "nan0"
+ "nanRole"
+ "ndiDataAddressCount"
+ "ndiSessions"
+ "ndiSessions[%lu].dataAddress"
+ "ndiSessions[%lu].interfaceName"
+ "ndiSessions[%lu].sessionCount"
+ "no address"
+ "null"
+ "objectAtIndexedSubscript:"
+ "objectForKeyedSubscript:"
+ "pairingRequestEndedForPublisher:bySubscriber:reason:"
+ "peerDataAddress"
+ "peerNmiMacAddress"
+ "performance:"
+ "publishKeysBlobForMulticastSession:"
+ "publishPairingRequestEnded reason: %ld"
+ "publishPairingRequestEndedWithSubscriber:reason:"
+ "publisher:getKeysBlobForMulticastSession:"
+ "qosType"
+ "queryNANDataPathState"
+ "queryNANDataPathStateWithCompletionHandler:"
+ "queryNANEnabled"
+ "queryNANEnabledWithCompletionHandler:"
+ "queryNANState"
+ "queryNANStateWithCompletionHandler:"
+ "rangeOfString:"
+ "rangeOfString:options:"
+ "role"
+ "rtmLowLatencySessionRefCount"
+ "rtmSessionRefCount"
+ "rtmSessionWith24GOnlyCount"
+ "security"
+ "selfAddress"
+ "selfRankM"
+ "selfRankR"
+ "serviceId"
+ "sessionCount"
+ "sessionInfos"
+ "sessionInfos[%lu].dpId"
+ "sessionInfos[%lu].dpRole"
+ "sessionInfos[%lu].initiatorDataAddress"
+ "sessionInfos[%lu].peerDataAddress"
+ "sessionInfos[%lu].peerNmiMacAddress"
+ "sessionInfos[%lu].qosType"
+ "sessionInfos[%lu].security"
+ "sessionInfos[%lu].serviceId"
+ "sessionInfos[%lu].sessionState"
+ "sessionState"
+ "sessionWith24GOnlyPeerCount"
+ "setDpStateUpdatedHandler:"
+ "setGtkKey:"
+ "setIgtkKey:"
+ "setKeyBlob:"
+ "setKeyExchangeOverMedium:"
+ "setLastDataPathStateChangedOptions:"
+ "setLastStateChangedOptions:"
+ "setObject:forKeyedSubscript:"
+ "sortedArrayUsingSelector:"
+ "startMonitoringNANStateWithConfiguration:completionHandler:"
+ "stringForQosType:"
+ "stringForSecurity:"
+ "stringForSessionState:"
+ "substringToIndex:"
+ "totalSessionCounter"
+ "tsf"
+ "updatedNANDpState:"
+ "updatedNANDpStateWithChangedOptions:changedOptions:"
+ "updatedNANState:"
+ "updatedNANStateWithChangedOptions:changedOptions:"
+ "v12@?0B8"
+ "v16@?0@\"<WiFiAwareDatapathInfoXPC>\"8"
+ "v16@?0@\"WiFiAwareDataPathState\"8"
+ "v16@?0@\"WiFiAwareState\"8"
+ "v24@0:8@\"NSData\"16"
+ "v24@0:8@\"WiFiAwareDataPathState\"16"
+ "v24@0:8@\"WiFiAwareState\"16"
+ "v24@0:8@?<v@?@\"WiFiAwareDataPathState\">16"
+ "v24@0:8@?<v@?@\"WiFiAwareDatapathPerformanceReport\">16"
+ "v24@0:8@?<v@?@\"WiFiAwareState\">16"
+ "v24@0:8@?<v@?B>16"
+ "v32@0:8@\"WiFiAwareDataPathState\"16@\"NSArray\"24"
+ "v32@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16q24"
+ "v32@0:8@\"WiFiAwareState\"16@\"NSArray\"24"
+ "v32@0:8@\"WiFiAwareStateMonitorConfiguration\"16@?<v@?q>24"
+ "v44@0:8C16q20@\"WiFiMACAddress\"28@?<v@?q>36"
+ "v48@0:8@\"NSString\"16@\"NSString\"24q32@?<v@?@\"NSData\">40"
+ "\xd1Q"
- "<WiFiAwareDatapathConfiguration: discoveryResult=%@, serviceType=%s, passphrase=%@, pmk=%@, pmkID=%@, serviceSpecificInfo=%@, internetSharing=%@, pairingMethod=%s, pairingCaching=%s, pairSetupServiceSpecificInfo=%@>, connectionMode=%ld, pairingMetadata=%@"
- "<WiFiAwareMulticastConfiguration: multicastAddress=%@, dynamicLinkRate=%s>"
- "@108@0:8@16q24@32@40@48@56@64q72B80@84q92@100"
- "WiFiAwareDatapathPerformanceReport.durationActive"
- "WiFiAwareDatapathPerformanceReport.localTimestamp"
- "WiFiAwareDatapathPerformanceReport.signalStrength"
- "WiFiAwareDatapathPerformanceReport.throughputCapacity"
- "WiFiAwareDatapathPerformanceReport.throughputCeiling"
- "WiFiAwareDatapathPerformanceReport.timestamp"
- "WiFiAwareDatapathPerformanceReport.txLatency"
- "WiFiAwarePublishConfiguration.dynamicLinkRate"
- "initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:"
- "performanceFor:datapathType:peerMacAddress:"
- "queryPerformanceReportFor:datapathType:peerMacAddress:completion:"
- "v44@0:8C16q20@\"WiFiMACAddress\"28@?<v@?@\"WiFiAwareDatapathPerformanceReport\">36"
- "\xc1Q"

```
