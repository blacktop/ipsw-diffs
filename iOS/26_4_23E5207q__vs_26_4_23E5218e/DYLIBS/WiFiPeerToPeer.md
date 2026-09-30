## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-855.25.0.0.0
-  __TEXT.__text: 0x28fe4
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x3b5c
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x6467
-  __TEXT.__oslogstring: 0xb97
+855.30.4.1.0
+  __TEXT.__text: 0x2ef08
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0x4164
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x6b34
   __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__unwind_info: 0xab0
-  __TEXT.__objc_classname: 0x884
-  __TEXT.__objc_methname: 0x9462
-  __TEXT.__objc_methtype: 0x1e4d
-  __TEXT.__objc_stubs: 0x4a40
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0xee8
-  __DATA_CONST.__objc_classlist: 0x178
+  __TEXT.__oslogstring: 0xb97
+  __TEXT.__unwind_info: 0xbc8
+  __TEXT.__objc_classname: 0x8fa
+  __TEXT.__objc_methname: 0xa2c3
+  __TEXT.__objc_methtype: 0x20bc
+  __TEXT.__objc_stubs: 0x50a0
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x1080
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a38
+  __DATA_CONST.__objc_selrefs: 0x1c80
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x168
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x4920
-  __AUTH_CONST.__objc_const: 0x6ac0
+  __DATA_CONST.__objc_superrefs: 0x190
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x5540
+  __AUTH_CONST.__objc_const: 0x76c8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x51c
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__data: 0x9c0
   __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0x70

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32990D28-8CA3-3D22-B691-60F4CA9B1716
-  Functions: 1190
-  Symbols:   4225
-  CStrings:  2987
+  UUID: 56D708A9-1CEA-3FA8-A8A3-E3B2A74DEB27
+  Functions: 1311
+  Symbols:   4618
+  CStrings:  3345
 
Symbols:
+ +[WiFiAwareBandSchedule supportsSecureCoding]
+ +[WiFiAwareChannelSchedule supportsSecureCoding]
+ +[WiFiAwareNDIInfo supportsSecureCoding]
+ +[WiFiAwareRadioSchedule supportsSecureCoding]
+ +[WiFiAwareSrvInfo supportsSecureCoding]
+ +[WiFiAwareSrvSessionInfo supportsSecureCoding]
+ -[WiFiAwareBandSchedule .cxx_destruct]
+ -[WiFiAwareBandSchedule channels]
+ -[WiFiAwareBandSchedule copyWithZone:]
+ -[WiFiAwareBandSchedule description]
+ -[WiFiAwareBandSchedule encodeWithCoder:]
+ -[WiFiAwareBandSchedule initWithChannels:]
+ -[WiFiAwareBandSchedule initWithCoder:]
+ -[WiFiAwareChannelSchedule .cxx_destruct]
+ -[WiFiAwareChannelSchedule band]
+ -[WiFiAwareChannelSchedule bandwidth]
+ -[WiFiAwareChannelSchedule channel]
+ -[WiFiAwareChannelSchedule copyWithZone:]
+ -[WiFiAwareChannelSchedule description]
+ -[WiFiAwareChannelSchedule encodeWithCoder:]
+ -[WiFiAwareChannelSchedule initWithChannel:bandwidth:band:period:timeBitmap:]
+ -[WiFiAwareChannelSchedule initWithCoder:]
+ -[WiFiAwareChannelSchedule period]
+ -[WiFiAwareChannelSchedule timeBitmap]
+ -[WiFiAwareDataPathSessionInfo initWithDpId:dpRole:serviceId:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:sessionState:]
+ -[WiFiAwareDataPathState initWithInterfaceName:interfaceAddr:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiInfos:preferredChannelNumbers:preferredChannelClasses:ndiSessionInfos:]
+ -[WiFiAwareDataPathState interfaceAddr]
+ -[WiFiAwareDataPathState ndiInfos]
+ -[WiFiAwareDataPathState ndiSessionInfos]
+ -[WiFiAwareDataPathState preferredChannelClasses]
+ -[WiFiAwareDataPathState preferredChannelNumbers]
+ -[WiFiAwareDataPathState(BoldFormatting) descriptionWithChangedOptions:forceAllChangedOptions:]
+ -[WiFiAwareNDIInfo .cxx_destruct]
+ -[WiFiAwareNDIInfo copyWithZone:]
+ -[WiFiAwareNDIInfo encodeWithCoder:]
+ -[WiFiAwareNDIInfo initWithCoder:]
+ -[WiFiAwareNDIInfo initWithNdiName:ndiAddr:sessionCount:security:qosType:]
+ -[WiFiAwareNDIInfo init]
+ -[WiFiAwareNDIInfo ndiAddr]
+ -[WiFiAwareNDIInfo ndiName]
+ -[WiFiAwareNDIInfo qosType]
+ -[WiFiAwareNDIInfo security]
+ -[WiFiAwareNDIInfo sessionCount]
+ -[WiFiAwareRadioSchedule .cxx_destruct]
+ -[WiFiAwareRadioSchedule band24GHz]
+ -[WiFiAwareRadioSchedule band5GHz]
+ -[WiFiAwareRadioSchedule copyWithZone:]
+ -[WiFiAwareRadioSchedule description]
+ -[WiFiAwareRadioSchedule encodeWithCoder:]
+ -[WiFiAwareRadioSchedule infraChannelClass]
+ -[WiFiAwareRadioSchedule infraChannel]
+ -[WiFiAwareRadioSchedule initWithCoder:]
+ -[WiFiAwareRadioSchedule initWithInterfaceName:interfaceAddr:isEnabled:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannelsCount:preferredChannelNumbers:]
+ -[WiFiAwareRadioSchedule init]
+ -[WiFiAwareRadioSchedule interfaceAddr]
+ -[WiFiAwareRadioSchedule interfaceName]
+ -[WiFiAwareRadioSchedule isEnabled]
+ -[WiFiAwareRadioSchedule preferredChannelClasses]
+ -[WiFiAwareRadioSchedule preferredChannelNumbers]
+ -[WiFiAwareRadioSchedule preferredChannelsCount]
+ -[WiFiAwareRadioSchedule primaryChannelClass]
+ -[WiFiAwareRadioSchedule primaryChannel]
+ -[WiFiAwareRadioSchedule secondaryChannelClass]
+ -[WiFiAwareRadioSchedule secondaryChannel]
+ -[WiFiAwareRadioSchedule setInterfaceAddr:]
+ -[WiFiAwareRadioSchedule setInterfaceName:]
+ -[WiFiAwareRadioSchedule setIsEnabled:]
+ -[WiFiAwareRadioSchedule supportsDualBand]
+ -[WiFiAwareRadioSchedule supportsSimultaneousDualBand]
+ -[WiFiAwareRadioSchedule(DetailedDescription) detailedDescriptionWithChangedOptions:previousSchedule:]
+ -[WiFiAwareRadioSchedule(DetailedDescription) detailedDescriptionWithChangedOptions:previousSchedule:forceAllChangedOptions:]
+ -[WiFiAwareSrvInfo .cxx_destruct]
+ -[WiFiAwareSrvInfo copyWithZone:]
+ -[WiFiAwareSrvInfo description]
+ -[WiFiAwareSrvInfo encodeWithCoder:]
+ -[WiFiAwareSrvInfo initWithCoder:]
+ -[WiFiAwareSrvInfo initWithInterfaceName:interfaceAddr:isEnabled:publishServiceCount:subscribeServiceCount:srvSessionCount:srvSessionInfos:]
+ -[WiFiAwareSrvInfo init]
+ -[WiFiAwareSrvInfo interfaceAddr]
+ -[WiFiAwareSrvInfo interfaceName]
+ -[WiFiAwareSrvInfo isEnabled]
+ -[WiFiAwareSrvInfo publishServiceCount]
+ -[WiFiAwareSrvInfo srvSessionCount]
+ -[WiFiAwareSrvInfo srvSessionInfos]
+ -[WiFiAwareSrvInfo subscribeServiceCount]
+ -[WiFiAwareSrvInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousSrvInfo:]
+ -[WiFiAwareSrvSessionInfo .cxx_destruct]
+ -[WiFiAwareSrvSessionInfo copyWithZone:]
+ -[WiFiAwareSrvSessionInfo description]
+ -[WiFiAwareSrvSessionInfo encodeWithCoder:]
+ -[WiFiAwareSrvSessionInfo initWithCoder:]
+ -[WiFiAwareSrvSessionInfo initWithSrvId:srvType:srvName:srvHash:ndiInfos:numofPeers:]
+ -[WiFiAwareSrvSessionInfo ndiInfos]
+ -[WiFiAwareSrvSessionInfo numofPeers]
+ -[WiFiAwareSrvSessionInfo srvHash]
+ -[WiFiAwareSrvSessionInfo srvId]
+ -[WiFiAwareSrvSessionInfo srvName]
+ -[WiFiAwareSrvSessionInfo srvType]
+ -[WiFiAwareState initWithInterfaceName:interfaceAddr:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:]
+ -[WiFiAwareState interfaceAddr]
+ -[WiFiAwareState(BoldFormatting) descriptionWithChangedOptions:forceAllChangedOptions:]
+ -[WiFiAwareStateMonitor availUpdatedHandler]
+ -[WiFiAwareStateMonitor beginAvailabilityMonitoring]
+ -[WiFiAwareStateMonitor beginDataPathMonitoring]
+ -[WiFiAwareStateMonitor beginSrvInfoMonitoring]
+ -[WiFiAwareStateMonitor endAvailabilityMonitoring]
+ -[WiFiAwareStateMonitor endDataPathMonitoring]
+ -[WiFiAwareStateMonitor endSrvInfoMonitoring]
+ -[WiFiAwareStateMonitor getFormattedRadioScheduleDescription:]
+ -[WiFiAwareStateMonitor getFormattedSrvInfoDescription:]
+ -[WiFiAwareStateMonitor lastRadioScheduleChangedOptions]
+ -[WiFiAwareStateMonitor lastRadioSchedule]
+ -[WiFiAwareStateMonitor lastSrvInfoChangedOptions]
+ -[WiFiAwareStateMonitor lastSrvInfo]
+ -[WiFiAwareStateMonitor queryNANAvail]
+ -[WiFiAwareStateMonitor queryNANSrv]
+ -[WiFiAwareStateMonitor setAvailUpdatedHandler:]
+ -[WiFiAwareStateMonitor setLastRadioSchedule:]
+ -[WiFiAwareStateMonitor setLastRadioScheduleChangedOptions:]
+ -[WiFiAwareStateMonitor setLastSrvInfo:]
+ -[WiFiAwareStateMonitor setLastSrvInfoChangedOptions:]
+ -[WiFiAwareStateMonitor setSrvInfoUpdatedHandler:]
+ -[WiFiAwareStateMonitor srvInfoUpdatedHandler]
+ -[WiFiAwareStateMonitor updatedNANAvailability:]
+ -[WiFiAwareStateMonitor updatedNANAvailabilityWithChangedOptions:changedOptions:]
+ -[WiFiAwareStateMonitor updatedNANAvailabilityWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiAwareStateMonitor updatedNANDpStateWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiAwareStateMonitor updatedNANSrvInfo:]
+ -[WiFiAwareStateMonitor updatedNANSrvInfoWithChangedOptions:changedOptions:]
+ -[WiFiAwareStateMonitor updatedNANSrvInfoWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiAwareStateMonitor updatedNANStateWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ _OBJC_CLASS_$_WiFiAwareBandSchedule
+ _OBJC_CLASS_$_WiFiAwareChannelSchedule
+ _OBJC_CLASS_$_WiFiAwareNDIInfo
+ _OBJC_CLASS_$_WiFiAwareRadioSchedule
+ _OBJC_CLASS_$_WiFiAwareSrvInfo
+ _OBJC_CLASS_$_WiFiAwareSrvSessionInfo
+ _OBJC_IVAR_$_WiFiAwareBandSchedule._channels
+ _OBJC_IVAR_$_WiFiAwareChannelSchedule._band
+ _OBJC_IVAR_$_WiFiAwareChannelSchedule._bandwidth
+ _OBJC_IVAR_$_WiFiAwareChannelSchedule._channel
+ _OBJC_IVAR_$_WiFiAwareChannelSchedule._period
+ _OBJC_IVAR_$_WiFiAwareChannelSchedule._timeBitmap
+ _OBJC_IVAR_$_WiFiAwareDataPathState._interfaceAddr
+ _OBJC_IVAR_$_WiFiAwareDataPathState._ndiInfos
+ _OBJC_IVAR_$_WiFiAwareDataPathState._ndiSessionInfos
+ _OBJC_IVAR_$_WiFiAwareDataPathState._preferredChannelClasses
+ _OBJC_IVAR_$_WiFiAwareDataPathState._preferredChannelNumbers
+ _OBJC_IVAR_$_WiFiAwareNDIInfo._ndiAddr
+ _OBJC_IVAR_$_WiFiAwareNDIInfo._ndiName
+ _OBJC_IVAR_$_WiFiAwareNDIInfo._qosType
+ _OBJC_IVAR_$_WiFiAwareNDIInfo._security
+ _OBJC_IVAR_$_WiFiAwareNDIInfo._sessionCount
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._band24GHz
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._band5GHz
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._infraChannel
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._infraChannelClass
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._interfaceAddr
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._interfaceName
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._isEnabled
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._preferredChannelClasses
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._preferredChannelNumbers
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._preferredChannelsCount
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._primaryChannel
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._primaryChannelClass
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._secondaryChannel
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._secondaryChannelClass
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._supportsDualBand
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._supportsSimultaneousDualBand
+ _OBJC_IVAR_$_WiFiAwareSrvInfo._interfaceAddr
+ _OBJC_IVAR_$_WiFiAwareSrvInfo._interfaceName
+ _OBJC_IVAR_$_WiFiAwareSrvInfo._isEnabled
+ _OBJC_IVAR_$_WiFiAwareSrvInfo._publishServiceCount
+ _OBJC_IVAR_$_WiFiAwareSrvInfo._srvSessionCount
+ _OBJC_IVAR_$_WiFiAwareSrvInfo._srvSessionInfos
+ _OBJC_IVAR_$_WiFiAwareSrvInfo._subscribeServiceCount
+ _OBJC_IVAR_$_WiFiAwareSrvSessionInfo._ndiInfos
+ _OBJC_IVAR_$_WiFiAwareSrvSessionInfo._numofPeers
+ _OBJC_IVAR_$_WiFiAwareSrvSessionInfo._srvHash
+ _OBJC_IVAR_$_WiFiAwareSrvSessionInfo._srvId
+ _OBJC_IVAR_$_WiFiAwareSrvSessionInfo._srvName
+ _OBJC_IVAR_$_WiFiAwareSrvSessionInfo._srvType
+ _OBJC_IVAR_$_WiFiAwareState._interfaceAddr
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._availUpdatedHandler
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastRadioSchedule
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastRadioScheduleChangedOptions
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastSrvInfo
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastSrvInfoChangedOptions
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._srvInfoUpdatedHandler
+ _OBJC_METACLASS_$_WiFiAwareBandSchedule
+ _OBJC_METACLASS_$_WiFiAwareChannelSchedule
+ _OBJC_METACLASS_$_WiFiAwareNDIInfo
+ _OBJC_METACLASS_$_WiFiAwareRadioSchedule
+ _OBJC_METACLASS_$_WiFiAwareSrvInfo
+ _OBJC_METACLASS_$_WiFiAwareSrvSessionInfo
+ _WiFiAwareQoSTypeToString
+ _WiFiAwareSecurityTypeToString
+ __OBJC_$_CLASS_METHODS_WiFiAwareBandSchedule
+ __OBJC_$_CLASS_METHODS_WiFiAwareChannelSchedule
+ __OBJC_$_CLASS_METHODS_WiFiAwareNDIInfo
+ __OBJC_$_CLASS_METHODS_WiFiAwareRadioSchedule
+ __OBJC_$_CLASS_METHODS_WiFiAwareSrvInfo
+ __OBJC_$_CLASS_METHODS_WiFiAwareSrvSessionInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareBandSchedule
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareChannelSchedule
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareNDIInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareRadioSchedule
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareSrvInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareSrvSessionInfo
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareBandSchedule
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareChannelSchedule
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareNDIInfo
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareRadioSchedule(DetailedDescription)
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareSrvInfo(DetailedDescription)
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareSrvSessionInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareBandSchedule
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareChannelSchedule
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareNDIInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareRadioSchedule
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareSrvInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareSrvSessionInfo
+ __OBJC_$_PROP_LIST_WiFiAwareBandSchedule
+ __OBJC_$_PROP_LIST_WiFiAwareChannelSchedule
+ __OBJC_$_PROP_LIST_WiFiAwareNDIInfo
+ __OBJC_$_PROP_LIST_WiFiAwareRadioSchedule
+ __OBJC_$_PROP_LIST_WiFiAwareSrvInfo
+ __OBJC_$_PROP_LIST_WiFiAwareSrvSessionInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareBandSchedule
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareChannelSchedule
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareNDIInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareRadioSchedule
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareSrvInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareSrvSessionInfo
+ __OBJC_CLASS_RO_$_WiFiAwareBandSchedule
+ __OBJC_CLASS_RO_$_WiFiAwareChannelSchedule
+ __OBJC_CLASS_RO_$_WiFiAwareNDIInfo
+ __OBJC_CLASS_RO_$_WiFiAwareRadioSchedule
+ __OBJC_CLASS_RO_$_WiFiAwareSrvInfo
+ __OBJC_CLASS_RO_$_WiFiAwareSrvSessionInfo
+ __OBJC_METACLASS_RO_$_WiFiAwareBandSchedule
+ __OBJC_METACLASS_RO_$_WiFiAwareChannelSchedule
+ __OBJC_METACLASS_RO_$_WiFiAwareNDIInfo
+ __OBJC_METACLASS_RO_$_WiFiAwareRadioSchedule
+ __OBJC_METACLASS_RO_$_WiFiAwareSrvInfo
+ __OBJC_METACLASS_RO_$_WiFiAwareSrvSessionInfo
+ ___125-[WiFiAwareRadioSchedule(DetailedDescription) detailedDescriptionWithChangedOptions:previousSchedule:forceAllChangedOptions:]_block_invoke
+ ___125-[WiFiAwareRadioSchedule(DetailedDescription) detailedDescriptionWithChangedOptions:previousSchedule:forceAllChangedOptions:]_block_invoke_2
+ ___36-[WiFiAwareStateMonitor queryNANSrv]_block_invoke
+ ___36-[WiFiAwareStateMonitor queryNANSrv]_block_invoke_2
+ ___38-[WiFiAwareStateMonitor queryNANAvail]_block_invoke
+ ___38-[WiFiAwareStateMonitor queryNANAvail]_block_invoke_2
+ ___79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.149
+ ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke.163
+ ___87-[WiFiAwareState(BoldFormatting) descriptionWithChangedOptions:forceAllChangedOptions:]_block_invoke
+ ___95-[WiFiAwareDataPathState(BoldFormatting) descriptionWithChangedOptions:forceAllChangedOptions:]_block_invoke
+ ___95-[WiFiAwareSrvInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousSrvInfo:]_block_invoke
+ ___95-[WiFiAwareSrvInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousSrvInfo:]_block_invoke_2
+ ___95-[WiFiAwareSrvInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousSrvInfo:]_block_invoke_3
+ ___95-[WiFiAwareSrvInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousSrvInfo:]_block_invoke_4
+ ___block_descriptor_40_e8_32bs_e26_v16?0"WiFiAwareSrvInfo"8ls32l8
+ ___block_descriptor_40_e8_32bs_e32_v16?0"WiFiAwareRadioSchedule"8ls32l8
+ ___block_descriptor_40_e8_32bs_e41_"NSString"24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_41_e8_32bs_e41_"NSString"24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_41_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_41_e8_32s_e41_"NSString"24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e46_B24?0"WiFiAwareSrvSessionInfo"8"NSString"16ls40l8s32l8
+ ___block_literal_global.184
+ ___block_literal_global.186
+ ___block_literal_global.224
+ ___block_literal_global.280
+ ___block_literal_global.283
+ ___block_literal_global.286
+ ___block_literal_global.376
+ ___block_literal_global.529
+ ___block_literal_global.620
+ ___block_literal_global.622
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$availUpdatedHandler
+ _objc_msgSend$band
+ _objc_msgSend$band24GHz
+ _objc_msgSend$band5GHz
+ _objc_msgSend$beginMonitoring
+ _objc_msgSend$channel
+ _objc_msgSend$channels
+ _objc_msgSend$descriptionWithChangedOptions:forceAllChangedOptions:
+ _objc_msgSend$detailedDescriptionWithChangedOptions:previousSchedule:forceAllChangedOptions:
+ _objc_msgSend$detailedDescriptionWithChangedOptions:previousSrvInfo:
+ _objc_msgSend$endMonitoring
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$infraChannel
+ _objc_msgSend$initWithChannel:bandwidth:band:period:timeBitmap:
+ _objc_msgSend$initWithChannels:
+ _objc_msgSend$initWithDpId:dpRole:serviceId:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:sessionState:
+ _objc_msgSend$initWithInterfaceName:interfaceAddr:isEnabled:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannelsCount:preferredChannelNumbers:
+ _objc_msgSend$initWithInterfaceName:interfaceAddr:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:
+ _objc_msgSend$initWithInterfaceName:interfaceAddr:isEnabled:publishServiceCount:subscribeServiceCount:srvSessionCount:srvSessionInfos:
+ _objc_msgSend$initWithInterfaceName:interfaceAddr:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiInfos:preferredChannelNumbers:preferredChannelClasses:ndiSessionInfos:
+ _objc_msgSend$initWithNdiName:ndiAddr:sessionCount:security:qosType:
+ _objc_msgSend$initWithSrvId:srvType:srvName:srvHash:ndiInfos:numofPeers:
+ _objc_msgSend$interfaceAddr
+ _objc_msgSend$lastRadioSchedule
+ _objc_msgSend$lastRadioScheduleChangedOptions
+ _objc_msgSend$lastSrvInfo
+ _objc_msgSend$lastSrvInfoChangedOptions
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$ndiAddr
+ _objc_msgSend$ndiInfos
+ _objc_msgSend$ndiName
+ _objc_msgSend$ndiSessionInfos
+ _objc_msgSend$numofPeers
+ _objc_msgSend$period
+ _objc_msgSend$preferredChannelClasses
+ _objc_msgSend$preferredChannelNumbers
+ _objc_msgSend$preferredChannelsCount
+ _objc_msgSend$primaryChannel
+ _objc_msgSend$queryNANAvailWithCompletionHandler:
+ _objc_msgSend$queryNANSrvWithCompletionHandler:
+ _objc_msgSend$secondaryChannel
+ _objc_msgSend$setLastRadioSchedule:
+ _objc_msgSend$setLastRadioScheduleChangedOptions:
+ _objc_msgSend$setLastSrvInfo:
+ _objc_msgSend$setLastSrvInfoChangedOptions:
+ _objc_msgSend$srvHash
+ _objc_msgSend$srvId
+ _objc_msgSend$srvInfoUpdatedHandler
+ _objc_msgSend$srvName
+ _objc_msgSend$srvSessionInfos
+ _objc_msgSend$srvType
+ _objc_msgSend$stringValue
+ _objc_msgSend$supportsDualBand
+ _objc_msgSend$supportsSimultaneousDualBand
+ _objc_msgSend$timeBitmap
+ _objc_msgSend$updatedNANAvailabilityWithChangedOptions:changedOptions:
+ _objc_msgSend$updatedNANDpStateWithChangedOptions:changedOptions:
+ _objc_msgSend$updatedNANSrvInfoWithChangedOptions:changedOptions:
+ _objc_msgSend$updatedNANStateWithChangedOptions:changedOptions:
+ _objc_opt_new
- +[WiFiAwareDataPathInfoPerDataAddress supportsSecureCoding]
- -[WiFiAwareDataPathInfoPerDataAddress .cxx_destruct]
- -[WiFiAwareDataPathInfoPerDataAddress copyWithZone:]
- -[WiFiAwareDataPathInfoPerDataAddress dataAddress]
- -[WiFiAwareDataPathInfoPerDataAddress encodeWithCoder:]
- -[WiFiAwareDataPathInfoPerDataAddress initWithCoder:]
- -[WiFiAwareDataPathInfoPerDataAddress initWithInterfaceName:dataAddress:sessionCount:]
- -[WiFiAwareDataPathInfoPerDataAddress init]
- -[WiFiAwareDataPathInfoPerDataAddress interfaceName]
- -[WiFiAwareDataPathInfoPerDataAddress sessionCount]
- -[WiFiAwareDataPathSessionInfo initWithDpId:dpRole:serviceId:security:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:qosType:sessionState:]
- -[WiFiAwareDataPathSessionInfo qosType]
- -[WiFiAwareDataPathSessionInfo security]
- -[WiFiAwareDataPathState customPreferredChannelClass]
- -[WiFiAwareDataPathState customPreferredChannelNumber]
- -[WiFiAwareDataPathState initWithInterfaceName:macAddress:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiDataAddressCount:ndiSessions:customPreferredChannelNumber:customPreferredChannelClass:sessionInfos:]
- -[WiFiAwareDataPathState macAddress]
- -[WiFiAwareDataPathState ndiDataAddressCount]
- -[WiFiAwareDataPathState ndiSessions]
- -[WiFiAwareDataPathState sessionInfos]
- -[WiFiAwareState initWithInterfaceName:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfAddress:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:]
- -[WiFiAwareState selfAddress]
- _OBJC_CLASS_$_WiFiAwareDataPathInfoPerDataAddress
- _OBJC_IVAR_$_WiFiAwareDataPathInfoPerDataAddress._dataAddress
- _OBJC_IVAR_$_WiFiAwareDataPathInfoPerDataAddress._interfaceName
- _OBJC_IVAR_$_WiFiAwareDataPathInfoPerDataAddress._sessionCount
- _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._qosType
- _OBJC_IVAR_$_WiFiAwareDataPathSessionInfo._security
- _OBJC_IVAR_$_WiFiAwareDataPathState._customPreferredChannelClass
- _OBJC_IVAR_$_WiFiAwareDataPathState._customPreferredChannelNumber
- _OBJC_IVAR_$_WiFiAwareDataPathState._macAddress
- _OBJC_IVAR_$_WiFiAwareDataPathState._ndiDataAddressCount
- _OBJC_IVAR_$_WiFiAwareDataPathState._ndiSessions
- _OBJC_IVAR_$_WiFiAwareDataPathState._sessionInfos
- _OBJC_IVAR_$_WiFiAwareState._selfAddress
- _OBJC_METACLASS_$_WiFiAwareDataPathInfoPerDataAddress
- __OBJC_$_CLASS_METHODS_WiFiAwareDataPathInfoPerDataAddress
- __OBJC_$_CLASS_PROP_LIST_WiFiAwareDataPathInfoPerDataAddress
- __OBJC_$_INSTANCE_METHODS_WiFiAwareDataPathInfoPerDataAddress
- __OBJC_$_INSTANCE_VARIABLES_WiFiAwareDataPathInfoPerDataAddress
- __OBJC_$_PROP_LIST_WiFiAwareDataPathInfoPerDataAddress
- __OBJC_CLASS_PROTOCOLS_$_WiFiAwareDataPathInfoPerDataAddress
- __OBJC_CLASS_RO_$_WiFiAwareDataPathInfoPerDataAddress
- __OBJC_METACLASS_RO_$_WiFiAwareDataPathInfoPerDataAddress
- ___64-[WiFiAwareState(BoldFormatting) descriptionWithChangedOptions:]_block_invoke
- ___72-[WiFiAwareDataPathState(BoldFormatting) descriptionWithChangedOptions:]_block_invoke
- ___79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.145
- ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke.159
- ___block_descriptor_40_e8_32s_e41_"NSString"24?0"NSString"8"NSString"16ls32l8
- ___block_literal_global.174
- ___block_literal_global.176
- ___block_literal_global.220
- ___block_literal_global.257
- ___block_literal_global.261
- ___block_literal_global.372
- ___block_literal_global.482
- ___block_literal_global.614
- ___block_literal_global.616
- _objc_msgSend$customPreferredChannelClass
- _objc_msgSend$customPreferredChannelNumber
- _objc_msgSend$dataAddress
- _objc_msgSend$initWithDpId:dpRole:serviceId:security:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:qosType:sessionState:
- _objc_msgSend$initWithInterfaceName:dataAddress:sessionCount:
- _objc_msgSend$initWithInterfaceName:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfAddress:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:
- _objc_msgSend$initWithInterfaceName:macAddress:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiDataAddressCount:ndiSessions:customPreferredChannelNumber:customPreferredChannelClass:sessionInfos:
- _objc_msgSend$ndiSessions
- _objc_msgSend$selfAddress
- _objc_msgSend$sessionInfos
CStrings:
+ "\n    %@"
+ "\n    %@ (%@, Security=%@, QoS=%@)"
+ "\n  NDI Addresses:"
+ "\n  Service Sessions:"
+ "\f"
+ "\x1b[1m%@\x1b[0m%@ "
+ "\x1b[1m%u\x1b[0m"
+ "\x1b[1m<no radio schedule>\x1b[0m"
+ "\x1b[1m<no service info>\x1b[0m"
+ "\x1b[1m<no state available>\x1b[0m"
+ "    Dual Band: %@\n"
+ "    Infrastructure Channel: %@\n"
+ "    Preferred Channels Count: %u\n"
+ "    Primary Channel: %@\n"
+ "    Secondary Channel: %@\n"
+ "    Simultaneous Dual Band: %@\n"
+ "  2.4GHz: %lu channels\n"
+ "  5GHz: %lu channels"
+ "  Global Parameters:\n"
+ " Total/Est/2GOnly/RTM/RTM2GOnly/RTM-LLW=<%u/%u/%u/%u/%u/%u> "
+ "\""
+ "%02X"
+ "%@%@ "
+ "%@: %@, %@, "
+ "%d/%d"
+ "++"
+ "+++"
+ "++="
+ ",\n"
+ ", NDIs=%lu"
+ ", Security%lu=%@"
+ ", Security=%@"
+ "---"
+ "--:--:--:--:--:--"
+ "-0-"
+ "/"
+ "0"
+ "0 NDI, "
+ "2.4GHz"
+ "2G"
+ "5G"
+ "5GHz"
+ "6G"
+ "<%@: %@, Publishers=%u, Subscribers=%u, Sessions=%u"
+ "<%@: %@, pub=%@, sub=%@"
+ "<Map%ld %@"
+ "<no radio schedule>"
+ "<no service info>"
+ ">\n"
+ "@\"WiFiAwareBandSchedule\""
+ "@\"WiFiAwareRadioSchedule\""
+ "@\"WiFiAwareSrvInfo\""
+ "@144@0:8@16@24B32B36Q40q48@56q64q72@80q88q96@104q112q120q128Q136"
+ "@40@0:8I16I20I24I28@32"
+ "@44@0:8@16@24I32C36I40"
+ "@56@0:8@16@24B32I36I40I44@48"
+ "@56@0:8C16Q20@28@36@44I52"
+ "@64@0:8C16Q20C28@32@40@48Q56"
+ "@92@0:8@16@24B32I36I40I44I48I52I56@60@68@76@84"
+ "@96@0:8@16@24B32@36@44B52B56@60@68@76I84@88"
+ "B16@?0@\"NSString\"8"
+ "B24@?0@\"WiFiAwareSrvSessionInfo\"8@\"NSString\"16"
+ "BandSchedule: %lu channels"
+ "Channel %u, %uMHz, %@, Period=%uTU, Slots=%@"
+ "DB=%@ SDB=%@ Supp.Bands=%@ Pri/Sec/Infra Ch=%@/%@/%@ Pref.Ch=%@"
+ "DetailedDescription"
+ "GTKGCMP128"
+ "GTKGCMP256"
+ "InstId=%@ Type=%@ Hash=%@ NDI=%@ Peers=%@ QoS=%@ Enc=%@ Srv=%@"
+ "Invalid"
+ "No"
+ "None"
+ "Open"
+ "PUB"
+ "Pref.Ch/Class=%@/%@>"
+ "Pref.Ch/Class==%@/%@>"
+ "Pref.Ch=%@"
+ "Pref.Ch=0"
+ "PrefChannel/Class=%@"
+ "PrefChannel/Class=none"
+ "PrefChannels=%@"
+ "PrefChannels=none"
+ "SUB"
+ "SrvID=%u, Type=%@, Name=\"%@\", Hash=%@, Peers=%u"
+ "T@\"NSArray\",&,N,V_lastRadioScheduleChangedOptions"
+ "T@\"NSArray\",&,N,V_lastSrvInfoChangedOptions"
+ "T@\"NSArray\",R,N,V_channels"
+ "T@\"NSArray\",R,N,V_ndiInfos"
+ "T@\"NSArray\",R,N,V_ndiSessionInfos"
+ "T@\"NSArray\",R,N,V_preferredChannelClasses"
+ "T@\"NSArray\",R,N,V_preferredChannelNumbers"
+ "T@\"NSArray\",R,N,V_srvSessionInfos"
+ "T@\"NSData\",R,N,V_srvHash"
+ "T@\"NSData\",R,N,V_timeBitmap"
+ "T@\"NSNumber\",R,N,V_infraChannel"
+ "T@\"NSNumber\",R,N,V_infraChannelClass"
+ "T@\"NSNumber\",R,N,V_primaryChannel"
+ "T@\"NSNumber\",R,N,V_primaryChannelClass"
+ "T@\"NSNumber\",R,N,V_secondaryChannel"
+ "T@\"NSNumber\",R,N,V_secondaryChannelClass"
+ "T@\"NSString\",C,N,V_interfaceName"
+ "T@\"NSString\",R,N,V_ndiName"
+ "T@\"NSString\",R,N,V_srvName"
+ "T@\"WiFiAwareBandSchedule\",R,N,V_band24GHz"
+ "T@\"WiFiAwareBandSchedule\",R,N,V_band5GHz"
+ "T@\"WiFiAwareRadioSchedule\",&,N,V_lastRadioSchedule"
+ "T@\"WiFiAwareSrvInfo\",&,N,V_lastSrvInfo"
+ "T@\"WiFiMACAddress\",C,N,V_interfaceAddr"
+ "T@\"WiFiMACAddress\",R,N,V_interfaceAddr"
+ "T@\"WiFiMACAddress\",R,N,V_ndiAddr"
+ "T@?,C,N,V_availUpdatedHandler"
+ "T@?,C,N,V_srvInfoUpdatedHandler"
+ "TB,N,V_isEnabled"
+ "TB,R,N,V_supportsDualBand"
+ "TB,R,N,V_supportsSimultaneousDualBand"
+ "TC,R,N,V_srvId"
+ "TI,R,N,V_band"
+ "TI,R,N,V_bandwidth"
+ "TI,R,N,V_channel"
+ "TI,R,N,V_numofPeers"
+ "TI,R,N,V_period"
+ "TI,R,N,V_preferredChannelsCount"
+ "TI,R,N,V_publishServiceCount"
+ "TI,R,N,V_srvSessionCount"
+ "TI,R,N,V_subscribeServiceCount"
+ "TQ,R,N,V_srvType"
+ "Total/Est/2GOnly/RTM/RTM2GOnly/RTM-LLW=<%u/%u/%u/%u/%u/%u> "
+ "UNK"
+ "UNK(%d)"
+ "UNK(%u)"
+ "Unknown"
+ "Unknown(%u)"
+ "WiFiAwareBandSchedule"
+ "WiFiAwareChannelSchedule"
+ "WiFiAwareNDIInfo"
+ "WiFiAwareRadioSchedule"
+ "WiFiAwareRadioSchedule:\n"
+ "WiFiAwareSrvInfo"
+ "WiFiAwareSrvSessionInfo"
+ "Yes"
+ "_availUpdatedHandler"
+ "_band"
+ "_band24GHz"
+ "_band5GHz"
+ "_channel"
+ "_channels"
+ "_infraChannel"
+ "_infraChannelClass"
+ "_interfaceAddr"
+ "_lastRadioSchedule"
+ "_lastRadioScheduleChangedOptions"
+ "_lastSrvInfo"
+ "_lastSrvInfoChangedOptions"
+ "_ndiAddr"
+ "_ndiInfos"
+ "_ndiName"
+ "_ndiSessionInfos"
+ "_numofPeers"
+ "_period"
+ "_preferredChannelClasses"
+ "_preferredChannelNumbers"
+ "_preferredChannelsCount"
+ "_primaryChannel"
+ "_primaryChannelClass"
+ "_publishServiceCount"
+ "_secondaryChannel"
+ "_secondaryChannelClass"
+ "_srvHash"
+ "_srvId"
+ "_srvInfoUpdatedHandler"
+ "_srvName"
+ "_srvSessionCount"
+ "_srvSessionInfos"
+ "_srvType"
+ "_subscribeServiceCount"
+ "_supportsDualBand"
+ "_supportsSimultaneousDualBand"
+ "_timeBitmap"
+ "arrayWithCapacity:"
+ "availUpdatedHandler"
+ "band"
+ "band24GHz"
+ "band5GHz"
+ "beginAvailabilityMonitoring"
+ "beginDataPathMonitoring"
+ "beginSrvInfoMonitoring"
+ "channel"
+ "channels"
+ "descriptionWithChangedOptions:forceAllChangedOptions:"
+ "detailedDescriptionWithChangedOptions:previousSchedule:"
+ "detailedDescriptionWithChangedOptions:previousSchedule:forceAllChangedOptions:"
+ "detailedDescriptionWithChangedOptions:previousSrvInfo:"
+ "endAvailabilityMonitoring"
+ "endDataPathMonitoring"
+ "endSrvInfoMonitoring"
+ "getFormattedRadioScheduleDescription:"
+ "getFormattedSrvInfoDescription:"
+ "hasPrefix:"
+ "hasSuffix:"
+ "infraChannel"
+ "infraChannelClass"
+ "initWithChannel:bandwidth:band:period:timeBitmap:"
+ "initWithChannels:"
+ "initWithDpId:dpRole:serviceId:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:sessionState:"
+ "initWithInterfaceName:interfaceAddr:isEnabled:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannelsCount:preferredChannelNumbers:"
+ "initWithInterfaceName:interfaceAddr:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:"
+ "initWithInterfaceName:interfaceAddr:isEnabled:publishServiceCount:subscribeServiceCount:srvSessionCount:srvSessionInfos:"
+ "initWithInterfaceName:interfaceAddr:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiInfos:preferredChannelNumbers:preferredChannelClasses:ndiSessionInfos:"
+ "initWithNdiName:ndiAddr:sessionCount:security:qosType:"
+ "initWithSrvId:srvType:srvName:srvHash:ndiInfos:numofPeers:"
+ "interfaceAddr"
+ "lastRadioSchedule"
+ "lastRadioScheduleChangedOptions"
+ "lastSrvInfo"
+ "lastSrvInfoChangedOptions"
+ "mutableCopy"
+ "ndi%lu: %@, "
+ "ndiAddr"
+ "ndiInfos"
+ "ndiInfos[%lu].ndiName"
+ "ndiInfos[%lu].sessionCount"
+ "ndiName"
+ "ndiSessionInfos"
+ "ndiSessionInfos[%lu].dpId"
+ "ndiSessionInfos[%lu].dpRole"
+ "ndiSessionInfos[%lu].initiatorDataAddress"
+ "ndiSessionInfos[%lu].peerDataAddress"
+ "ndiSessionInfos[%lu].peerNmiMacAddress"
+ "ndiSessionInfos[%lu].qosType"
+ "ndiSessionInfos[%lu].security"
+ "ndiSessionInfos[%lu].serviceId"
+ "ndiSessionInfos[%lu].sessionState"
+ "numofPeers"
+ "period"
+ "preferredChannelClasses"
+ "preferredChannelNumbers"
+ "preferredChannelsCount"
+ "primaryChannel"
+ "primaryChannelClass"
+ "publishServiceCount"
+ "queryNANAvail"
+ "queryNANAvailWithCompletionHandler:"
+ "queryNANSrv"
+ "queryNANSrvWithCompletionHandler:"
+ "secondaryChannel"
+ "secondaryChannelClass"
+ "setAvailUpdatedHandler:"
+ "setInterfaceAddr:"
+ "setIsEnabled:"
+ "setLastRadioSchedule:"
+ "setLastRadioScheduleChangedOptions:"
+ "setLastSrvInfo:"
+ "setLastSrvInfoChangedOptions:"
+ "setSrvInfoUpdatedHandler:"
+ "srvHash"
+ "srvId"
+ "srvInfoUpdatedHandler"
+ "srvName"
+ "srvSessionCount"
+ "srvSessionInfos"
+ "srvSessionInfos.%@"
+ "srvType"
+ "stringValue"
+ "subscribeServiceCount"
+ "supportsDualBand"
+ "supportsSimultaneousDualBand"
+ "timeBitmap"
+ "updatedNANAvailability:"
+ "updatedNANAvailabilityWithChangedOptions:changedOptions:"
+ "updatedNANAvailabilityWithChangedOptions:changedOptions:forceAllChangedOptions:"
+ "updatedNANDpStateWithChangedOptions:changedOptions:forceAllChangedOptions:"
+ "updatedNANSrvInfo:"
+ "updatedNANSrvInfoWithChangedOptions:changedOptions:"
+ "updatedNANSrvInfoWithChangedOptions:changedOptions:forceAllChangedOptions:"
+ "updatedNANStateWithChangedOptions:changedOptions:forceAllChangedOptions:"
+ "v16@?0@\"WiFiAwareRadioSchedule\"8"
+ "v16@?0@\"WiFiAwareSrvInfo\"8"
+ "v24@0:8@\"WiFiAwareRadioSchedule\"16"
+ "v24@0:8@\"WiFiAwareSrvInfo\"16"
+ "v24@0:8@?<v@?@\"WiFiAwareRadioSchedule\">16"
+ "v24@0:8@?<v@?@\"WiFiAwareSrvInfo\">16"
+ "v32@0:8@\"WiFiAwareRadioSchedule\"16@\"NSArray\"24"
+ "v32@0:8@\"WiFiAwareSrvInfo\"16@\"NSArray\"24"
+ "v36@0:8@\"WiFiAwareDataPathState\"16@\"NSArray\"24B32"
+ "v36@0:8@\"WiFiAwareRadioSchedule\"16@\"NSArray\"24B32"
+ "v36@0:8@\"WiFiAwareSrvInfo\"16@\"NSArray\"24B32"
+ "v36@0:8@\"WiFiAwareState\"16@\"NSArray\"24B32"
+ "v36@0:8@16@24B32"
- "%@: %@, %@>"
- "@144@0:8@16B24B28Q32q40@48@56q64q72@80q88q96@104q112q120q128Q136"
- "@36@0:8@16@24I32"
- "@72@0:8C16Q20C28C32@36@44@52I60Q64"
- "@96@0:8@16@24B32I36I40I44I48I52I56I60@64@72@80@88"
- "PK-128"
- "PK-256"
- "PrefChannel=%@/%@>"
- "PrefChannel=%d/%d"
- "PrefChannel=%d/%d\n"
- "T@\"NSArray\",R,N,V_ndiSessions"
- "T@\"NSArray\",R,N,V_sessionInfos"
- "T@\"NSNumber\",R,N,V_customPreferredChannelClass"
- "T@\"NSNumber\",R,N,V_customPreferredChannelNumber"
- "T@\"WiFiMACAddress\",R,N,V_dataAddress"
- "T@\"WiFiMACAddress\",R,N,V_selfAddress"
- "TI,R,N,V_ndiDataAddressCount"
- "WiFiAwareDataPathInfoPerDataAddress"
- "_customPreferredChannelClass"
- "_customPreferredChannelNumber"
- "_dataAddress"
- "_ndiDataAddressCount"
- "_ndiSessions"
- "_selfAddress"
- "_sessionInfos"
- "customPreferredChannelClass"
- "customPreferredChannelNumber"
- "dataAddress"
- "initWithDpId:dpRole:serviceId:security:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:qosType:sessionState:"
- "initWithInterfaceName:dataAddress:sessionCount:"
- "initWithInterfaceName:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfAddress:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:"
- "initWithInterfaceName:macAddress:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiDataAddressCount:ndiSessions:customPreferredChannelNumber:customPreferredChannelClass:sessionInfos:"
- "ndiDataAddressCount"
- "ndiSessions"
- "ndiSessions[%lu].interfaceName"
- "selfAddress"
- "sessionInfos[%lu].dpId"
- "sessionInfos[%lu].dpRole"
- "sessionInfos[%lu].initiatorDataAddress"
- "sessionInfos[%lu].peerDataAddress"
- "sessionInfos[%lu].peerNmiMacAddress"
- "sessionInfos[%lu].qosType"
- "sessionInfos[%lu].security"
- "sessionInfos[%lu].serviceId"
- "sessionInfos[%lu].sessionState"

```
