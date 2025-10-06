## TimeSync

> `/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`

```diff

-1230.2.0.0.0
+1240.15.0.0.0
   __TEXT.__text: 0x6e22c
   __TEXT.__auth_stubs: 0x900
   __TEXT.__objc_methlist: 0x7224

   __TEXT.__unwind_info: 0x1e98
   __TEXT.__eh_frame: 0x4c
   __TEXT.__objc_classname: 0xd66
-  __TEXT.__objc_methname: 0xb816
+  __TEXT.__objc_methname: 0xb82a
   __TEXT.__objc_methtype: 0x1c33
   __TEXT.__objc_stubs: 0x73e0
   __DATA_CONST.__got: 0x58

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xdd48
   __DATA_CONST.__objc_selrefs: 0x2358
+  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA_CONST.__objc_classrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__cfstring: 0x4f80
+  __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x498
-  __DATA.__objc_protorefs: 0xa0
-  __DATA.__objc_classrefs: 0x3d8
-  __DATA.__objc_superrefs: 0x3d8
   __DATA.__objc_ivar: 0xa34
   __DATA.__data: 0xb48
   __DATA.__bss: 0x88
-  __DATA_DIRTY.__const: 0x5a0
+  __DATA_DIRTY.__const: 0x2c0
   __DATA_DIRTY.__objc_const: 0x3328
   __DATA_DIRTY.__objc_data: 0x2620
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12AA7C36-D751-3CD8-9FD4-472DD561A5D0
+  UUID: 3646040A-3B27-3BE7-A9D0-28787EBBFFA9
   Functions: 2845
   Symbols:   9033
-  CStrings:  4019
+  CStrings:  4020
 
Symbols:
+ ___104-[TSXgPTPClock addUnicastUDPv4EtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.122
+ ___104-[TSXgPTPClock addUnicastUDPv4PtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.115
+ ___104-[TSXgPTPClock addUnicastUDPv6EtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.124
+ ___104-[TSXgPTPClock addUnicastUDPv6PtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.118
+ ___105-[TSXClockManager addUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:error:]_block_invoke.97
+ ___108-[TSXgPTPClock addUnicastLinkLayerEtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.126
+ ___108-[TSXgPTPClock addUnicastLinkLayerPtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.120
+ ___127-[TSXgPTPNetworkPort requestRemoteMessageIntervalsWithPDelayMessageInterval:syncMessageInterval:announceMessageInterval:error:]_block_invoke.342
+ ___169-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke.74
+ ___21-[TSXgPTPClock ports]_block_invoke.129
+ ___31-[TSXgPTPPort updateProperties]_block_invoke.84
+ ___32-[TSXgPTPNetworkPort addClient:]_block_invoke.352
+ ___32-[TSXgPTPPort initWithEndpoint:]_block_invoke.70
+ ___34-[TSXUserFilteredClock isAdaptive]_block_invoke.79
+ ___35-[TSXUserFilteredClock filterShift]_block_invoke.77
+ ___35-[TSXgPTPClock _getInitialSyncInfo]_block_invoke.136
+ ___35-[TSXgPTPNetworkPort removeClient:]_block_invoke.355
+ ___37-[TSXKernelClock _getInitialSyncInfo]_block_invoke.77
+ ___37-[TSXKernelClock getClockIdentifier:]_block_invoke.75
+ ___38-[TSXgPTPNetworkPort enablePortError:]_block_invoke.345
+ ___39-[TSXgPTPManager addPTPInstance:error:]_block_invoke.73
+ ___39-[TSXgPTPNetworkPort disablePortError:]_block_invoke.346
+ ___43-[TSXUserFilteredClock nominalMachInterval]_block_invoke.74
+ ___43-[TSXgPTPPort stopAutomaticPropertyUpdates]_block_invoke.92
+ ___44-[TSXClockManager addgPTPServicesWithError:]_block_invoke.92
+ ___44-[TSXClockManager availableClockIdentifiers]_block_invoke.95
+ ___44-[TSXgPTPPort startAutomaticPropertyUpdates]_block_invoke.88
+ ___45-[TSXUserFilteredClock nominalDomainInterval]_block_invoke.76
+ ___45-[TSXgPTPManager systemDomainClockIdentifier]_block_invoke.101
+ ___46-[TSXgPTPManager addAirPlayPTPInstance:error:]_block_invoke.92
+ ___47-[TSXClockManager releaseDynamicClockID:error:]_block_invoke.88
+ ___47-[TSXClockManager removegPTPServicesWithError:]_block_invoke.93
+ ___47-[TSXExpositorClient gPTPManagerDiagnosticInfo]_block_invoke.91
+ ___48-[TSXClockManager getTranslationClockIdentifier]_block_invoke.107
+ ___48-[TSXExpositorClient clockManagerDiagnosticInfo]_block_invoke.78
+ ___48-[TSXgPTPManager addTimeOfDayPTPInstance:error:]_block_invoke.102
+ ___48-[TSXgPTPManager avbPTPInstance0ClockIdentifier]_block_invoke.78
+ ___48-[TSXgPTPManager avbPTPInstance1ClockIdentifier]_block_invoke.82
+ ___48-[TSXgPTPManager avbPTPInstance2ClockIdentifier]_block_invoke.85
+ ___48-[TSXgPTPManager avbPTPInstance3ClockIdentifier]_block_invoke.88
+ ___49-[TSClockInterface didChangeClockMasterForClock:]_block_invoke.71
+ ___49-[TSXClockManager getTimeSyncTimeClockIdentifier]_block_invoke.101
+ ___49-[TSXgPTPManager addCopresencePTPInstance:error:]_block_invoke.97
+ ___49-[TSXgPTPNetworkPort registerAsyncCallbackError:]_block_invoke.348
+ ___50-[TSXClockManager addTSNCaptureServicesWithError:]_block_invoke.103
+ ___50-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke.71
+ ___50-[TSXExpositorClient clockNameForClockIdentifier:]_block_invoke.101
+ ___50-[TSXUserFilteredClock resetSyncServiceWithError:]_block_invoke.72
+ ___50-[TSXgPTPNetworkPort restoreReceiveMatchingError:]_block_invoke.344
+ ___51-[TSXUserFilteredClock resetFilterToNominal:error:]_block_invoke.73
+ ___51-[TSXgPTPManager airPlayPTPInstanceClockIdentifier]_block_invoke.91
+ ___51-[TSXgPTPNetworkPort deregisterAsyncCallbackError:]_block_invoke.349
+ ___52-[TSXClockManager getTimeSyncTimeIsMachAbsoluteTime]_block_invoke.110
+ ___52-[TSXgPTPManager removeAirPlayPTPInstanceWithError:]_block_invoke.93
+ ___53-[TSXClockManager nextAvailableDynamicClockID:error:]_block_invoke.86
+ ___53-[TSXClockManager removeTSNCaptureServicesWithError:]_block_invoke.104
+ ___54-[TSXgPTPManager copresencePTPInstanceClockIdentifier]_block_invoke.96
+ ___54-[TSXgPTPManager removeAVBPTPInstanceWithIndex:error:]_block_invoke.77
+ ___55-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke.78
+ ___55-[TSXgPTPManager removeCopresencePTPInstanceWithError:]_block_invoke.98
+ ___56-[TSXgPTPManager removePTPInstanceWithIdentifier:error:]_block_invoke.75
+ ___57-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke.82
+ ___58-[TSXgPTPManager addAVBPTPInstanceIndex:identifier:error:]_block_invoke.76
+ ___60-[TSXgPTPClock removeLinkLayerPortFromInterfaceNamed:error:]_block_invoke.114
+ ___63-[TSXClockManager removeUserFilteredClockWithIdentifier:error:]_block_invoke.98
+ ___64-[TSXExpositorClient kernelClockAvailableKernelClockIdentifiers]_block_invoke.94
+ ___68-[TSXExpositorClient clockManagerDaemonClassNameForClockIdentifier:]_block_invoke.88
+ ___70-[TSXClockManager addMappingFromClockID:toCoreAudioClockDomain:error:]_block_invoke.89
+ ___73-[TSXUserFilteredClock addTimestampWithMachAbsolute:andDomainTime:error:]_block_invoke.70
+ ___75-[TSXgPTPClock addLinkLayerPortOnInterfaceNamed:allocatedPortNumber:error:]_block_invoke.112
+ ___75-[TSXgPTPClock removeReverseSyncFromInterfaceNamed:withDomainNumner:error:]_block_invoke.135
+ ___79-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke.68
+ ___82-[TSXClockManager removeMappingFromClockIDToCoreAudioClockDomainForClockID:error:]_block_invoke.91
+ ___83-[TSXExpositorClient clockManagerDiagnosticInfoForClockIdentifier:daemonClassName:]_block_invoke.83
+ ___83-[TSXgPTPClock addReverseSyncOnInterfaceNamed:withDomainNumner:syncInterval:error:]_block_invoke.134
+ ___85-[TSXExpositorClient gPTPPortDiagnosticInfoForPortWithClockIdentifier:andPortNumber:]_block_invoke.98
+ ___89-[TSXgPTPClock removeUnicastUDPv4EtEPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.123
+ ___89-[TSXgPTPClock removeUnicastUDPv4PtPPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.116
+ ___89-[TSXgPTPClock removeUnicastUDPv6EtEPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.125
+ ___89-[TSXgPTPClock removeUnicastUDPv6PtPPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.119
+ ___90-[TSXClockManager getConnectionForClockWithClockIdentifier:daemonClockClassName:endpoint:]_block_invoke.114
+ ___92-[TSXgPTPNetworkPort overrideReceiveMatchingWithRemoteClockIdentity:remotePortNumber:error:]_block_invoke.343
+ ___93-[TSXgPTPClock removeUnicastLinkLayerEtEPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.127
+ ___93-[TSXgPTPClock removeUnicastLinkLayerPtPPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.121
+ ___99-[TSXClockManager getConnectionForPortWithClockIdentifier:portNumber:daemonPortClassName:endpoint:]_block_invoke.118
+ ___block_literal_global.100
+ ___block_literal_global.106
+ ___block_literal_global.109
+ ___block_literal_global.113
+ ___block_literal_global.117
+ ___block_literal_global.157
+ ___block_literal_global.178
+ ___block_literal_global.351
+ ___block_literal_global.354
+ ___block_literal_global.73
+ ___block_literal_global.77
+ ___block_literal_global.82
+ ___block_literal_global.84
+ ___block_literal_global.87
+ ___block_literal_global.91
+ ___block_literal_global.93
+ ___block_literal_global.95
+ ___block_literal_global.97
- ___104-[TSXgPTPClock addUnicastUDPv4EtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.121
- ___104-[TSXgPTPClock addUnicastUDPv4PtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.114
- ___104-[TSXgPTPClock addUnicastUDPv6EtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.123
- ___104-[TSXgPTPClock addUnicastUDPv6PtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.117
- ___105-[TSXClockManager addUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:error:]_block_invoke.96
- ___108-[TSXgPTPClock addUnicastLinkLayerEtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.125
- ___108-[TSXgPTPClock addUnicastLinkLayerPtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:]_block_invoke.119
- ___127-[TSXgPTPNetworkPort requestRemoteMessageIntervalsWithPDelayMessageInterval:syncMessageInterval:announceMessageInterval:error:]_block_invoke.341
- ___169-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke.73
- ___21-[TSXgPTPClock ports]_block_invoke.128
- ___31-[TSXgPTPPort updateProperties]_block_invoke.83
- ___32-[TSXgPTPNetworkPort addClient:]_block_invoke.351
- ___32-[TSXgPTPPort initWithEndpoint:]_block_invoke.69
- ___34-[TSXUserFilteredClock isAdaptive]_block_invoke.78
- ___35-[TSXUserFilteredClock filterShift]_block_invoke.76
- ___35-[TSXgPTPClock _getInitialSyncInfo]_block_invoke.135
- ___35-[TSXgPTPNetworkPort removeClient:]_block_invoke.354
- ___37-[TSXKernelClock _getInitialSyncInfo]_block_invoke.76
- ___37-[TSXKernelClock getClockIdentifier:]_block_invoke.74
- ___38-[TSXgPTPNetworkPort enablePortError:]_block_invoke.344
- ___39-[TSXgPTPManager addPTPInstance:error:]_block_invoke.72
- ___39-[TSXgPTPNetworkPort disablePortError:]_block_invoke.345
- ___43-[TSXUserFilteredClock nominalMachInterval]_block_invoke.73
- ___43-[TSXgPTPPort stopAutomaticPropertyUpdates]_block_invoke.91
- ___44-[TSXClockManager addgPTPServicesWithError:]_block_invoke.91
- ___44-[TSXClockManager availableClockIdentifiers]_block_invoke.94
- ___44-[TSXgPTPPort startAutomaticPropertyUpdates]_block_invoke.87
- ___45-[TSXUserFilteredClock nominalDomainInterval]_block_invoke.75
- ___45-[TSXgPTPManager systemDomainClockIdentifier]_block_invoke.100
- ___46-[TSXgPTPManager addAirPlayPTPInstance:error:]_block_invoke.91
- ___47-[TSXClockManager releaseDynamicClockID:error:]_block_invoke.87
- ___47-[TSXClockManager removegPTPServicesWithError:]_block_invoke.92
- ___47-[TSXExpositorClient gPTPManagerDiagnosticInfo]_block_invoke.90
- ___48-[TSXClockManager getTranslationClockIdentifier]_block_invoke.106
- ___48-[TSXExpositorClient clockManagerDiagnosticInfo]_block_invoke.77
- ___48-[TSXgPTPManager addTimeOfDayPTPInstance:error:]_block_invoke.101
- ___48-[TSXgPTPManager avbPTPInstance0ClockIdentifier]_block_invoke.77
- ___48-[TSXgPTPManager avbPTPInstance1ClockIdentifier]_block_invoke.81
- ___48-[TSXgPTPManager avbPTPInstance2ClockIdentifier]_block_invoke.84
- ___48-[TSXgPTPManager avbPTPInstance3ClockIdentifier]_block_invoke.87
- ___49-[TSClockInterface didChangeClockMasterForClock:]_block_invoke.70
- ___49-[TSXClockManager getTimeSyncTimeClockIdentifier]_block_invoke.100
- ___49-[TSXgPTPManager addCopresencePTPInstance:error:]_block_invoke.96
- ___49-[TSXgPTPNetworkPort registerAsyncCallbackError:]_block_invoke.347
- ___50-[TSXClockManager addTSNCaptureServicesWithError:]_block_invoke.102
- ___50-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke.70
- ___50-[TSXExpositorClient clockNameForClockIdentifier:]_block_invoke.100
- ___50-[TSXUserFilteredClock resetSyncServiceWithError:]_block_invoke.71
- ___50-[TSXgPTPNetworkPort restoreReceiveMatchingError:]_block_invoke.343
- ___51-[TSXUserFilteredClock resetFilterToNominal:error:]_block_invoke.72
- ___51-[TSXgPTPManager airPlayPTPInstanceClockIdentifier]_block_invoke.90
- ___51-[TSXgPTPNetworkPort deregisterAsyncCallbackError:]_block_invoke.348
- ___52-[TSXClockManager getTimeSyncTimeIsMachAbsoluteTime]_block_invoke.109
- ___52-[TSXgPTPManager removeAirPlayPTPInstanceWithError:]_block_invoke.92
- ___53-[TSXClockManager nextAvailableDynamicClockID:error:]_block_invoke.85
- ___53-[TSXClockManager removeTSNCaptureServicesWithError:]_block_invoke.103
- ___54-[TSXgPTPManager copresencePTPInstanceClockIdentifier]_block_invoke.95
- ___54-[TSXgPTPManager removeAVBPTPInstanceWithIndex:error:]_block_invoke.76
- ___55-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke.77
- ___55-[TSXgPTPManager removeCopresencePTPInstanceWithError:]_block_invoke.97
- ___56-[TSXgPTPManager removePTPInstanceWithIdentifier:error:]_block_invoke.74
- ___57-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke.81
- ___58-[TSXgPTPManager addAVBPTPInstanceIndex:identifier:error:]_block_invoke.75
- ___60-[TSXgPTPClock removeLinkLayerPortFromInterfaceNamed:error:]_block_invoke.113
- ___63-[TSXClockManager removeUserFilteredClockWithIdentifier:error:]_block_invoke.97
- ___64-[TSXExpositorClient kernelClockAvailableKernelClockIdentifiers]_block_invoke.93
- ___68-[TSXExpositorClient clockManagerDaemonClassNameForClockIdentifier:]_block_invoke.87
- ___70-[TSXClockManager addMappingFromClockID:toCoreAudioClockDomain:error:]_block_invoke.88
- ___73-[TSXUserFilteredClock addTimestampWithMachAbsolute:andDomainTime:error:]_block_invoke.69
- ___75-[TSXgPTPClock addLinkLayerPortOnInterfaceNamed:allocatedPortNumber:error:]_block_invoke.111
- ___75-[TSXgPTPClock removeReverseSyncFromInterfaceNamed:withDomainNumner:error:]_block_invoke.134
- ___79-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke.67
- ___82-[TSXClockManager removeMappingFromClockIDToCoreAudioClockDomainForClockID:error:]_block_invoke.90
- ___83-[TSXExpositorClient clockManagerDiagnosticInfoForClockIdentifier:daemonClassName:]_block_invoke.82
- ___83-[TSXgPTPClock addReverseSyncOnInterfaceNamed:withDomainNumner:syncInterval:error:]_block_invoke.133
- ___85-[TSXExpositorClient gPTPPortDiagnosticInfoForPortWithClockIdentifier:andPortNumber:]_block_invoke.97
- ___89-[TSXgPTPClock removeUnicastUDPv4EtEPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.122
- ___89-[TSXgPTPClock removeUnicastUDPv4PtPPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.115
- ___89-[TSXgPTPClock removeUnicastUDPv6EtEPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.124
- ___89-[TSXgPTPClock removeUnicastUDPv6PtPPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.118
- ___90-[TSXClockManager getConnectionForClockWithClockIdentifier:daemonClockClassName:endpoint:]_block_invoke.113
- ___92-[TSXgPTPNetworkPort overrideReceiveMatchingWithRemoteClockIdentity:remotePortNumber:error:]_block_invoke.342
- ___93-[TSXgPTPClock removeUnicastLinkLayerEtEPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.126
- ___93-[TSXgPTPClock removeUnicastLinkLayerPtPPortFromInterfaceNamed:withDestinationAddress:error:]_block_invoke.120
- ___99-[TSXClockManager getConnectionForPortWithClockIdentifier:portNumber:daemonPortClassName:endpoint:]_block_invoke.117
- ___block_literal_global.105
- ___block_literal_global.108
- ___block_literal_global.112
- ___block_literal_global.116
- ___block_literal_global.156
- ___block_literal_global.177
- ___block_literal_global.350
- ___block_literal_global.353
- ___block_literal_global.68
- ___block_literal_global.72
- ___block_literal_global.76
- ___block_literal_global.80
- ___block_literal_global.83
- ___block_literal_global.86
- ___block_literal_global.89
- ___block_literal_global.92
- ___block_literal_global.94
- ___block_literal_global.96
- ___block_literal_global.99
CStrings:
+ "T@\"NSString\",?,R,C"

```
